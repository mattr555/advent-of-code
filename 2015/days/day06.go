package days

import (
	"fmt"
	"regexp"
	"strconv"
)

type gridInstruction struct {
	op             string
	sx, sy, ex, ey int
}

func parseGridInstructions(lines []string) []gridInstruction {
	r := regexp.MustCompile(`(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)`)
	ret := make([]gridInstruction, len(lines))
	for ix, i := range lines {
		matches := r.FindSubmatch([]byte(i))
		op := string(matches[1])
		sx, _ := strconv.Atoi(string(matches[2]))
		sy, _ := strconv.Atoi(string(matches[3]))
		ex, _ := strconv.Atoi(string(matches[4]))
		ey, _ := strconv.Atoi(string(matches[5]))
		ret[ix] = gridInstruction{
			op, sx, sy, ex, ey,
		}
	}
	return ret
}

func Six(lines []string) {
	instructions := parseGridInstructions(lines)

	var grid [1000][1000]bool
	for _, i := range instructions {
		for x := i.sx; x <= i.ex; x++ {
			for y := i.sy; y <= i.ey; y++ {
				switch i.op {
				case "turn on":
					grid[x][y] = true
				case "turn off":
					grid[x][y] = false
				case "toggle":
					grid[x][y] = !grid[x][y]
				}
			}
		}
	}

	p1 := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			if grid[x][y] {
				p1++
			}
		}
	}
	fmt.Println(p1)

	var igrid [1000][1000]int
	for _, i := range instructions {
		for x := i.sx; x <= i.ex; x++ {
			for y := i.sy; y <= i.ey; y++ {
				switch i.op {
				case "turn on":
					igrid[x][y]++
				case "turn off":
					igrid[x][y]--
					if igrid[x][y] < 0 {
						igrid[x][y] = 0
					}
				case "toggle":
					igrid[x][y] += 2
				}
			}
		}
	}

	p2 := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			p2 += igrid[x][y]
		}
	}
	fmt.Println(p2)
}
