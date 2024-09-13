package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var brailleMap = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
	'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
	'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
	'z': "O..OOO", ' ': "......",
}

var numberMap = map[rune]string{
	'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
	'6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}

const (
	capitalSymbol = ".....O"
	numberSymbol  = ".O.OOO"
)

func translateToBraille(input string) string {
	var result strings.Builder
	isNumber := false

	for i, char := range input {
		if unicode.IsUpper(char) {
			result.WriteString(capitalSymbol)
			char = unicode.ToLower(char)
		}

		if unicode.IsDigit(char) {
			if !isNumber {
				result.WriteString(numberSymbol)
				isNumber = true
			}
			result.WriteString(numberMap[char])
		} else {
			isNumber = false
			result.WriteString(brailleMap[char])
		}

		if i < len(input)-1 && unicode.IsDigit(rune(input[i+1])) && !unicode.IsDigit(char) {
			result.WriteString(numberSymbol)
			isNumber = true
		}
	}

	return result.String()
}

func translateToText(input string) string {
	var result strings.Builder
	isCapital := false
	isNumber := false

	for i := 0; i < len(input); i += 6 {
		if i+6 > len(input) {
			break
		}

		symbol := input[i : i+6]

		if symbol == capitalSymbol {
			isCapital = true
			continue
		}

		if symbol == numberSymbol {
			isNumber = true
			continue
		}

		if symbol == "......" {
			result.WriteRune(' ')
			isNumber = false
			continue
		}

		var char rune
		if isNumber {
			for digit, braille := range numberMap {
				if braille == symbol {
					char = digit
					break
				}
			}
		} else {
			for letter, braille := range brailleMap {
				if braille == symbol {
					char = letter
					break
				}
			}
		}

		if isCapital {
			char = unicode.ToUpper(char)
			isCapital = false
		}

		result.WriteRune(char)
	}

	return result.String()
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide input text or Braille.")
		return
	}

	input := strings.Join(os.Args[1:], " ")

	if strings.ContainsAny(input, "O.") && len(input)%6 == 0 {
		fmt.Print(translateToText(input))
	} else {
		fmt.Print(translateToBraille(input))
	}
}
