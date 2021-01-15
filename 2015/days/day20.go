package days

import (
	"fmt"
	"strconv"
)

func Twenty(lines []string) {
	target, _ := strconv.Atoi(lines[0])

	house := 2
	for {
		elves := 1 + house
		for j := 2; j*j <= house; j++ {
			if j*j == house {
				elves += j
			} else if house%j == 0 {
				elves += j
				elves += house / j
			}
		}
		if elves*10 >= target {
			fmt.Println(house)
			break
		}
		house++
	}

	house = 2
	for {
		elves := house
		if house <= 50 {
			elves += 1
		}
		for j := 2; j*j <= house; j++ {
			if j*j == house && j*50 >= house {
				elves += j
			} else if house%j == 0 {
				if j*50 >= house {
					elves += j
				}
				if (house/j)*50 >= house {
					elves += house / j
				}
			}
		}
		if elves*11 >= target {
			fmt.Println(house)
			break
		}
		house++
	}
}
