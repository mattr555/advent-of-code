package days

import (
	"fmt"
	"strconv"
)

func Seventeen(lines []string) {
	containers := make([]int, len(lines))
	for ix, v := range lines {
		n, _ := strconv.Atoi(v)
		containers[ix] = n
	}

	var f func(int, int, int) int
	f = func(amt, c, containersLeft int) int {
		if amt == 0 || (containersLeft > 0 && c == 0 && amt == containers[c]) {
			return 1
		} else if amt < 0 || c < 0 || containersLeft == 0 {
			return 0
		} else {
			return f(amt-containers[c], c-1, containersLeft-1) + f(amt, c-1, containersLeft)
		}
	}

	fmt.Println(f(150, len(containers)-1, len(containers))) // part 1: no limit on number of containers
	p2 := 0
	c := 1
	for p2 == 0 {
		p2 = f(150, len(containers)-1, c)
		c++
	}
	fmt.Println(p2)
}
