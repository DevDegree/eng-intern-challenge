package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var alphanumToBraille = map[string]string{
	"a": "O.....",
	"b": "O.O...",
	"c": "OO....",
	"d": "OO.O..",
	"e": "O..O..",
	"f": "OOO...",
	"g": "OOOO..",
	"h": "O.OO..",
	"i": ".OO...",
	"j": ".OOO..",
	"k": "O...O.",
	"l": "O.O.O.",
	"m": "OO..O.",
	"n": "OO.OO.",
	"o": "O..OO.",
	"p": "OOO.O.",
	"q": "OOOOO.",
	"r": "O.OOO.",
	"s": ".OO.O.",
	"t": ".OOOO.",
	"u": "O...OO",
	"v": "O.O.OO",
	"w": ".OOO.O",
	"x": "OO..OO",
	"y": "OO.OOO",
	"z": "O..OOO",
	" ": "......",
	"1": "O.....",
	"2": "O.O...",
	"3": "OO....",
	"4": "OO.O..",
	"5": "O..O..",
	"6": "OOO...",
	"7": "OOOO..",
	"8": "O.OO..",
	"9": ".OO...",
	"0": ".OOO..",
}

var brailleToAlpha = map[string]string{
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
	"......": " ",
	".....O": "capital",
	".O.OOO": "number",
}

var brailleToNum = map[string]string{
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
	"......": " ",
}

// determines if a string s is English or Braille
func isBraille(s string) bool {
	// number of characters in s should be a multiple of 6
	if len(s)%6 != 0 {
		return false
	}

	// all character should either be . or O
	for _, char := range s {
		if char != 'O' && char != '.' {
			return false
		}
	}

	return true
}

// converts a string s from braille to english
func brailleToEnglish(s string) string {
	var output string
	isCapital := false
	isNum := false
	for i := 0; i < len(s); i += 6 {
		brailleChar := s[i : i+6]
		if isNum {
			if engChar, exists := brailleToNum[brailleChar]; exists {
				if engChar == " " {
					output += engChar
					isNum = false
				} else {
					output += engChar
				}
			} else {
				log.Fatal("Error: Invalid input.")
			}
		} else {
			if engChar, exists := brailleToAlpha[brailleChar]; exists {
				if engChar == "capital" {
					isCapital = true
				} else if engChar == "number" {
					isNum = true
				} else if isCapital {
					engChar = strings.ToUpper(engChar)
					output += engChar
					isCapital = false
				} else {
					output += engChar
				}
			} else {
				log.Fatal("Error: Invalid input.")
			}
		}
	}
	return output
}

// converts a string s from english to braille
func englishToBraille(s string) string {
	var capFollows = ".....O"
	var numFollow = ".O.OOO"
	var isNum = false
	var output string
	for i := 0; i < len(s); i++ {
		engChar := s[i : i+1]

		// if the next character is a number
		if _, err := strconv.ParseInt(engChar, 10, 64); err == nil {
			if !isNum { // not already reading numbers
				output += numFollow
				isNum = true
			}
			if brailleChar, exists := alphanumToBraille[engChar]; exists {
				output += brailleChar
			} else {
				log.Fatal("Error: Invalid input.")
			}
		} else {
			isNum = false

			// if the next character is capitalized
			if strings.ToLower(engChar) != engChar && strings.ToUpper(engChar) == engChar {
				output += capFollows
				engChar = strings.ToLower(engChar)
			}
			if brailleChar, exists := alphanumToBraille[engChar]; exists {
				output += brailleChar
			} else {
				log.Fatal("Error: Invalid input.")
			}
		}
	}
	return output
}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("Error: Invalid input.")
	}

	input := strings.Join(os.Args[1:], " ")

	// determine if input is English or Braille
	var output string
	if isBraille(input) {
		output = brailleToEnglish(input)
		fmt.Println(output)
	} else {
		output = englishToBraille(input)
		fmt.Println(output)
	}
}
