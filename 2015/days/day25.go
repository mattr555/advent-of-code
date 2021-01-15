package days

import (
	"fmt"
	"regexp"
	"strconv"
)

//copied from some random go playground
//computes a**b % m
func powMod(a, b, m int) int {
	a = a % m
	p := 1 % m
	for b > 0 {
		if b&1 != 0 {
			p = (p * a) % m
		}
		b >>= 1
		a = (a * a) % m
	}
	return p
}

func Twentyfive(lines []string) {
	reg := regexp.MustCompile(`To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).`)
	m := reg.FindSubmatch([]byte(lines[0]))
	r, _ := strconv.Atoi(string(m[1]))
	c, _ := strconv.Atoi(string(m[2]))
	nOnDiagsBefore := (r + c - 2) * (r + c - 1) / 2
	pow := nOnDiagsBefore + c - 1
	const mod = 33554393
	factor := powMod(252533, pow, mod)
	fmt.Println(20151125 * factor % mod)
}
