package braille

import (
	"errors"
	"strings"
	"unicode"
)

var (
	ErrBadCapital = errors.New("bad capital")
	ErrBadNumber  = errors.New("bad number")
	ErrBadSymbol  = errors.New("bad symbol")
)

func Translate(input string) (string, error) {
	if isBraille(input) {
		return translateBraille(input)
	}
	return translateEnglish(input)
}

func translateBraille(input string) (string, error) {
	var output strings.Builder

	for i := 0; i < len(input); {
		var nextSymbol symbol
		for _, s := range alphabet {
			if s.braille == input[i:i+6] {
				nextSymbol = s
				break
			}
		}

		switch nextSymbol.kind {
		case symbolKindLetter, symbolKindDigit:
			var letter symbol
			for _, s := range letterSymbols {
				if s.braille == input[i:i+6] {
					letter = s
					break
				}
			}
			output.WriteRune(letter.english)
			i += 6

		case symbolKindSpace:
			output.WriteRune(spaceSymbol.english)
			i += 6

		case symbolKindCapitalFollows:
			i += 6
			if i >= len(input) {
				return output.String(), ErrBadCapital
			}
			var letter symbol
			for _, s := range letterSymbols {
				if s.braille == input[i:i+6] {
					letter = s
					break
				}
			}
			if letter.kind == symbolKindUnknown {
				return output.String(), ErrBadCapital
			}
			output.WriteRune(unicode.ToUpper(letter.english))
			i += 6

		case symbolKindNumberFollows:
			i += 6
			if i >= len(input) {
				return output.String(), ErrBadNumber
			}
			var numDigits int
			for i < len(input) {
				var nextDigit symbol
				for _, s := range digitSymbols {
					if s.braille == input[i:i+6] {
						nextDigit = s
						break
					}
				}
				if nextDigit.kind != symbolKindDigit {
					break
				}
				output.WriteRune(nextDigit.english)
				i += 6
				numDigits++
			}
			if numDigits == 0 {
				return output.String(), ErrBadNumber
			}

		case symbolKindUnknown:
			return output.String(), ErrBadSymbol
		}
	}

	return output.String(), nil
}

func translateEnglish(input string) (string, error) {
	var output strings.Builder

	for i := 0; i < len(input); {
		var nextSymbol symbol
		for _, s := range alphabet {
			if s.english == unicode.ToLower(rune(input[i])) {
				nextSymbol = s
				break
			}
		}

		switch nextSymbol.kind {
		case symbolKindLetter:
			if unicode.IsUpper(rune(input[i])) {
				output.WriteString(capitalFollowsSymbol.braille)
			}
			output.WriteString(nextSymbol.braille)
			i++

		case symbolKindSpace:
			output.WriteString(spaceSymbol.braille)
			i++

		case symbolKindDigit:
			output.WriteString(numberFollowsSymbol.braille)
			for i < len(input) {
				var nextDigit symbol
				for _, s := range alphabet {
					if s.english == rune(input[i]) {
						nextDigit = s
						break
					}
				}
				if nextDigit.kind != symbolKindDigit {
					break
				}
				output.WriteString(nextDigit.braille)
				i++
			}

		case symbolKindUnknown:
			return output.String(), ErrBadSymbol
		}
	}

	return output.String(), nil
}

func isBraille(input string) bool {
	if len(input)%6 != 0 {
		return false
	}

	for i := 0; i < len(input); i += 6 {
		var nextSymbol symbol
		for _, s := range alphabet {
			if s.braille == input[i:i+6] {
				nextSymbol = s
				break
			}
		}
		if nextSymbol.kind == symbolKindUnknown {
			return false
		}
	}

	return true
}
