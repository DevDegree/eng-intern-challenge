package main

import (
	"fmt"
	"os"
	"strings"
)

/** Constants */
var brailleDict = map[string]string{
	"a":   "O.....",
	"b":   "O.O...",
	"c":   "OO....",
	"d":   "OO.O..",
	"e":   "O..O..",
	"f":   "OOO...",
	"g":   "OOOO..",
	"h":   "O.OO..",
	"i":   ".OO...",
	"j":   ".OOO..",
	"k":   "O...O.",
	"l":   "O.O.O.",
	"m":   "OO..O.",
	"n":   "OO.OO.",
	"o":   "O..OO.",
	"p":   "OOO.O.",
	"q":   "OOOOO.",
	"r":   "O.OOO.",
	"s":   ".OO.O.",
	"t":   ".OOOO.",
	"u":   "O...OO",
	"v":   "O.O.OO",
	"w":   ".OOO.O",
	"x":   "OO..OO",
	"y":   "OO.OOO",
	"z":   "O..OOO",
	"CAP": ".....O",
	"NUM": ".O.OOO",
	" ":   "......",
	"0":   ".OOO..",
	"1":   "O.....",
	"2":   "O.O...",
	"3":   "OO....",
	"4":   "OO.O..",
	"5":   "O..O..",
	"6":   "OOO...",
	"7":   "OOOO..",
	"8":   "O.OO..",
	"9":   ".OO...",
}

var reverseBrailleLetters = map[string]string{
	"O.....": "a",
	"O.O...": "b",
	"OO....": "c",
	"OO.O..": "d",
	"O..O..": "e",
	"OOO...": "f",
	"OOOO..": "g",
	"O.OO..": "h",
	".OO...": "i",
	".OOO..": "j",
	"O...O.": "k",
	"O.O.O.": "l",
	"OO..O.": "m",
	"OO.OO.": "n",
	"O..OO.": "o",
	"OOO.O.": "p",
	"OOOOO.": "q",
	"O.OOO.": "r",
	".OO.O.": "s",
	".OOOO.": "t",
	"O...OO": "u",
	"O.O.OO": "v",
	".OOO.O": "w",
	"OO..OO": "x",
	"OO.OOO": "y",
	"O..OOO": "z",
}

var reverseSpecialCharacters = map[string]string{
	".O.OOO": "NUM",
	"......": " ",
}

var reverseBrailleNumbers = map[string]string{
	".OOO..": "0",
	"O.....": "1",
	"O.O...": "2",
	"OO....": "3",
	"OO.O..": "4",
	"O..O..": "5",
	"OOO...": "6",
	"OOOO..": "7",
	"O.OO..": "8",
	".OO...": "9",
}

/**
 * Checks if the given string consists only of the characters 'O' and '.'.
 * @param {string} str - The string to check.
 * @returns {boolean} - Returns true if all characters in the string are either 'O' or '.', otherwise false.
 */
func checkIsBraille(str string) bool {
	for _, c := range str {
		if c != 'O' && c != '.' {
			return false
		}
	}
	return len(str)%6 == 0
}

/**
 * Checks if the given character is an uppercase letter.
 * @param {string} char - The character to check.
 * @returns {boolean} - Returns true if the character is an uppercase letter, otherwise false.
 */
func isCapitalLetter(char rune) bool {
	return char >= 'A' && char <= 'Z'
}

/**
 * Checks if the given character is a lowercase letter.
 * @param {string} char - The character to check.
 * @returns {boolean} - Returns true if the character is a lowercase letter, otherwise false.
 */
func isLowerLetter(char rune) bool {
	return char >= 'a' && char <= 'z'
}

/**
 * Checks if the given character is a numeric digit.
 * @param {string} char - The character to check.
 * @returns {boolean} - Returns true if the character is a numeric digit, otherwise false.
 */
func isNumeric(char rune) bool {
	return char >= '0' && char <= '9'
}

/**
 * Converts a string of English text into Braille representation.
 * @param {string} str - The string to convert to Braille.
 * @returns {string} - The Braille representation of the input string.
 */
func englishToBraille(str string) string {
	numericState := false
	result := ""

	for _, char := range str {
		var newChar string

		if isCapitalLetter(char) {
			newChar = brailleDict["CAP"] + brailleDict[strings.ToLower(string(char))]
		} else if isLowerLetter(char) {
			newChar = brailleDict[string(char)]
		} else if isNumeric(char) {
			newChar = brailleDict[string(char)]
			if !numericState {
				numericState = true
				newChar = brailleDict["NUM"] + newChar
			}
		} else if char == ' ' {
			if numericState {
				numericState = false
			}
			newChar = brailleDict[" "]
		}

		result += newChar
	}

	return result
}

/**
 * Converts a string of Braille representation into English text.
 * @param {string} str - The Braille string to convert to English.
 * @returns {string} - The English text representation of the input Braille string.
 */
func brailleToEnglish(str string) string {
	result := ""
	numericState := false

	for i := 0; i < len(str); i += 6 {
		char := str[i : i+6]
		var newChar string

		if char == brailleDict["NUM"] {
			numericState = true
		} else if char == brailleDict[" "] {
			if numericState {
				numericState = false
			}
			newChar = " "
		} else if numericState {
			newChar = reverseBrailleNumbers[char]
		} else if char == brailleDict["CAP"] {
			i += 6
			nextChar := str[i : i+6]
			newChar = strings.ToUpper(reverseBrailleLetters[nextChar])
		} else {
			newChar = reverseBrailleLetters[char]
		}

		result += newChar
	}

	return result
}

func main() {
	// Gets input from command line arguments
	inputString := strings.Join(os.Args[1:], " ")

	// Checks if the input string is Braille
	isBraille := checkIsBraille(inputString)

	// Converts the input string based on whether it is Braille or English
	var result string
	if isBraille {
		result = brailleToEnglish(inputString)
	} else {
		result = englishToBraille(inputString)
	}

	fmt.Println(result)
}
