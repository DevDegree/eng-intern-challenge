package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"unicode"
)

const (
	CapitalFollows string = ".....O"
	DecimalFollows string = ".O...O"
	NumberFollows  string = ".O.OOO"
)

func main() {
	var input string
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate")
		return
	}
	// Join with a space to preservce spaces in input.
	input = strings.TrimSpace(strings.Join(os.Args[1:], " "))
	isEnglish := IsEnglish(input)
	var result string
	var err error
	if isEnglish {
		result, err = EnglishToBraille(input)
	} else {
		result, err = BrailleToEnglish(input)
	}
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(result)
}

// IsEnglish is a function that returns true if the input is english, and false if the input is braille.
func IsEnglish(input string) bool {
	const (
		dotRune      = '.'
		capitalORune = 'O'
	)
	for _, r := range input {
		isBrailleRune := (r == dotRune || r == capitalORune)
		if !isBrailleRune {
			return true
		}
	}
	return false
}

// EnglishToBraille is a function that returns a converted Braille string from an English string
// As per Readme, only handles characters and numbers not including decimal and special symbols
func EnglishToBraille(input string) (string, error) {
	lookup := GetEnglishToBrailleLookup()
	var result strings.Builder
	for i := 0; i < len(input); i++ {
		char := rune(input[i])
		if unicode.IsDigit(char) {
			var number strings.Builder
			j := i
			for j < len(input) && unicode.IsDigit(rune(input[j])) {
				numberChar := rune(input[j])
				if braille, ok := lookup[numberChar]; ok {
					number.WriteString(braille)
				} else {
					log.Fatalf("unable to convert from %v", numberChar)
				}
				j += 1
			}
			result.WriteString(NumberFollows)
			result.WriteString(number.String())
			i = j - 1
		} else {
			if unicode.IsUpper(char) {
				result.WriteString(CapitalFollows)
			}
			if braille, ok := lookup[unicode.ToLower(char)]; ok {
				result.WriteString(braille)
			} else {
				log.Fatalf("unable to convert from %v", char)
			}
		}
	}
	return result.String(), nil
}

// BrailleToEnglish is a function that returns a converted English string from a Braille string
// As per Readme, only handles characters and numbers not including decimal and special symbols
func BrailleToEnglish(input string) (string, error) {
	characterLookup, digitLookup := GetBrailleToEnglishLookup()
	var result strings.Builder
	if len(input)%6 != 0 {
		log.Fatalf("invalid braille length detected")
	}
	for i := 0; i < len(input); i += 6 {
		isUppercase := false
		braille := input[i : i+6]
		if braille == NumberFollows {
			// consume till the end
			j := i + 6
			var numberString strings.Builder
			for j < len(input) && input[j:j+6] != "......" {
				digitBraille := input[j : j+6]
				if char, ok := digitLookup[digitBraille]; ok {

					numberString.WriteRune(char)
				} else {
					log.Fatalf("unable to convert from %v", digitBraille)
				}
				j += 6
			}
			i = j
			result.WriteString(numberString.String())
		} else {
			if braille == CapitalFollows {
				//consume the next 6 characters to get the real value
				i += 6
				braille = input[i : i+6]
				isUppercase = true
			}
			if char, ok := characterLookup[braille]; ok {
				if isUppercase {
					result.WriteRune(unicode.ToUpper(char))
				} else {
					result.WriteRune(char)
				}
			} else {
				log.Fatalf("unable to convert from %v", braille)
			}
		}
	}
	return result.String(), nil
}

// GetEnglishToBrailleLookup returns the character lookup table for converting English into Braille.
func GetEnglishToBrailleLookup() map[rune]string {
	return map[rune]string{
		// Lowercase letters and space
		'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
		'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
		'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
		'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
		'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
		'z': "O..OOO", ' ': "......",

		// Numbers
		'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
		'6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
	}
}

// GetBrailleToEnglishLookoup returns 2 character lookup tables for converting Braille into English.
// Needs 2 since some brail strings map to multiple characters.
func GetBrailleToEnglishLookup() (map[string]rune, map[string]rune) {
	BrailleToEnglishCharacters := map[string]rune{
		// Braille patterns to lowercase letters
		"O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
		"OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
		"O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
		"OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
		"O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
		"O..OOO": 'z', "......": ' ',
	}
	BrailleToEnglishDigits := map[string]rune{
		"O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5',
		"OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0',
	}
	return BrailleToEnglishCharacters, BrailleToEnglishDigits
}
