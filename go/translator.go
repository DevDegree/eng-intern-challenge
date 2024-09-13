package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var englishToBraille = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
	"z": "O..OOO",
	"capital_follows": ".....O", "decimal_follows": ".O...O", "number_follows": ".O.OOO", " ": "......",
}

var numbersToBraille = map[string]string{
	"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 
}

var brailleToEnglish = map[string]string{}
var brailleToNumbers = map[string]string{}

func init() {
	for k, v := range englishToBraille {
		brailleToEnglish[v] = k
	}
	for k, v := range numbersToBraille {
		brailleToNumbers[v] = k
	}
}

func isEnglish(input string) bool {
	for _, char := range input {
		lowerChar := unicode.ToLower(char)
		if (lowerChar >= 'a' && lowerChar <= 'z' && char != 'O') || (char >= '0' && char <= '9') {
			return true
		}
	}
	return false
}

func translateToBraille(input string) {
	insideNumber := false

	for _, char := range input {
		if unicode.IsUpper(char) {
			fmt.Print(englishToBraille["capital_follows"])
		}

		if insideNumber && char == ' ' {
			insideNumber = false
		}

		if unicode.IsDigit(char) {
			if !insideNumber {
				fmt.Print(englishToBraille["number_follows"])
				insideNumber = true
			}
			fmt.Print(numbersToBraille[string(char)])
			continue
		}

		braille := englishToBraille[strings.ToLower(string(char))]
		fmt.Print(braille)
	}

	fmt.Println()
}

func translateToEnglish(input string) {
	var characters []string
	
	for i := 0; i < len(input); i += 6 {
		if i+6 <= len(input) {
			characters = append(characters, input[i:i+6])
		}
	}

	capitalFollows := false
	numberFollows := false

	for _, char := range characters {
		if char == englishToBraille["capital_follows"] {
			capitalFollows = true
			continue
		}
		if char == englishToBraille["number_follows"] {
			numberFollows = true
			continue
		}
	
		englishChar := brailleToEnglish[char]
		if (numberFollows) {
			englishChar = brailleToNumbers[char]
		}

		if numberFollows && englishChar >= "a" && englishChar <= "j" {
			englishChar = string('1' + (englishChar[0] - 'a'))
		} else if capitalFollows {
			englishChar = strings.ToUpper(englishChar)
			capitalFollows = false
		}

		fmt.Print(englishChar)

		if englishChar == " " {
			numberFollows = false
		}
	}

	fmt.Println()
}

func main() {
	input := strings.Join(os.Args[1:], " ")

	if isEnglish(input) {
		translateToBraille(input)
	} else {
		translateToEnglish(input)
	}
}