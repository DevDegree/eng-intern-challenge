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
	input = strings.Join(os.Args[1:], " ")
}
