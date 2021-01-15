package days

import (
	"fmt"
	"regexp"
	"strconv"
)

type dinerPair struct {
	a, b string
}

func Thirteen(lines []string) {
	reg := regexp.MustCompile(`(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).`)
	happiness := map[dinerPair]int{}
	diners := map[string]bool{}
	for _, i := range lines {
		matches := reg.FindSubmatch([]byte(i))
		da := string(matches[1])
		db := string(matches[4])
		v, _ := strconv.Atoi(string(matches[3]))
		switch string(matches[2]) {
		case "gain":
			happiness[dinerPair{da, db}] = v
		case "lose":
			happiness[dinerPair{da, db}] = -v
		}
		diners[da] = true
		diners[db] = true
	}

	a := make([]string, 0, len(diners))
	for k := range diners {
		a = append(a, k)
	}

	best := 0
	f := func(l []string) {
		s := 0
		for ix, me := range l {
			//janky because Go's modulus is weird
			left := l[len(l)-1]
			if ix > 0 {
				left = l[(ix-1)%len(l)]
			}
			right := l[(ix+1)%len(l)]
			s += happiness[dinerPair{me, left}]
			s += happiness[dinerPair{me, right}]
		}

		if s > best {
			best = s
		}
	}

	// from day 9
	genPerm(len(a), a, f)
	fmt.Println(best)

	for _, v := range a {
		happiness[dinerPair{"Me", v}] = 0
		happiness[dinerPair{v, "Me"}] = 0
	}
	a = append(a, "Me")
	best = 0
	genPerm(len(a), a, f)
	fmt.Println(best)
}
