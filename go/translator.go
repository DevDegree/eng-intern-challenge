package main

import (
	"fmt"
	"os"
	"strings"
)

const (
	brailleCapitalFollows = ".....O"
	brailleNumberFollows  = ".O.OOO"
	brailleSpace          = "......"
)

var brailleToIndex = map[string]byte{
	"O.....": 0,
	"O.O...": 1,
	"OO....": 2,
	"OO.O..": 3,
	"O..O..": 4,
	"OOO...": 5,
	"OOOO..": 6,
	"O.OO..": 7,
	".OO...": 8,
	".OOO..": 9,
	"O...O.": 10,
	"O.O.O.": 11,
	"OO..O.": 12,
	"OO.OO.": 13,
	"O..OO.": 14,
	"OOO.O.": 15,
	"OOOOO.": 16,
	"O.OOO.": 17,
	".OO.O.": 18,
	".OOOO.": 19,
	"O...OO": 20,
	"O.O.OO": 21,
	".OOO.O": 22,
	"OO..OO": 23,
	"OO.OOO": 24,
	"O..OOO": 25,
}

var indexToBraille = reverseMap(brailleToIndex)

func reverseMap(m map[string]byte) map[rune]string {
	reversed := make(map[rune]string)
	for k, v := range m {
		reversed[rune(v)] = k
	}
	return reversed
}

func isBraille(text string) bool {
	for _, c := range text {
		if c != 'O' && c != '.' {
			return false
		}
	}

	return true
}

func englishToBraille(text string) (string, error) {
	var sb strings.Builder

	emittedNumber := false
	for _, c := range text {
		if c >= 'a' && c <= 'z' {
			sb.WriteString(indexToBraille[c-'a'])
		} else if c >= 'A' && c <= 'Z' {
			sb.WriteString(brailleCapitalFollows)
			sb.WriteString(indexToBraille[c-'A'])
		} else if c >= '0' && c <= '9' {
			if !emittedNumber {
				sb.WriteString(brailleNumberFollows)
				emittedNumber = true
			}

			if c == '0' {
				sb.WriteString(indexToBraille[9])
			} else {
				sb.WriteString(indexToBraille[c-'1'])
			}
		} else if c == ' ' {
			emittedNumber = false
			sb.WriteString(brailleSpace)
		} else {
			return "", fmt.Errorf("unsupported english character '%c'", c)
		}
	}

	return sb.String(), nil
}

func brailleToEnglish(text string) (string, error) {
	var sb strings.Builder

	capital := false // should encode a capital letter next
	number := false  // should encode numbers next

	if len(text)%6 != 0 {
		return "", fmt.Errorf("invalid braille length %d (not a multiple of 6)", len(text))
	}

	for i := 0; i < len(text); i += 6 {
		chunk := text[i : i+6]

		if chunk == brailleCapitalFollows {
			capital = true
			continue
		} else if chunk == brailleNumberFollows {
			number = true
		} else if chunk == brailleSpace {
			sb.WriteByte(' ')
			number = false
		} else {
			index, ok := brailleToIndex[chunk]
			if !ok {
				return "", fmt.Errorf("unknown braille string '%s'", chunk)
			}

			if number {
				if index > 9 {
					return "", fmt.Errorf("invalid braille number '%s'", chunk)
				}
				sb.WriteByte('0' + (index+1)%10) // wraps index 9 around to '0'
			} else if capital {
				sb.WriteByte('A' + index)
			} else {
				sb.WriteByte('a' + index)
			}
		}

		capital = false
	}

	return sb.String(), nil
}

func main() {
	input := strings.Join(os.Args[1:], " ")

	var output string
	var err error
	if isBraille(input) {
		output, err = brailleToEnglish(input)
	} else {
		output, err = englishToBraille(input)
	}

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(output)
	}
}
