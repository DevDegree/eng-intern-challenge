package main

import (
	"fmt"
	"os"
	"strings"
)

const (
	maxBrailleChars = 6
)

const (
	CapitalFollows uint8 = iota
	DecimalFollows
	NumberFollows
)

var FollowActionsMap = map[string]uint8{
	".....O": CapitalFollows,
	".O...O": DecimalFollows,
	".O.OOO": NumberFollows,
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
	'<': ".OO..O",
	'>': "O..OO.",
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
	// braille statement chars are ASCII. so if we
	// iterate over the string, we get the correct rune

	sbRes := strings.Builder{}
	var makeCap bool
	var isNumber bool

    // more efficient way for string concatenation
    // it prevents copying the string over and over
    // with every iteration, especially her that we know
    // the maximum capacity of the underlying slice is 
    // at most 6
	sb := strings.Builder{}
	sb.Grow(maxBrailleChars)

mainLoop:
	for i, c := range brailleStatement {
		sb.WriteRune(c)

		if (i+1)%maxBrailleChars == 0 {
			singleBraille := sb.String()

			followAction, prs := FollowActionsMap[singleBraille]
			if prs {
				switch followAction {
				case NumberFollows:
					isNumber = true
					sb.Reset()
					continue mainLoop

				case CapitalFollows:
					makeCap = true
					sb.Reset()
					continue mainLoop

				case DecimalFollows:
					// pass
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

func translateToBraille(englishWords []string) {

}

func main() {
	if len(os.Args) < 2 {
		panic("must provide arguments to cli")
	}

	/*
		Assumptions
		    1. ONLY braille inputs start with .
		    2. It will ONLY be one braille input
	*/
	if len(os.Args) >= 3 || (len(os.Args) == 2 && !strings.HasPrefix(os.Args[1], ".")) {
		translateToBraille(os.Args[1:])
	}

	fmt.Println(translateToEnglish(os.Args[1]))
}
