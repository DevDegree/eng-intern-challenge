package main

import (
	"fmt"
	"os"
	"regexp"
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

// Braille --> English
func (t *Translator) TranslateToAlpha(input string) string {
	var output strings.Builder
	var capitalizeNext, numberMode bool

	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6]

		switch {
		case brailleChar == t.Symbols['C']:
			capitalizeNext = true
			continue

		case brailleChar == t.Symbols['C']:
			capitalizeNext = true
			continue

		case brailleChar == t.Symbols['N']:
			numberMode = true
			continue

		}
		if numberMode {
			if num, ok := t.NumberB2E[brailleChar]; ok {
				output.WriteString(string(num))
				continue
			}
		}

		if alpha, ok := t.AlphaB2E[brailleChar]; ok {
			if capitalizeNext {
				output.WriteString(strings.ToUpper(string(alpha)))
				capitalizeNext = false
			} else {
				output.WriteString(string(alpha))
			}
		} else if punct, ok := t.PunctB2E[brailleChar]; ok {
			output.WriteString(string(punct))
		} else {
			fmt.Printf("[!] Unsupported Braille pattern skipped: %s\n", brailleChar)
		}

		// Reset number mode after a space (Symbol S)
		if brailleChar == t.Symbols['S'] {
			numberMode = false
		}
	}

	return output.String()
}

// Language Detection
func isBraille(input string) bool {
	//(O, ., and spaces)
	re := regexp.MustCompile(`^[O. ]+$`)
	return re.MatchString(input)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("[!] No input no translation.")
		return
	}

	input := strings.Join(os.Args[1:], " ")
	translator := NewTranslator()

	if isBraille(input) {
		if len(input)%6 != 0 {
			fmt.Println("[!] Invalid Braille input: Length must be a multiple of 6.")
			return
		} else {
			fmt.Println(translator.TranslateToAlpha(input))

		}
	} else {
		fmt.Println(translator.TranslateToBraille(input))
	}
}
