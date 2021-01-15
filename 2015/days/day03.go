package days

import "fmt"

type vertex struct {
	x, y int
}

var directions = map[rune]vertex{
	'^': {0, 1},
	'>': {1, 0},
	'v': {0, -1},
	'<': {-1, 0},
}

func Three(lines []string) {
	s := lines[0]
	x, y := 0, 0
	visited := map[vertex]bool{}
	for _, i := range s {
		visited[vertex{x, y}] = true
		v, _ := directions[i]
		x += v.x
		y += v.y
	}
	visited[vertex{x, y}] = true
	fmt.Println(len(visited))

	visited = map[vertex]bool{}
	sx, sy := 0, 0
	rx, ry := 0, 0
	for i := 0; i < len(s); i += 2 {
		visited[vertex{sx, sy}] = true
		visited[vertex{rx, ry}] = true
		v, _ := directions[rune(s[i])]
		sx += v.x
		sy += v.y
		v, _ = directions[rune(s[i+1])]
		rx += v.x
		ry += v.y
	}
	visited[vertex{sx, sy}] = true
	visited[vertex{rx, ry}] = true
	fmt.Println(len(visited))
}
