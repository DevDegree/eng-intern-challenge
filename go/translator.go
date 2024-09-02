package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	BRAILLE_SYMB_LEN = 6
	CAPITAL_FOLLOWS  = ".....O"
	NUMBER_FOLLOWS   = ".O.OOO"
)

var ENGLISH_BRAILLE_MAPPING = map[rune]string{
	'a': "O.....",
	'b': "O.O...",
	'c': "OO....",
	'd': "OO.O..",
	'e': "O..O..",
	'f': "OOO...",
	'g': "OOOO..",
	'h': "O.OO..",
	'i': ".OO...",
	'j': ".OOO..",
	'k': "O...O.",
	'l': "O.O.O.",
	'm': "OO..O.",
	'n': "OO.OO.",
	'o': "O..OO.",
	'p': "OOO.O.",
	'q': "OOOOO.",
	'r': "O.OOO.",
	's': ".OO.O.",
	't': ".OOOO.",
	'u': "O...OO",
	'v': "O.O.OO",
	'w': ".OOO.O",
	'x': "OO..OO",
	'y': "OO.OOO",
	'z': "O..OOO",
	' ': "......",
}

var BRAILLE_ENGLISH_MAPPING = map[string]rune{
	"O.....": 'a',
	"O.O...": 'b',
	"OO....": 'c',
	"OO.O..": 'd',
	"O..O..": 'e',
	"OOO...": 'f',
	"OOOO..": 'g',
	"O.OO..": 'h',
	".OO...": 'i',
	".OOO..": 'j',
	"O...O.": 'k',
	"O.O.O.": 'l',
	"OO..O.": 'm',
	"OO.OO.": 'n',
	"O..OO.": 'o',
	"OOO.O.": 'p',
	"OOOOO.": 'q',
	"O.OOO.": 'r',
	".OO.O.": 's',
	".OOOO.": 't',
	"O...OO": 'u',
	"O.O.OO": 'v',
	".OOO.O": 'w',
	"OO..OO": 'x',
	"OO.OOO": 'y',
	"O..OOO": 'z',
	"......": ' ',
}

var NUMBER_BRAILLE_MAPPING = map[rune]string{
	'0': ".OOO..",
	'1': "O.....",
	'2': "O.O...",
	'3': "OO....",
	'4': "OO.O..",
	'5': "O..O..",
	'6': "OOO...",
	'7': "OOOO..",
	'8': "O.OO..",
	'9': ".OO...",
}

var BRAILLE_NUMBER_MAPPING = map[string]rune{
	".OOO..": '0',
	"O.....": '1',
	"O.O...": '2',
	"OO....": '3',
	"OO.O..": '4',
	"O..O..": '5',
	"OOO...": '6',
	"OOOO..": '7',
	"O.OO..": '8',
	".OO...": '9',
}

type CONVERSION_MODE uint8

const (
	BRAILLE_TO_ENGLISH = iota
	ENGLISH_TO_BRAILLE
)

type Convertor interface {
	Convert(str string) string
}

type Translator struct {
	mode      CONVERSION_MODE
	convertor Convertor
}

type EnglishToBrailleConvertor struct{}

type BrailleToEnglishConvertor struct{}

func NewTranslator(mode CONVERSION_MODE) *Translator {
	translator := Translator{mode: mode}

	if mode == BRAILLE_TO_ENGLISH {
		translator.convertor = &BrailleToEnglishConvertor{}
	}
	if mode == ENGLISH_TO_BRAILLE {
		translator.convertor = &EnglishToBrailleConvertor{}
	}

	return &translator
}

func (t *Translator) Translate(str string) string {
	return t.convertor.Convert(str)
}

func (c *EnglishToBrailleConvertor) Convert(str string) string {
	stringBuilder := strings.Builder{}
	numberFollows := false

	for _, ch := range str {
		if unicode.IsNumber(ch) {
			if !numberFollows {
				stringBuilder.WriteString(NUMBER_FOLLOWS)
				numberFollows = true
			}
			stringBuilder.WriteString(NUMBER_BRAILLE_MAPPING[ch])
		}

		if unicode.IsUpper(ch) {
			stringBuilder.WriteString(CAPITAL_FOLLOWS)
			ch = unicode.ToLower(ch)
		}
		stringBuilder.WriteString(ENGLISH_BRAILLE_MAPPING[ch])

	}
	return stringBuilder.String()
}

func (c *BrailleToEnglishConvertor) Convert(str string) string {
	stringBuilder := strings.Builder{}
	numberFollows := false
	capitalFollows := false

	for i := 0; i < len(str); i += BRAILLE_SYMB_LEN {
		currentSymbol := str[i : i+BRAILLE_SYMB_LEN]

		if currentSymbol == NUMBER_FOLLOWS {
			numberFollows = true
			continue
		}

		if currentSymbol == CAPITAL_FOLLOWS {
			capitalFollows = true
			continue
		}

		if numberFollows {
			if numberChar, ok := BRAILLE_NUMBER_MAPPING[currentSymbol]; ok {
				stringBuilder.WriteRune(numberChar)
			} else {
				numberFollows = false
			}
			continue
		}

		englishChar := BRAILLE_ENGLISH_MAPPING[currentSymbol]
		if capitalFollows {
			englishChar = unicode.ToUpper(englishChar)
			capitalFollows = false
		}
		stringBuilder.WriteRune(englishChar)
	}
	return stringBuilder.String()
}

func determineConversionMode(str string) CONVERSION_MODE {
	// Braille letters contain at least one period and it's length must be a multiple of 6
	if strings.Contains(str, ".") && len(str)%6 == 0 {
		return BRAILLE_TO_ENGLISH
	}
	return ENGLISH_TO_BRAILLE
}

func main() {
	strToTranslate := strings.Join(os.Args[1:], " ")
	conversionMode := determineConversionMode(strToTranslate)
	translator := NewTranslator(conversionMode)
	fmt.Println(translator.Translate(strToTranslate))
}
