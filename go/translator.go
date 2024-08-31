package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	CAPITAL_FOLLOWS = ".....O"
	NUMBERS_FOLLOW  = ".O.OOO"
)

var ALPHABET_BRAILLE_MAP = map[rune]string{
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

var NUMBERS_BRAILLE_MAP = map[rune]string{
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

var (
	BRAILLE_ALPHABET_MAP = invertMap(ALPHABET_BRAILLE_MAP)
	BRAILLE_NUMBERS_MAP  = invertMap(NUMBERS_BRAILLE_MAP)
)

func invertMap(m map[rune]string) map[string]rune {
	inverted := make(map[string]rune)
	for k, v := range m {
		inverted[v] = k
	}
	return inverted
}

type Translator interface {
	Translate(text string) string
}

type BrailleToEnglish struct{}

func (b *BrailleToEnglish) New() *BrailleToEnglish {
	return &BrailleToEnglish{}
}

func (b *BrailleToEnglish) Translate(braille string) string {
	var english strings.Builder
	i := 0
	capitalizeNext := false
	numberMode := false

	for i < len(braille) {
		char := braille[i : i+6]
		if char == CAPITAL_FOLLOWS {
			capitalizeNext = true
		} else if char == NUMBERS_FOLLOW {
			numberMode = true
		} else if char == "......" {
			english.WriteRune(' ')
			numberMode = false
		} else {
			if numberMode {
				english.WriteRune(BRAILLE_NUMBERS_MAP[char])
			} else {
				letter := BRAILLE_ALPHABET_MAP[char]
				if capitalizeNext {
					letter = unicode.ToUpper(letter)
				}
				english.WriteRune(letter)
			}
			capitalizeNext = false
		}
		i += 6
	}

	return english.String()
}

type EnglishToBraille struct{}

func (e *EnglishToBraille) Translate(text string) string {
	var braille strings.Builder
	mode := "alphabet"

	for _, char := range text {
		switch {
		case unicode.IsUpper(char):
			mode = "alphabet"
			braille.WriteString(CAPITAL_FOLLOWS)
			braille.WriteString(ALPHABET_BRAILLE_MAP[unicode.ToLower(char)])
		case unicode.IsDigit(char):
			if mode == "alphabet" {
				mode = "number"
				braille.WriteString(NUMBERS_FOLLOW)
				braille.WriteString(NUMBERS_BRAILLE_MAP[char])
			} else {
				braille.WriteString(NUMBERS_BRAILLE_MAP[char])
			}
		default:
			mode = "alphabet"
			braille.WriteString(ALPHABET_BRAILLE_MAP[char])
		}
	}

	return braille.String()
}

func isEnglish(s string) bool {
	return strings.IndexFunc(s, func(r rune) bool {
		return !unicode.IsLetter(r) && !unicode.IsDigit(r) && !unicode.IsSpace(r)
	}) == -1
}

func isBraille(s string) bool {
	return strings.IndexFunc(s, func(r rune) bool {
		return r != '.' && r != '0'
	}) == -1
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("No arguments given")
		return
	}

	input := strings.Join(os.Args[1:], " ")

	if isEnglish(input) {
		translator := &EnglishToBraille{}
		fmt.Println(translator.Translate(input))
	} else if isBraille(input) {
		translator := &BrailleToEnglish{}
		fmt.Println(translator.Translate(input))
	} else {
		fmt.Println("Invalid input")
	}
}
