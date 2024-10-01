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
		return translateFromLatinToBraille(word)
	}
	if helpers.IsBraille(word) {
		// word is packed and not already split by spaces
		// hence, split on braille space character,
		// translate each word and return result
		brailleWords := strings.Split(word, mappers.BRAILLE_SPACE)
		var translation []string
		for _, braille_word := range brailleWords {
			res, err := translateFromBrailleToLatin(braille_word)
			if err != nil {
				return "", err
			}
			translation = append(translation, res)
		}
		return strings.Join(translation, " "), nil
	}
	// unreachable (given the underlying logic)
	return "", errors.New("unable to classify text")
}

func translateFromLatinToBraille(word string) (string, error) {
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

func translateFromBrailleToLatin(word string) (string, error) {
	var translation []rune

	chunkSize := 6
	var capitalizeNextCharMode = false
	var numericMode = false

	for chunkPointer := 0; chunkPointer < len(word); chunkPointer += chunkSize {
		chunk := word[chunkPointer : chunkPointer+chunkSize]
		if chunk == mappers.BRAILLE_CAPITAL_FOLLOWS {
			capitalizeNextCharMode = true
			continue
		}
		if chunk == mappers.BRAILLE_NUMBER_FOLLOWS {
			numericMode = true
			continue
		}

		if capitalizeNextCharMode {
			nextChar, ok := mappers.BRAILLE_TO_LETTERS[chunk]
			if !ok {
				return "", errors.New("capital did NOT follow")
			}
			capitalizedChar := unicode.ToUpper(nextChar)
			translation = append(translation, capitalizedChar)
			capitalizeNextCharMode = false
		} else if numericMode {
			number, ok := mappers.BRAILLE_TO_NUMBERS[chunk]
			if !ok {
				return "", errors.New("braille of number ill-formatted")
			}
			translation = append(translation, number)

		} else {
			letter, isLetter := mappers.BRAILLE_TO_LETTERS[chunk]
			punctuation, isPunctuation := mappers.BRAILLE_TO_PUNCTUATION[chunk]

			if isLetter {
				translation = append(translation, letter)
			} else if isPunctuation {
				translation = append(translation, punctuation)
			} else {
				return "", errors.New("invalid braille provided")
			}
		}

	}
	return string(translation), nil
}
