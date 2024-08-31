package main

import (
	"fmt"
	"os"
	"strings"
)

var brailleMap = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
	"z": "O..OOO",
	"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
	"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
	".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
	";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
	"(": "O.O..O", ")": ".O.OO.", " ": "......",
}

var reverseMapAlpha = map[string]string{
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
	"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
	"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
	"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
	"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
	"O..OOO": "z",
}

var reverseMapSymbols = map[string]string{
	"..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
	"..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
	"O.O..O": "(", ".O.OO.": ")",
}

var reverseMapNumbers = map[string]string{
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
	"OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
	"..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
	"..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
	"O.O..O": "(", ".O.OO.": ")", "O..OO.": ">",
}

const (
	capitalBrailleSymbol = ".....O"
	decimalBrailleSymbol = ".O...O"
	numberBrailleSymbol  = ".O.OOO"
)

func translateToBraille(input string) string {
	var result strings.Builder
	isNumber := false
	for _, char := range input {
		c := string(char)
		switch {
		case c >= "A" && c <= "Z":
			result.WriteString(capitalBrailleSymbol)
			result.WriteString(brailleMap[strings.ToLower(c)])
		case c >= "0" && c <= "9":
			if !isNumber {
				result.WriteString(numberBrailleSymbol)
				isNumber = true
			}
			result.WriteString(brailleMap[c])
		case c == ".":
			result.WriteString(decimalBrailleSymbol)
		case c == " ":
			result.WriteString(brailleMap[c])
			isNumber = false
		default:
			if val, ok := brailleMap[c]; ok {
				result.WriteString(val)
			}

		}
	}
	return result.String()
}

func translateToEnglish(input string) string {
	var result strings.Builder
	isCapital := false
	isNumber := false

	for i := 0; i < len(input); i += 6 {
		symbol := input[i : i+6]

		switch symbol {
		case capitalBrailleSymbol:
			isCapital = true
		case numberBrailleSymbol:
			isNumber = true
		case decimalBrailleSymbol:
			result.WriteString(".")
		default:
			if isNumber {
				if val, ok := reverseMapNumbers[symbol]; ok {
					result.WriteString(val)
				} else if val, ok := reverseMapSymbols[symbol]; ok {
					result.WriteString(val)
				}

			} else {
				if val, ok := reverseMapAlpha[symbol]; ok {
					if isCapital {
						result.WriteString(strings.ToUpper(val))
						isCapital = false
					} else {
						result.WriteString(val)
					}
				} else if val, ok := reverseMapSymbols[symbol]; ok {
					result.WriteString(val)
				}
			}
			if symbol == "......" {
				result.WriteString(" ")
				isNumber = false
			}
		}
	}

	return result.String()
}

func isEnglish(input string) bool {
	return strings.ContainsAny(input, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?:;-/<>()")
}

func isBraille(input string) bool {
	return strings.ContainsAny(input, "O.") && len(input)%6 == 0 && input != "OOOOOO"
}

func main() {
	if len(os.Args) > 1 {
		input := strings.Join(os.Args[1:], " ")

		if isBraille(input) {
			fmt.Println(translateToEnglish(input))
		} else if isEnglish(input) {
			fmt.Println(translateToBraille(input))
		} else {
			fmt.Println("Invalid input")
		}
	} else {
		fmt.Println("Usage: go run translator.go [input_string]")
	}
}
