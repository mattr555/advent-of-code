package days

import "fmt"

func runConway(on map[vertex]bool, cornersStuck bool) int {
	for step := 0; step < 100; step++ {
		neighborCount := map[vertex]int{}
		newOn := map[vertex]bool{}
		for v := range on {
			for dx := -1; dx <= 1; dx++ {
				for dy := -1; dy <= 1; dy++ {
					if dx == 0 && dy == 0 {
						continue
					}
					neighborCount[vertex{v.x + dx, v.y + dy}]++
				}
			}
		}
		for v, neighbors := range neighborCount {
			if v.x >= 0 && v.x < 100 && v.y >= 0 && v.y < 100 {
				if on[v] && neighbors >= 2 && neighbors <= 3 {
					newOn[v] = true
				} else if !on[v] && neighbors == 3 {
					newOn[v] = true
				}
			}
		}

		if cornersStuck {
			newOn[vertex{0, 0}] = true
			newOn[vertex{0, 99}] = true
			newOn[vertex{99, 0}] = true
			newOn[vertex{99, 99}] = true
		}

		on = newOn
	}

	return len(on)
}

func Eighteen(lines []string) {
	p1on := map[vertex]bool{}
	p2on := map[vertex]bool{}
	for x, l := range lines {
		for y, r := range l {
			if r == '#' {
				p1on[vertex{x, y}] = true
				p2on[vertex{x, y}] = true
			}
		}
	}
	p2on[vertex{0, 0}] = true
	p2on[vertex{0, 99}] = true
	p2on[vertex{99, 0}] = true
	p2on[vertex{99, 99}] = true

	fmt.Println(runConway(p1on, false))
	fmt.Println(runConway(p2on, true))
}
