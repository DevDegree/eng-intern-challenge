package lib

import (
	"errors"
	"solution/helpers"
	"solution/mappers"
	"strings"
	"unicode"
	"unicode/utf8"
)

func Translate(word string) (string, error) {
	if word == "" {
		return "", nil
	}
	if helpers.IsLatin(word) {
		return translate_from_latin_to_braille(word)
	}
	if helpers.IsBraille(word) {
		return translate_from_braille_to_latin(word)
	}
	// unreachable (given the underlying logic)
	return "", errors.New("unable to classify text")
}

func translate_from_latin_to_braille(word string) (string, error) {
	var translation []string
	numericMode := false
	for position, character := range word {
		if helpers.IsAlphabet(character) {
			if unicode.IsUpper(character) {
				translation = append(translation, mappers.BRAILLE_CAPITAL_FOLLOWS)
			}
			lowered := unicode.ToLower(character)
			translation = append(translation, mappers.LETTERS_TO_BRAILLE[lowered])

		} else if helpers.IsNumeric(character) {
			if !numericMode {
				numericMode = true
				translation = append(translation, mappers.BRAILLE_NUMBER_FOLLOWS)
			}
			translation = append(translation, mappers.NUMBERS_TO_BRAILLE[character])

		} else if helpers.IsPunctuation(character) {
			// sanity checks
			if numericMode {
				if character != '.' {
					return "", errors.New("invalid string according to technical requirements")
				}
				if position == len(word)-1 {
					return "", errors.New("invalid number format")
				}

				peak, _ := utf8.DecodeRuneInString(word[position+1:])
				if !helpers.IsNumeric(peak) {
					return "", errors.New("invalid number format")
				}

			}
			translation = append(translation, mappers.PUNCTUATION_TO_BRAILLE[character])
		} else {
			return "", errors.New("unknown character")
		}

	}

	return strings.Join(translation, ""), nil

}

func translate_from_braille_to_latin(word string) (string, error) {
	var translation []rune
	chunk_pointer := 0
	chunk_size := 6
	var capitalize_next_char_mode = false
	var numeric_mode = false

	for chunk_pointer < len(word) {
		chunk := word[chunk_pointer : chunk_pointer+chunk_size]
		if chunk == mappers.BRAILLE_CAPITAL_FOLLOWS {
			capitalize_next_char_mode = true
			chunk_pointer += chunk_size
			continue
		}
		if chunk == mappers.BRAILLE_NUMBER_FOLLOWS {
			numeric_mode = true
			chunk_pointer += chunk_size
			continue
		}

		if capitalize_next_char_mode {
			next_char, ok := mappers.BRAILLE_TO_LETTERS[chunk]
			if !ok {
				return "", errors.New("capital did NOT follow")
			}
			capitalized_char := unicode.ToUpper(next_char)
			translation = append(translation, capitalized_char)
			capitalize_next_char_mode = false
		} else if numeric_mode {
			number, ok := mappers.BRAILLE_TO_NUMBERS[chunk]
			if !ok {
				return "", errors.New("braille of number ill-formatted")
			}
			translation = append(translation, number)

		} else {
			letter, is_letter := mappers.BRAILLE_TO_LETTERS[chunk]
			punctuation, is_punctuation := mappers.BRAILLE_TO_PUNCTUATION[chunk]

			if is_letter {
				translation = append(translation, letter)
			} else if is_punctuation {
				translation = append(translation, punctuation)
			} else {
				return "", errors.New("invalid braille provided")
			}
		}
		chunk_pointer += chunk_size
	}
	return string(translation), nil
}
