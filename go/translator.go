package main

import (
	"fmt"
	"os"
	"strings"
)

// Braille constants
const (
	CapitalFollows = ".....O"
	DecimalFollows = ".O...O"
	NumberFollows  = ".O.OOO"
	Space          = "......"
)

// Braille map for letters
var brailleMap = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
	".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
	";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
	"(": "O.O..O", ")": ".O.OO.",
}

// Braille map for numbers
var numberMap = map[string]string{
	"1": "O.....",
	"2": "O.O...",
	"3": "OO....",
	"4": "OO.O..",
	"5": "O..O..",
	"6": "OOO...",
	"7": "OOOO..",
	"8": "O.OO..",
	"9": ".OO...",
	"0": ".OOO..",
}

var reverseNumberMap map[string]string

var reverseBrailleMap map[string]string

// Initialize the maps
func init() {
	reverseBrailleMap = make(map[string]string)
	for k, v := range brailleMap {
		reverseBrailleMap[v] = k
	}
	reverseNumberMap = make(map[string]string)
	for k, v := range numberMap {
		reverseNumberMap[v] = k
	}
}

// Convert English to Braille
func toBraille(input string) string {
	var result strings.Builder
	isNumber := false

	for _, char := range input {
		if char == ' ' {
			result.WriteString(Space)
			isNumber = false
			continue
		}

		lowerChar := strings.ToLower(string(char))

		if char >= '0' && char <= '9' {
			if !isNumber {
				result.WriteString(NumberFollows)
				isNumber = true
			}
			result.WriteString(numberMap[string(char)])
		} else {
			isNumber = false
			if char >= 'A' && char <= 'Z' {
				result.WriteString(CapitalFollows)
			}
			if val, ok := brailleMap[lowerChar]; ok {
				result.WriteString(val)
			}
		}
	}
	return result.String()
}

// Convert Braille to English
func toEnglish(input string) string {
	var result strings.Builder
	var isCapital, isNumber bool
	for i := 0; i < len(input); i += 6 {
		if i+6 > len(input) {
			break
		}
		char := input[i : i+6]

		switch char {
		case CapitalFollows:
			isCapital = true
			continue
		case NumberFollows:
			isNumber = true
			continue
		case Space:
			result.WriteString(" ")
		default:
			if isNumber {
				if val, ok := reverseNumberMap[char]; ok {
					result.WriteString(val)
				} else {
					isNumber = false
					i -= 6
				}
			} else if val, ok := reverseBrailleMap[char]; ok {
				if isCapital {
					result.WriteString(strings.ToUpper(val))
					isCapital = false
				} else {
					result.WriteString(val)
				}
			} else {
				fmt.Printf("Unknown character: %s\n", char)
			}
		}
	}
	return result.String()
}

func main() {
	if len(os.Args) <= 1 {
		fmt.Println("Usage: translator <text>")
		return
	}

	input := strings.Join(os.Args[1:], " ")
	if isBraille(input) {
		fmt.Println(toEnglish(input))
	} else {
		fmt.Println(toBraille(input))
	}
}

// Helper function to check if the input is valid Braille
func isBraille(input string) bool {
	validChars := "O."
	for _, char := range input {
		if !strings.ContainsRune(validChars, char) {
			return false
		}
	}
	return len(input)%6 == 0
}
