package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	var input string
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate")
		return
	}
	// Join with a space to preservce spaces in input.
	input = strings.TrimSpace(strings.Join(os.Args[1:], " "))
}

// IsEnglish is a function that returns true if the input is english, and false if the input is braille.
func IsEnglish(input string) bool {
	const (
		dotRune      = '.'
		capitalORune = 'O'
	)
	for _, r := range input {
		isBrailleRune := (r == dotRune || r == capitalORune)
		if !isBrailleRune {
			return true
		}
	}
	return false
}
