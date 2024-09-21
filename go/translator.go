package main

import (
	"fmt"
	"strings"
	"unicode"
)

// Struct to represent translation state
type Translator struct {
	AlphaE2B    map[rune]string
	NumberE2B   map[rune]string
	PunctE2B    map[rune]string
	AlphaB2E    map[string]rune
	NumberB2E   map[string]rune
	PunctB2E    map[string]rune
	Symbols     map[rune]string
	taskMap     map[string]func(rune) string // Task map for different scenarios
	numberMode  bool
	capitalMode bool
}

// Enable bi-directional hashmap for English <--> Braille
func CreateReverseMapping(mapping map[rune]string) map[string]rune {
	reverseMapping := make(map[string]rune)
	for k, v := range mapping {
		reverseMapping[v] = k
	}
	return reverseMapping
}

// Initialize a new Translator with mappings
func NewTranslator() *Translator {
	AlphaE2B := map[rune]string{
		'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
		'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
		'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
		'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
		'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO",
		' ': "......",
	}

	NumberE2B := map[rune]string{
		'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
		'6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
	}

	PunctE2B := map[rune]string{
		'.': "..OO.O", '?': "..O.OO", '!': "..OOO.", ':': "..OO..", ';': "..O.O.",
		'-': "....OO", '/': ".O..O.", '(': "O.O..O", ')': ".O.OO.", ' ': "......",
	}

	Symbols := map[rune]string{
		'C': ".....O", // Capital Follows
		'N': ".O.OOO", // Number Follows
		'S': "......", // Space or end symbol
	}

	t := &Translator{
		AlphaE2B:    AlphaE2B,
		NumberE2B:   NumberE2B,
		PunctE2B:    PunctE2B,
		Symbols:     Symbols,
		AlphaB2E:    CreateReverseMapping(AlphaE2B),
		NumberB2E:   CreateReverseMapping(NumberE2B),
		PunctB2E:    CreateReverseMapping(PunctE2B),
		numberMode:  false,
		capitalMode: false,
	}

	// Initialize the task map with functions per scenarios
	t.taskMap = map[string]func(rune) string{
		"space":       t.handleSpace,
		"number":      t.handleNumber,
		"uppercase":   t.handleUppercase,
		"lowercase":   t.handleLowercase,
		"punctuation": t.handlePunctuation,
	}

	return t
}

// Series of scenarios
func (t *Translator) handleSpace(r rune) string {
	t.numberMode = false
	t.capitalMode = false
	return t.AlphaE2B[' ']
}

func (t *Translator) handleNumber(r rune) string {
	if !t.numberMode {
		t.numberMode = true
		return t.Symbols['N'] + t.NumberE2B[r]
	}
	return t.NumberE2B[r]
}

func (t *Translator) handleUppercase(r rune) string {
	return t.Symbols['C'] + t.AlphaE2B[unicode.ToLower(r)]
}

func (t *Translator) handleLowercase(r rune) string {
	t.numberMode = false
	return t.AlphaE2B[r]
}

func (t *Translator) handlePunctuation(r rune) string {
	if braille, ok := t.PunctE2B[r]; ok {
		return braille
	}
	fmt.Printf("[!] Unsupported punctuation skipped: %c\n", r)
	return ""
}

// English --> Braille
func (t *Translator) TranslateToBraille(input string) string {
	var output strings.Builder

	for _, r := range input {
		var taskKey string

		switch {
		case unicode.IsSpace(r):
			taskKey = "space"
		case unicode.IsDigit(r):
			taskKey = "number"
		case unicode.IsUpper(r):
			taskKey = "uppercase"
		case unicode.IsLower(r):
			taskKey = "lowercase"
		case unicode.IsPunct(r) || strings.ContainsRune(".?!:-;/()", r):
			taskKey = "punctuation"
		default:
			fmt.Printf("[!] Unsupported character skipped: %c\n", r)
			continue
		}

		// Use task map to centralize translation logics
		output.WriteString(t.taskMap[taskKey](r))
	}
	return output.String()
}
