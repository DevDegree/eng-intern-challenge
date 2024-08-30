package main

import (
	"fmt"
	"os"
	"strings"
)

var englishToBraille = map[string]string{
	"a": "O.....", "b": "O.O...",
	"c": "OO....", "d": "OO.O..",
	"e": "O..O..", "f": "OOO...",
	"g": "OOOO..", "h": "O.OO..",
	"i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.",
	"m": "OO..O.", "n": "OO.OO.",
	"o": "O..OO.", "p": "OOO.O.",
	"q": "OOOOO.", "r": "O.OOO.",
	"s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO",
	"w": ".OOO.O", "x": "OO..OO",
	"y": "OO.OOO", "z": "O..OOO",

	" ":       "......",
	"capital": ".....O",
	"number":  ".O.OOO",

	"0": ".OOO..", "1": "O.....",
	"2": "O.O...", "3": "OO....",
	"4": "OO.O..", "5": "O..O..",
	"6": "OOO...", "7": "OOOO..",
	"8": "O.OO..", "9": ".OO...",
}

var brailleToEnglish = make(map[string]string)

func init() {
	for k, v := range englishToBraille {
		brailleToEnglish[v] = k
	}
}

func isBraille(input string) bool {
	return strings.ContainsAny(input, "O.") && len(input)%6 == 0
}

func translateToBraille(input string) string {
	var braille string
	inNumberSequence := false
	for _, char := range input {
		c := string(char)
		if c >= "A" && c <= "Z" {
			braille += englishToBraille["capital"]
			c = strings.ToLower(c)
			inNumberSequence = false // End number sequence if we encounter a capital letter
		}
		if c >= "0" && c <= "9" {
			if !inNumberSequence {
				braille += englishToBraille["number"]
				inNumberSequence = true
			}
			// Use the corresponding letter for the number
			c = string('a' + (c[0] - '0'))
		} else {
			inNumberSequence = false
		}
		if brailleChar, ok := englishToBraille[c]; ok {
			braille += brailleChar
		}
	}
	return braille
}

func translateToEnglish(input string) string {
	var english string
	isCapital := false
	isNumber := false

	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6]

		switch brailleChar {
		case englishToBraille["capital"]:
			isCapital = true
		case englishToBraille["number"]:
			isNumber = true
		default:
			if engChar, ok := brailleToEnglish[brailleChar]; ok {
				if isNumber {
					if engChar >= "a" && engChar <= "j" {
						engChar = string('0' + (engChar[0] - 'a'))
					}
					isNumber = false
				} else if isCapital {
					engChar = strings.ToUpper(engChar)
					isCapital = false
				}
				english += engChar
			}
		}
	}
	return english
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate.")
		return
	}
	input := strings.Join(os.Args[1:], " ")

	var result string
	if isBraille(input) {
		result = translateToEnglish(input)
	} else {
		result = translateToBraille(input)
	}
	fmt.Println(result)
}
