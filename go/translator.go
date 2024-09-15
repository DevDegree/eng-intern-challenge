package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

// pseudo-constant maps of braille <-> english alphabets, since maps cannot be `const`
var braille = map[string]string{
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
	".....O": "caps",
	".O...O": "deci",
	".O.OOO": "nums",
	"..OO.O": ".",
	"..O...": ",",
	"..O.OO": "?",
	"..OOO.": "!",
	"..OO..": ":",
	"..O.O.": ";",
	"....OO": "-",
	".O..O.": "/",
	//".OO..O": "<",
	//"O..OO.": ">", // duplicates/collides with "o", moved to numbers map
	"O.O..O": "(",
	".O.OO.": ")",
	"......": " ",
}

var numbers = map[string]string{
	"O.....": "1",
	"O.O...": "2",
	"OO....": "3",
	"OO.O..": "4",
	"O..O..": "5",
	"OOO...": "6",
	"OOOO..": "7",
	"O.OO..": "8",
	".OO...": "9",
	".OOO..": "O",
	".OO..O": "<",
	"O..OO.": ">",
}

// braille -> capital english letters map
var capitals = make(map[string]string, 26)

// english -> braille map
var english = make(map[string]string, 52)

func initMaps() {
	// initialize remaining maps from existing pseudo-constant ones
	for k, v := range braille {
		capitals[k] = strings.ToUpper(v) // convert all pairs, even though we only need the capital letters
	}
	//  combine the lowercase braille and numbers for the english -> braille map
	for k, v := range braille {
		english[v] = k
	}
	for k, v := range numbers {
		english[v] = k
	}

	// adjust some braille values, set after other maps are constructed to avoid collisions
	braille[".O...O"] = "."
}

func engToBraille(args []string) {
	// determine the type of character:
	var numberMode bool
	for i, word := range args {

		// spaces exist between the indices (words)
		// specifically, output a space before each word except the first
		if i != 0 {
			fmt.Print(english[" "])
		}

		// - reset number mode, since it only applies to the word
		numberMode = false

		for _, c := range word {
			switch {
			// handle different types of characters (numbers, capitals) by ASCII value
			// these cases require additional braille symbols to be outputted before the visible english character
			case (c-'0' >= 0 && c-'0' < 10): // current character is a number
				if !numberMode {
					numberMode = true
					fmt.Print(english["nums"]) // output the 'number follows' character at the beginning of a number
				}
			case (c-'A' >= 0 && c-'A' < 26):
				fmt.Print(english["caps"]) // output 'capital follows' character, effective for the next character only
				c = unicode.ToLower(c)
			}

			var letter string
			// handle mode-specific character overrides
			// - distinguish between . (period) and . (decimal point)
			if c == '.' && numberMode {
				letter = "deci"
			} else {
				letter = string(c)
			}
			fmt.Print(english[letter])
		}
	}
}
func brailleToEng(args []string) {
	// braille input looks to be 1 continuous string, so args should only have 1 index
	var currentMap map[string]string = braille
	var capMode bool

	for _, word := range args {
		for i := 0; i < len(word); i += 6 {
			s := word[i : i+6] // split the braille into 6-character-long symbols

			switch {
			case s == english["caps"]:
				currentMap = capitals // set the map to use capitals, which should reset after the next symbol is printed
				capMode = true
				continue
			case s == english["nums"]:
				currentMap = numbers // set the map to use numbers, which shoul reset at the end of a word
				continue
			case s == english[" "]: // at the end of a word, reset the map to default
				currentMap = braille
			}
			fmt.Print(currentMap[s])
			if capMode == true {
				capMode = false
				currentMap = braille
			}
		}
	}
}

func main() {
	initMaps()

	// determine braille or english input
	input := "english"
	word := os.Args[1]
	if len(word) >= 6 {
		_, ok := braille[word[:6]]
		if ok {
			input = "braille"
		}
	}

	switch input {
	case "english":
		engToBraille(os.Args[1:])
	case "braille":
		brailleToEng(os.Args[1:])
	}
}
