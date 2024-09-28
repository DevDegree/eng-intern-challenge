package main

import (
	"errors"
	"fmt"
	"os"
	"strings"
	"unicode"
)

const capitalBraille = ".....O"
const numberBraille = ".O.OOO"

// In the spec we assume that we do not have symbols
// "Entire english alphabet, capitalize, spaces and numbers 0-9"
var brailleToEnglish = map[string]string{
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
	"OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
	"OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
	".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
	"OO.OOO": "y", "O..OOO": "z", "......": " ",
}

var brailleToNumeric = map[string]string{
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
	"OOOO..": "7", "O.OO..": "9", ".OO...": "9", ".OOO..": "0",
}

var englishToBraille = make(map[string]string)
var numericToBraille = make(map[string]string)

func init() {
	for k, v := range brailleToEnglish {
		englishToBraille[v] = k
	}

	for k, v := range brailleToNumeric {
		numericToBraille[v] = k
	}
}

// Interface over braille translation maps. Returns the value from the map if good, error if not
func getBrailleValue(char rune) (string, error) {
	switch {
	case unicode.IsDigit(char):
		if braille, ok := numericToBraille[string(char)]; ok {
			return braille, nil
		}

		return "", fmt.Errorf("Digit not found in Braille map: %c", char) //This should literally never happen

	case unicode.IsLetter(char) || char == ' ':
		lower := unicode.ToLower(char)

		if braille, ok := englishToBraille[string(lower)]; ok {
			return braille, nil
		}

		return "", fmt.Errorf("Letter not found in Braille map: %c", char)

	default:
		return "", fmt.Errorf("Unsupported character type: %c", char)
	}
}

func getEngValue(braille string, isNumeric bool) (string, error) {
	if isNumeric {
		if value, ok := brailleToNumeric[braille]; ok {
			return value, nil
		}

		return "", fmt.Errorf("Braille not found in digit map: %s", braille)
	} else {
		if value, ok := brailleToEnglish[braille]; ok {
			return value, nil
		}

		return "", fmt.Errorf("Braille not found in english map: %s", braille)
	}
}

// Slice an input string we think is braille into 6 char windows, error if not possible
func sliceIntoBraille(input string) ([]string, error) {
	if len(input)%6 != 0 {
		return nil, errors.New("Cannot slice input string into windows of 6")
	}

	var chunks []string

	for i := 0; i < len(input); i += 6 {
		chunks = append(chunks, input[i:i+6])
	}

	return chunks, nil
}

func translateEnglishToBraille(input string) (string, error) {
	var result strings.Builder

	numberFlag := false

	for _, char := range input {
		if unicode.IsUpper(char) {
			result.WriteString(capitalBraille)
		}

		if unicode.IsDigit(char) {
			//Numeric flags are on a "per space" basis, we check if numeric has already been set
			if !numberFlag {
				numberFlag = true
				result.WriteString(numberBraille)
			}
		}

		if char == ' ' { //If we hit a space character, we can reset our numeric flag to false
			numberFlag = false
		}

		braille, err := getBrailleValue(char)

		if err != nil {
			return "", errors.New("Braille translation failed")
		}

		result.WriteString(braille)
	}

	return result.String(), nil
}

func translateBrailleToEnglish(input string) (string, error) {
	chunks, err := sliceIntoBraille(input)

	if err != nil {
		return "", err
	}

	var result strings.Builder
	capitalFlag := false
	numberFlag := false

	for _, chunk := range chunks {
		switch chunk {
		case capitalBraille:
			capitalFlag = true
			continue
		case numberBraille:
			numberFlag = true
			continue
		}

		value, err := getEngValue(chunk, numberFlag)

		if err != nil {
			return "", err
		}

		if capitalFlag {
			value = strings.ToUpper(value)
			capitalFlag = false
		}

		if value == " " {
			numberFlag = false
		}

		result.WriteString(value)
	}
	return result.String(), nil
}

func main() {
	cliArgs := os.Args

	if len(cliArgs) < 2 {
		fmt.Println("Error: Provide an input string for translation")
		os.Exit(1)
	}

	inputString := strings.Join(cliArgs[1:], " ")

	//In our case we do not have . as valid english values, so we use that to check which translation to perform
	//However if it was, the code is setup so that we can still choose which translation to do:
	//Start as Braille, if we hit an error we simply try again as English
	//(English is always valid braille, but the other way around isn't true)

	//Regex isn't a good idea (Check str for only O, .), we can have a bunch of those as nonsensical english (O.O as ex)

	//Can't really test more without modifying the test files (maybe screws with github workflow??)
	var translation string
	var err error

	if strings.ContainsAny(inputString, ".") { //If we find "." in our string, treat it as braille (will always work with curr assumptions)
		translation, err = translateBrailleToEnglish(inputString)

		if err != nil {
			// If Braille translation failed, attempt English translatioun (If our assumption wasn't true...)
			translation, err = translateEnglishToBraille(inputString)
		}
	} else {
		translation, err = translateEnglishToBraille(inputString)
	}
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println(translation)
	}
}
