package main

import (
	"fmt"
	"os"
	"strings"
)

var bra2EngAlp = map[string]string{
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
	"O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
	".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
	"OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
	"OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
	"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
	"OO.OOO": "y", "O..OOO": "z",
}

var bra2EngInt = map[string]string{
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
	"O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8",
	".OO...": "9", ".OOO..":"0",
}

var eng2Bra = map[string]string{
	"a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..",
	"e" : "O..O..", "f" : "OOO...", "g" : "OOOO..", "h" : "O.OO..",
	"i" : ".OO...", "j" : ".OOO..", "k" : "O...O.", "l" : "O.O.O.",
	"m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.", "p" : "OOO.O.",
	"q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.",
	"u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
	"y" : "OO.OOO", "z" : "O..OOO", 
	"1" : "O.....", "2" : "O.O...", "3" : "OO....", "4" : "OO.O..",
	"5" : "O..O..", "6" : "OOO...", "7" : "OOOO..", "8" : "O.OO..",
	"9" : ".OO...", "0" : ".OOO..", "capitalize" : ".....O", "number" : ".O.OOO",
}

func transEng2Bra(input string) string {
	var res strings.Builder
	isNumber := false 
	for _, char := range input {
		c := string(char)
		if c >= "A" && c <= "Z" {
			res.WriteString(eng2Bra["capitalize"])
			c = strings.ToLower(c)
		}

		if c >= "0" && c <= "9" && !isNumber {
			res.WriteString(eng2Bra["number"])
			isNumber = true 
		} else if c == " " {
			isNumber = false 
			res.WriteString("......")
			continue 
		}

		if bra, ok := eng2Bra[c]; ok {
			res.WriteString(bra)
		}
	}
	return res.String()
}

func transBra2Eng(input string) string {
	var res strings.Builder
	isCapitalize := false
	isNumber := false 

	for i := 0; i < len(input); i += 6 {
		symbol := input[i : i+6]
		if symbol == ".....O" {
			isCapitalize = true
			continue
		}
		if symbol == ".O.OOO" {
			isNumber = true
			continue 
		}
		if symbol == "......" {
			res.WriteString(" ")
			isNumber = false
			continue 
		}

		if isNumber {
			res.WriteString(bra2EngInt[symbol])
		} else {
			if isCapitalize {
				res.WriteString(strings.ToUpper(bra2EngAlp[symbol]))
				isCapitalize = false 
			} else {
				res.WriteString(bra2EngAlp[symbol])
			}
		}
	}
	return res.String()
}

func main() {
	len := len(os.Args)
	if len < 2 {
		fmt.Println("Please provide a string to translate")
		return 
	}
	input := strings.Join(os.Args[1:len], " ")

	if strings.Contains(input, ".") {
		fmt.Println(transBra2Eng(input))
	} else {
		fmt.Println(transEng2Bra(input))
	}
}
