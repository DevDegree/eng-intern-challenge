package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	capitalPrefix = ".....O"
	numberPrefix  = ".O.OOO"
	brailleCell   = 6
)

var brailleAlphabet = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
	"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
	"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
	" ": "......",
}

var brailleToAlpha map[string]string

func init() {
	brailleToAlpha = make(map[string]string, len(brailleAlphabet))
	for k, v := range brailleAlphabet {
		brailleToAlpha[v] = k
	}
}

func toBraille(input string) (string, error) {
	var result strings.Builder
	numberMode := false

	for _, char := range input {
		switch {
		case unicode.IsDigit(char):
			if !numberMode {
				result.WriteString(numberPrefix)
				numberMode = true
			}
			result.WriteString(brailleAlphabet[string(char)])
		case unicode.IsUpper(char):
			if numberMode {
				numberMode = false
			}
			result.WriteString(capitalPrefix)
			result.WriteString(brailleAlphabet[strings.ToLower(string(char))])
		case unicode.IsSpace(char):
			result.WriteString(brailleAlphabet[" "])
			numberMode = false
		case unicode.IsLower(char):
			if numberMode {
				numberMode = false
			}
			if braille, ok := brailleAlphabet[string(char)]; ok {
				result.WriteString(braille)
			} else {
				return "", fmt.Errorf("unsupported character: %c", char)
			}
		default:
			return "", fmt.Errorf("unsupported character: %c", char)
		}
	}
	return result.String(), nil
}

func toEnglish(input string) (string, error) {
	var result strings.Builder
	numberMode := false
	capitalMode := false

	if len(input)%brailleCell != 0 {
		return "", fmt.Errorf("invalid Braille input: length must be a multiple of %d", brailleCell)
	}

	for i := 0; i < len(input); i += brailleCell {
		brailleChar := input[i : i+brailleCell]
		switch brailleChar {
		case capitalPrefix:
			capitalMode = true
		case numberPrefix:
			numberMode = true
		default:
			if letter, exists := brailleToAlpha[brailleChar]; exists {
				if numberMode {
					result.WriteString(letter)
				} else if capitalMode {
					result.WriteString(strings.ToUpper(letter))
					capitalMode = false
				} else {
					result.WriteString(letter)
				}
			} else {
				return "", fmt.Errorf("invalid Braille character: %s", brailleChar)
			}
			numberMode = false
		}
	}
	return result.String(), nil
}

func isBraille(input string) bool {
	return len(input) > 0 && strings.Contains(input, "O.")
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide input to translate.")
		return
	}

	input := strings.Join(os.Args[1:], " ")

	var output string
	var err error

	if isBraille(input) {
		output, err = toEnglish(input)
	} else {
		output, err = toBraille(input)
	}

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	fmt.Println(output)
}