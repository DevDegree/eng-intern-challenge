package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var englishToBraille = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
	'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
	'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
	'z': "O..OOO",
	'0': ".O.OOO", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
	'5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...",
	' ': "......",
}

var brailleToEnglish = make(map[string]rune)

const (
	numberPrefix  = ".O.OOO"
	capitalPrefix = ".....O"
)

func init() {
	for k, v := range englishToBraille {
		brailleToEnglish[v] = k
	}
}

func translateToBraille(input string) string {
	var result strings.Builder
	isNumber := false

	for _, char := range input {
		if unicode.IsUpper(char) {
			result.WriteString(capitalPrefix)
			char = unicode.ToLower(char)
		}

		if unicode.IsDigit(char) && !isNumber {
			result.WriteString(numberPrefix)
			isNumber = true
		} else if !unicode.IsDigit(char) && char != ' ' {
			// Reset the number flag if we encounter a non-digit character (except space)
			isNumber = false
		}

		if braille, ok := englishToBraille[char]; ok {
			result.WriteString(braille)
		}
		// Note: If the character is not in our map, it's silently ignored
	}

	return result.String()
}

func translateToEnglish(input string) string {
	var result strings.Builder
	capitalize := false
	isNumber := false

	for i := 0; i < len(input); i += 6 {
		// Break if there's not enough characters left for a full Braille character
		if i+6 > len(input) {
			break
		}

		// Extract the current 6-character Braille segment
		segment := input[i : i+6]

		if segment == capitalPrefix {
			capitalize = true
			continue
		}

		if segment == numberPrefix {
			isNumber = true
			continue
		}

		if char, ok := brailleToEnglish[segment]; ok {
			if capitalize {
				char = unicode.ToUpper(char)
				capitalize = false // Reset the capitalize flag
			}

			if isNumber && unicode.IsLetter(char) {
				// Convert letters to numbers (a->1, b->2, etc.)
				result.WriteRune(rune(char - 'a' + '1'))
			} else {
				result.WriteRune(char)
			}

			// Reset number mode if we encounter a space
			if char == ' ' {
				isNumber = false
			}
		}
		// Note: If the segment is not in our map, it's silently ignored
	}

	return result.String()
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate")
		return
	}

	input := strings.Join(os.Args[1:], " ")

	if strings.Contains(input, "O") || strings.Contains(input, ".") {
		fmt.Print(translateToEnglish(input))
	} else {
		fmt.Print(translateToBraille(input))
	}
}
