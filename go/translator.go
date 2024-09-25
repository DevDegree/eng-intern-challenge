package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var brailleAlphabet = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO", ' ': "......",
}

var brailleNumbers = map[rune]string{
	'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}

var capitalSymbol = ".....O"
var numberSymbol = ".O.OOO"

var englishAlphabet = make(map[string]rune)
var englishNumbers = make(map[string]rune)

func initEnglishMaps() {
	for letter, braille := range brailleAlphabet {
		englishAlphabet[braille] = letter
	}
	for digit, braille := range brailleNumbers {
		englishNumbers[braille] = digit
	}
}

// A braille string will only contain 'O' and '.'
// However if the string is not divisible by 6 assume it is not braille
func isBraille(inputString string) bool {
	if len(inputString)%6 != 0 {
		return false
	}
	for _, val := range inputString {
		if val != 'O' && val != '.' {
			return false
		}
	}
	return true
}

func isCapital(char rune) bool {
	return unicode.IsUpper(char)
}

func convertToBraille(englishString string) string {
	var output strings.Builder
	isInputtingNumbers := false

	for _, char := range englishString {
		if isCapital(char) {
			output.WriteString(capitalSymbol)
			char = unicode.ToLower(char)
		}

		if char >= '0' && char <= '9' {
			if !isInputtingNumbers {
				output.WriteString(numberSymbol)
				isInputtingNumbers = true
			}
			output.WriteString(brailleNumbers[char])
		} else {
			isInputtingNumbers = false
			output.WriteString(brailleAlphabet[char])
		}
	}
	return output.String()
}

// Converts the long braille string into array of symbols (6 chars)
func intoBrailleSymbols(brailleString string) []string {
	var output []string
	for i := 0; i < len(brailleString); i += 6 {
		output = append(output, brailleString[i:i+6])
	}
	return output
}

func convertToEnglish(brailleString string) string {
	initEnglishMaps()
	var output strings.Builder
	isCapitalMode := false
	isInputtingNumbers := false
	symbols := intoBrailleSymbols(brailleString)

	var char rune
	for _, symbol := range symbols {
		if symbol == capitalSymbol {
			isCapitalMode = true
		} else if symbol == numberSymbol {
			isInputtingNumbers = true
		} else {
			if isInputtingNumbers {
				char = englishNumbers[symbol]
			} else {
				char = englishAlphabet[symbol]
				if isCapitalMode {
					char = unicode.ToUpper(char)
					isCapitalMode = false
				}
			}

			output.WriteRune(char)

			if char == ' ' {
				isInputtingNumbers = false
			}
		}
	}

	return output.String()
}

func main() {
	// Join all arguments with a space between them
	input := strings.Join(os.Args[1:], " ")
	var output strings.Builder
	if len(os.Args) > 1 {
		// Check if input is Braille or English
		if isBraille(input) {
			output.WriteString(convertToEnglish(input))
		} else {
			output.WriteString(convertToBraille(input))
		}

		fmt.Println(output.String())
	} else {
		fmt.Println("Error! No input")
	}
}
