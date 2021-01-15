package days

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func Two(lines []string) {
	p1 := 0
	p2 := 0

	for _, gift := range lines {
		var xs [3]int
		for ix, i := range strings.Split(gift, "x") {
			i, _ := strconv.Atoi(i)
			xs[ix] = i
		}

		sort.Ints(xs[:])
		p1 += 3*xs[0]*xs[1] + 2*xs[1]*xs[2] + 2*xs[0]*xs[2]
		p2 += 2*(xs[0]+xs[1]) + xs[0]*xs[1]*xs[2]
	}

	fmt.Println(p1)
	fmt.Println(p2)
}
