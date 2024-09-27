package main

import (
	"fmt"
	"os"
	"solution/braille"
	"strings"
)

func main() {
	// Check if arguments passed
	if len(os.Args) < 2 {
		fmt.Println("Please provide a sentence in either English or Braille")
		return
	}

	// Convert arguments to string
	args := os.Args[1:]
	sentence := strings.Join(args, " ")

	// Check if sentence is in Braille or English
	if braille.IsBraille(sentence) {
		fmt.Println(braille.ToEnglish(sentence))
	} else {
		fmt.Println(braille.ToBraille(sentence))
	}
}