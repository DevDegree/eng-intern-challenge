package main

import (
	"fmt"
	"os"
	"strings"
)

var uppercaseMode bool
var numberMode bool

func allBrailleChars(testString string) bool {
	for _, c := range testString {
		if c != 'O' && c != '.' {
			return false
		}
	}

	return true
}

func isNum(char string) bool {
	return char == "1" || char == "2" || char == "3" || char == "4" ||
		char == "5" || char == "6" || char == "7" || char == "8" ||
		char == "9" || char == "0"
}

func isUpper(char string) bool {
	return strings.ToUpper(char) == char
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

func englishToBraille(char string) string {
	var brailleSet strings.Builder

	if isNum(char) && !numberMode {
		brailleSet.WriteString(".O.OOO")

		numberMode = true
	} else if !isNum(char) && isUpper(char) {
		brailleSet.WriteString(".....O")
	}

	switch char {
	case "1", "a", "A":
		brailleSet.WriteString("O.....")
	case "2", "b", "B":
		brailleSet.WriteString("O.O...")
	case "3", "c", "C":
		brailleSet.WriteString("OO....")
	case "4", "d", "D":
		brailleSet.WriteString("OO.O..")
	case "5", "e", "E":
		brailleSet.WriteString("O..O..")
	case "6", "f", "F":
		brailleSet.WriteString("OOO...")
	case "7", "g", "G":
		brailleSet.WriteString("OOOO..")
	case "8", "h", "H":
		brailleSet.WriteString("O.OO..")
	case "9", "i", "I":
		brailleSet.WriteString(".OO...")
	case "10", "j", "J":
		brailleSet.WriteString(".OOO..")
	case "k", "K":
		brailleSet.WriteString("O...O.")
	case "l", "L":
		brailleSet.WriteString("O.O.O.")
	case "m", "M":
		brailleSet.WriteString("OO..O.")
	case "n", "N":
		brailleSet.WriteString("OO.OO.")
	case "o", "O":
		brailleSet.WriteString("O..OO.")
	case "p", "P":
		brailleSet.WriteString("OOO.O.")
	case "q", "Q":
		brailleSet.WriteString("OOOOO.")
	case "r", "R":
		brailleSet.WriteString("O.OOO.")
	case "s", "S":
		brailleSet.WriteString(".OO.O.")
	case "t", "T":
		brailleSet.WriteString(".OOOO.")
	case "u", "U":
		brailleSet.WriteString("O...OO")
	case "v", "V":
		brailleSet.WriteString("O.O.OO")
	case "w", "W":
		brailleSet.WriteString(".OOO.O")
	case "x", "X":
		brailleSet.WriteString("OO..OO")
	case "y", "Y":
		brailleSet.WriteString("OO.OOO")
	case "z", "Z":
		brailleSet.WriteString("O..OOO")
	case " ":
		brailleSet.WriteString("......")
		numberMode = false
	}

	return brailleSet.String()
}

func main() {
	var translatedString strings.Builder

	// check for English case (if spaces or non-Braille chars present, must be English)
	if len(os.Args) > 2 || !allBrailleChars(os.Args[1]) {
		// parse English
		for i, arg := range os.Args[1:] {
			for _, c := range arg {
				translatedString.WriteString(englishToBraille(string(c)))
			}

			if i < len(os.Args)-2 {
				translatedString.WriteString("......")
				numberMode = false
			}
		}
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

	fmt.Println(translatedString.String())
}
