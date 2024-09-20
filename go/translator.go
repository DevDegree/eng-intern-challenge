/* trunk-ignore-all(gofmt) */
package main

import (
	"fmt"
	"strings"
	"unicode"
	"os"
)

// Define some Constant Rune Representation
const (
	capitalFollows = ".....O"
	numberFollows  = ".O.OOO"
	brailleWidth = 6
)

var brailleMapping = map[rune]string{
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
	'w': ".OOOOO",
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
	'0': ".OOOO.",
	' ': "......", // Space
}

// Hardcoded reverse mapping for Braille to english text translation
var reverseBrailleMapping = map[string]rune{
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
	".OOOOO": 'w',
	"OO..OO": 'x',
	"OO.OOO": 'y',
	"O..OOO": 'z',
	"......": ' ', // Space
}

func translateEnglishTextToBraille(text string) string {
    var braille strings.Builder
    curNumber := false

    for _, ch := range text {
        if curNumber && !(ch >= '0' && ch <= '9') && ch == ' ' {
            curNumber = false
            braille.WriteString(brailleMapping[' '])
			continue
        }

        if ch >= 'A' && ch <= 'Z' {
            braille.WriteString(capitalFollows)
            ch = unicode.ToLower(ch)
        } else if ch >= '0' && ch <= '9' {
            if !curNumber {
                braille.WriteString(numberFollows)
                curNumber = true
            }
        }

        brailleChar, ok := brailleMapping[ch]
        if !ok {
            brailleChar = "......"
        }
        braille.WriteString(brailleChar)
    }
    return braille.String()
}


func translateBrailleTextToEnglish(text string) string {
    var english strings.Builder
    var brailleWord strings.Builder
    curCapital := false
    curNumber := false

    for i := 0; i < len(text); i += brailleWidth {
        if i+brailleWidth > len(text) {
            break // Avoid out-of-range errors
        }
        
        brailleWord.Reset() // Reset the builder for each word
        brailleWord.WriteString(text[i:i+brailleWidth])

        if brailleWord.String() == capitalFollows {
            curCapital = true
            continue
        }

        if brailleWord.String() == numberFollows {
            curNumber = true
            continue
        }

        englishChar, ok := reverseBrailleMapping[brailleWord.String()]
        if !ok {
            englishChar = ' '
        }

        if englishChar == ' ' {
            // Assume this space ends the stream of numbers
            if curNumber {
                curNumber = false
            }
        }

        if curCapital {
            englishChar = unicode.ToUpper(englishChar)
			curCapital = false
        }

        if curNumber {
            englishChar = brailleLettertoDigit(englishChar)
        }

        english.WriteRune(englishChar)
    }

    return english.String()
}




func brailleLettertoDigit (ch rune) rune {
	if ch == 'j' {
		return '0'
	}
	return ch - ('a' - '1')

}

// detectBrailleInput return true if the input is braille, and false otherwise
func detectBrailleInput(text string) bool {
	//see if the input is only composed of . and o
	for _, ch := range text {
		if ch != '.' && ch != 'O' {
			return false
		}
	}

	//see if the input length is divisible by 6
	return (len(text) % 6) == 0
}


func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run translator.go <text1> <text2> ...")
		return
	}

	var inputText strings.Builder

	for i, arg := range os.Args[1:] {
		inputText.WriteString(arg)
		if i < len(os.Args[1:])-1 {
			inputText.WriteString(" ")
		}
	}


	var output string;

	if detectBrailleInput(inputText.String()) {
		output = translateBrailleTextToEnglish(inputText.String())
	} else {
		output = translateEnglishTextToBraille(inputText.String())
	}

	fmt.Println(output)
}
