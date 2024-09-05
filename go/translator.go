package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var englishToBrailleMap = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
	'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
	'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
	'z': "O..OOO", ' ': "......",
}

var brailleToEnglishMap = make(map[string]rune)

var numberPrefix = ".O.OOO"
var capitalPrefix = ".....O"

func init() {
	for k, v := range englishToBrailleMap {
		brailleToEnglishMap[v] = k
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate")
		return
	}

	input := strings.Join(os.Args[1:], " ")

	if isBraille(input) {
		fmt.Println(brailleToEnglish(input))
	} else {
		fmt.Println(englishToBraille(input))
	}
}

func isBraille(s string) bool {
	return strings.Count(s, "O")+strings.Count(s, ".") == len(s) && len(s)%6 == 0
}

func brailleToEnglish(s string) string {
	var result strings.Builder
	isCapital := false
	isNumber := false

	for i := 0; i < len(s); i += 6 {
		symbol := s[i : i+6]

		if symbol == capitalPrefix {
			isCapital = true
			continue
		}

		if symbol == numberPrefix {
			isNumber = true
			continue
		}

		if char, ok := brailleToEnglishMap[symbol]; ok {
			if isNumber {
				result.WriteRune(rune(char - 'a' + '1'))
				if char == 'j' {
					result.WriteRune('0')
				}
			} else {
				if isCapital {
					char = unicode.ToUpper(char)
					isCapital = false
				}
				result.WriteRune(char)
			}
		}

		if symbol == "......" {
			isNumber = false
		}
	}

	return result.String()
}

func englishToBraille(s string) string {
	var result strings.Builder
	isNumber := false

	for _, char := range s {
		if unicode.IsUpper(char) {
			result.WriteString(capitalPrefix)
			char = unicode.ToLower(char)
		}

		if unicode.IsDigit(char) {
			if !isNumber {
				result.WriteString(numberPrefix)
				isNumber = true
			}
			if char == '0' {
				result.WriteString(englishToBrailleMap['j'])
			} else {
				result.WriteString(englishToBrailleMap[rune(char-'1'+'a')])
			}
		} else {
			if isNumber && char != ' ' {
				result.WriteString("......")
				isNumber = false
			}
			if braille, ok := englishToBrailleMap[char]; ok {
				result.WriteString(braille)
			}
		}
	}

	return result.String()
}
