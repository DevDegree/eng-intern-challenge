package main

import (
	"fmt"
	"os"
	"strings"
)

const (
	CapitalIndicator = ".....O"
	NumberIndicator  = ".O.OOO"
	BrailleSpace     = "......"
)

// Braille patterns for letters
var brailleAlphabet = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
}

// Braille patterns for numbers
var brailleNumbers = map[string]string{
	"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
	"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

// Special Braille patterns
var brailleSpecial = map[string]string{
	"CAP": CapitalIndicator,
	"NUM": NumberIndicator,
	" ":   BrailleSpace,
}

// Translate English text to Braille
func translateToBraille(text string) string {
	var result strings.Builder
	numberMode := false

	for _, char := range text {
		c := string(char)
		if c >= "A" && c <= "Z" { // Handle uppercase letters
			result.WriteString(brailleSpecial["CAP"])
			c = strings.ToLower(c)
		}

		if c >= "0" && c <= "9" { // Handle digits
			if !numberMode {
				result.WriteString(brailleSpecial["NUM"])
				numberMode = true
			}
			result.WriteString(brailleNumbers[c])
		} else {
			if braille, exists := brailleAlphabet[c]; exists {
				result.WriteString(braille)
			} else {
				result.WriteString(BrailleSpace) // Default to space for unknown characters
			}
			numberMode = false
		}
	}
	return result.String()
}

// Translate Braille to English text
func translateToEnglish(braille string) string {
	words := strings.Fields(braille)
	var result strings.Builder
	capitalizeNext := false
	numberMode := false

	for _, word := range words {
		switch word {
		case CapitalIndicator:
			capitalizeNext = true
		case NumberIndicator:
			numberMode = true
		default:
			if numberMode {
				for num, code := range brailleNumbers {
					if word == code {
						result.WriteString(num)
						break
					}
				}
				numberMode = false
			} else {
				for letter, code := range brailleAlphabet {
					if word == code {
						if capitalizeNext {
							result.WriteString(strings.ToUpper(letter))
							capitalizeNext = false
						} else {
							result.WriteString(letter)
						}
						break
					}
				}
			}
		}
	}
	return result.String()
}

// Determine if input is Braille
func isBraille(input string) bool {
	return strings.ContainsAny(input, "O.")
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: braille-translator <text>")
		return
	}

	input := strings.Join(os.Args[1:], " ")

	var result string
	if isBraille(input) {
		result = translateToEnglish(input)
	} else {
		result = translateToBraille(input)
	}

	fmt.Println(result)
}
