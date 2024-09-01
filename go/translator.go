package main

import (
	"fmt"
	"os"
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
