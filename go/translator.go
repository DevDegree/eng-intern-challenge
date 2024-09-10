package main

import (
	"fmt"
	"os"
	"regexp"
	"solution/translations"
)

var (
	englishAlphabetRegex = regexp.MustCompile("^[a-zA-Z0-9 ]+$")
	brailleAlphabetRegex = regexp.MustCompile("^[.O]+$")
)

type Language string

const (
	English Language = "ENGLISH"
	Braille Language = "BRAILLE"
)

func GetLanguage(text string) (Language, error) {
	if len(text)%6 == 0 && brailleAlphabetRegex.MatchString(text) {
		return Braille, nil
	}
	if englishAlphabetRegex.MatchString(text) {
		return English, nil
	}
	return "", fmt.Errorf("unsupported language")
}

type TranslationStrategy interface {
	Translate(text string) (string, error)
}

type Translator struct {
	strategy TranslationStrategy
}

func (t *Translator) setStrategy(strategy TranslationStrategy) {
	t.strategy = strategy
}

func (t *Translator) Translate(text string) (string, error) {
	return t.strategy.Translate(text)
}

func main() {
	args := os.Args
	if len(args) != 2 {
		println(args[1])
		panic("Usage: ")
	}

	translationSentence := args[1]

	sourceSentenceLanguage, err := GetLanguage(translationSentence)
	if err != nil {
		panic(err)
	}

	var translationStrategy TranslationStrategy = nil
	switch sourceSentenceLanguage {
	case Braille:
		brailleToEnglishTranslator, err := translations.NewBrailleTranslator("english")
		if err != nil {
			panic(err)
		}
		translationStrategy = brailleToEnglishTranslator
	case English:
		englishToBrailleTranslator, err := translations.NewEnglishTranslator("braille")
		if err != nil {
			panic(err)
		}
		translationStrategy = englishToBrailleTranslator
	}

	translator := &Translator{}
	translator.setStrategy(translationStrategy)
	translatedSentence, err := translator.Translate(translationSentence)
	if err != nil {
		panic(err)
	}

	println(translatedSentence)
}
