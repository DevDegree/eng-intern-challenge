package translations

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
	"regexp"
	"strings"
	"unicode"
)

type EnglishTranslator struct {
	multiDigitTraillingRegex *regexp.Regexp

	englishToOperatorMapping         map[string]string
	englishToAlphabetMapping         map[string]string
	englishToSpecialCharacterMapping map[string]string
	englishToNumberMapping           map[string]string
}

func NewEnglishTranslator(language string) (*EnglishTranslator, error) {
	englishTranslationFile, err := os.Open("resources/english.json")
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

	if englishTranslationMap[language] == nil {
		return nil, fmt.Errorf("braille translation to language %s does not exist", err)
	}

	multiDigitTraillingRegex, _ := regexp.Compile("^[a-zA-Z]+$")

	return &EnglishTranslator{
		multiDigitTraillingRegex:         multiDigitTraillingRegex,
		englishToOperatorMapping:         englishTranslationMap[language]["operator"],
		englishToAlphabetMapping:         englishTranslationMap[language]["alphabet"],
		englishToSpecialCharacterMapping: englishTranslationMap[language]["specialCharacter"],
		englishToNumberMapping:           englishTranslationMap[language]["number"],
	}, nil
}

func (bt *EnglishTranslator) translateWord(word string) (string, error) {
	hasMultiDigitTraillingRegex := bt.multiDigitTraillingRegex.MatchString(word)
	hasParsedFirstMultiDigit := false

	translatedWord := ""

	for _, c := range word {
		if unicode.IsLetter(c) {
			if unicode.IsUpper(c) {
				capitalFollows, ok := bt.englishToOperatorMapping[string(CapitalFollows)]
				if !ok {
					return "", fmt.Errorf("translation file missing operator %s", CapitalFollows)
				}
				translatedWord += capitalFollows
				c = unicode.ToLower(c)
			}
			if lowercaseLetter, isLowerCaseLetter := bt.englishToAlphabetMapping[string(c)]; isLowerCaseLetter {
				translatedWord += lowercaseLetter
				continue
			}
			return "", fmt.Errorf("unsupported letter %c", c)
		} else if unicode.IsNumber(c) {
			if hasMultiDigitTraillingRegex {
				if !hasParsedFirstMultiDigit {
					numberFollows, ok := bt.englishToOperatorMapping[string(NumberFollows)]
					if !ok {
						return "", fmt.Errorf("translation file missing operator %s", NumberFollows)
					}
					translatedWord += numberFollows
					hasParsedFirstMultiDigit = true
				}
			} else {
				decimalFollows, ok := bt.englishToOperatorMapping[string(DecimalFollows)]
				if !ok {
					return "", fmt.Errorf("translation file missing operator %s", DecimalFollows)
				}
				translatedWord += decimalFollows
			}
			if digit, isDigit := bt.englishToNumberMapping[string(c)]; isDigit {
				translatedWord += digit
				continue
			}
			return "", fmt.Errorf("unsupported number %c", c)
		} else {
			return "", fmt.Errorf("unsupported character %c", c)
		}
	}

	return translatedWord, nil
}

func (bt *EnglishTranslator) Translate(s string) (string, error) {
	spaceSplitTranslationText := strings.Split(s, " ")
	translatedText := ""

	space, ok := bt.englishToSpecialCharacterMapping[" "]
	if !ok {
		return "", fmt.Errorf("translation file missing space special character")
	}
	for i, word := range spaceSplitTranslationText {
		translatedWord, err := bt.translateWord(word)
		if err != nil {
			return "", err
		}

		if i > 0 {
			translatedText += space
		}

		translatedText += translatedWord
	}
	return translatedText, nil
}
