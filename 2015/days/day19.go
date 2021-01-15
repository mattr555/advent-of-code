package days

import (
	"fmt"
	"strings"
)

/*
TODO: cheated by looking at the solution thread

Transformations only of the form

X => X X
X => X Rn X Ar
X => X Rn X Y X Ar
X => X Rn X Y X Y X Ar
*/

type transformation struct {
	in  string
	out string
}

func runTransform(transformations []transformation, currentStep map[string]bool) map[string]bool {
	ret := map[string]bool{}
	for molecule := range currentStep {
		for _, trans := range transformations {
			s := strings.Split(molecule, trans.in)
			for replace := 0; replace < len(s)-1; replace++ {
				b := strings.Builder{}
				for i := 0; i < len(s)-1; i++ {
					b.WriteString(s[i])
					if i == replace {
						b.WriteString(trans.out)
					} else {
						b.WriteString(trans.in)
					}
				}
				b.WriteString(s[len(s)-1])
				ret[b.String()] = true
			}
		}
	}
	return ret
}

func Nineteen(lines []string) {
	transformations := make([]transformation, len(lines)-2)
	reversed := make([]transformation, len(lines)-2)
	molecule := lines[len(lines)-1]

	for ix, t := range lines[:len(lines)-2] {
		in := strings.Split(t, " => ")[0]
		out := strings.Split(t, " => ")[1]
		transformations[ix] = transformation{in, out}
		reversed[ix] = transformation{out, in}
	}

	fmt.Println(len(runTransform(transformations, map[string]bool{molecule: true})))

	thisStep := map[string]bool{
		molecule: true,
	}

	c := 0
	for {
		nextStep := runTransform(reversed, thisStep)
		thisStep = nextStep
		c++
		if _, ok := thisStep["e"]; ok {
			break
		}
		fmt.Println(c)
	}
	fmt.Println(c)
}
