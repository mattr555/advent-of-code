package days

import (
	"fmt"
	"strconv"
)

func subsetSums(target int, xs []int, partial []int, partialSum int, c chan []int) {
	if partialSum > target {
		return
	}
	if partialSum == target {
		c <- partial
	}
	for ix, i := range xs {
		p := make([]int, len(partial)+1)
		copy(p, partial)
		p[len(partial)] = i
		subsetSums(target, xs[ix+1:], p, partialSum+i, c)
	}
}

func balanceSleigh(xs []int, groups int) int {
	s := 0
	c := make(chan []int)
	for _, i := range xs {
		s += i
	}

	go func() {
		subsetSums(s/groups, xs, make([]int, 0), 0, c)
		close(c)
	}()

	bestLen := len(xs)
	bestQE := 0
	for s := range c {
		q := 1
		for _, i := range s {
			q *= i
		}
		if len(s) < bestLen {
			bestLen = len(s)
			bestQE = q
		} else if len(s) == bestLen && q < bestQE {
			bestQE = q
		}
	}
	return bestQE
}

func Twentyfour(lines []string) {
	xs := make([]int, len(lines))
	for ix, i := range lines {
		n, _ := strconv.Atoi(i)
		xs[ix] = n
	}

	fmt.Println(balanceSleigh(xs, 3))
	fmt.Println(balanceSleigh(xs, 4))
}
