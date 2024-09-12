package main

import (
	"fmt"
	"os"
	"strings"

	"solution/braille"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: translator <input>")
		os.Exit(1)
	}

	input := strings.Join(os.Args[1:], " ")
	output, err := braille.Translate(input)
	fmt.Println(output)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
