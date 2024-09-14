package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

var brailleToEnglish = map[string]string{
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
	".....O": "capital",
	".O.OOO": "number",
	".O...O": "decimal",
	"......": " ",
}

var englishToBraille = map[string]string{
	"a":       "O.....",
	"b":       "O.O...",
	"c":       "OO....",
	"d":       "OO.O..",
	"e":       "O..O..",
	"f":       "OOO...",
	"g":       "OOOO..",
	"h":       "O.OO..",
	"i":       ".OO...",
	"j":       ".OOO..",
	"k":       "O...O.",
	"l":       "O.O.O.",
	"m":       "OO..O.",
	"n":       "OO.OO.",
	"o":       "O..OO.",
	"p":       "OOO.O.",
	"q":       "OOOOO.",
	"r":       "O.OOO.",
	"s":       ".OO.O.",
	"t":       ".OOOO.",
	"u":       "O...OO",
	"v":       "O.O.OO",
	"w":       ".OOO.O",
	"x":       "OO..OO",
	"y":       "OO.OOO",
	"z":       "O..OOO",
	"capital": ".....O",
	"number":  ".O.OOO",
	"decimal": ".O...O",
	" ":       "......",
}

var alphabetToNumber = map[string]string{
	"a": "1",
	"b": "2",
	"c": "3",
	"d": "4",
	"e": "5",
	"f": "6",
	"g": "7",
	"h": "8",
	"i": "9",
	"j": "0",
}

var numberToAlphabet = map[string]string{
	"1": "a",
	"2": "b",
	"3": "c",
	"4": "d",
	"5": "e",
	"6": "f",
	"7": "g",
	"8": "h",
	"9": "i",
	"0": "j",
}

func parseConvertBraille(brailleString string) string {
	numbers := false
	returnString := ""

	for i := 0; i < (len(brailleString) / 6); i++ {
		brailleChar := brailleString[i*6 : (i+1)*6]
		englishChar, ok := brailleToEnglish[brailleChar]

		if !ok {
			os.Exit(1)
		}

		if numbers {
			englishChar, ok = alphabetToNumber[englishChar]
			if !ok {
				os.Exit(1)
			}
		}

		if englishChar == "capital" {
			i++
			brailleChar = brailleString[i*6 : (i+1)*6]
			englishChar, ok = brailleToEnglish[brailleChar]
			if !ok {
				os.Exit(1)
			}
			englishChar = string(englishChar[0] - 32)
		} else if englishChar == "number" {
			numbers = true
			continue
		}

		returnString += englishChar
	}

	return returnString
}

func parseConvertANString(ANString string) string {
	numbers := false
	returnString := ""
	for _, char := range ANString {

		if char >= 'A' && char <= 'Z' {
			returnString += englishToBraille["capital"]
			returnString += englishToBraille[string(char+32)]
			if numbers {
				numbers = false
			}
			continue
		} else if char >= '0' && char <= '9' {
			if !numbers {
				returnString += englishToBraille["number"]
			}
			returnString += englishToBraille[numberToAlphabet[string(char)]]
			if !numbers {
				numbers = true
			}
			continue
		} else if char == ' ' {
			returnString += englishToBraille[" "]
			if numbers {
				numbers = false
			}
			continue
		}

		englishChar, ok := englishToBraille[string(char)]

		if !ok {
			os.Exit(1)
		}

		returnString += englishChar
	}

	return returnString
}

func main() {
	args := os.Args[1:]
	input := strings.Join(args, " ")

	braillePattern := regexp.MustCompile(`^[.O]+$`)

	if braillePattern.MatchString(input) {
		convertedString := parseConvertBraille(input)
		fmt.Println(convertedString)
	} else {
		convertedString := parseConvertANString(input)
		fmt.Println(convertedString)
	}
}
