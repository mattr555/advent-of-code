package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"time"

	days "./days"
)

var dayMap = map[string]func([]string){
	"1":  days.One,
	"2":  days.Two,
	"3":  days.Three,
	"4":  days.Four,
	"5":  days.Five,
	"6":  days.Six,
	"7":  days.Seven,
	"8":  days.Eight,
	"9":  days.Nine,
	"10": days.Ten,
	"11": days.Eleven,
	"12": days.Twelve,
	"13": days.Thirteen,
	"14": days.Fourteen,
	"15": days.Fifteen,
	"16": days.Sixteen,
	"17": days.Seventeen,
	"18": days.Eighteen,
	"19": days.Nineteen,
	"20": days.Twenty,
	"21": days.Twentyone,
}

func main() {
	d := os.Args[1]
	callFunc, ok := dayMap[d]
	if !ok {
		panic("day not found")
	}

	n, _ := strconv.Atoi(d)
	filename := fmt.Sprintf("data/day%02d.txt", n)
	if len(os.Args) > 2 {
		filename = os.Args[2]
	}

	filecontents, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(fmt.Sprintf("bad file %s", filename))
	}

	start := time.Now()
	callFunc(strings.Split(strings.Trim(string(filecontents), "\n"), "\n"))
	elapsed := time.Since(start)
	fmt.Printf("execution took %s\n", elapsed)
}
