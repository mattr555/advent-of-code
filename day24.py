import math
from copy import deepcopy

FIRE = 'fire'
RADIATION = 'radiation'
BLUDGEONING = 'bludgeoning'
SLASHING = 'slashing'
COLD = 'cold'

class Group(object):
    def __init__(self, units, hp, ap, attackType, initiative, immunities, weaknesses, _id=None):
        self.units = units
        self.hp = hp
        self.ap = ap
        self.attackType = attackType
        self.initiative = initiative
        self.immunities = immunities
        self.weaknesses = weaknesses
        self._id = _id
    
    def __repr__(self):
        if self._id:
            return "Group #{}".format(self._id)
        return "Group<{} units, {} hp, {} ap, {} initiative>".format(self.units, self.hp, self.ap, self.initiative)
    
    @property
    def effectivePower(self):
        return self.units * self.ap

    def damageDealtTo(self, other):
        if self.attackType in other.immunities:
            return 0
        elif self.attackType in other.weaknesses:
            return 2 * self.effectivePower
        return self.effectivePower
    
    def chooseTarget(self, availableEnemies):
        s = sorted(availableEnemies, key=lambda i: (-self.damageDealtTo(i), -i.effectivePower, -i.initiative))
        myTarget = next((x for x in s), None)
        if myTarget and self.damageDealtTo(myTarget) == 0:
            return None
        # print(self, "chose", myTarget)
        return myTarget
    
    def attack(self, other):
        damageToDeal = self.damageDealtTo(other)
        toKill = math.floor(damageToDeal / other.hp)
        actuallyKilled = min(toKill, other.units)
        other.units -= actuallyKilled
        return actuallyKilled

# immuneSystem = []
# immuneSystem.append(Group(17, 5390, 4507, FIRE, 2, [], [RADIATION, BLUDGEONING], "Imm1"))
# immuneSystem.append(Group(989, 1274, 25, SLASHING, 3, [FIRE], [BLUDGEONING, SLASHING], "Imm2"))

# infection = []
# infection.append(Group(801, 4706, 116, BLUDGEONING, 1, [], [RADIATION], "Inf1"))
# infection.append(Group(4485, 2961, 12, SLASHING, 4, [RADIATION], [FIRE, COLD], "Inf2"))

immuneSystem = [
    Group(2321, 10326, 42, FIRE, 4, [SLASHING], []),
    Group(2899, 9859, 32, SLASHING, 11, [], []),
    Group(4581, 7073, 11, RADIATION, 9, [], [SLASHING]),
    Group(5088, 7917, 15, FIRE, 17, [BLUDGEONING, FIRE, RADIATION], [SLASHING]),
    Group(786, 1952, 23, SLASHING, 16, [FIRE, BLUDGEONING, SLASHING, COLD], []),
    Group(3099, 7097, 17, RADIATION, 8, [], [BLUDGEONING]),
    Group(4604, 4901, 8, FIRE, 13, [], []),
    Group(7079, 10328, 14, BLUDGEONING, 18, [], []),
    Group(51, 11243, 1872, COLD, 15, [], []),
    Group(4910, 5381, 10, SLASHING, 19, [FIRE], [RADIATION])
]

infection = [
    Group(1758, 23776, 24, RADIATION, 2, [], []),
    Group(4000, 12869, 5, COLD, 14, [], []),
    Group(2319, 43460, 33, RADIATION, 3, [], [BLUDGEONING, COLD]),
    Group(1898, 44204, 39, RADIATION, 1, [COLD], [RADIATION]),
    Group(2764, 50667, 31, RADIATION, 5, [], [SLASHING, RADIATION]),
    Group(3046, 27907, 16, SLASHING, 7, [RADIATION, FIRE], []),
    Group(1379, 8469, 8, COLD, 20, [COLD], []),
    Group(1824, 25625, 23, RADIATION, 6, [BLUDGEONING], []),
    Group(115, 41114, 686, SLASHING, 10, [FIRE], [SLASHING, BLUDGEONING]),
    Group(4054, 51210, 22, COLD, 12, [RADIATION, COLD, FIRE], [])
]

def run(immuneSystem, infection, maxRounds=20000, debug=False):
    roundNum = 0
    while len(immuneSystem) > 0 and len(infection) > 0 and roundNum < maxRounds:
        # target selection
        if debug:
            print("====================================")
        targets = {}
        availableImmune = set(immuneSystem)
        availableInfection = set(infection)
        for selector in sorted(immuneSystem + infection, key=lambda i: (-i.effectivePower, -i.initiative)):
            if selector in immuneSystem:
                enemies = availableInfection
            else:
                enemies = availableImmune
                
            t = selector.chooseTarget(enemies)
            if t is not None:
                targets[selector] = t
                enemies.remove(t)
        
        # damage
        for attacker in sorted(immuneSystem + infection, key=lambda i: -i.initiative):
            if attacker in targets:
                killed = attacker.attack(targets[attacker])
                if debug:
                    print(attacker, "attacks", targets[attacker], "killing", killed)
        
        # cleanup
        immuneSystem = list(filter(lambda i: i.units > 0, immuneSystem))
        infection = list(filter(lambda i: i.units > 0, infection))
        roundNum += 1

    if roundNum == maxRounds:
        return None
    return sum([i.units for i in immuneSystem]) - sum([i.units for i in infection])

print(-run(deepcopy(immuneSystem), deepcopy(infection)))

for boost in range(50):
    boosted = deepcopy(immuneSystem)
    for i in boosted:
        i.ap += boost
    res = run(boosted, deepcopy(infection))
    print("boost:", boost, "result:", res)

