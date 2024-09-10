package translations

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"os"
	"solution/languages"
	"strings"
)

type BrailleToEnglishTranslator struct {
	currentOperator *Operator

	brailleToOperatorMapping         map[string]string
	brailleToAlphabetMapping         map[string]string
	brailleToSpecialCharacterMapping map[string]string
	brailleToNumberMapping           map[string]string
}

func NewBrailleToEnglishTranslator() (*BrailleToEnglishTranslator, error) {
	brailleTranslationFile, err := os.Open("resources/fromBrailleTranslations.json")
	if err != nil {
		return nil, fmt.Errorf("error opening Braille translation JSON file: %w", err)
	}
	defer brailleTranslationFile.Close()

	brailleTranslationBytes, err := io.ReadAll(brailleTranslationFile)
	if err != nil {
		return nil, fmt.Errorf("error reading Braille translation JSON file: %w", err)
	}

	var brailleTranslationMap map[string]map[string]map[string]string
	err = json.Unmarshal(brailleTranslationBytes, &brailleTranslationMap)
	if err != nil {
		return nil, fmt.Errorf("error parsing Braille translation JSON file: %w", err)
	}

	destinationLanguage := string(languages.English)

	if brailleTranslationMap[destinationLanguage] == nil {
		return nil, fmt.Errorf("braille translation for language %s does not exist", destinationLanguage)
	}

	return &BrailleToEnglishTranslator{
		brailleToOperatorMapping:         brailleTranslationMap[destinationLanguage]["operator"],
		brailleToAlphabetMapping:         brailleTranslationMap[destinationLanguage]["alphabet"],
		brailleToSpecialCharacterMapping: brailleTranslationMap[destinationLanguage]["specialCharacter"],
		brailleToNumberMapping:           brailleTranslationMap[destinationLanguage]["number"],
	}, nil
}

func (bet *BrailleToEnglishTranslator) translateCharacter(word string) (string, error) {
	if len(word) != 6 {
		return "", errors.New("braille character must have exactly 6 characters")
	}

	if bet.currentOperator == nil {
		if operatorStr, isOperator := bet.brailleToOperatorMapping[word]; isOperator {
			parsedOperator, err := StringToOperator(operatorStr)
			if err != nil {
				return "", fmt.Errorf("error parsing Braille operator: %w", err)
			}
			bet.currentOperator = &parsedOperator
			return "", nil
		}

		if specialCharacter, isSpecialCharacter := bet.brailleToSpecialCharacterMapping[word]; isSpecialCharacter {
			return specialCharacter, nil
		}

		if lowercaseAlphabet, isAlphabet := bet.brailleToAlphabetMapping[word]; isAlphabet {
			bet.currentOperator = nil
			return lowercaseAlphabet, nil
		}

		return "", fmt.Errorf("invalid Braille character: %s", word)
	} else {
		switch *bet.currentOperator {
		case CapitalFollows:
			if lowercaseAlphabet, isAlphabet := bet.brailleToAlphabetMapping[word]; isAlphabet {
				bet.currentOperator = nil
				return strings.ToUpper(lowercaseAlphabet), nil
			}
			return "", fmt.Errorf("invalid alphabet for capital follows: %s", word)
		case DecimalFollows:
			if lowercaseDecimal, isAlphabet := bet.brailleToNumberMapping[word]; isAlphabet {
				bet.currentOperator = nil
				return lowercaseDecimal, nil
			}
			return "", fmt.Errorf("invalid decimal character: %s", word)
		case NumberFollows:
			if number, isNumber := bet.brailleToNumberMapping[word]; isNumber {
				return number, nil
			}
			if specialCharacter, isSpecialCharacter := bet.brailleToSpecialCharacterMapping[word]; isSpecialCharacter {
				if specialCharacter == " " {
					bet.currentOperator = nil
					return specialCharacter, nil
				}
				return "", fmt.Errorf("invalid special character in number context: %s", word)
			}
			return "", fmt.Errorf("invalid number character: %s", word)
		}
	}

	return "", fmt.Errorf("unexpected error while translating character: %s", word)
}

func (bet *BrailleToEnglishTranslator) Translate(text string) (string, error) {
	if len(text)%6 != 0 {
		return "", errors.New("invalid string length: Braille characters must be in multiples of 6")
	}

	var translatedString strings.Builder
	for i := 0; i < len(text); i += 6 {
		translatedCharacter, err := bet.translateCharacter(text[i : i+6])
		if err != nil {
			return "", fmt.Errorf("error translating Braille character: %w", err)
		}
		translatedString.WriteString(translatedCharacter)
	}

	return translatedString.String(), nil
}
