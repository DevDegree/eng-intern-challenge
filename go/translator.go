package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var alphabetMap = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....",
	'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
	'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...",
	'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
	'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
	'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
	's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO",
	'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
	'y': "OO.OOO", 'z': "O..OOO", ' ': "......",
}

var numberMap = map[rune]string{
	'1': "O.....", '2': "O.O...", '3': "OO....",
	'4': "OO.O..", '5': "O..O..", '6': "OOO...",
	'7': "OOOO..", '8': "O.OO..", '9': ".OO...",
}

const (
	CAPITAL_BRAILLE = ".....O"
	NUMBER_BRAILLE  = ".O.OOO"
)

func stringToBraille(str string) {
	numCount := 0

	for _, ch := range str {
		switch {
		case unicode.IsUpper(ch):
			fmt.Printf("%s", CAPITAL_BRAILLE)
			fmt.Printf("%s", alphabetMap[unicode.ToLower(ch)])
			numCount = 0
		case unicode.IsDigit(ch):
			if numCount == 0 {
				fmt.Printf("%s", NUMBER_BRAILLE)
			}
			fmt.Printf("%s", numberMap[ch])
			numCount++
		default:
			fmt.Printf("%s", alphabetMap[ch])
			numCount = 0
		}
	}
}

func main() {
	// Check if there are arguments passed
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <param1> <param2> ... <paramN>")
		return
	}

	input_text := strings.Join(os.Args[1:], " ")

	stringToBraille(input_text)
}
