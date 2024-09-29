package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	if len(os.Args) > 1 {
		input := strings.Join(os.Args[1:], " ")
		checker := strings.ReplaceAll(strings.ReplaceAll(input, "O", ""), ".", "")
		if (checker) == "" {
			translateBrailleToEnglish(input)
		} else {
			translateEnglishToBraille(input)
		}
	} else {
	}
}

func translateBrailleToEnglish(input string) {
	var output string
	capital := false
	number := false

	var brailleToEnglish = map[string]string{
		"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
		"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
		"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
		"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
		"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
		"O..OOO": "z", "......": " ", ".....O": "CAP", ".O...O": "DEC", ".O.OOO": "#",
		"..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
		"..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
		/*"O..OO.": ">" duplicate key */
		"O.O..O": "(", ".O.OO.": ")",
	}

	var brailleToNumber = map[string]string{
		"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
		"OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
	}

	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6]
		if brailleChar == ".....O" {
			capital = true
			continue
		}
		if brailleChar == ".O.OOO" {
			number = true
			continue
		}
		if brailleChar == "......" {
			number = false
			output += " "
			continue
		}

		if number {
			output += brailleToNumber[string(brailleChar)]
		} else if capital {
			output += strings.ToUpper(brailleToEnglish[string(brailleChar)])
			capital = false
		} else {
			output += brailleToEnglish[string(brailleChar)]
		}

	}

	fmt.Println(output)
}

func translateEnglishToBraille(input string) {

	var englishToBraille = map[string]string{
		"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
		"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
		"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
		"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
		"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
		"z": "O..OOO", " ": "......", "1": "O.....", "2": "O.O...", "3": "OO....",
		"4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
		"9": ".OO...", "0": ".OOO..", "CAP": ".....O", "DEC": ".O...O", "#": ".O.OOO",
		".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
		";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
		"(": "O.O..O", ")": ".O.OO.",
	}

	var output string
	number := false

	for _, char := range input {
		if char >= 'A' && char <= 'Z' {
			output += englishToBraille["CAP"]
			char += 32
			output += englishToBraille[string(char)]
			continue
		}

		if char >= '0' && char <= '9' && !number {
			output += englishToBraille["#"]
			number = true
			output += englishToBraille[string(char)]
			continue
		}

		if char == ' ' {
			output += englishToBraille[" "]
			number = false
			continue
		}

		output += englishToBraille[string(char)]

	}

	fmt.Println(output)
}
