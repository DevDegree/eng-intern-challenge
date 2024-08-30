package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

type BrailleTranslator struct {
	letterReps map[string]string
	numberReps map[string]string
}

func NewBrailleTranslator() *BrailleTranslator {
	return &BrailleTranslator{
		letterReps: map[string]string{
			"a":               "O.....",
			"b":               "O.O...",
			"c":               "OO....",
			"d":               "OO.O..",
			"e":               "O..O..",
			"f":               "OOO...",
			"g":               "OOOO..",
			"h":               "O.OO..",
			"i":               ".OO...",
			"j":               ".OOO..",
			"k":               "O...O.",
			"l":               "O.O.O.",
			"m":               "OO..O.",
			"n":               "OO.OO.",
			"o":               "O..OO.",
			"p":               "OOO.O.",
			"q":               "OOOOO.",
			"r":               "O.OOO.",
			"s":               ".OO.O.",
			"t":               ".OOOO.",
			"u":               "O...OO",
			"v":               "O.O.OO",
			"w":               ".OOO.O",
			"x":               "OO..OO",
			"y":               "OO.OOO",
			"z":               "O..OOO",
			" ":               "......",
			"capital follows": ".....O",
			"number follows":  ".O.OOO",
		},
		numberReps: map[string]string{
			"0": ".OOO..",
			"1": "O.....",
			"2": "O.O...",
			"3": "OO....",
			"4": "OO.O..",
			"5": "O..O..",
			"6": "OOO...",
			"7": "OOOO..",
			"8": "O.OO..",
			"9": ".OO...",
			" ": "......",
		},
	}
}

func (bt *BrailleTranslator) brailleToEnglish(initialString string) string {
	charSize := 6
	if len(initialString)%charSize != 0 {
		return "ERROR: Braille text is invalid"
	}

	letterBrailleReps := make(map[string]string)
	for k, v := range bt.letterReps {
		letterBrailleReps[v] = k
	}

	numberBrailleReps := make(map[string]string)
	for k, v := range bt.numberReps {
		numberBrailleReps[v] = k
	}

	var res strings.Builder
	var capitalFollows, numberFollows bool

	for i := 0; i < len(initialString); i += charSize {
		brailleChar := initialString[i : i+charSize]
		var newChar string

		if !numberFollows {
			newChar = letterBrailleReps[brailleChar]
		} else {
			newChar = numberBrailleReps[brailleChar]
			if len(newChar) == 0 {
				numberFollows = false
				newChar = letterBrailleReps[brailleChar]
			}
		}

		switch newChar {
		case "capital follows":
			capitalFollows = true
			continue
		case "number follows":
			numberFollows = true
			continue
		case " ":
			numberFollows = false
			res.WriteString(" ")
		default:
			if capitalFollows {
				res.WriteString(strings.ToUpper(newChar))
				capitalFollows = false
			} else {
				res.WriteString(newChar)
			}
		}
	}

	return res.String()
}

func (bt *BrailleTranslator) englishToBraille(initialString string) string {
	var res strings.Builder
	isNumeric := false

	for _, char := range initialString {
		switch {
		case char >= 'a' && char <= 'z':
			if isNumeric {
				isNumeric = false
			}
			res.WriteString(bt.letterReps[string(char)])
		case char >= 'A' && char <= 'Z':
			if isNumeric {
				isNumeric = false
			}
			res.WriteString(bt.letterReps["capital follows"])
			res.WriteString(bt.letterReps[strings.ToLower(string(char))])
		case char >= '0' && char <= '9':
			if !isNumeric {
				isNumeric = true
				res.WriteString(bt.letterReps["number follows"])
			}
			res.WriteString(bt.numberReps[strings.ToLower(string(char))])
		case char == ' ':
			isNumeric = false
			res.WriteString(bt.letterReps[" "])
		default:
			isNumeric = false
			res.WriteString(bt.letterReps[string(char)])
		}
	}

	return res.String()
}

func isBraille(text string) bool {
	match, _ := regexp.MatchString("^[O.]*$", text)
	return match
}

func isAlphanumericalOrSpace(text string) bool {
	match, _ := regexp.MatchString("^[a-zA-Z0-9\\s]*$", text)
	return match
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run translator.go <text>")
		return
	}

	text := strings.Join(os.Args[1:], " ")
	translator := NewBrailleTranslator()

	if isBraille(text) {
		fmt.Println(translator.brailleToEnglish(text))
	} else if isAlphanumericalOrSpace(text) {
		fmt.Println(translator.englishToBraille(text))
	} else {
		fmt.Printf("ERROR: text is not Braille or English: %s\n", text)
	}
}
