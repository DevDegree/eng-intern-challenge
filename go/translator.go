package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

const CAPS string = ".....O"
const NUM string = ".O.OOO"
const SPACE string = "......."

var engToBraileNum = map[rune]string{
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

var engToBraile = map[rune]string{
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

var braileToEng = map[string]rune{
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
	"......": ' ',
}

var braileToEnglishNum = map[string]rune{
	"O.....": '1',
	"O.O...": '2',
	"OO....": '3',
	"OO.O..": '4',
	"O..O..": '5',
	"OOO...": '6',
	"OOOO..": '7',
	"O.OO..": '8',
	".OO...": '9',
	".OOO..": '0',
}

func main() {
	textToTranslate := strings.Join(os.Args[1:], " ")

	fmt.Println(translate(textToTranslate))

}

func translate(text string) string {

	if len(text) != 0 {

	}

	if len(text)%6 != 0 {
		return englishToBraile(text)
	}

	translation, err := braileToEnglish(text)

	if err != nil {
		return englishToBraile(text)
	}

	return translation
}

func englishToBraile(text string) string {

	translatedString := ""
	isNumber := false

	for _, char := range text {

		value, _ := engToBraile[unicode.ToLower(char)]

		if unicode.IsUpper(char) {
			translatedString += CAPS
		}

		if unicode.IsDigit(char) {
			if !isNumber {
				isNumber = true
				translatedString += NUM
			}

			value, _ = engToBraileNum[char]
		}

		if isNumber && !unicode.IsDigit(char) {
			isNumber = false
		}

		translatedString += value
	}

	return translatedString
}

func braileToEnglish(text string) (string, error) {

	translatedString := ""
	isCaps := false
	isNum := false
	currString := text

	for i := 0; i < len(text)/6; i++ {
		value, ok := braileToEng[currString[:6]]
		if !ok {
			if currString[:6] == CAPS {
				isCaps = true
			} else if currString[:6] == NUM {
				isNum = true
			}

			currString = currString[6:]
			continue
		}

		if isCaps {
			value = unicode.ToUpper(value)
			isCaps = false
		} else if isNum {
			if value != ' ' {
				value = braileToEnglishNum[currString[:6]]
			} else {
                isNum = false
			}
		}

		translatedString += string(value)
		currString = currString[6:]
	}

	return translatedString, nil
}
