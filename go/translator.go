package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

var brailleToAlpha = map[string]string{
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
	"......": "space",
	".....O": "capital",
	".O.OOO": "number",
	".O...O": "decimal",
}

var brailleToNumber = map[string]string{
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
}
var brailleToDecimal = map[string]string{}
var alphaToBraille = reverseMap(brailleToAlpha)
var numberToBraille = reverseMap(brailleToNumber)

func reverseMap(originalMap map[string]string) map[string]string {
	reversedMap := make(map[string]string, len(originalMap))
	for k, v := range originalMap {
		reversedMap[v] = k
	}
	return reversedMap
}

func translateToBraille(input string) string {
	var output string
	numberMode := false
	for _, c := range input {
		if c >= 'A' && c <= 'Z' {
			output += alphaToBraille["capital"]
			output += alphaToBraille[string(c+32)]
		} else if c >= 'a' && c <= 'z' {
			output += alphaToBraille[string(c)]
		} else if c >= '0' && c <= '9' {
			if !numberMode {
				numberMode = true
				output += alphaToBraille["number"]
			}
			output += numberToBraille[string(c)]
		} else {
			output += alphaToBraille["space"]
			numberMode = false
		}
	}
	return output
}

func translateToAlpha(input string) string {
	var englishOutput string
	var capitalizeNext bool
	var numberMode bool

	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6]

		if brailleChar == alphaToBraille["capital"] {
			capitalizeNext = true
			continue
		}

		if brailleChar == alphaToBraille["number"] {
			numberMode = true
			continue
		}

		if numberMode {
			if letter, exists := brailleToNumber[brailleChar]; exists {
				englishOutput += letter
				continue
			}
		}

		if letter, exists := brailleToAlpha[brailleChar]; exists {
			if capitalizeNext {
				letter = strings.ToUpper(letter)
				capitalizeNext = false
			}
			englishOutput += letter
		}

		if brailleChar == alphaToBraille["space"] {
			numberMode = false
		}
	}

	return englishOutput
}

func isBraille(input string) bool {
	regexPattern := "^([O.]{6})+$"
	match, _ := regexp.MatchString(regexPattern, input)
	return match
}

func main() {
	args := strings.Join(os.Args[1:], " ")
	if isBraille(args) {
		output := translateToAlpha(args)
		fmt.Println(output)
	} else {
		output := translateToBraille(args)
		fmt.Println(output)
	}
}
