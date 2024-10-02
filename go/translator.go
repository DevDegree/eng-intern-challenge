package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	args := os.Args[1:]
	engine := Engine{args}

	result := engine.Process()

	fmt.Println(result)
}

const BRAILLE_WORD_LENGTH = 6

type Engine struct {
	input []string
}

type Language int

const (
	ENGLISH Language = iota
	BRAILLE
)

type ParseState int

const (
	ALPHABETS ParseState = iota
	NUMBERS
)

func (e *Engine) Process() string {
	language := e.checkType()

	var result string

	if language == ENGLISH {
		result = e.toBraille()
	} else if language == BRAILLE {
		result = e.toEnglish()
	}

	return result
}

func (e *Engine) checkType() Language {
	var inputType Language
	if strings.Contains(e.input[0], ".") && strings.ContainsAny(e.input[0], "Oo") {
		inputType = BRAILLE
	}

	return inputType
}

func (e *Engine) toEnglish() string {
	origin := e.input[0]

	var state ParseState
	capital := false
	result := ""

	index := 0
	for index < len(origin) {
		str := origin[index : index+6]

		switch state {
		case ALPHABETS:
			switch str {
			case dictionary["CAPITAL_FOLLOWS"]:
				capital = true

			case dictionary["NUMBER_FOLLOWS"]:
				state = NUMBERS

			default:
				char := dictionaryAlphabet[str]
				if !capital {
					char = strings.ToLower(char)
				}
				capital = false
				result += char
			}

		case NUMBERS:
			switch str {
			case dictionary["SPACE"]:
				state = ALPHABETS
				result += " "

			default:
				result += dictionaryNumbers[str]
			}
		}

		index += BRAILLE_WORD_LENGTH
	}

	return result
}

func (e *Engine) toBraille() string {
	result := ""

	var state ParseState

	for i, word := range e.input {
		for _, r := range word {
			char := string(r)

			if char == " " {
				// space
				result += dictionary["SPACE"]
				state = ALPHABETS
			} else if unicode.IsDigit(r) {
				// number
				if state == ALPHABETS {
					result += dictionary["NUMBER_FOLLOWS"]
					state = NUMBERS
				}
				result += dictionary[char]
			} else if unicode.IsLetter(r) {
				if unicode.IsUpper(r) {
					// alphabet upper case
					result += dictionary["CAPITAL_FOLLOWS"]
				}
				result += dictionary[strings.ToUpper(char)]
			}
		}

		if i < len(e.input)-1 {
			result += dictionary["SPACE"]
		}
	}

	return result
}

var dictionary = map[string]string{
	// Alphabets
	"A": "O.....",
	"B": "O.O...",
	"C": "OO....",
	"D": "OO.O..",
	"E": "O..O..",
	"F": "OOO...",
	"G": "OOOO..",
	"H": "O.OO..",
	"I": ".OO...",
	"J": ".OOO..",
	"K": "O...O.",
	"L": "O.O.O.",
	"M": "OO..O.",
	"N": "OO.OO.",
	"O": "O..OO.",
	"P": "OOO.O.",
	"Q": "OOOOO.",
	"R": "O.OOO.",
	"S": ".OO.O.",
	"T": ".OOOO.",
	"U": "O...OO",
	"V": "O.O.OO",
	"W": ".OOO.O",
	"X": "OO..OO",
	"Y": "OO.OOO",
	"Z": "O..OOO",

	// Numbers
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

	// Indicator
	"CAPITAL_FOLLOWS": ".....O",
	"NUMBER_FOLLOWS":  ".O.OOO",
	"SPACE":           "......",
}

var dictionaryAlphabet = map[string]string{
	"O.....": "A",
	"O.O...": "B",
	"OO....": "C",
	"OO.O..": "D",
	"O..O..": "E",
	"OOO...": "F",
	"OOOO..": "G",
	"O.OO..": "H",
	".OO...": "I",
	".OOO..": "J",
	"O...O.": "K",
	"O.O.O.": "L",
	"OO..O.": "M",
	"OO.OO.": "N",
	"O..OO.": "O",
	"OOO.O.": "P",
	"OOOOO.": "Q",
	"O.OOO.": "R",
	".OO.O.": "S",
	".OOOO.": "T",
	"O...OO": "U",
	"O.O.OO": "V",
	".OOO.O": "W",
	"OO..OO": "X",
	"OO.OOO": "Y",
	"O..OOO": "Z",

	// Space
	"......": " ",
}

var dictionaryNumbers = map[string]string{
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
