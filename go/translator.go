package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
	"unicode/utf8"
)

type Language int

const (
	English = iota + 1
	Braille
)

var brailleDigitMap = map[string]string{
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

var englishToBrailleMap = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
	'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
	'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
	'z': "O..OOO", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
	'5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...",
	'0': ".OOO..", '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.",
	':': "..OO..", ';': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O",
	'>': "O..OO.", '(': "O.O..O", ')': ".O.OO.", ' ': "......",
}

var brailleToEnglishMap = map[string]string{
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
	"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
	"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
	"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
	"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
	"O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
	"..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
	"O.O..O": "(", ".O.OO.": ")", "......": " ",
}

func main() {
	if len(os.Args) > 1 {
		input := strings.Join(os.Args[1:], " ")
		if languageIdentifier(input) == Braille {
			fmt.Println(brailleToEnglish(input))
		} else {
			fmt.Println(englishToBraille(input))
		}
	} else {
		fmt.Println("Error: No input provided")
	}
}

func languageIdentifier(input string) Language {
	for _, char := range input {
		if char != 'O' && char != '.' {
			return English
		}
	}
	return Braille
}

func englishToBraille(input string) string {
	res := ""
	numberNext := true
	decimalNext := false
	for _, ch := range input {
		if unicode.IsDigit(ch) {
			res += categorizeString(ch, numberNext, &decimalNext)
			numberNext = false
		} else if unicode.IsSpace(ch) {
			res += categorizeString(ch, false, &decimalNext)
			numberNext = true
		} else if ch == ',' || ch == '.' {
			decimalNext = true
			res += categorizeString(ch, false, &decimalNext)
		} else {
			res += categorizeString(ch, false, &decimalNext)
		}
	}
	return res
}

func categorizeString(ch rune, prefix bool, decimalNext *bool) string {
	str := ""
	if unicode.IsDigit(ch) {
		if prefix {
			str += ".O.OOO"
			str += englishToBrailleMap[ch]
		} else {
			str += englishToBrailleMap[ch]
		}
	} else if *decimalNext {
		str += ".O...O"
		*decimalNext = false
	} else if unicode.IsLetter(ch) && unicode.IsUpper(ch) {
		str += ".....O"
		str += englishToBrailleMap[unicode.ToLower(ch)]
	} else if unicode.IsLetter(ch) || unicode.IsSpace(ch) {
		str += englishToBrailleMap[ch]
	} else {
		str += englishToBrailleMap[ch]
	}
	return str
}

func brailleToEnglish(input string) string {
	res := ""
	capitalNext := false
	numberNext := false
	for i := 0; i < len(input); i += 6 {
		if i+6 > len(input) {
			break
		}

		brailleCell := input[i : i+6]

		if brailleCell == ".....O" {
			capitalNext = true
			continue
		}
		if brailleCell == ".O.OOO" {
			numberNext = true
			continue
		}
		if brailleCell == ".O...O" {
			res += ","
			continue
		}

		if brailleCell == "......" {
			numberNext = false
			res += " "
			continue
		}

		if brailleCell == "O..OO." {
			beforeChar := brailleToEnglishMap[input[i-6:i]]
			b, _ := utf8.DecodeRuneInString(beforeChar)
			if isAlpha(byte(b)) || unicode.IsSpace(b) {
				res += "o"
				continue
			}
			res += ">"
			continue
		}

		if capitalNext {
			res += strings.ToUpper(brailleToEnglishMap[brailleCell])
			capitalNext = false
			continue
		}

		if numberNext {
			if digit, exists := brailleDigitMap[brailleCell]; exists {
				res += digit
			}
			continue
		}

		res += brailleToEnglishMap[brailleCell]
	}
	return res
}

func isAlpha(c byte) bool {
	if c >= 'a' && c <= 'z' {
		return true
	}
	return false
}
