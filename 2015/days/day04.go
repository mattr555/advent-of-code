package days

import (
	"crypto/md5"
	"fmt"
)

func Four(lines []string) {
	prefix := lines[0]
	p1Found := false
	for i := 1; ; i++ {
		s := fmt.Sprintf("%s%d", prefix, i)
		h := md5.Sum([]byte(s))
		if !p1Found && h[0] == 0 && h[1] == 0 && h[2]&0xf0 == 0 {
			fmt.Printf("%d: %x\n", i, h)
			p1Found = true
		}
		if h[0] == 0 && h[1] == 0 && h[2] == 0 {
			fmt.Printf("%d: %x\n", i, h)
			break
		}
	}
}
