package days

import "fmt"

func incrementPassword(pw []byte) {
	for i := len(pw) - 1; i >= 0; i-- {
		if pw[i] == 'z' {
			pw[i] = 'a'
		} else {
			pw[i]++
			return
		}
	}
}

func hasIncreasingStraight(pw []byte) bool {
	for i := 0; i < len(pw)-3; i++ {
		if pw[i] == (pw[i+1]-1) && pw[i] == (pw[i+2]-2) {
			return true
		}
	}
	return false
}

func hasDisallowedLetters(pw []byte) bool {
	for i := 0; i < len(pw); i++ {
		if pw[i] == 'i' || pw[i] == 'o' || pw[i] == 'l' {
			return true
		}
	}
	return false
}

func hasTwoNonOverlappingPairs(pw []byte) bool {
	pairCount := 0
	i := 0
	for i < len(pw)-1 {
		if pw[i] == pw[i+1] {
			pairCount++
			i += 2
		} else {
			i++
		}
	}
	return pairCount >= 2
}

func validatePassword(pw []byte) bool {
	return hasIncreasingStraight(pw) && !hasDisallowedLetters(pw) && hasTwoNonOverlappingPairs(pw)
}

func Eleven(lines []string) {
	s := []byte(lines[0])
	for !validatePassword(s) {
		incrementPassword(s)
	}
	fmt.Println(string(s))
	incrementPassword(s)
	for !validatePassword(s) {
		incrementPassword(s)
	}
	fmt.Println(string(s))
}
