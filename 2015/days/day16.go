package days

import (
	"fmt"
	"regexp"
	"strconv"
)

func Sixteen(lines []string) {
	reg := regexp.MustCompile(`Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)`)
	mySue := map[string]int{
		"children":    3,
		"cats":        7,
		"samoyeds":    2,
		"pomeranians": 3,
		"akitas":      0,
		"vizslas":     0,
		"goldfish":    5,
		"trees":       3,
		"cars":        2,
		"perfumes":    1,
	}

	p1, p2 := 0, 0
	for ix, line := range lines {
		matches := reg.FindSubmatch([]byte(line))

		p1ok, p2ok := true, true
		for i := 1; i < 7; i += 2 {
			s := string(matches[i])
			n, _ := strconv.Atoi(string(matches[i+1]))
			if mySue[s] != n {
				p1ok = false
			}

			switch s {
			case "cats", "trees":
				if mySue[s] >= n {
					p2ok = false
				}
			case "pomeranians", "goldfish":
				if mySue[s] <= n {
					p2ok = false
				}
			default:
				if mySue[s] != n {
					p2ok = false
				}
			}
		}

		if p1ok {
			p1 = ix + 1
		}
		if p2ok {
			p2 = ix + 1
		}
	}
	fmt.Println(p1)
	fmt.Println(p2)
}
