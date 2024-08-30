package main

import (
	"fmt"
	"os"
	"strings"
)

// englishToBraille maps English characters to their Braille representations
var englishToBraille = map[string]string{
	"a": "O.....", "b": "O.O...",
	"c": "OO....", "d": "OO.O..",
	"e": "O..O..", "f": "OOO...",
	"g": "OOOO..", "h": "O.OO..",
	"i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.",
	"m": "OO..O.", "n": "OO.OO.",
	"o": "O..OO.", "p": "OOO.O.",
	"q": "OOOOO.", "r": "O.OOO.",
	"s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO",
	"w": ".OOO.O", "x": "OO..OO",
	"y": "OO.OOO", "z": "O..OOO",

	" ":       "......",
	"capital": ".....O",
	"number":  ".O.OOO",
}

// numberToBraille maps numbers to their Braille representations
/*
	NOTE:- Here the correct braille representaitions for numbers were picked, these dont pass the test!
	to pass the test case use these
	"0": "O.....", "1": "O.O...",
    "2": "OO....", "3": "OO.O..",
    "4": "O..O..", "5": "OOO...",
    "6": "OOOO..", "7": "O.OO..",
    "8": ".OO...", "9": ".OOO..",

	UPDATE: Fixed!
*/

var numberToBraille = map[string]string{
	"0": ".OOO..", "1": "O.....",
	"2": "O.O...", "3": "OO....",
	"4": "OO.O..", "5": "O..O..",
	"6": "OOO...", "7": "OOOO..",
	"8": "O.OO..", "9": ".OO...",
}

// isBraille checks if the input string is a valid Braille representation
func isBraille(input string) bool {
	return strings.ContainsAny(input, "O.") && len(input)%6 == 0
}

// translateToBraille converts an English string to Braille
func translateToBraille(input string) string {
	var braille string
	inNumberSequence := false
	for _, char := range input {
		c := string(char)

		// Handle capitalization
		if c >= "A" && c <= "Z" {
			braille += englishToBraille["capital"]
			c = strings.ToLower(c)
			inNumberSequence = false
		}

		// Handle numbers
		if c >= "0" && c <= "9" {
			if !inNumberSequence {
				braille += englishToBraille["number"]
				inNumberSequence = true
			}
			braille += numberToBraille[c]
		} else {
			inNumberSequence = false
		}

		// Translate character to Braille
		if brailleChar, ok := englishToBraille[c]; ok {
			braille += brailleChar
		}
	}

	return braille
}

// translateToEnglish converts a Braille string to English
func translateToEnglish(input string) string {
	var english string
	isCapital := false
	isNumber := false

	// Process input in chunks of 6 characters (one Braille cell)
	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6]

		switch brailleChar {
		case englishToBraille["capital"]:
			isCapital = true
		case englishToBraille["number"]:
			isNumber = true
		case englishToBraille[" "]:
			isNumber = false
			english += " "
		default:
			if isNumber {
				english += brailleToNumber[brailleChar]
			} else {
				engChar := brailleToEnglish[brailleChar]
				if isCapital {
					engChar = strings.ToUpper(engChar)
					isCapital = false
				}
				english += engChar
			}

		}
	}
	return english
}

// brailleToEnglish and brailleToNumber are reverse mappings for translation
var brailleToEnglish = make(map[string]string)
var brailleToNumber = make(map[string]string)

// init initializes the reverse mappings
func init() {
	for k, v := range englishToBraille {
		brailleToEnglish[v] = k
	}
	for k, v := range numberToBraille {
		brailleToNumber[v] = k
	}
}

func main() {
	// Check if input is provided
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate.")
		return
	}

	// Join all arguments into a single string
	input := strings.Join(os.Args[1:], " ")

	var result string
	if isBraille(input) {
		result = translateToEnglish(input)
	} else {
		result = translateToBraille(input)
	}
	fmt.Println(result)
}
