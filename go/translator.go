/*
This package will handle the translation of braille string to
English and vice versa.

There are certain assumptions for the logic
Assumptions
    1. If input braille, it will ONLY be one input
    2. Symbols `<`, `>`, `)`, and `(` have been ignored
*/

package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	maxBrailleChars = 6
)

const (
	capitalFollowsBraille string = ".....O"
	decimalFollowsBraille string = ".O...O"
	numberFollowsBraille  string = ".O.OOO"
)

const (
	capitalFollowsAction uint8 = iota
	decimalFollowsAction
	numberFollowsAction
)

var followActionsMap = map[string]uint8{
	capitalFollowsBraille: capitalFollowsAction,
	decimalFollowsBraille: decimalFollowsAction,
	numberFollowsBraille:  numberFollowsAction,
}

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
	'.': "..OO.O",
	',': "..O...",
	'?': "..O.OO",
	'!': "..OOO.",
	':': "..OO..",
	';': "..O.O.",
	'-': "....OO",
	'/': ".O..O.",
	// '<': ".OO..O",
	// '>': "O..OO.",
	'(': "O.O..O",
	')': ".O.OO.",
	' ': "......",
}

var brailleToEnglishNumMap = map[string]string{
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

var brailleToEnglishAlphMap = map[string]string{
	"O.....": "a",
	"O.O...": "b",
	"OO....": "c",
	"OO.O..": "d",
	"O..O..": "e",
	"OOO...": "f",
	"OOOO..": "g",
	"O.OO..": "h",
	".OO...": "i",
	".OOO..": "j",
	"O...O.": "k",
	"O.O.O.": "l",
	"OO..O.": "m",
	"OO.OO.": "n",
	"O..OO.": "o",
	"OOO.O.": "p",
	"OOOOO.": "q",
	"O.OOO.": "r",
	".OO.O.": "s",
	".OOOO.": "t",
	"O...OO": "u",
	"O.O.OO": "v",
	".OOO.O": "w",
	"OO..OO": "x",
	"OO.OOO": "y",
	"O..OOO": "z",
	"..OO.O": ".",
	"..O...": ",",
	"..O.OO": "?",
	"..OOO.": "!",
	"..OO..": ":",
	"..O.O.": ";",
	"....OO": "-",
	".O..O.": "/",
	// ".OO..O": "<",
	// "O..OO.": ">",
	"O.O..O": "(",
	".O.OO.": ")",
	"......": " ",
}

func translateToEnglish(brailleStatement string) string {
	// more efficient way for string concatenation
	// it prevents copying the string over and over
	// with every iteration, especially her that we know
	// the maximum capacity of the underlying slice is
	// at most 6
	sb := strings.Builder{}
	sb.Grow(maxBrailleChars)

    sbRes := strings.Builder{}
	var makeCap bool
	var isNumber bool

mainLoop:
	// braille statement chars are ASCII. so if we
	// iterate over the string, we get the correct rune
	for i, c := range brailleStatement {
		sb.WriteRune(c)

		if (i+1)%maxBrailleChars == 0 {
			singleBraille := sb.String()

			followAction, prs := followActionsMap[singleBraille]
			if prs {
				switch followAction {
				case numberFollowsAction:
					isNumber = true
					sb.Reset()
					continue mainLoop

				case capitalFollowsAction:
					makeCap = true
					sb.Reset()
					continue mainLoop

				case decimalFollowsAction:
					sbRes.WriteString(".")
					sb.Reset()
					continue mainLoop
				}
			}

			var englishString string
			if isNumber {
				englishString, prs = brailleToEnglishNumMap[singleBraille]
				if !prs {
					// this means that this character is a space
					englishString = brailleToEnglishAlphMap[singleBraille]
					isNumber = false
				}

			} else {
				englishString, prs = brailleToEnglishAlphMap[singleBraille]
				if !prs {
					panic("non existent english string in map")
				}

				if makeCap {
					englishString = strings.ToUpper(englishString)
					makeCap = false
				}
			}

			sbRes.WriteString(englishString)
			sb.Reset()
		}
	}

	return sbRes.String()
}

// Concatenates all the words together
// and puts a space between them.
func concatString(words []string) string {
	sb := strings.Builder{}
	for i, word := range words {
		word = strings.TrimSpace(word)
		sb.WriteString(word)

		if i != len(words)-1 {
			sb.WriteString(" ")
		}
	}
	return sb.String()
}

func translateToBraille(concatedWords string) string {
	sb := strings.Builder{}
	sb.Grow(maxBrailleChars) // there will at least one english char
	writeNumberFollow := true

	for _, engRune := range concatedWords {
		if unicode.IsUpper(engRune) {
			sb.WriteString(capitalFollowsBraille)
			engRune = unicode.ToLower(engRune)
		}

		// If it's the first occurrence of a number
		// FollowNumber prefix must be added before
		// numbers sequence
		if unicode.IsNumber(engRune) {
			if writeNumberFollow {
				sb.WriteString(numberFollowsBraille)
				writeNumberFollow = false
			}
		}

		// If this is the case, we're still writing numbers and "."
		// does not represent period rather a decimcal point
		if !writeNumberFollow && string(engRune) == "." {
			sb.WriteString(decimalFollowsBraille)
			continue
		}

		// existence of space means the end of numbers
		// sequence. Setting the flag to true to write the
		// braille string for the next number seq occurrence
		if unicode.IsSpace(engRune) {
			writeNumberFollow = true
		}

		brailString, prs := englishToBrailleMap[engRune]
		if !prs {
			panic("invalid input to cli")
		}

		sb.WriteString(brailString)
	}

	return sb.String()
}

func isInputBraille(firstArg string) bool {
	for _, char := range firstArg {
		if char != 'O' && char != '.' {
			return false
		}
	}

	return true
}

func main() {
	if len(os.Args) < 2 {
		panic("must provide arguments to cli")
	}

	if isInputBraille(os.Args[1]) {
		fmt.Println(translateToEnglish(os.Args[1]))
	} else {
		concatedWords := concatString(os.Args[1:])
		fmt.Println(translateToBraille(concatedWords))
	}
}
