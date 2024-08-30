package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var englishToBraille = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
	"z": "O..OOO",

	"O": ".OOO..", "1": "O.....", 
	" ": "......", 
	"capital_follows": ".....O","number_follows": ".O.OOO",
}

func main() {
	input := strings.Join(os.Args[1:], " ")

	for _, char := range input {
		if (unicode.IsUpper(char)) {
			fmt.Print(englishToBraille["capital_follows"])
		}
		if (unicode.IsDigit(char)) {
			fmt.Print(englishToBraille["number_follows"])
		}
		
		braille := englishToBraille[string(unicode.ToLower(char))]
		fmt.Print(braille)
	}
	fmt.Println()
}