package main

import (
	"fmt"
	"os"
	"strings"
)

// English letter Braille sequence to character mapping
var brailleToEnglishChar = map[string]string{
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

// Special character Braille sequence to meaning mapping
var brailleToEnglishSpecial = map[string]string{
	"O.....": "1",
	"O.O...": "2",
	"OO....": "3",
	"OO.O..": "4",
	"O..O..": "5",
	"OOO...": "6",
	"OOOO..": "7",
	"O.OO..": "8",
	".OO...": "9",
	".OOO..": "0",
	".....O": "CAPITAL",
	".O...O": "DECIMAL",
	".O.OOO": "NUMBER",
	"..OO.O": ".",
	"..O...": ",",
	"..O.OO": "?",
	"..OOO.": "!",
	"..OO..": ":",
	"..O.O.": ";",
	"....OO": "-",
	".O..O.": "/",
	".OO..O": "<",
	"O..OO.": ">",
	"O.O..O": "(",
	".O.OO.": ")",
	"......": " ",
}

func translateBrailleToEnglish(input string) (englishString string) {

	readingMode := "STRING"
	for brailleIndex := 0; brailleIndex < len(input); brailleIndex += 6 {
		brailleSequence := input[brailleIndex : brailleIndex+6]

		// Default reading mode
		if readingMode == "STRING" {
			// Lowercase letter case
			character, characterExists := brailleToEnglishChar[brailleSequence]
			if characterExists {
				englishString += character

			} else { // All other cases use special characters
				character = brailleToEnglishSpecial[brailleSequence]
				// Set reading mode for the capital letter delimiter
				if character == "CAPITAL" {
					readingMode = "CAPITAL"

					// Decimal delimiter is unexplained - we assume it is same as the
					// number delimiter, except with the possible occurrence of a decimal point
				} else if character == "NUMBER" || character == "DECIMAL" {
					readingMode = "NUMBER"

				} else { // Case for all other special characters
					englishString += character
				}
			}

			// Flag set when we are reading a number, including only 0-9 and a decimal point
		} else if readingMode == "NUMBER" {
			character := brailleToEnglishSpecial[brailleSequence]
			englishString += character
			// reset to default reading mode after a space
			if character == " " {
				readingMode = "STRING"
			}

			// Flag set when this character is a capital letter
		} else if readingMode == "CAPITAL" {
			character := brailleToEnglishChar[brailleSequence]
			englishString += strings.ToUpper(character)
			readingMode = "STRING"
		}
	}

	return
}

func translateEnglishToBraille(input string) (brailleString string) {

	// Using the braille mapping, create a reverse english to braille mapping
	englishToBraille := make(map[string]string)
	// Add all lowercase letters
	for brailleSequence, character := range brailleToEnglishChar {
		englishToBraille[character] = brailleSequence
	}
	// Add all special letters
	for brailleSequence, character := range brailleToEnglishSpecial {
		englishToBraille[character] = brailleSequence
	}

	writingMode := "STRING"
	for characterIndex, character := range input {
		// Default writing mode
		if writingMode == "STRING" {
			brailleSequence, brailleExists := englishToBraille[string(character)]
			// Uppercase letter case
			if !brailleExists {
				brailleString += englishToBraille["CAPITAL"]
				brailleString += englishToBraille[strings.ToLower(string(character))]
			} else {
				// Number case
				if character <= '9' && character >= '0' {
					// Check if the number contains a decimal point to
					// differentiate between the number and decimal delimiters
					decimalFound := false
					for numberIndex := characterIndex; numberIndex < len(input); numberIndex++ {
						if input[numberIndex] == '.' {
							decimalFound = true
							break
							// numbers end with a space
						} else if input[numberIndex] == ' ' {
							break
						}
					}
					if decimalFound {
						brailleString += englishToBraille["DECIMAL"]
					} else {
						brailleString += englishToBraille["NUMBER"]
					}
					writingMode = "NUMBER"
				}
				// All non-uppercase letters, numbers, and special characters
				brailleString += brailleSequence
			}

			// Number writing mode assumes the number delimiter has already been written
		} else if writingMode == "NUMBER" {
			brailleSequence := englishToBraille[string(character)]
			brailleString += brailleSequence
			if character == ' ' { // Numbers end in a space
				writingMode = "STRING"
			}
		}
	}

	return
}

// Input: Input string, split into words as command line arguments
// Output: Braille or English translation of the input string to stdout
func main() {
	// Concatenate all arguments into a single input string
	numArguments := len(os.Args) - 1

	var input string
	if numArguments == 0 {
		input = ""
	} else {
		input = os.Args[1]
		for argumentIndex := 2; argumentIndex <= numArguments; argumentIndex++ {
			input += " " + os.Args[argumentIndex]
		}
	}

	// Detect whether the input string is braille or not
	// If the string is purely 'O' and '.', it is braille
	// This is fool-proof, since you cannot make a valid english string using only O
	brailleCharCount := 0
	for _, inputCharacter := range input {
		if inputCharacter == 'O' || inputCharacter == '.' {
			brailleCharCount++
		}
	}
	isBraille := brailleCharCount == len(input)

	// Output the english translation for a braille input, braille for english
	var translation string
	if isBraille {
		translation = translateBrailleToEnglish(input)
	} else {
		translation = translateEnglishToBraille(input)
	}

	// Output final result to stdout
	fmt.Println(translation)
}
