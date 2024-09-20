package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
	"unicode"
)

// Braille alphabet to English and vice versa mappings
var brailleLettersE2B = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
	"g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
	"m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
	"s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
	"y": "OO.OOO", "z": "O..OOO",
}

var brailleLettersB2E = map[string]string{
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
	"OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
	"OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
	".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
	"OO.OOO": "y", "O..OOO": "z",
}

// Braille numbers map
var brailleNumbersE2B = map[string]string{
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
	"OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

// Braille special characters
const (
	NUMBER_FOLLOWS  = ".O.OOO" // Signifies a number follows
	CAPITAL_FOLLOWS = ".....O" // Signifies a capital letter follows
	SPACE           = "......" // Braille representation for space
)

func main() {
	// Get arguments from the command-line
	args := os.Args[1:]
	input := strings.Join(args, " ") // Join arguments into a single string

	if input == "" {
		fmt.Println("Error: No input provided.")
		return
	}

	// Detect if the input is in Braille format
	isBrailleInput := detectBraille(input)

	var convertedString string
	var err error
	if isBrailleInput {
		// Convert Braille to English
		convertedString, err = convertToEnglish(input)
	} else {
		// Convert English to Braille
		convertedString, err = convertToBraille(input)
	}

	// Handle conversion errors, if any
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// Print the final result
	fmt.Print(convertedString)
}

// detectBraille checks if the input is a valid Braille string
func detectBraille(input string) bool {
	isBraille, _ := regexp.MatchString("^[O.]*$", input)
	return isBraille
}

// convertToEnglish converts a Braille string to its English equivalent
func convertToEnglish(brailleInput string) (string, error) {
	var result string
	var isNextCapital, areNextNumbers bool

	// Iterate over each 6-character Braille block
	for i := 0; i < len(brailleInput); i += 6 {
		if i+6 > len(brailleInput) {
			return "", fmt.Errorf("invalid Braille input, incomplete character sequence")
		}

		brailleChar := brailleInput[i : i+6]

		switch brailleChar {
		case NUMBER_FOLLOWS:
			areNextNumbers = true
			isNextCapital = false
		case SPACE:
			areNextNumbers = false
			isNextCapital = false
			result += " "
		case CAPITAL_FOLLOWS:
			isNextCapital = true
			areNextNumbers = false
		default:
			if areNextNumbers {
				if number, found := brailleNumbersE2B[brailleChar]; found {
					result += number
				} else {
					return "", fmt.Errorf("invalid number Braille sequence: %s", brailleChar)
				}
			} else if isNextCapital {
				if letter, found := brailleLettersB2E[brailleChar]; found {
					result += strings.ToUpper(letter)
				} else {
					return "", fmt.Errorf("invalid letter Braille sequence: %s", brailleChar)
				}
				isNextCapital = false
			} else {
				if letter, found := brailleLettersB2E[brailleChar]; found {
					result += letter
				} else {
					return "", fmt.Errorf("invalid letter Braille sequence: %s", brailleChar)
				}
			}
		}
	}
	return result, nil
}

// convertToBraille converts an English string to Braille
func convertToBraille(englishInput string) (string, error) {
	var result string
	var isNumberMode bool

	// Iterate over each character in the input string
	for _, char := range englishInput {
		if unicode.IsSpace(char) {
			result += SPACE
			isNumberMode = false
			continue
		}

		if unicode.IsDigit(char) {
			if !isNumberMode {
				result += NUMBER_FOLLOWS
				isNumberMode = true
			}
			brailleChar := brailleLettersE2B[string('a'+char-'1')]
			result += brailleChar
		} else if unicode.IsLetter(char) {
			if isNumberMode {
				result += SPACE
				isNumberMode = false
			}
			if unicode.IsUpper(char) {
				result += CAPITAL_FOLLOWS
			}
			brailleChar, found := brailleLettersE2B[string(unicode.ToLower(char))]
			if !found {
				return "", fmt.Errorf("unsupported letter: %c", char)
			}
			result += brailleChar
		} else {
			return "", fmt.Errorf("unsupported character: %c", char)
		}
	}
	return result, nil
}
