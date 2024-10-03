package main

import (
	"errors"
	"os"
	"strconv"
	"strings"
)

var brailleMap = map[string]string{
	"a":   "O.....",
	"b":   "O.O...",
	"c":   "OO....",
	"d":   "OO.O..",
	"e":   "O..O..",
	"f":   "OOO...",
	"g":   "OOOO..",
	"h":   "O.OO..",
	"i":   ".OO...",
	"j":   ".OOO..",
	"k":   "O...O.",
	"l":   "O.O.O.",
	"m":   "OO..O.",
	"n":   "OO.OO.",
	"o":   "O..OO.",
	"p":   "OOO.O.",
	"q":   "OOOOO.",
	"r":   "O.OOO.",
	"s":   ".OO.O.",
	"t":   ".OOOO.",
	"u":   "O...OO",
	"v":   "O.O.OO",
	"w":   ".OOO.O",
	"x":   "OO..OO",
	"y":   "OO.OOO",
	"z":   "O..OOO",
	"1":   "O.....",
	"2":   "O.O...",
	"3":   "OO....",
	"4":   "OO.O..",
	"5":   "O..O..",
	"6":   "OOO...",
	"7":   "OOOO..",
	"8":   "O.OO..",
	"9":   ".OO...",
	"0":   ".OOO..",
	".":   "..OO.O",
	" ":   "......",
	"cap": ".....O",
	"num": ".O.OOO",
}

var engMap = map[string]string{
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
	"..OO.O": ".",
	"......": " ",
	".....O": "cap",
	".O.OOO": "num",
}

func main() {
	msg := os.Args[1:]
	if len(msg) == 0 {
		panic("No argument provided!")
	}

	var result string
	var err error
	if isEnglish(msg) {
		var builder strings.Builder
		for i := 0; i < len(msg)-1; i++ {
			builder.WriteString(msg[i] + " ")
		}
		builder.WriteString(msg[len(msg)-1])
		result, err = engToBraille(builder.String())
	} else {
		result, err = brailleToEng(msg[0])
	}

	if err != nil {
		panic(err)
	}

	println(result)
}

// Convert from English to Braille code
func engToBraille(msg string) (string, error) {
	var builder strings.Builder
	isNum := false
	for _, c := range msg {
		if c >= 'A' && c <= 'Z' {
			builder.WriteString(brailleMap["cap"])
			c = c + 32
		}
		braille, ok := brailleMap[string(c)]
		if !ok {
			return braille, errors.New("invalid character" + string(c))
		}
		if c >= '0' && c <= '9' {
			if !isNum {
				builder.WriteString(brailleMap["num"])
				isNum = true
			}
		} else if c == ' ' {
			isNum = false
		}
		builder.WriteString(braille)
	}
	return builder.String(), nil
}

// Convert from Braille code to English
func brailleToEng(msg string) (string, error) {
	var builder strings.Builder
	isCap := false
	isNum := false

	for i := 0; i < len(msg); i += 6 {
		eng, ok := engMap[msg[i:i+6]]
		if !ok {
			return eng, errors.New("invalid braille code")
		}

		if eng == "cap" {
			isCap = true
		} else if eng == "num" {
			isNum = true
		} else {
			if eng == " " && isNum {
				isNum = false
			}
			if isCap {
				builder.WriteString(strings.ToUpper(eng))
				isCap = false
			} else if isNum {
				if eng[0] >= 'k' || eng[0] <= 'a' {
					return "", errors.New("invalid number")
				}
				number := (eng[0] - 'a' + 1) % 10
				builder.WriteString(strconv.Itoa(int(number)))
			} else {
				builder.WriteString(eng)
			}
		}
	}
	return builder.String(), nil
}

// Check if the input is English or not
func isEnglish(args []string) bool {
	if len(args) > 1 || len(args[0])%6 != 0 {
		return true
	}
	// if any character is not capital O or a dot, then it is a string
	for _, c := range args[0] {
		if c != 'O' && c != '.' {
			return true
		}
	}
	return false
}
