package main

import (
	"fmt"
	"os"
	"strings"
)

var englishToBraille = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
}

var numberToBraille = map[string]string{
	"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
	"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

var brailleToEnglish = map[string]string{}
var brailleToNumber = map[string]string{}

func init() {
	for k, v := range englishToBraille {
		brailleToEnglish[v] = k
	}
	for k, v := range numberToBraille {
		brailleToNumber[v] = k
	}
}

func isBraille(input string) bool {
	for _, char := range input {
		if char != 'O' && char != '.' {
			return false
		}
	}
	return true
}

func convertBrailleToEnglish(input string) string {
	var out string
	capitalFollows := false
	numberFollows := false

	for i := 0; i < len(input); i += 6 {
		if i+6 > len(input) {
			break
		}
		symbol := input[i : i+6]

		if symbol == ".....O" {
			capitalFollows = true
			continue
		} else if symbol == ".O.OOO" {
			numberFollows = true
			continue
		}

		if symbol == "......" {
			out += " "
			numberFollows = false
		} else if numberFollows {
			char, exists := brailleToNumber[symbol]
			if exists {
				out += char
			}
		} else {
			char, exists := brailleToEnglish[symbol]
			if exists {
				if capitalFollows {
					out += strings.ToUpper(char)
					capitalFollows = false
				} else {
					out += char
				}
			}
		}
	}

	return out
}

func convertEnglishToBraille(input string) string {
	var out string
	numberFollows := false

	for _, char := range input {
		if char >= 'a' && char <= 'z' {
			out += englishToBraille[string(char)]
			numberFollows = false
		} else if char >= 'A' && char <= 'Z' {
			out += ".....O" + englishToBraille[string(char+'a'-'A')]
			numberFollows = false
		} else if char == ' ' {
			out += "......"
			numberFollows = false
		} else if char >= '0' && char <= '9' {
			if !numberFollows {
				out += ".O.OOO"
				numberFollows = true
			}
			out += numberToBraille[string(char)]
		}
	}

	return out
}

func main() {
	if len(os.Args) < 2 {
		return
	}

	input := strings.Join(os.Args[1:], " ")

	var output string
	if isBraille(input) {
		output = convertBrailleToEnglish(input)
	} else {
		output = convertEnglishToBraille(input)
	}

	fmt.Println(output)
}
