package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
	"unicode"
)

var ErrMissingArguments = errors.New("missing required cli arguments")

type Translator struct {
	text               string
	letterToBrailleMap map[string]string
	numberToBrailleMap map[string]string
	brailleToLetterMap map[string]string
	brailleToNumberMap map[string]string
}

// creates a new translator unit
func NewTranslator(text string) *Translator {
	var t Translator
	t.text = text
	t.letterToBrailleMap = map[string]string{
		"CAPITAL_FOLLOWS": ".....O",
		"NUMBER_FOLLOWS":  ".O.OOO",
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
	}
	t.numberToBrailleMap = map[string]string{
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
	}
	t.brailleToLetterMap = reverseMap(t.letterToBrailleMap)
	t.brailleToNumberMap = reverseMap(t.numberToBrailleMap)
	return &t
}

// checks if the provided arguments are Braille
func (t *Translator) isBraille() bool {
	// Braille characters consist of 6 'O' and '.' characters
	if len(t.text)%6 != 0 {
		return false
	}
	// Check that text consists of valid Braille tokens
	for i := 0; i < len(t.text); i += 6 {
		token := t.text[i : i+6]
		if _, ok := t.brailleToLetterMap[token]; !ok {
			return false
		}
	}

	return true
}

// checks if the provided arguments are Alphanumeric
func (t *Translator) isAlphanumeric() bool {
	for _, c := range t.text {
		if !unicode.IsLetter(c) && !unicode.IsNumber(c) {
			return false
		}
	}
	return true
}

// processes arguments, joins them together, and removes leading/trailing whitespace
func handleArguments() (string, error) {
	if len(os.Args) < 2 {
		return "", ErrMissingArguments
	}
	args := os.Args[1:]
	return strings.TrimSpace(strings.Join(args, " ")), nil
}

func reverseMap(m map[string]string) map[string]string {
	newMap := make(map[string]string, len(m))
	for k, v := range m {
		newMap[v] = k
	}
	return newMap
}

func main() {
	text, err := handleArguments()

	if err != nil {
		log.Fatalf("invalid args: %s\n", err)
	}

	fmt.Println(text)
}
