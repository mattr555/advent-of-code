package days

import (
	"fmt"
	"strconv"
	"strings"
)

func runComputerProgram(lines []string, a, b int) int {
	ip := 0
	for ip < len(lines) {
		s := strings.Split(lines[ip], " ")
		switch s[0] {
		case "hlf":
			if s[1] == "a" {
				a /= 2
			} else {
				b /= 2
			}
		case "tpl":
			if s[1] == "a" {
				a *= 3
			} else {
				b *= 3
			}
		case "inc":
			if s[1] == "a" {
				a++
			} else {
				b++
			}
		case "jmp":
			n, _ := strconv.Atoi(s[1])
			ip += n - 1
		case "jie":
			n, _ := strconv.Atoi(s[2])
			if (s[1] == "a," && a%2 == 0) || (s[1] == "b," && b%2 == 0) {
				ip += n - 1
			}
		case "jio":
			n, _ := strconv.Atoi(s[2])
			if (s[1] == "a," && a == 1) || (s[1] == "b," && b == 1) {
				ip += n - 1
			}
		}
		ip++
	}
	return b
}

func Twentythree(lines []string) {
	fmt.Println(runComputerProgram(lines, 0, 0))
	fmt.Println(runComputerProgram(lines, 1, 0))
}
