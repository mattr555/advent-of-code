package days

import (
	"fmt"
	"strconv"
	"strings"
)

type cityPair struct {
	orig, dest string
}

func genPerm(k int, a []string, f func([]string)) {
	//heap's algorithm
	if k == 1 {
		f(a)
	} else {
		for i := 0; i < k; i++ {
			genPerm(k-1, a, f)
			if k%2 == 0 {
				a[0], a[k-1] = a[k-1], a[0]
			} else {
				a[i], a[k-1] = a[k-1], a[i]
			}
		}
	}
}

func Nine(lines []string) {
	distMap := map[cityPair]int{}
	citySet := map[string]bool{}

	for _, l := range lines {
		xs := strings.Split(l, " ")
		citySet[xs[0]] = true
		citySet[xs[2]] = true
		d, _ := strconv.Atoi(xs[4])
		distMap[cityPair{xs[0], xs[2]}] = d
		distMap[cityPair{xs[2], xs[0]}] = d
	}

	a := make([]string, 0, len(citySet))
	for k := range citySet {
		a = append(a, k)
	}

	p1 := 1000000000 // a big int
	p2 := 0
	f := func(l []string) {
		d := 0
		for i := 0; i < len(l)-1; i++ {
			d += distMap[cityPair{l[i], l[i+1]}]
		}
		if d < p1 {
			p1 = d
		}
		if d > p2 {
			p2 = d
		}
	}

	genPerm(len(a), a, f)
	fmt.Println(p1)
	fmt.Println(p2)
}
