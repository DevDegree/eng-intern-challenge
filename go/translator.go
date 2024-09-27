package main

import (
	"fmt"
	"os"
	"strings"
)

// braille mappings
var alphaToBraile = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO", ' ': "......",
}

var numToBraile = map[rune]string{
	'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}

var capitalFollow = ".....O"
var numFollow = ".O.OOO"

func brailleToEnglish(input string) string {

	var brailleToAlpha = map[string]rune{}
	var brailleToNum = map[string]rune{}

	for letter, braille := range alphaToBraile {
		brailleToAlpha[braille] = letter
	}

	for number, braille := range numToBraile {
		brailleToNum[braille] = number
	}

	output := ""
	isCapital := false
	isNumber := false

	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6]

		//special symbol checks
		if brailleChar == capitalFollow {
			isCapital = true
			continue
		}

		if brailleChar == numFollow {
			isNumber = true
			continue
		}

		if brailleChar == alphaToBraile[' '] {
			isNumber = false
			output += " "
			continue
		}

		if isNumber {
			if translatedNum, exists := brailleToNum[brailleChar]; exists {
				output += string(translatedNum)
			} else {
				output += "?"
			}
		} else {
			if translatedAlpha, exists := brailleToAlpha[brailleChar]; exists {
				if isCapital {
					output += strings.ToUpper(string(translatedAlpha))
					isCapital = false
				} else {
					output += string(translatedAlpha)
				}
			} else {
				output += "?"
			}
		}
	}

	return strings.TrimSpace(output)
}

func englishToBraille(input string) string {
	output := ""
	isNumber := false

	for _, char := range input {
		if char >= 'A' && char <= 'Z' {
			output += capitalFollow
			char = char + 32 // convert to lowercase
			isNumber = false
		}
		if char >= '0' && char <= '9' {
			if !isNumber {
				output += numFollow
				isNumber = true
			}
			output += numToBraile[char]
		} else {
			output += alphaToBraile[char]
			isNumber = false
		}

	}
	return strings.TrimSpace(output)
}

func main() {

	var input string

	if len(os.Args) < 2 {
		// testing, also prevent crashes
		// input = strings.TrimSpace(".O.OOOOOOOOOO.....O.O....O...OO.OO.......O......OO..OO")
		input = strings.TrimSpace(".O.OOOaaaaaaOOOOOO")
		// input = strings.TrimSpace("")
	} else {
		input = strings.Join(os.Args[1:], " ")
	}

	isBraille := true

	//check if input is braille or not

	if len(input)%6 != 0 {
		isBraille = false
	} else {
		for _, char := range input {
			if char != 'O' && char != '.' {
				isBraille = false
				break
			}
		}

	}

	if isBraille {
		fmt.Println(brailleToEnglish(input))
	} else {
		fmt.Println(englishToBraille(input))
	}

}
