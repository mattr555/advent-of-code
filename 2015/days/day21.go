package days

import (
	"fmt"
	"strconv"
	"strings"
)

type rpgItem struct {
	cost, damage, armor int
}

type rpgPlayer struct {
	hp, damage, armor int
}

func playRPGFight(me, boss rpgPlayer) bool {
	meDamageDeals := me.damage - boss.armor
	if meDamageDeals < 1 {
		meDamageDeals = 1
	}
	bossDamageDeals := boss.damage - me.armor
	if bossDamageDeals < 1 {
		bossDamageDeals = 1
	}

	meRounds := me.hp / bossDamageDeals
	if me.hp%bossDamageDeals > 0 {
		meRounds++
	}
	bossRounds := boss.hp / meDamageDeals
	if boss.hp%meDamageDeals > 0 {
		bossRounds++
	}
	return meRounds >= bossRounds
}

func Twentyone(lines []string) {
	weapons := []rpgItem{
		{8, 4, 0},
		{10, 5, 0},
		{25, 6, 0},
		{40, 7, 0},
		{74, 8, 0},
	}

	armors := []rpgItem{
		{0, 0, 0},
		{13, 0, 1},
		{31, 0, 2},
		{53, 0, 3},
		{75, 0, 4},
		{102, 0, 5},
	}

	rings := []rpgItem{
		{0, 0, 0},
		{0, 0, 0},
		{25, 1, 0},
		{50, 2, 0},
		{100, 3, 0},
		{20, 0, 1},
		{40, 0, 2},
		{80, 0, 3},
	}

	bossHp, _ := strconv.Atoi(strings.Split(lines[0], ": ")[1])
	bossDamage, _ := strconv.Atoi(strings.Split(lines[1], ": ")[1])
	bossArmor, _ := strconv.Atoi(strings.Split(lines[2], ": ")[1])

	boss := rpgPlayer{bossHp, bossDamage, bossArmor}
	bestCost := 10000000
	worstCost := 0
	for _, weapon := range weapons {
		for _, armor := range armors {
			for r1ix := range rings {
				r1 := rings[r1ix]
				for r2ix := r1ix + 1; r2ix < len(rings); r2ix++ {
					r2 := rings[r2ix]
					c := weapon.cost + armor.cost + r1.cost + r2.cost
					if c < bestCost || c > worstCost {
						me := rpgPlayer{
							100,
							weapon.damage + armor.damage + r1.damage + r2.damage,
							weapon.armor + armor.armor + r1.armor + r2.armor,
						}
						res := playRPGFight(me, boss)

						if res && c < bestCost {
							bestCost = c
						} else if !res && c > worstCost {
							worstCost = c
						}
					}
				}
			}
		}
	}
	fmt.Println(bestCost)
	fmt.Println(worstCost)
}
