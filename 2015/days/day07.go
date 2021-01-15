package days

import (
	"fmt"
	"strconv"
	"strings"
)

type wire struct {
	lhs []string
	rhs string
}

func parseWireInput(lines []string) []wire {
	ret := make([]wire, len(lines))
	for ix, i := range lines {
		sides := strings.Split(i, " -> ")
		ret[ix] = wire{strings.Split(sides[0], " "), sides[1]}
	}
	return ret
}

func evaluateWires(wires []wire, overrideVals map[string]uint16) map[string]uint16 {
	//modifies wireVals in place
	//inefficient way of doing it: just keep looping and evaluating until
	//the whole system stabilizes
	//better way is to properly toposort. only need to propagate once in that order

	wireVals := map[string]uint16{}

	parseOp := func(s string) uint16 {
		n, err := strconv.Atoi(s)
		if err != nil {
			//wire is just equivalent to other wire
			if x, ok := overrideVals[s]; ok {
				return x
			}
			return wireVals[s]
		}
		return uint16(n)
	}

	for {
		changed := false
		for _, w := range wires {
			var newVal uint16

			if _, ok := overrideVals[w.rhs]; ok {
				continue
			}

			switch len(w.lhs) {
			case 1:
				newVal = parseOp(w.lhs[0])
			case 2:
				//only case is NOT operation
				newVal = ^parseOp(w.lhs[1])
			case 3:
				//binary operation
				a := parseOp(w.lhs[0])
				b := parseOp(w.lhs[2])

				switch w.lhs[1] {
				case "AND":
					newVal = a & b
				case "OR":
					newVal = a | b
				case "LSHIFT":
					newVal = a << b
				case "RSHIFT":
					newVal = a >> b
				}
			}
			if newVal != wireVals[w.rhs] {
				wireVals[w.rhs] = newVal
				changed = true
			}
		}

		if !changed {
			break
		}
	}

	return wireVals
}

func Seven(lines []string) {
	wires := parseWireInput(lines)
	wireVals := evaluateWires(wires, map[string]uint16{})
	fmt.Println(wireVals["a"])

	wireVals = evaluateWires(wires, map[string]uint16{"b": wireVals["a"]})
	fmt.Println(wireVals["a"])
}
