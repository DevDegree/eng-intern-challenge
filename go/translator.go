package main

import (
	"fmt"
	"os"
	"strings"
)

type InputType int32
const (
	BRAILLE InputType = 0
	ENGLISH InputType = 1
)


func main() {
	if len(os.Args) < 2 {
		// No argument provided
        return
    }

	// Build braille/english mappers the other way around
	for braille, english := range BrailleToEnglish {
		EnglishToBraille[english] = braille
	}
	for braille, number := range BrailleToNumber {
		NumberToBraille[number] = braille
	}

	args := os.Args[1:]
	joined_args := strings.Join(args, " ")
	var input_type InputType = classify_input(joined_args)

	if input_type == BRAILLE {
		fmt.Println(braille_to_english(joined_args))
	} else if input_type == ENGLISH {
		fmt.Println(english_to_braille(joined_args))
	}
}

// Determine if input is english or braille
func classify_input(input string) InputType{
	for _, char := range input {
		if _, ok := EnglishToBraille[string(char)]; ok {
			return ENGLISH
		} else if _, ok := NumberToBraille[string(char)]; ok {
			return ENGLISH
		}
	}
	return BRAILLE
}

// Translate braille input to english
func braille_to_english(braille string) string {
	var translated strings.Builder
	var capitalize bool
	var write_number bool
	n := len(braille)

	for i := 0; i < n; i += 6 {
		braille_char := braille[i : i+6]

		switch braille_char {
		case CapitalFollows:
			capitalize = true
		case NumberFollows:
			write_number = true
		case DecimalFollows:
			translated.WriteString(".")
		case Space:
			write_number = false
			translated.WriteString(" ")
		default:
			if write_number {
				translated.WriteString(BrailleToNumber[braille_char])
			} else {
				english_char := BrailleToEnglish[braille_char]
				if capitalize {
					english_char = strings.ToUpper(english_char)
					capitalize = false
				}
				translated.WriteString(english_char)
			}
		}
	}
	return translated.String()
}

// Translate english input to braille
func english_to_braille(english string) string {
	var translated strings.Builder
	var write_number bool

	n := len(english)

 	for i := 0; i < n; i++ {
		english_char := string(english[i])

		if english_char == " " {
			write_number = false
			translated.WriteString(Space)
		} else if braille, ok := NumberToBraille[english_char]; ok {
			if !write_number {
				write_number = true
				translated.WriteString(NumberFollows)
			}
			translated.WriteString(braille)
		} else {
			if english_char == strings.ToUpper(english_char) {
				translated.WriteString(CapitalFollows)
				english_char = strings.ToLower(english_char)
			}
			braille := EnglishToBraille[english_char]
			translated.WriteString(braille)
		}
	}
	return translated.String()
}


// Character mappers for translation
// Note: Couldn't separate this to a different file within package
// 	due to test running command "go run translator.go" and not "go run ."

const (
	CapitalFollows = ".....O"
	DecimalFollows = ".O...O"
	NumberFollows = ".O.OOO"
	Space = "......"
)

var BrailleToEnglish = map[string]string{
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

var BrailleToNumber = map[string]string {
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

var EnglishToBraille = map[string]string{}
var NumberToBraille = map[string]string{}