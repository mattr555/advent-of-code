package days

import (
	"fmt"
	"strconv"
	"strings"
)

type spellPlayer struct {
	hp, damage, armor, mana int
	hardMode                bool
}

type spellEffects struct {
	shield, poison, recharge int
}

const (
	magicMissileCost = 53
	drainCost        = 73
	shieldCost       = 113
	poisonCost       = 173
	rechargeCost     = 229
)

func playSpellFight(me, boss spellPlayer, eff spellEffects, meTurn bool, spent int, best *int) {
	if spent >= *best {
		//fail fast: not going to be able to beat the best so far
		return
	}

	if meTurn && me.hardMode {
		me.hp -= 1
		if me.hp <= 0 {
			return
		}
	}

	if eff.shield > 0 {
		me.armor = 7
		eff.shield--
	} else {
		me.armor = 0
	}

	if eff.poison > 0 {
		boss.hp -= 3
		eff.poison--
	}

	if eff.recharge > 0 {
		me.mana += 101
		eff.recharge--
	}

	if boss.hp <= 0 {
		//boss is dead
		if spent < *best {
			//we did it in less mana than seen before
			*best = spent
		}
		return
	}

	if !meTurn {
		//on the boss's turn, he just hits.
		me.hp -= boss.damage - me.armor
		if me.hp <= 0 {
			//I die, don't register a win
			return
		}
		playSpellFight(me, boss, eff, true, spent, best)
	} else {
		if me.mana < magicMissileCost {
			//I can't do anything, so I die.
			return
		}

		if me.mana >= magicMissileCost {
			//Magic Missile
			newBoss := boss
			newBoss.hp -= 4
			newMe := me
			newMe.mana -= magicMissileCost
			playSpellFight(newMe, newBoss, eff, false, spent+magicMissileCost, best)
		}

		if me.mana >= drainCost {
			//Drain
			newBoss := boss
			newBoss.hp -= 2
			newMe := me
			newMe.hp += 2
			newMe.mana -= drainCost
			playSpellFight(newMe, newBoss, eff, false, spent+drainCost, best)
		}

		if me.mana >= shieldCost && eff.shield == 0 {
			//Shield
			newMe := me
			newMe.mana -= shieldCost
			newEff := eff
			newEff.shield = 6
			playSpellFight(newMe, boss, newEff, false, spent+shieldCost, best)
		}

		if me.mana >= poisonCost && eff.poison == 0 {
			//Poison
			newMe := me
			newMe.mana -= poisonCost
			newEff := eff
			newEff.poison = 6
			playSpellFight(newMe, boss, newEff, false, spent+poisonCost, best)
		}

		if me.mana >= rechargeCost && eff.recharge == 0 {
			//Recharge
			newMe := me
			newMe.mana -= rechargeCost
			newEff := eff
			newEff.recharge = 5
			playSpellFight(newMe, boss, newEff, false, spent+rechargeCost, best)
		}
	}
}

func Twentytwo(lines []string) {
	bossHp, _ := strconv.Atoi(strings.Split(lines[0], ": ")[1])
	bossDamage, _ := strconv.Atoi(strings.Split(lines[1], ": ")[1])

	me := spellPlayer{hp: 50, mana: 500}
	boss := spellPlayer{hp: bossHp, damage: bossDamage}

	p1 := 100000000
	playSpellFight(me, boss, spellEffects{}, true, 0, &p1)
	fmt.Println(p1)

	me.hardMode = true
	p2 := 100000000
	playSpellFight(me, boss, spellEffects{}, true, 0, &p2)
	fmt.Println(p2)
}
