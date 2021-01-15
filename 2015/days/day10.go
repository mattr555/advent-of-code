package days

import (
	"fmt"
	"strings"
)

func Ten(lines []string) {
	s := lines[0]
	for iter := 0; iter < 50; iter++ {
		// lesson learned: strings are immutable, string concatenation is not good
		// so use a Builder
		newS := strings.Builder{}
		i := 0
		for i < len(s) {
			c := 1
			for i+c < len(s) && s[i] == s[i+c] {
				c++
			}
			newS.WriteRune(rune('0' + c))
			newS.WriteRune(rune(s[i]))
			i += c
		}
		s = newS.String()
		if iter == 39 {
			fmt.Println(len(s))
		}
	}
	fmt.Println(len(s))
}
