package main

import (
	"log"
	"os"
	"strings"
	"unicode"
)

var englishToBrailleMap = map[rune]string{
	'a': "O.....",
	'b': "O.O...",
	'c': "OO....",
	'd': "OO.O..",
	'e': "O..O..",
	'f': "OOO...",
	'g': "OOOO..",
	'h': "O.OO..",
	'i': ".OO...",
	'j': ".OOO..",
	'k': "O...O.",
	'l': "O.O.O.",
	'm': "OO..O.",
	'n': "OO.OO.",
	'o': "O..OO.",
	'p': "OOO.O.",
	'q': "OOOOO.",
	'r': "O.OOO.",
	's': ".OO.O.",
	't': ".OOOO.",
	'u': "O...OO",
	'v': "O.O.OO",
	'w': ".OOO.O",
	'x': "OO..OO",
	'y': "OO.OOO",
	'z': "O..OOO",
	' ': "......",
}

var numbersToBrailleMap = map[rune]string{
	'1': "O.....",
	'2': "O.O...",
	'3': "OO....",
	'4': "OO.O..",
	'5': "O..O..",
	'6': "OOO...",
	'7': "OOOO..",
	'8': "O.OO..",
	'9': ".OO...",
	'0': ".OOO..",
}

var capitalFollows = ".....O"
var numberFollows = ".O.OOO"

func main() {
	input := getInput()
	if len(input) == 0 {
		return
	}
	output := stringHandler(input)
	os.Stdout.WriteString(output)
}

// Get input from the runtime and join it into a single string
func getInput() string {
	args := os.Args[1:]
	input := strings.Join(args, " ")
	return input
}

// Handle the input string
func stringHandler(input string) string {
	if isBraille(input) {
		return BrailleToEnglish(input)
	}
	return EnglishToBraille(input)
}

// Check if the string is braille
func isBraille(string string) bool {
	for _, c := range string {
		if c != 'O' && c != '.' {
			return false
		}
	}
	return true
}

// Convert the input string to braille.
// It will return an error if the input string is not valid.
func BrailleToEnglish(braille string) string {
	if (len(braille) % 6) != 0 {
		log.Fatalf("Invalid braille input %v", braille)
	}
	output := ""
	isNextCharacterCapital := false
	isNextCharacterNumber := false
	for i := 0; i < len(braille); i += 6 {
		char := braille[i : i+6]
		if char == capitalFollows {
			isNextCharacterCapital = true
			continue
		}
		if char == numberFollows {
			isNextCharacterNumber = true
			continue
		}
		if char == "......" {
			output = output + " "
			isNextCharacterNumber = false
			continue
		}
		if isNextCharacterNumber {
			for k, v := range numbersToBrailleMap {
				if v == char {
					output = output + string(k)
					break
				}
			}
			continue
		}
		for k, v := range englishToBrailleMap {
			if v == char {
				if isNextCharacterCapital {
					output = output + strings.ToUpper(string(k))
					isNextCharacterCapital = false
				} else {
					output = output + string(k)
				}
				break
			}
		}
	}
	return output
}

// Convert the input string to English.
func EnglishToBraille(english string) string {
	output := ""
	numberFollowsIsAdded := false
	for _, c := range english {
		// Handle numbers
		if unicode.IsDigit(c) {
			if !numberFollowsIsAdded {
				output = output + numberFollows
				numberFollowsIsAdded = true
			}
			output = output + numbersToBrailleMap[c]
			continue
		}
		if c == ' ' {
			numberFollowsIsAdded = false
		}

		// Handle capital letters
		if unicode.IsUpper(c) {
			output = output + capitalFollows + englishToBrailleMap[unicode.ToLower(c)]
			continue
		}

		// Handle other characters
		output = output + englishToBrailleMap[c]
	}
	return output
}
