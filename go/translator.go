package main

import (
	"fmt"
	"os"
	"strings"
)

// Maps for translation
var englishToBraille = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
	'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
	'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
	'z': "O..OOO",
	'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
	'6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
	' ': "......",
	'.': "..OO.O", ',': ".O....", '?': "..O.OO", '!': "..OOO.", ':': "..OO..",
	';': "..0.0.", '-': "....00", '/': ".0..0.", '<': ".00..0", '>': "0..00.",
	'(': "0.0..0", ')': ".0.00.",
}

var brailleToEnglish = map[string]rune{
	"O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
	"OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
	"O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
	"OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
	"O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
	"O..OOO": 'z',
	"......": ' ',
}

// Mapping for numbers, identical to the first ten letters a-j but used when number mode is on
var brailleToNumbers = map[string]rune{
	"O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5',
	"OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0',
}

// Mapping for decimals, also using the first ten letters a-j but in decimal mode
var brailleToDecimals = map[string]rune{
	"..OO.O": '.', ".O....": ',', "..O.OO": '?', "..OOO.": '!', "..OO..": ':',
	"..0.0.": ';', "....00": '-', ".0..0.": '/', ".00..0": '<', "0..00.": '>',
	"0.0..0": '(', ".0.00.": ')',
}

// Special characters for capitalization, numbers, and decimals
var brailleSpecialCharacters = map[string]string{
	".....O": "capital follows", // Capital follows
	".O.OOO": "number follows",  // Number follows
	".O...O": "decimal follows", // Decimal follows
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate.")
		return
	}

	input := os.Args[1]

	fmt.Println(input)

	// if isBraille(input) {
	// 	fmt.Println(translateToEnglish(input))
	// } else {
	// 	fmt.Println(translateToBraille(input))
	// }
}

// isBraille checks if the input string is in Braille format
func isBraille(input string) bool {
	return strings.ContainsAny(input, "O.")
}
