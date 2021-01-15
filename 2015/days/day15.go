package days

import (
	"fmt"
	"regexp"
	"strconv"
)

//initial: n = len(a), k = 100
func partitions(n int, k int, a []int, c chan []int) {
	if n == 1 {
		a[n-1] = k
		out := make([]int, len(a))
		copy(out, a)
		c <- out
	} else {
		for i := 0; i <= k; i++ {
			a[n-1] = i
			partitions(n-1, k-i, a, c)
		}
	}
}

type ingredient struct {
	capacity   int
	durability int
	flavor     int
	texture    int
	calories   int
}

func Fifteen(lines []string) {
	reg := regexp.MustCompile(`\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)`)
	ingredients := make([]ingredient, len(lines))
	for ix, l := range lines {
		matches := reg.FindSubmatch([]byte(l))
		c, _ := strconv.Atoi(string(matches[1]))
		d, _ := strconv.Atoi(string(matches[2]))
		f, _ := strconv.Atoi(string(matches[3]))
		t, _ := strconv.Atoi(string(matches[4]))
		cal, _ := strconv.Atoi(string(matches[5]))
		ingredients[ix] = ingredient{c, d, f, t, cal}
	}
	fmt.Println(ingredients)

	c := make(chan []int)
	go func() {
		a := make([]int, len(ingredients))
		partitions(len(ingredients), 100, a, c)
		close(c)
	}()

	p1 := 0
	p2 := 0
	for part := range c {
		// fmt.Println(part)
		c, d, f, t, cal := 0, 0, 0, 0, 0
		for ix, n := range part {
			c += n * ingredients[ix].capacity
			d += n * ingredients[ix].durability
			f += n * ingredients[ix].flavor
			t += n * ingredients[ix].texture
			cal += n * ingredients[ix].calories
		}
		if c > 0 && d > 0 && f > 0 && t > 0 {
			score := c * d * f * t
			if score > p1 {
				p1 = score
			}
			if cal == 500 && score > p2 {
				p2 = score
			}
		}
	}
	fmt.Println(p1)
	fmt.Println(p2)
}
