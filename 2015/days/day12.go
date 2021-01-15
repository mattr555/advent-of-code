package days

import (
	"encoding/json"
	"fmt"
	"strings"
)

func parseList(dec *json.Decoder) (p1, p2 float64) {
	for dec.More() {
		t, _ := dec.Token()
		switch v := t.(type) {
		case float64:
			p1 += v
			p2 += v
		case json.Delim:
			switch v {
			case '{':
				tp1, tp2 := parseObject(dec)
				p1 += tp1
				p2 += tp2
			case '[':
				tp1, tp2 := parseList(dec)
				p1 += tp1
				p2 += tp2
			}
		}
	}
	dec.Token()
	return p1, p2
}

func parseObject(dec *json.Decoder) (p1, p2 float64) {
	readingKey := true
	hasRed := false
	for dec.More() {
		t, _ := dec.Token()
		switch v := t.(type) {
		case string:
			if v == "red" && !readingKey {
				hasRed = true
			}
		case float64:
			p1 += v
			p2 += v
		case json.Delim:
			switch v {
			case '{':
				tp1, tp2 := parseObject(dec)
				p1 += tp1
				p2 += tp2
			case '[':
				tp1, tp2 := parseList(dec)
				p1 += tp1
				p2 += tp2
			}
		}

		readingKey = !readingKey
	}
	dec.Token()
	if hasRed {
		p2 = 0
	}
	return p1, p2
}

func Twelve(lines []string) {
	s := lines[0]
	dec := json.NewDecoder(strings.NewReader(s))
	p1, p2 := 0.0, 0.0
	firstTok, _ := dec.Token()
	switch firstTok.(json.Delim) {
	case '[':
		p1, p2 = parseList(dec)
	case '{':
		p1, p2 = parseObject(dec)
	}

	fmt.Println(p1)
	fmt.Println(p2)
}
