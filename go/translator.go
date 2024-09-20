package main

import (
	"fmt"
	"os"
	"strings"
)

var uppercaseMode bool
var numberMode bool

func allBraileChars(testString string) bool {
	for _, c := range testString {
		if c != 'O' && c != '.' {
			return false
		}
	}

	return true
}

func brailleToEnglish(charSet string) string {
	var c string
	switch charSet {
	case "O.....":
		if numberMode {
			c = "1"
		} else {
			c = "a"
		}
	case "O.O...":
		if numberMode {
			c = "2"
		} else {
			c = "b"
		}
	case "OO....":
		if numberMode {
			c = "3"
		} else {
			c = "c"
		}
	case "OO.O..":
		if numberMode {
			c = "4"
		} else {
			c = "d"
		}
	case "O..O..":
		if numberMode {
			c = "5"
		} else {
			c = "e"
		}
	case "OOO...":
		if numberMode {
			c = "6"
		} else {
			c = "f"
		}
	case "OOOO..":
		if numberMode {
			c = "7"
		} else {
			c = "g"
		}
	case "O.OO..":
		if numberMode {
			c = "8"
		} else {
			c = "h"
		}
	case ".OO...":
		if numberMode {
			c = "9"
		} else {
			c = "i"
		}
	case ".OOO..":
		if numberMode {
			c = "0"
		} else {
			c = "j"
		}
	case "O...O.":
		c = "k"
	case "O.O.O.":
		c = "l"
	case "OO..O.":
		c = "m"
	case "OO.OO.":
		c = "n"
	case "O..OO.":
		c = "o"
	case "OOO.O.":
		c = "p"
	case "OOOOO.":
		c = "q"
	case "O.OOO.":
		c = "r"
	case ".OO.O.":
		c = "s"
	case ".OOOO.":
		c = "t"
	case "O...OO":
		c = "u"
	case "O.O.OO":
		c = "v"
	case ".OOO.O":
		c = "w"
	case "OO..OO":
		c = "x"
	case "OO.OOO":
		c = "y"
	case "O..OOO":
		c = "z"
	case "......":
		c = " "
		numberMode = false
	}

	if uppercaseMode {
		c = strings.ToUpper(c)
	}

	uppercaseMode = charSet == ".....O"
	numberMode = numberMode || charSet == ".O.OOO"

	return c
}

func main() {
	fmt.Println(len(os.Args), os.Args)

	var translatedString strings.Builder

	// check for English case (if spaces or non-Braille chars present, must be English)
	if len(os.Args) > 2 || !allBraileChars(os.Args[1]) {
		// parse English
	} else {
		// parse Braile
		var curBraille strings.Builder

		for i, c := range os.Args[1] {
			curBraille.WriteString(string(c))

			if i%6 == 5 {
				translatedString.WriteString(brailleToEnglish(curBraille.String()))
				curBraille.Reset()
			}
		}
	}
}
