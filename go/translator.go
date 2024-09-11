package main

import (
	"fmt"
	"os"
	"solution/languages"
	"solution/translations"
	"strings"
)

func Translate(sourceSentence string) (string, error) {
	sourceSentenceLanguage, err := languages.DetectLanguage(sourceSentence)
	if err != nil {
		return "", fmt.Errorf("error detecting language: %v\n", err)
	}

	var translationStrategy translations.TranslationStrategy = nil
	switch sourceSentenceLanguage {
	case languages.Braille:
		brailleToEnglishTranslator, err := translations.NewBrailleToEnglishTranslator()
		if err != nil {
			return "", fmt.Errorf("error initializing Braille to English translator: %v\n", err)
		}
		translationStrategy = brailleToEnglishTranslator
	case languages.English:
		englishToBrailleTranslator, err := translations.NewEnglishToBrailleTranslator()
		if err != nil {
			return "", fmt.Errorf("error initializing English to Braille translator: %v\n", err)
		}
		translationStrategy = englishToBrailleTranslator
	default:
		return "", fmt.Errorf("unsupported translation from language %s\n", sourceSentenceLanguage)
	}

	translator := translations.NewTranslator(translationStrategy)

	translatedSentence, err := translator.Translate(sourceSentence)
	if err != nil {
		return "", fmt.Errorf("error during translation: %v\n", err)
	}

	return translatedSentence, nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Usage: %s <sentence>\n", os.Args[0])
		os.Exit(1)
	}
	sourceSentence := strings.Join(os.Args[1:], " ")

	translatedSentence, err := Translate(sourceSentence)
	if err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}

	println(translatedSentence)
}
