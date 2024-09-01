package helpers

import "slices"

var (
	punctuations = []rune{'.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' '}
)

func isAlphabet(ch rune) bool {
	return ch >= 'a' && ch <= 'z'
}
func isNumeric(ch rune) bool {
	return ch >= '0' && ch <= '9'
}
func IsLatin(word string) bool {
	for _, c := range word {
		if !isAlphabet(c) && !isNumeric(c) && !slices.Contains(punctuations, c) {
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
