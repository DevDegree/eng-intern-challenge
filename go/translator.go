package main

import (
	"fmt"
	"os"
	"strings"
)

// Constants representing special Braille symbols
const (
	CAPITAL      string = ".....O" // Braille symbol indicating the next letter should be capitalized
	NUMBER       string = ".O.OOO" // Braille symbol indicating the following characters are numbers
	SPACE        string = "......" // Braille symbol for a space
	DECIMAL      string = ".O...O" // Braille symbol for a decimal point
	BRAILLE_SIZE int    = 6        // Length of a Braille character
)

// Brille to English Map
var brailleToEngLetterMap = map[string]string{
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

// Braille to English number map
var brailleToNumMap = map[string]string{
	"O.....": "1",
	"O.O...": "2",
	"OO....": "3",
	"OO.O..": "4",
	"O..O..": "5",
	"OOO...": "6",
	"OOOO..": "7",
	"O.OO..": "8",
	".OO...": "9",
	".OOO..": "O",
}

// English to Brille Map
var englishToBrailleMap = map[string]string{
	"a": "O.....",
	"b": "O.O...",
	"c": "OO....",
	"d": "OO.O..",
	"e": "O..O..",
	"f": "OOO...",
	"g": "OOOO..",
	"h": "O.OO..",
	"i": ".OO...",
	"j": ".OOO..",
	"k": "O...O.",
	"l": "O.O.O.",
	"m": "OO..O.",
	"n": "OO.OO.",
	"o": "O..OO.",
	"p": "OOO.O.",
	"q": "OOOOO.",
	"r": "O.OOO.",
	"s": ".OO.O.",
	"t": ".OOOO.",
	"u": "O...OO",
	"v": "O.O.OO",
	"w": ".OOO.O",
	"x": "OO..OO",
	"y": "OO.OOO",
	"z": "O..OOO",
	"1": "O.....",
	"2": "O.O...",
	"3": "OO....",
	"4": "OO.O..",
	"5": "O..O..",
	"6": "OOO...",
	"7": "OOOO..",
	"8": "O.OO..",
	"9": ".OO...",
	"O": ".OOO..",
	" ": "......",
}

// Check if the input character is uppercase
func isBraille(input string) bool {
	for _, char := range input {
		if char != 'O' && char != '.' {
			return false
		}
	}
	return true
}

// Check if the input character is uppercase
func isCapital(inputChar rune) bool {
	if inputChar >= 'A' && inputChar <= 'Z' {
		return true
	}
	return false
}

// Check if the input character is a digit (0-9)
func isNumber(inputChar rune) bool {
	return inputChar >= '0' && inputChar <= '9'
}

// Convert English text to Braille
func englishToBraille(englishStr string) string {
	var result strings.Builder
	var prevChar rune = ' ' // Track the previous character

	for _, englishChar := range englishStr {
		if isCapital(englishChar) { // If character is uppercase
			result.WriteString(CAPITAL) // Add Braille capital indicator
			englishChar += 'a' - 'A'    // Convert to lowercase
		}

		brailleChar, exists := englishToBrailleMap[string(englishChar)]
		if exists {
			if isNumber(englishChar) && prevChar == ' ' { // Check if character is a number
				result.WriteString(NUMBER) // Add Braille number indicator
			}
			result.WriteString(brailleChar) // Add the Braille equivalent
			prevChar = englishChar          // Update previous character
		}
	}
	return result.String()
}

// Convert Braille to English text
func brailleToEnglish(brailleStr string) string {
	var result strings.Builder
	toCapitalize, isNumberMode := false, false // Track capitalization and number modes

	for i := 0; i < len(brailleStr); i += BRAILLE_SIZE {
		if i+BRAILLE_SIZE > len(brailleStr) { // Ensure not to exceed string length
			break
		}

		brailleVal := brailleStr[i : i+BRAILLE_SIZE] // Get each Braille character

		// Handle special Braille indicators
		switch brailleVal {
		case CAPITAL:
			toCapitalize = true
			continue
		case NUMBER:
			isNumberMode = true
			continue
		case SPACE:
			result.WriteString(" ")
			isNumberMode = false
			continue
		}

		// Convert Braille to English based on current mode (number or letter)
		if isNumberMode {
			if englishVal, exists := brailleToNumMap[brailleVal]; exists {
				result.WriteString(englishVal)
			}
		} else {
			if englishVal, exists := brailleToEngLetterMap[brailleVal]; exists {
				if toCapitalize {
					englishVal = strings.ToUpper(englishVal) // Capitalize letter
					toCapitalize = false
				}
				result.WriteString(englishVal)
			}
		}
	}
	return result.String()
}

// Main translation function to determine input type and convert accordingly
func Translator(input string) string {
	if isBraille(input) {
		// translate into English
		return brailleToEnglish(input)
	}
	// translate into Braille
	return englishToBraille(input)
}

func main() {
	// read the input
	inputStr := strings.Join(os.Args[1:], " ")
	// translate the input into correct language
	result := Translator(inputStr)
	// print the output
	fmt.Println(result)
}
