package helpers

import (
	"slices"

	"unicode"
)

var (
	punctuations = []rune{'.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' '}
)

func IsAlphabet(ch rune) bool {
	return ch >= 'a' && ch <= 'z'
}
func IsNumeric(ch rune) bool {
	return ch >= '0' && ch <= '9'
}
func IsPunctuation(ch rune) bool {
	return slices.Contains(punctuations, ch)
}
func IsLatin(word string) bool {
	for _, character := range word {
		lowered := unicode.ToLower(character)
		if !IsAlphabet(lowered) && !IsNumeric(character) && !IsPunctuation(character) {
			return false
		}
	}
	return !IsBraille(word)
}

func IsBraille(word string) bool {
	if len(word)%6 != 0 {
		return false
	}
	for _, c := range word {
		if c != '.' && c != 'O' {
			return false
		}
	}
	return true
}
