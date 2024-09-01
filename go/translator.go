package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate.")
		return
	}

	input := os.Args[1]

	fmt.Println(input)

	// if isBraille(input) {
	// 	fmt.Println(translateToEnglish(input))
	// } else {
	// 	fmt.Println(translateToBraille(input))
	// }
}

// isBraille checks if the input string is in Braille format
func isBraille(input string) bool {
	return strings.ContainsAny(input, "O.")
}
