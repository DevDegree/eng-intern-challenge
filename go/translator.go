package main

import (
	"fmt"
	"os"
)

const (
	BRAILLE_SPACE           = "......"
	BRAILLE_CAPITAL_FOLLOWS = ".....O"
	BRAILLE_DECIMAL_FOLLOWS = ".O...O"
	BRAILLE_NUMBER_FOLLOWS  = ".O.OOO"
)

func main() {
	argsWithoutProg := os.Args[1:]
	fmt.Printf("%v\n", argsWithoutProg)
}
