package main

import (
	"fmt"
	"os"
)

func main() {
	argsWithoutProg := os.Args[1:]
	fmt.Printf("%v\n", argsWithoutProg)
}
