from collections import deque

INST_PARAMS = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3
}

class IntcodeVM(object):
    def __init__(self, prog):
        self.prog = list(prog)
        self.ip = 0
        self.input = deque()
        self.output = []

    def _interpret_op(self, op):
        modes = []
        o = op % 100
        op //= 100
        while op > 0:
            modes.append(op % 10)
            op //= 10
        return o, modes

    def addInput(self, l):
        self.input.extend(l)
    
    def clearOutput(self):
        self.output = []

    def _setV(self, offset, v):
        self.prog[self.prog[self.ip + offset]] = v

    def runToBlock(self):
        while self.prog[self.ip] != 99:
            op, modes = self._interpret_op(self.prog[self.ip])
            modes += [0] * (INST_PARAMS[op] - len(modes))
            
            values = []
            for ix, mode in enumerate(modes):
                if mode == 0:
                    values.append(self.prog[self.prog[self.ip+ix+1]])
                else:
                    values.append(self.prog[self.ip+ix+1])

            skip_inc = False
            if op == 1:
                self._setV(3, values[0] + values[1])
            elif op == 2:
                self._setV(3, values[0] * values[1])
            elif op == 3:
                if len(self.input) == 0:
                    # blocked
                    return False
                self._setV(1, self.input.popleft())
            elif op == 4:
                self.output.append(values[0])
            elif op == 5:
                if values[0] != 0:
                    self.ip = values[1]
                    skip_inc = True
            elif op == 6:
                if values[0] == 0:
                    self.ip = values[1]
                    skip_inc = True
            elif op == 7:
                if values[0] < values[1]:
                    self._setV(3, 1)
                else:
                    self._setV(3, 0)
            elif op == 8:
                if values[0] == values[1]:
                    self._setV(3, 1)
                else:
                    self._setV(3, 0)
            
            if not skip_inc:
                self.ip += INST_PARAMS[op] + 1
        return True