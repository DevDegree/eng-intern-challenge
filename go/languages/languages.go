package languages

import (
	"fmt"
	"regexp"
)

type Language string

const (
	English Language = "english"
	Braille Language = "braille"
)

func DetectLanguage(text string) (Language, error) {
	englishRegex := regexp.MustCompile("^[a-zA-Z0-9 ]+$")
	brailleRegex := regexp.MustCompile("^[.O]+$")

	switch {
	case len(text)%6 == 0 && brailleRegex.MatchString(text):
		return Braille, nil
	case englishRegex.MatchString(text):
		return English, nil
	default:
		return "", fmt.Errorf("unsupported language")
	}
}
