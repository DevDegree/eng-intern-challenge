package main

import (
	"fmt"
	"os"
	"strings"
)

var lettersMap = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.",
	'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO",
}

var numbersMap = map[rune]string{
	'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}

var indicatorsMap = map[rune]string{
	'C': ".....O", 'N': ".O.OOO", ' ': "......",
}

var reverseLettersMap = map[string]rune{}
var reverseNumbersMap = map[string]rune{}

func init() {
	for letter, braille := range lettersMap {
		reverseLettersMap[braille] = letter
	}
	for num, braille := range numbersMap {
		reverseNumbersMap[braille] = num
	}
}

func englishToBraille(english string) string {
	var output strings.Builder
	isNumber := false

	for _, char := range english {
		switch {
		case char >= 'A' && char <= 'Z':
			output.WriteString(indicatorsMap['C'])
			output.WriteString(lettersMap[char+'a'-'A'])

		case char >= 'a' && char <= 'z':
			output.WriteString(lettersMap[char])

		case char >= '0' && char <= '9':
			if !isNumber {
				isNumber = true
				output.WriteString(indicatorsMap['N'])
			}
			output.WriteString(numbersMap[char])

		case char == ' ':
			isNumber = false
			output.WriteString(indicatorsMap[char])

		default:
			if braille, ok := lettersMap[char]; ok {
				output.WriteString(braille)
			}
		}
	}
	return output.String()
}

func brailleToEnglish(braille string) string {
	var output strings.Builder
	isCaps := false
	isNumber := false

	for i := 0; i < len(braille); i += 6 {
		symbol := braille[i : i+6]

		switch {
		case symbol == indicatorsMap['C']:
			isCaps = true

		case symbol == indicatorsMap['N']:
			isNumber = true

		case symbol == indicatorsMap[' ']:
			output.WriteRune(' ')
			isNumber = false

		default:
			if isNumber {
				if letter, exists := reverseNumbersMap[symbol]; exists {
					output.WriteRune(letter)
				}
			} else {
				if letter, exists := reverseLettersMap[symbol]; exists {
					if isCaps {
						output.WriteRune(letter - 'a' + 'A')
						isCaps = false
					} else {
						output.WriteRune(letter)
					}
				}
			}

		}
	}
	return output.String()
}

func main() {
	isBraille := true
	input := strings.Join(os.Args[1:], " ")

	for _, char := range input {
		if char != '.' && char != 'O' && char != ' ' {
			isBraille = false
			break
		}
	}

	if isBraille {
		fmt.Println(brailleToEnglish(input))
	} else {
		fmt.Println(englishToBraille(input))
	}
}
