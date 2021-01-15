package days

import (
	"fmt"
	"strings"
)

func vowelCount(s string) (c int) {
	for _, i := range "aeiou" {
		c += strings.Count(s, string(i))
	}
	return
}

func hasDouble(s string) bool {
	for i := 0; i < len(s)-1; i++ {
		if s[i] == s[i+1] {
			return true
		}
	}
	return false
}

func hasProhibitedSubstring(s string) bool {
	prohibited := []string{"ab", "cd", "pq", "xy"}
	for _, i := range prohibited {
		if strings.Contains(s, i) {
			return true
		}
	}
	return false
}

func doublePair(s string) bool {
	for i := 0; i < len(s)-3; i++ {
		a := s[i : i+2]
		if strings.Contains(s[i+2:], a) {
			return true
		}
	}
	return false
}

func hasDoubleWithSpace(s string) bool {
	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+2] {
			return true
		}
	}
	return false
}

func Five(lines []string) {
	p1 := 0
	for _, i := range lines {
		if vowelCount(i) >= 3 && hasDouble(i) && !hasProhibitedSubstring(i) {
			p1++
		}
	}
	fmt.Println(p1)

	p2 := 0
	for _, i := range lines {
		if doublePair(i) && hasDoubleWithSpace(i) {
			p2++
		}
	}
	fmt.Println(p2)
}
