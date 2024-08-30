package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"unicode"
)

var ErrMissingArguments = errors.New("missing required cli arguments")
var ErrArgumentsNotBraille = errors.New("the supplied arguments are not Braille")
var ErrArgumentsNotAlphanumeric = errors.New("the supplied arguments are not Alphanumeric")
var ErrArgumentsNotBrailleOrAlphanumeric = errors.New("the supplied arguments are not Alphanumeric or Braille")

type Translator struct {
	args               []string
	letterToBrailleMap map[string]string
	numberToBrailleMap map[string]string
	brailleToLetterMap map[string]string
	brailleToNumberMap map[string]string
}

// creates a new translator unit
func NewTranslator(args []string) *Translator {
	var t Translator
	t.args = args
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
	for _, text := range t.args {
		// Braille characters consist of 6 'O' and '.' characters
		if len(text)%6 != 0 {
			return false
		}
		// Check that text consists of valid Braille tokens
		for i := 0; i < len(text); i += 6 {
			token := text[i : i+6]
			if _, ok := t.brailleToLetterMap[token]; !ok {
				return false
			}
		}
	}

	return true
}

// checks if the provided arguments are Alphanumeric
func (t *Translator) isAlphanumeric() bool {
	for _, text := range t.args {
		for _, c := range text {
			if !unicode.IsSpace(c) && !unicode.IsLetter(c) && !unicode.IsNumber(c) {
				return false
			}
		}
	}
	return true
}

func (t *Translator) toBraille() (string, error) {
	if !t.isBraille() {
		return "", fmt.Errorf("expected Braille input: %s", ErrArgumentsNotBraille)
	}
	// convert to braille
	return "braille", nil
}

func (t *Translator) toEnglish() (string, error) {
	if !t.isAlphanumeric() {
		return "", fmt.Errorf("expected Alphanumeric input: %s", ErrArgumentsNotAlphanumeric)
	}
	// convert to english
	return "english", nil
}

func (t *Translator) Translate() (string, error) {
	if t.isBraille() {
		return t.toBraille()
	} else if t.isAlphanumeric() {
		return t.toEnglish()
	}
	return "", fmt.Errorf("expected Alphanumeric or Braille input: %s", ErrArgumentsNotBrailleOrAlphanumeric)
}

// checks that more than atleast one argument (excluding program) is provided
func handleArguments() ([]string, error) {
	if len(os.Args) < 2 {
		return nil, ErrMissingArguments
	}
	return os.Args[1:], nil
}

func reverseMap(m map[string]string) map[string]string {
	newMap := make(map[string]string, len(m))
	for k, v := range m {
		newMap[v] = k
	}
	return newMap
}

func main() {
	args, err := handleArguments()

	if err != nil {
		log.Fatalf("invalid args: %s\n", err)
	}

	translator := NewTranslator(args)

	convertedText, err := translator.Translate()
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println(convertedText)
}
