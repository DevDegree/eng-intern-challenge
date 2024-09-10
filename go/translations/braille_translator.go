package translations

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"os"
	"strings"
)

func NewBrailleTranslator(language string) (*BrailleTranslator, error) {
	brailleTranslationFile, err := os.Open("resources/braille.json")
	if err != nil {
		return nil, fmt.Errorf("error opening braille translation json file: %s", err)
	}
	defer brailleTranslationFile.Close()

	brailleTranslationBytes, err := io.ReadAll(brailleTranslationFile)
	if err != nil {
		return nil, fmt.Errorf("error reading braille translation json file: %s", err)
	}

	var brailleTranslationMap map[string]map[string]map[string]string
	err = json.Unmarshal(brailleTranslationBytes, &brailleTranslationMap)
	if err != nil {
		return nil, fmt.Errorf("error parsing braille translation json file: %s", err)
	}

	if brailleTranslationMap[language] == nil {
		return nil, fmt.Errorf("braille translation to language %s does not exist", err)
	}

	return &BrailleTranslator{
		brailleToOperatorMapping:         brailleTranslationMap[language]["operator"],
		brailleToAlphabetMapping:         brailleTranslationMap[language]["alphabet"],
		brailleToSpecialCharacterMapping: brailleTranslationMap[language]["specialCharacter"],
		brailleToNumberMapping:           brailleTranslationMap[language]["number"],
	}, nil
}

type BrailleTranslator struct {
	currentOperator *Operator

	brailleToOperatorMapping         map[string]string
	brailleToAlphabetMapping         map[string]string
	brailleToSpecialCharacterMapping map[string]string
	brailleToNumberMapping           map[string]string
}

func (bt *BrailleTranslator) translateCharacter(word string) (string, error) {
	if len(word) != 6 {
		return "", errors.New("braille character must have 6 characters")
	}

	if bt.currentOperator == nil {
		if operatorStr, isOperator := bt.brailleToOperatorMapping[word]; isOperator {
			parsedOperator, err := StringToOperator(operatorStr)
			if err != nil {
				panic(fmt.Errorf("error parsing braille operator: %s", err))
			}

			bt.currentOperator = &parsedOperator
			return "", nil
		}

		if specialCharacter, isSpecialCharacter := bt.brailleToSpecialCharacterMapping[word]; isSpecialCharacter {
			return specialCharacter, nil
		}

		if lowercaseAlphabet, isAlphabet := bt.brailleToAlphabetMapping[word]; isAlphabet {
			bt.currentOperator = nil
			return lowercaseAlphabet, nil
		}

		panic(fmt.Errorf("invalid character"))
	} else {
		switch *bt.currentOperator {
		case CapitalFollows:
			if lowercaseAlphabet, isAlphabet := bt.brailleToAlphabetMapping[word]; isAlphabet {
				bt.currentOperator = nil
				return strings.ToUpper(lowercaseAlphabet), nil
			}
			panic(fmt.Errorf("alphabet not valid"))
		case DecimalFollows:
			if lowercaseDecimal, isAlphabet := bt.brailleToAlphabetMapping[word]; isAlphabet {
				return lowercaseDecimal, nil
			}
			panic(fmt.Errorf("decimal doesnt exist"))
		case NumberFollows:
			if number, isNumber := bt.brailleToNumberMapping[word]; isNumber {
				return number, nil
			}
			if specialCharacter, isSpecialCharacter := bt.brailleToSpecialCharacterMapping[word]; isSpecialCharacter {
				if specialCharacter == " " {
					bt.currentOperator = nil
					return specialCharacter, nil
				}
				panic("invalid string")
			}
			panic(fmt.Errorf("number not valid"))
		}
	}

	panic("invalid string")
}

func (bt *BrailleTranslator) Translate(text string) (string, error) {
	if len(text)%6 != 0 {
		panic("invalid string length")
	}

	translatedString := ""
	for i := 0; i < len(text); i += 6 {
		translatedCharacter, err := bt.translateCharacter(text[i : i+6])
		if err != nil {
			panic(err)
		}
		translatedString += translatedCharacter
	}
	return translatedString, nil
}
