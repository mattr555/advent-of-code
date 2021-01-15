package days

import "fmt"

func Eight(lines []string) {
	p1 := 0
	for _, l := range lines {
		t := 0
		i := 1
		for i < len(l)-1 {
			if l[i] == '\\' {
				if l[i+1] == '\\' || l[i+1] == '"' {
					i++
				} else if l[i+1] == 'x' {
					i += 3
				}
			}
			t++
			i++
		}
		p1 += len(l) - t
	}
	fmt.Println(p1)

	p2 := 0
	for _, l := range lines {
		t := 2 //for the two quotes wrapping our final string
		for i := 0; i < len(l); i++ {
			if l[i] == '\\' || l[i] == '"' {
				t += 2
			} else {
				t++
			}
		}
		p2 += t - len(l)
	}
	fmt.Println(p2)
}
