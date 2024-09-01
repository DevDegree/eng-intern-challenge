package main

import (
	"fmt"
	"os"
)

/*
Some questions I had to answer:
Due to the technical requirement:
When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
I am to assume
- numbers will only ever be in the format 123 or 123.123
- no double spaces such as "123 123  123" as one of the spaces would be included in the numbers


*/

func main() {
	argsWithoutProg := os.Args[1:]
	fmt.Printf("%v\n", argsWithoutProg)
}
