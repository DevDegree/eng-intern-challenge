package lib

import (
	"errors"
	"solution/helpers"
)

func Translate(word string) (string, error) {
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

	return "", errors.New("error translating")

}

func translate_from_braille_to_latin(word string) (string, error) {
	return "", errors.New("error translating")
}
