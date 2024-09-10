package translations

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
	"regexp"
	"solution/languages"
	"strings"
	"unicode"
)

type EnglishToBrailleTranslator struct {
	multiDigitTraillingRegex *regexp.Regexp

	capitalFollowsTranslation string
	decimalFollowsTranslation string
	numberFollowsTranslation  string

	englishToOperatorMapping         map[string]string
	englishToAlphabetMapping         map[string]string
	englishToSpecialCharacterMapping map[string]string
	englishToNumberMapping           map[string]string
}

func NewEnglishToBrailleTranslator() (*EnglishToBrailleTranslator, error) {
	englishTranslationFile, err := os.Open("resources/EnglishSourceTranslations.json")
	if err != nil {
		return nil, fmt.Errorf("error opening braille translation json file: %s", err)
	}
	defer englishTranslationFile.Close()

	englishTranslationBytes, err := io.ReadAll(englishTranslationFile)
	if err != nil {
		return nil, fmt.Errorf("error reading braille translation json file: %s", err)
	}

	var englishTranslationMap map[string]map[string]map[string]string
	err = json.Unmarshal(englishTranslationBytes, &englishTranslationMap)
	if err != nil {
		return nil, fmt.Errorf("error parsing braille translation json file: %s", err)
	}

	destinationLanguage := string(languages.Braille)

	if englishTranslationMap[destinationLanguage] == nil {
		return nil, fmt.Errorf("english translation to language %s does not exist", destinationLanguage)
	}

	translator := &EnglishToBrailleTranslator{
		englishToOperatorMapping:         englishTranslationMap[destinationLanguage]["operator"],
		englishToAlphabetMapping:         englishTranslationMap[destinationLanguage]["letter"],
		englishToSpecialCharacterMapping: englishTranslationMap[destinationLanguage]["special_character"],
		englishToNumberMapping:           englishTranslationMap[destinationLanguage]["decimal"],
	}

	multiDigitTraillingRegex, err := regexp.Compile("\\d{2,}$")
	if err != nil {
		return nil, fmt.Errorf("error compiling multi trailling digit regex: %s", err)
	}
	translator.multiDigitTraillingRegex = multiDigitTraillingRegex

	capitalFollowsTranslation, hasCapitalFollowsTranslation := translator.englishToOperatorMapping[string(CapitalFollows)]
	if !hasCapitalFollowsTranslation {
		return nil, fmt.Errorf("translation file missing operator %s", CapitalFollows)
	}
	translator.capitalFollowsTranslation = capitalFollowsTranslation

	numberFollowsTranslation, hasNumberFollowsTranslation := translator.englishToOperatorMapping[string(NumberFollows)]
	if !hasNumberFollowsTranslation {
		return nil, fmt.Errorf("translation file missing operator %s", NumberFollows)
	}
	translator.numberFollowsTranslation = numberFollowsTranslation

	decimalFollowsTranslation, hasDecimalFollowsTranslation := translator.englishToOperatorMapping[string(DecimalFollows)]
	if !hasDecimalFollowsTranslation {
		return nil, fmt.Errorf("translation file missing operator %s", DecimalFollows)
	}
	translator.decimalFollowsTranslation = decimalFollowsTranslation

	return translator, nil
}

func (ebt *EnglishToBrailleTranslator) translateLetterOnlyWord(word string) (string, error) {
	var translatedWord strings.Builder

	for _, c := range word {
		if unicode.IsUpper(c) {
			translatedWord.WriteString(ebt.capitalFollowsTranslation)
			c = unicode.ToLower(c)
		}
		if lowercaseLetterTranslation, hasLowerCaseLetterTranslation := ebt.englishToAlphabetMapping[string(c)]; hasLowerCaseLetterTranslation {
			translatedWord.WriteString(lowercaseLetterTranslation)
		} else {
			return "", fmt.Errorf("unsupported letter %c", c)
		}
	}

	return translatedWord.String(), nil
}

func (ebt *EnglishToBrailleTranslator) translateTraillingNumber(number string) (string, error) {
	var translatedNumber strings.Builder

	translatedNumber.WriteString(ebt.numberFollowsTranslation)

	for _, c := range number {
		if unicode.IsNumber(c) {
			if digitTranslation, hasDigitTranslation := ebt.englishToNumberMapping[string(c)]; hasDigitTranslation {
				translatedNumber.WriteString(digitTranslation)
			} else {
				return "", fmt.Errorf("unsupported digit %c", c)
			}
		} else {
			return "", fmt.Errorf("unexpected error translating number")
		}
	}

	return translatedNumber.String(), nil
}

func (ebt *EnglishToBrailleTranslator) translateWord(word string) (string, error) {
	var translatedWord strings.Builder

	sourceWithoutTraillingNumber := word
	sourceTraillingNumber := ""

	if hasMultiDigitTrailling := ebt.multiDigitTraillingRegex.MatchString(word); hasMultiDigitTrailling {
		startIndexOfTraillingNumber := ebt.multiDigitTraillingRegex.FindStringIndex(word)[0]

		sourceWithoutTraillingNumber = word[:startIndexOfTraillingNumber]
		sourceTraillingNumber = word[startIndexOfTraillingNumber:]
	}

	for _, c := range sourceWithoutTraillingNumber {
		if unicode.IsLetter(c) {

			if unicode.IsUpper(c) {
				translatedWord.WriteString(ebt.capitalFollowsTranslation)
				c = unicode.ToLower(c)
			}
			if lowercaseLetterTranslation, hasLowerCaseLetterTranslation := ebt.englishToAlphabetMapping[string(c)]; hasLowerCaseLetterTranslation {
				translatedWord.WriteString(lowercaseLetterTranslation)
			} else {
				return "", fmt.Errorf("unsupported letter %c", c)
			}
		} else if unicode.IsNumber(c) {
			translatedWord.WriteString(ebt.decimalFollowsTranslation)
			if digitTranslation, hasDigitTranslation := ebt.englishToNumberMapping[string(c)]; hasDigitTranslation {
				translatedWord.WriteString(digitTranslation)
			} else {
				return "", fmt.Errorf("unsupported number %c", c)
			}
		} else {
			return "", fmt.Errorf("unsupported character %c", c)
		}
	}

	if sourceTraillingNumber != "" {
		translatedTraillingNumber, err := ebt.translateTraillingNumber(sourceTraillingNumber)
		if err != nil {
			return "", fmt.Errorf("error translating trailing number %s", sourceTraillingNumber)
		}
		translatedWord.WriteString(translatedTraillingNumber)
	}

	return translatedWord.String(), nil
}

func (ebt *EnglishToBrailleTranslator) Translate(s string) (string, error) {
	spaceSplitTranslationText := strings.Split(s, " ")
	var translatedText strings.Builder

	translatedSpace, hasTranslatedSpace := ebt.englishToSpecialCharacterMapping[" "]
	if !hasTranslatedSpace {
		return "", fmt.Errorf("translation file missing space translation")
	}

	for i, word := range spaceSplitTranslationText {
		translatedWord, err := ebt.translateWord(word)
		if err != nil {
			return "", err
		}

		if i > 0 {
			translatedText.WriteString(translatedSpace)
		}

		translatedText.WriteString(translatedWord)
	}

	return translatedText.String(), nil
}
