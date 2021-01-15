package days

import (
	"fmt"
	"regexp"
	"strconv"
)

type reindeer struct {
	speed, flightTime, restTime int
	points                      int
}

func (r *reindeer) distance(time int) int {
	//slightly overkill but want to practice a method
	periodLength := r.flightTime + r.restTime
	fullPeriods := time / periodLength
	leftoverTime := time % periodLength
	var lastDist int
	if leftoverTime > r.flightTime {
		lastDist = r.speed * r.flightTime
	} else {
		lastDist = r.speed * leftoverTime
	}
	return lastDist + (r.speed * fullPeriods * r.flightTime)
}

const totalTime = 2503

func Fourteen(lines []string) {
	reg := regexp.MustCompile(`\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.`)
	p1 := 0
	reindeers := make([]reindeer, len(lines))
	for ix, l := range lines {
		matches := reg.FindSubmatch([]byte(l))
		s, _ := strconv.Atoi(string(matches[1]))
		ft, _ := strconv.Atoi(string(matches[2]))
		rt, _ := strconv.Atoi(string(matches[3]))
		r := reindeer{
			speed:      s,
			flightTime: ft,
			restTime:   rt,
		}
		d := r.distance(totalTime)
		if d > p1 {
			p1 = d
		}
		reindeers[ix] = r
	}
	fmt.Println(p1)

	for t := 1; t <= totalTime; t++ {
		bestDist, bestIx := 0, -1
		for ix := range reindeers {
			d := reindeers[ix].distance(t)
			if d > bestDist {
				bestDist = d
				bestIx = ix
			}
		}
		reindeers[bestIx].points++
	}

	p2 := 0
	for _, v := range reindeers {
		if v.points > p2 {
			p2 = v.points
		}
	}
	fmt.Println(p2)
}
