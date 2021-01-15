package days

import (
	"fmt"
)

func One(lines []string) {
	s := lines[0]
	p1 := 0
	p2 := -1
	for ix, i := range s {
		switch i {
		case '(':
			p1++
		case ')':
			p1--
		}
		if p2 == -1 && p1 < 0 {
			p2 = ix + 1
		}
	}
	fmt.Println(p1)
	fmt.Println(p2)
}
