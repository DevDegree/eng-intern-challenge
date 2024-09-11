package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	brailleCharLength = 6
	numberPrefix      = ".O.OOO"
	capitalPrefix     = ".....O"
)

var (
	englishToBrailleMap = map[rune]string{
		'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
		'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
		'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
		'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
		'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
		'z': "O..OOO", ' ': "......",
	}
	brailleToEnglishMap = make(map[string]rune)
)

func init() {
	for k, v := range englishToBrailleMap {
		brailleToEnglishMap[v] = k
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide strings to translate")
		os.Exit(1)
	}

	inputs := os.Args[1:]
	var results []string

	for _, input := range inputs {
		if isBraille(input) {
			result, _ := brailleToEnglish(input)
			results = append(results, result)
		} else {
			result, _ := englishToBraille(input)
			results = append(results, result)
		}
	}

	// Join the results with the Braille representation of a space
	fmt.Print(strings.Join(results, "......"))
}

func isBraille(s string) bool {
	return strings.Count(s, "O")+strings.Count(s, ".") == len(s) && len(s)%brailleCharLength == 0
}

func brailleToEnglish(s string) (string, error) {
	var result strings.Builder
	isCapital := false
	isNumber := false

	for i := 0; i < len(s); i += brailleCharLength {
		symbol := s[i : i+brailleCharLength]

		switch symbol {
		case capitalPrefix:
			isCapital = true
			continue
		case numberPrefix:
			isNumber = true
			continue
		}

		char, ok := brailleToEnglishMap[symbol]
		if !ok {
			return "", fmt.Errorf("invalid Braille symbol: %s", symbol)
		}

		if isNumber && unicode.IsLetter(char) {
			result.WriteRune(convertBrailleToNumber(char))
			continue
		}

		if isCapital && unicode.IsLetter(char) {
			char = unicode.ToUpper(char)
			isCapital = false
		}

		result.WriteRune(char)

		if char == ' ' {
			isNumber = false
		}
	}

	return result.String(), nil
}

func convertBrailleToNumber(char rune) rune {
	if char == 'j' {
		return '0'
	}
	return rune(char - 'a' + '1')
}

func englishToBraille(s string) (string, error) {
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
			result.WriteString(convertNumberToBraille(char))
		} else {
			if isNumber && char != ' ' {
				isNumber = false
			}
			braille, ok := englishToBrailleMap[char]
			if !ok {
				return "", fmt.Errorf("invalid character: %c", char)
			}
			result.WriteString(braille)
		}
	}

	return result.String(), nil
}

func convertNumberToBraille(char rune) string {
	if char == '0' {
		return englishToBrailleMap['j']
	}
	return englishToBrailleMap[rune(char-'1'+'a')]
}
