package main

import (
	"fmt"
	"os"
	"strings"
)

var letterToBraille = map[string]string{
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
}

var numberToBraille = map[string]string{
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

var symbolToBraille = map[string]string{
	".": "..OO.O",
	",": "..O...",
	"?": "..O.OO",
	"!": "..OOO.",
	":": "..OO..",
	";": "..O.O.",
	"-": "..O..O",
	"/": "..O..O",
	"<": ".OO..O",
	">": "O..OO.",
	"(": "O.O..O",
	")": ".O.OO.",
}

var identifierToBraille = map[string]string{
	"space":   "......",
	"capital": ".....O",
	"decimal": ".O...O",
	"number":  ".O.OOO",
}

var brailleToLetter = map[string]string{
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
}

var brailleToNumber = map[string]string{
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
}

var brailleToSymbol = map[string]string{
	"..OO.O": ".",
	"..O...": ",",
	"..O.OO": "?",
	"..OOO.": "!",
	"..OO..": ":",
	"..O.O.": ";",
	"..O..O": "-",
	".OO..O": "<",
	"O..OO.": ">",
	"O.O..O": "(",
	".O.OO.": ")",
}

var brailleToIdentifier = map[string]string{
	"......": "space",
	".....O": "capital",
	".O...O": "decimal",
	".O.OOO": "number",
}

func isBraille(input string) bool {
	for _, char := range input {
		if char != 'O' && char != '.' {
			return false
		}
	}

	if len(input)%6 != 0 {
		return false
	}

	for i := 0; i < len(input); i += 6 {
		end := i + 6
		if end > len(input) {
			return false
		}
		chunk := input[i:end]
		if _, exists := brailleToLetter[chunk]; exists {
			continue
		} else if _, exists := brailleToNumber[chunk]; exists {
			continue
		} else if _, exists := brailleToSymbol[chunk]; exists {
			continue
		} else if _, exists := brailleToIdentifier[chunk]; exists {
			continue
		} else {
			return false
		}
	}
	return true
}

func englishToBraille(input string) string {
	var output strings.Builder
	numberMode := false
	for i := 0; i < len(input); i++ {
		ch := input[i]
		if ch == ' ' {
			output.WriteString(identifierToBraille["space"])
			numberMode = false
		} else if ch >= '0' && ch <= '9' {
			if !numberMode {
				output.WriteString(identifierToBraille["number"])
				numberMode = true
			}
			brailleCode, exists := numberToBraille[string(ch)]
			if exists {
				output.WriteString(brailleCode)
			}
		} else if ch == '.' {
			if numberMode {
				output.WriteString(identifierToBraille["decimal"])
			} else {
				brailleCode, exists := symbolToBraille[string(ch)]
				if exists {
					output.WriteString(brailleCode)
				}
				numberMode = false
			}
		} else if ch >= 'A' && ch <= 'Z' {
			output.WriteString(identifierToBraille["capital"])
			brailleCode, exists := letterToBraille[strings.ToLower(string(ch))]
			if exists {
				output.WriteString(brailleCode)
			}
			numberMode = false
		} else if ch >= 'a' && ch <= 'z' {
			brailleCode, exists := letterToBraille[string(ch)]
			if exists {
				output.WriteString(brailleCode)
			}
			numberMode = false
		} else {
			brailleCode, exists := symbolToBraille[string(ch)]
			if exists {
				output.WriteString(brailleCode)
			}
			numberMode = false
		}
	}
	return output.String()
}

func brailleToEnglish(input string) string {
	var output strings.Builder
	numberMode := false
	capitalizeNext := false
	for i := 0; i < len(input); i += 6 {
		end := i + 6
		if end > len(input) {
			continue
		}
		chunk := input[i:end]
		if identifier, exists := brailleToIdentifier[chunk]; exists {
			if identifier == "space" {
				output.WriteByte(' ')
				numberMode = false
				capitalizeNext = false
			} else if identifier == "capital" {
				capitalizeNext = true
			} else if identifier == "number" {
				numberMode = true
			} else if identifier == "decimal" {
				output.WriteString(".")
			}
		} else {
			if numberMode {
				if ch, exists := brailleToNumber[chunk]; exists {
					output.WriteString(ch)
				} else {
					numberMode = false
					i -= 6
				}
			} else {
				if ch, exists := brailleToLetter[chunk]; exists {
					if capitalizeNext {
						output.WriteString(strings.ToUpper(ch))
						capitalizeNext = false
					} else {
						output.WriteString(ch)
					}
				} else if ch, exists := brailleToSymbol[chunk]; exists {
					output.WriteString(ch)
				}
			}
		}
	}
	return output.String()
}

func main() {
	args := os.Args[1:]
	if len(args) == 0 {
		fmt.Println("No input provided")
		return
	}
	input := strings.Join(args, " ")

	if isBraille(input) {
		output := brailleToEnglish(input)
		fmt.Print(output)
	} else {
		output := englishToBraille(input)
		fmt.Print(output)
	}
}
