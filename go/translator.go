package main

import (
	"fmt"
	"os"
	"strings"
)

// is the text in braille?
func isBraille(text string) bool {
	// if the length of the text is not divisible by 6, it is not braille
	if len(text) < 6 || len(text)%6 != 0 {
		return false
	}

	// check if theres a dot in the first 6 characters
	// if there is, it is braille because there are no punctation marks within the constraints
	for i := 0; i < 6; i += 1 {
		if text[i] == '.' {
			return true
		}
	}

	// if there is no dot in the first 6 characters, it is not braille
	return false
}

// maps a char to its corresponding number
// a -> 1, b -> 2, ..., j -> 0
func letterToNumberWrapped(c rune) rune {
	return ('a' + (c-'a'+1)%10) - 49
}

// subtract 32 to convert the letter to uppercase
func letterToUpperCase(c rune) rune {
	return c - 32
}

// add 32 to convert the letter to lowercase
func letterToLowerCase(c rune) rune {
	return c + 32
}

func translateFromBraille(braille string, buff *strings.Builder) {
	// grow the buffer to an approximate size to avoid reallocations
	buff.Grow(len(braille) / 6)

	numberFollows := false
	capitalFollows := false

	// iterate over the text in chunks of 6
	var chunk string
	for i := 0; i < len(braille); i += 6 {
		chunk = braille[i : i+6]

		switch chunk {
		case SPACE:
			buff.WriteRune(' ')
			numberFollows = false

		case NUMBER_FOLLOWS:
			numberFollows = true

		case CAPITAL_FOLLOWS:
			capitalFollows = true

		default:
			if numberFollows {
				buff.WriteRune(letterToNumberWrapped(brailleToChars[chunk]))
				continue
			}

			if capitalFollows {
				buff.WriteRune(letterToUpperCase(brailleToChars[chunk]))
				capitalFollows = false
				continue
			}

			buff.WriteRune(brailleToChars[chunk])
		}
	}
}

func translateToBraille(text string, buff *strings.Builder) {
	// grow the buffer to an approximate size to avoid reallocations
	buff.Grow(len(text) * 6)

	numberFollows := false

	// iterate over the text
	for _, c := range text {
		switch {
		case c == ' ':
			buff.WriteString(SPACE)
			numberFollows = false

		case c >= '0' && c <= '9':
			if !numberFollows {
				buff.WriteString(NUMBER_FOLLOWS)
				numberFollows = true
			}
			buff.WriteString(charsToBraille[c])

		case c >= 'A' && c <= 'Z':
			// if we are still in the middle of a number, we need to close it
			if numberFollows {
				buff.WriteString(SPACE)
				numberFollows = false
			}

			buff.WriteString(CAPITAL_FOLLOWS)
			buff.WriteString(charsToBraille[letterToLowerCase(c)])

		default:
			// if we are still in the middle of a number, we need to close it
			if numberFollows {
				buff.WriteString(SPACE)
				numberFollows = false
			}

			buff.WriteString(charsToBraille[c])
		}
	}
}

// consts and maps for the braille translation
const NUMBER_FOLLOWS = ".O.OOO"
const CAPITAL_FOLLOWS = ".....O"
const SPACE = "......"

var /* const */ brailleToChars = map[string]rune{
	"O.....": 'a',
	"O.O...": 'b',
	"OO....": 'c',
	"OO.O..": 'd',
	"O..O..": 'e',
	"OOO...": 'f',
	"OOOO..": 'g',
	"O.OO..": 'h',
	".OO...": 'i',
	".OOO..": 'j',
	"O...O.": 'k',
	"O.O.O.": 'l',
	"OO..O.": 'm',
	"OO.OO.": 'n',
	"O..OO.": 'o',
	"OOO.O.": 'p',
	"OOOOO.": 'q',
	"O.OOO.": 'r',
	".OO.O.": 's',
	".OOOO.": 't',
	"O...OO": 'u',
	"O.O.OO": 'v',
	".OOO.O": 'w',
	"OO..OO": 'x',
	"OO.OOO": 'y',
	"O..OOO": 'z',
}

var /* const */ charsToBraille = map[rune]string{
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

func main() {
	args := os.Args
	if len(args) < 2 {
		fmt.Println("Usage: translator <braille/english text>")
		return
	}

	buff := &strings.Builder{}
	if isBraille(args[1]) {
		// i've chosen to ignore spaces between braille characters
		// the constraints did not specify how to handle them
		for i := 1; i < len(args); i += 1 {
			translateFromBraille(args[i], buff)
		}
	} else {
		translateToBraille(args[1], buff)
		for i := 2; i < len(args); i += 1 {
			buff.WriteString(SPACE)
			translateToBraille(args[i], buff)
		}
	}

	fmt.Print(buff.String())
}
