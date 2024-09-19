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
	' ': "......",
}

const (
	CAPITAL_BRAILLE = ".....O"
	NUMBER_BRAILLE  = ".O.OOO"
)

var brailleToAlphabetMap = reverseMap(alphabetMap)
var brailleToNumberMap = reverseMap(numberMap)

func reverseMap(m map[rune]string) map[string]rune {
	result := make(map[string]rune, len(m))

	for k, v := range m {
		result[v] = k
	}
	return result
}

func stringToBraille(str string) {
	numberMode := false

	for _, ch := range str {
		switch {
		case unicode.IsUpper(ch):
			fmt.Print(CAPITAL_BRAILLE)
			fmt.Print(alphabetMap[unicode.ToLower(ch)])
			numberMode = false
		case unicode.IsDigit(ch):
			if !numberMode {
				fmt.Print(NUMBER_BRAILLE)
				numberMode = true
			}
			fmt.Print(numberMap[ch])
		default:
			fmt.Print(alphabetMap[ch])
			numberMode = false
		}
	}
}

func brailleToString(braille string) {
	if len(braille)%6 != 0 {
		return
	}

	capitalize := false
	number := false

	for i := 0; i < len(braille); i += 6 {
		cell := braille[i : i+6]
		switch {
		case cell == CAPITAL_BRAILLE:
			capitalize = true
			number = false
		case capitalize:
			fmt.Printf("%c", unicode.ToUpper(brailleToAlphabetMap[cell]))
			capitalize = false
			number = false
		case cell == NUMBER_BRAILLE:
			number = true
		case number:
			fmt.Printf("%c", brailleToNumberMap[cell])
		default:
			fmt.Printf("%c", brailleToAlphabetMap[cell])
			number = false
		}
	}
}

func isBraille(str string) bool {
	allowedChars := map[rune]bool{
		'O': true,
		'.': true,
	}

	// Ensure string only contains . and O
	for _, ch := range str {
		if !allowedChars[ch] {
			return false
		}
	}

	// Ensure string is a multiple of 6
	return len(str)%6 == 0
}

func main() {
	// Check if there are arguments passed
	if len(os.Args) < 2 {
		return
	}

	input_text := strings.Join(os.Args[1:], " ")

	if isBraille(input_text) {
		brailleToString(input_text)
	} else {
		stringToBraille(input_text)
	}
}
