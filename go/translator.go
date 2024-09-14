package main

import (
	"os"
	"strings"
)

// type BrailleEngilshTranslator interface {
// 	func translateToBraille()
// }

// type translator struct {
// 	string
// 	isBraille

// }

// func newTranslator(...) BrailleEngilshTranslator {

// }

// func (*Translator) translateToBraille

type BrailleValue struct {
	value byte
}

type BrailleMapping struct {
	character *BrailleValue
	number    *BrailleValue
	decimal   *BrailleValue
}

const UppercaseFollows = ".....O"
const NumberFollows = ".O.OOO"

var fromBrailleLetters = map[string]byte{
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
	"......": ' ', // space
}

var fromBrailleNumbers = map[string]byte{
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

var fromEnglishLetters map[byte]string
var fromEnglishNumbers map[byte]string

func main() {
	arg := strings.Join(os.Args[1:], " ")
	fromEnglishLetters = reverseMap(fromBrailleLetters)
	fromEnglishNumbers = reverseMap(fromBrailleNumbers)

	if isBraille(arg) {
		print(translateFromBraille(arg))
	} else {
		print(translateFromEnglish(arg))
	}

}

func reverseString(s string) string {
	result := ""
	for i := len(s); i >= 0; i-- {
		result += string(s[i])
	}
	return result
}

func reverseMap(m map[string]byte) map[byte]string {
	reversedMap := make(map[byte]string, len(m))
	for key, value := range m {
		reversedMap[value] = key
	}
	return reversedMap
}

func isUppercase(r byte) bool {
	return r >= 'A' && r <= 'Z'
}

func isDigit(b byte) bool {
	return b >= '.' && b <= '9'
}

func translateFromEnglish(s string) string {
	output := ""
	isNumbersRightNow := false
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			isNumbersRightNow = false
			output += fromEnglishLetters[s[i]]
			continue
		}
		
		// check number
		if !isNumbersRightNow && isDigit(s[i]) {
			output += NumberFollows
			isNumbersRightNow = true
		}
		if isNumbersRightNow {

			output += fromEnglishNumbers[s[i]]
			continue
		}

		// check upper case
		if isUppercase(s[i]) {
			output += UppercaseFollows
			output += fromEnglishLetters[s[i]+32]
			continue
		}

		// normal case
		output += fromEnglishLetters[s[i]]
	}
	return output
}

func translateFromBraille(s string) string{
	println(s)
	output := ""
	isNumbersRightNow := false
	isNextUppercase := false
	for i := 0; i < len(s); i += 6 {
		val := s[i:i+6]
		if val == NumberFollows{
			isNumbersRightNow = true
		} else if val == UppercaseFollows {
			isNextUppercase = true
		} else if val == "......" {
			isNumbersRightNow = false
			output += " "
		} else if isNumbersRightNow {
			output += string(fromBrailleNumbers[val])
		}  else if isNextUppercase {
			output += string(fromBrailleLetters[val] - 32)
			isNextUppercase = false
		} else {
			output += string(fromBrailleLetters[val])
			
		}
	}
	return output
}

func isBraille(s string) bool {
	for i := 0; i < len(s); i++ {
		if s[i] != 'O' && s[i] != '.' {
			return false
		}
	}
	return true
}
