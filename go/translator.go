package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
	"unicode"
)

var brailleToEnglishMap = map[string]string{
	".....O": "CF", // Capital Follows
	".O.OOO": "NF", // Number Follows
	"......": " ",  // Space character
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
	"OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
	"OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
	".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
	"OO.OOO": "y", "O..OOO": "z",
}

var brailleToNumbersMap = map[string]string{
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
	"OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

// instead of rewriting Braille maps backwards, use this function
func reverseMap(m map[string]string) map[string]string {
	reversed := make(map[string]string)

	for key, value := range m {
		reversed[value] = key
	}

	return reversed
}

func isBraille(input string) bool {
	// Use regex to determine whether the string only contains the letter "O" and "."
	match, _ := regexp.MatchString("^[O.]+$", input)

	return match
}

func brailleToEnglish(input string) string {
	var res strings.Builder

	var capitalizeNext = false // flag to track if the next letter should be capitalized
	var numbersFollow = false  // flag to track if numbers follow

	// loop through the input in chunks of 6
	for z := 0; z < len(input); z += 6 {
		char := input[z : z+6] // take 6-character Braille chunk

		var mapToUse map[string]string

		// if numbers should follow, use the brailleToNumbersMap, else use brailleToEnglishMap
		if numbersFollow {
			mapToUse = brailleToNumbersMap
		} else {
			mapToUse = brailleToEnglishMap
		}

		// if the 6 character Braille chunk is found in the map
		if key, exists := mapToUse[char]; exists {
			switch key {
			// if Number Follows, toggle flag
			case "NF":
				numbersFollow = true
			// if Capital Follows, toggle flag
			case "CF":
				capitalizeNext = true
			// if a space, reset numbersFollow flag
			case " ":
				numbersFollow = false
				fallthrough
			// append the character to the result, capitalizing if necessary
			default:
				if capitalizeNext {
					key = strings.ToUpper(key)

					capitalizeNext = false
				}

				res.WriteString(key)
			}
		}
	}

	return res.String()
}

// englishToBraille translates an English string into Braille
func englishToBraille(input string) string {
	var res strings.Builder

	var numbersFollow = false // flag to track if numbers follow

	// create reversed maps from the Braille-to-English/Numbers maps for translation
	var englishToBrailleMap = reverseMap(brailleToEnglishMap)
	var numbersToBrailleMap = reverseMap(brailleToNumbersMap)

	var mapToUse map[string]string

	// loop through each character in the input string
	for _, char := range input {
		var key = strings.ToLower(string(char))

		// if numbers should follow, use the numbersToBrailleMap, else use englishToBrailleMap
		if numbersFollow {
			mapToUse = numbersToBrailleMap
		} else {
			mapToUse = englishToBrailleMap
		}

		if unicode.IsUpper(char) {
			// if the character is uppercase, output the Capital Follows symbol first
			res.WriteString(mapToUse["CF"])
		} else if unicode.IsDigit(char) {
			// if the character is a digit, output the number follows symbol and toggle flag
			numbersFollow = true

			res.WriteString(mapToUse["NF"])

			mapToUse = numbersToBrailleMap
		}

		// write the corresponding Braille character
		if value, exists := mapToUse[key]; exists {
			res.WriteString(value)
		} else if key == " " {
			res.WriteString(englishToBrailleMap[" "])

			numbersFollow = false
		}
	}

	return res.String()
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Pass in an argument to decode")

		return
	}

	// join all command-line arguments into a single string
	var input string = strings.Join(os.Args[1:], " ")

	if isBraille(input) {
		fmt.Println(brailleToEnglish(input))
	} else {
		fmt.Println(englishToBraille(input))
	}
}
