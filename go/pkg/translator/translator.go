package translator

import (
	"fmt"
	"solution/pkg/dictionary"
	"strings"
)

type Modifier string

const (
	Capital Modifier = "capital"
	Decimal Modifier = "decimal"
	Number  Modifier = "number"
)

type Translator struct {
	dictionary dictionary.Dictionary
	modifier   *Modifier
	handlers   map[string]func(string) (string, bool)
	isBraille  bool
	chunkSize  int
}

func NewTranslator(isBraille bool) *Translator {
	dict := dictionary.NewDictionary()

	dict.Alphabet = map[string]string{
		"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
		"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
		"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
		"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
		"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
		"z": "O..OOO",
	}

	dict.Numbers = map[string]string{
		"0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
		"5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
	}

	dict.Symbols = map[string]string{
		" ": "......",
	}

	dict.Modifiers = map[string]string{
		"capital": ".....O", "decimal": ".O...O", "number": ".O.OOO",
	}

	translator := Translator{dictionary: dict, isBraille: isBraille, chunkSize: 1}

	if isBraille {
		translator.brailleMode()
	}

	return &translator
}

func (t *Translator) Translate(input []string) (string, error) {
	output := []string{}

	// We must make sure that the order of the handlers is consistent,
	// so that we don't confuse numbers with letters.
	handlerOrder := []string{"Alphabet", "Symbols", "Numbers", "Modifiers"}

	for _, text := range input {
		var splitText string

		for i := 0; i < len(text); i += t.chunkSize {
			chunk := text[i : i+t.chunkSize]

			if t.modifier != nil {
				splitText = t.handleModifier(chunk, splitText)
				continue
			}

			handlers := t.getHandlers()

			found := false
			for _, handlerKey := range handlerOrder {
				handler := handlers[handlerKey]
				if val, ok := handler(chunk); ok {
					splitText += val
					found = true
					break
				}
			}

			if !found {
				return "", fmt.Errorf("character %s not found in dictionary", chunk)
			}
		}

		output = append(output, splitText)
	}

	var delimiter string
	if t.isBraille {
		delimiter = " "
	} else {
		delimiter = t.dictionary.Symbols[" "]
	}

	return strings.Join(output, delimiter), nil
}

func (t *Translator) handleModifier(chunk, splitText string) string {
	switch *t.modifier {
	case Capital:
		if t.isBraille {
			splitText += strings.ToUpper(t.dictionary.Alphabet[chunk])
		} else {
			splitText += t.dictionary.Modifiers[string(Capital)] + t.dictionary.Alphabet[chunk]
		}
	case Decimal:
		if val, ok := t.dictionary.Numbers[chunk]; ok {
			if t.isBraille {
				splitText += "." + val
			} else {
				splitText += t.dictionary.Modifiers[string(Decimal)] + val
			}
		}
	case Number:
		if val, ok := t.dictionary.Numbers[chunk]; ok {
			splitText += val
		} else if " " == chunk || " " == t.dictionary.Symbols[chunk] {
			splitText += t.dictionary.Symbols[chunk]
			t.modifier = nil
		} else {
			// If it's not a number or space, treat it as regular text
			if val, ok := t.dictionary.Alphabet[chunk]; ok {
				splitText += val
			}
			t.modifier = nil
		}
		return splitText
	}
	t.modifier = nil

	return splitText
}

func (t *Translator) getHandlers() map[string]func(string) (string, bool) {
	handlers := map[string]func(string) (string, bool){
		"Alphabet": func(chunk string) (string, bool) {
			val, ok := t.dictionary.Alphabet[chunk]

			if val, isUpper := t.dictionary.Alphabet[strings.ToLower(chunk)]; !ok && isUpper {
				return t.dictionary.Modifiers[string(Capital)] + val, true
			}

			return val, ok
		},
		"Symbols": func(chunk string) (string, bool) { val, ok := t.dictionary.Symbols[chunk]; return val, ok },
	}

	if t.isBraille {
		handlers["Numbers"] = func(chunk string) (string, bool) {
			val, ok := t.dictionary.Numbers[chunk]

			if ok {
				modifier := Number
				t.modifier = &modifier
			}

			return val, ok
		}

		handlers["Modifiers"] = func(chunk string) (string, bool) {
			val, ok := t.dictionary.Modifiers[chunk]
			if ok {
				modifier := Modifier(val)
				t.modifier = &modifier
			}
			return "", ok
		}
	} else {
		handlers["Numbers"] = func(chunk string) (string, bool) {
			if val, ok := t.dictionary.Numbers[chunk]; ok {
				modifier := Number
				t.modifier = &modifier

				return t.dictionary.Modifiers[string(Number)] + val, true
			}

			return "", false
		}
	}

	return handlers
}

func (t *Translator) brailleMode() {
	t.isBraille = true
	t.dictionary = t.dictionary.Reverse()
	t.chunkSize = 6
}
