package main

import (
	"fmt"
	"os"
	"strings"
)

/*
	braille mappings.

note that we need to store them seperately as 1 and a are the same symbols
this is important when we translate from braille to english
as then we have two keys that map to the same value: O..... = a but O..... = 1
this saves an extra check at the cost of two seperate map variable
*/
var alphaToBraile = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO", ' ': "......",
}

var numToBraile = map[rune]string{
	'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}

// specific symbols
var capitalFollow = ".....O"
var numFollow = ".O.OOO"

// function to translate braille to english characters
func brailleToEnglish(input string) string {

	/*
		init the opposite maps only if the input is braille
		that way we can save time and space if input is only text
	*/
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
	// iterate over the braille input string 6 characters at a time
	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6] // since each braille charcter is 6 characters long

		//special symbol checks, a symbol can't be two different things at once
		if brailleChar == capitalFollow {
			isCapital = true
		} else if brailleChar == numFollow {
			isNumber = true
		} else if brailleChar == alphaToBraile[' '] {
			isNumber = false
			output += " "
		}

		if isNumber {
			if translatedNum, exists := brailleToNum[brailleChar]; exists {
				output += string(translatedNum)
			} else {
				output += "?"
				/*
					added error character output
					since we are not inputting or outputing the "?" symbol we can use this as unknown symbol
					we could also output just nothing but then user would be unaware of an error input
				*/
			}
		} else {
			if translatedAlpha, exists := brailleToAlpha[brailleChar]; exists {
				// since each capital only capitalizes the next letter, set to false to prevent next letter being capitalized
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

// function to translate english to braille
func englishToBraille(input string) string {
	output := ""
	isNumber := false

	// iterate over the input string
	for _, char := range input {
		// since there is a capital symbol ahead of each capital letter, output cap symbol each time
		if char >= 'A' && char <= 'Z' {
			output += capitalFollow
			char = char + 32 // convert to lowercase
			isNumber = false
		}

		// since we only output the number symbol ahead of the first number in a chain,
		// only output when we hit the first number in a row
		if char >= '0' && char <= '9' {
			if !isNumber {
				output += numFollow
				isNumber = true
			}
			output += numToBraile[char]
		} else { //if not number than its a character
			output += alphaToBraile[char]
			isNumber = false
		}

	}

	return strings.TrimSpace(output)
}

/*
function to check if the input is braille or .
the logic is that is that if the input string is not a multiple of 6, it must be text
if it is a muliple of 6, we check if the charcters are braille characters or not
*/
func isBraille(input string) bool {
	if len(input)%6 != 0 {
		return false
	}

	for _, char := range input {
		if char != 'O' && char != '.' {
			return false
		}
	}

	return true
}

func main() {

	var input string

	if len(os.Args) < 2 {
		// testing, also prevent crashes
		// input = strings.TrimSpace(".O.OOOOOOOOOO.....O.O....O...OO.OO.......O......OO..OO")
		// input = strings.TrimSpace(".O.OOOaaaaaaOOOOOO")
		// input = strings.TrimSpace("")
	} else {
		input = strings.Join(os.Args[1:], " ")
	}

	//print statements
	if isBraille(input) {
		fmt.Println(brailleToEnglish(input))
	} else {
		fmt.Println(englishToBraille(input))
	}

}
