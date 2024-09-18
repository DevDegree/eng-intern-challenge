package main

import (
	"fmt"
	"os"
	"strings"
)

var brailleMappingCharacters = map[string]string{
	// letters
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
	"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
	"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
	"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
	"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
	// Special Char
	".....O": "CAPS", ".O.OOO": "NUM", "......": " ",
}

var englishMapping = invertMappingMethod(brailleMappingCharacters)

var numberMapping = map[string]string{
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
	"OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

var revNumberMapping = invertMappingMethod(numberMapping)

func invertMappingMethod(mapping map[string]string) map[string]string {
	tempMap := make(map[string]string)
	for k, v := range mapping {
		tempMap[v] = k
	}
	return tempMap
}

func isBraille(inputString string) bool {
	for _, ch := range inputString {
		if ch != 'O' && ch != '.' {
			return false
		}
	}
	return true
}

func brailleToEngConversion(inputString string) string {
	var result strings.Builder
	capital := false
	number := false
	for i := 0; i < len(inputString); i += 6 {
		segment := inputString[i : i+6]
		if value, found := brailleMappingCharacters[segment]; found {
			switch value {
			case "CAPS":
				capital = true
			case "NUM":
				number = true
			case " ":
				number = false
				result.WriteRune(' ')
			default:
				if capital {
					result.WriteRune(rune(value[0] - 32)) // convert to uppercase
					capital = false
				} else if number {
					result.WriteString(numberMapping[segment])
				} else {
					result.WriteString(value)
				}
			}
		}
	}
	return result.String()
}

func engToBrailleConversion(inputString string) string {
	var result strings.Builder
	isNumber := false

	for _, char := range inputString {
		if isDigit(char) && revNumberMapping[string(char)] != "" {
			if !isNumber {
				result.WriteString(englishMapping["NUM"])
			}
			isNumber = true
			result.WriteString(revNumberMapping[string(char)])
		} else if englishMapping[string(char)] != "" || englishMapping[strings.ToLower(string(char))] != "" {
			isNumber = false
			if char >= 'A' && char <= 'Z' {
				result.WriteString(englishMapping["CAPS"])
				char = char + 32 // convert to lowercase
			}
			result.WriteString(englishMapping[string(char)])
		}
	}
	return result.String()
}

func isDigit(ch rune) bool {
	return ch >= '0' && ch <= '9'
}

func main() {
	if len(os.Args) > 1 {
		input := strings.Join(os.Args[1:], " ")
		if isBraille(input) {
			fmt.Println(brailleToEngConversion(input))
		} else {
			fmt.Println(engToBrailleConversion(input))
		}
	} else {
		fmt.Println("")
	}
}
