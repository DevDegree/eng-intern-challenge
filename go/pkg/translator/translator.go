package translator

import (
	"fmt"
	"solution/pkg/dictionary"
	"strings"
)

type modifier string

const (
	Capital modifier = "capital"
	Number  modifier = "number"
)

// Translator handles the translation of text to braille and vice versa
type Translator struct {
	dictionary dictionary.Dictionary
	modifier   *modifier
	handlers   map[string]func(string) (string, bool)
	isBraille  bool
	chunkSize  int
}

// NewTranslator creates a new translator with the given isBraille flag
func NewTranslator(isBraille bool) *Translator {
	t := Translator{
		dictionary: dictionary.Init(),
		isBraille:  isBraille,
		chunkSize:  1,
	}

	if isBraille {
		t.brailleMode()
	}

	// Define the default handlers for the dictionary
	t.handlers = map[string]func(string) (string, bool){
		"Alphabet": func(chunk string) (string, bool) {
			val, ok := t.dictionary.Alphabet[chunk]

			if val, isUpper := t.dictionary.Alphabet[strings.ToLower(chunk)]; !ok && isUpper {
				return t.dictionary.Modifiers[string(Capital)] + val, true
			}

			return val, ok
		},
		"Symbols": func(chunk string) (string, bool) { val, ok := t.dictionary.Symbols[chunk]; return val, ok },
		"Numbers": func(chunk string) (string, bool) {
			val, ok := t.dictionary.Numbers[chunk]

			if ok {
				modifier := Number
				t.modifier = &modifier

				if !t.isBraille {
					return t.dictionary.Modifiers[string(Number)] + val, true
				}
			}

			return val, ok
		},
		"Modifiers": func(chunk string) (string, bool) {
			val, ok := t.dictionary.Modifiers[chunk]
			if ok {
				modifier := modifier(val)
				t.modifier = &modifier
			}
			return "", ok
		},
	}

	return &t
}

// Translate converts the input text to braille or regular text depending on the Translator's configuration
func (t *Translator) Translate(input []string) (string, error) {
	output := []string{}

	for _, text := range input {
		splitText, err := t.processText(text)
		if err != nil {
			return "", err
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

// We must make sure that the order of the handlers is consistent,
// so that we don't confuse numbers with letters.
var handlerOrder = []string{"Alphabet", "Symbols", "Numbers", "Modifiers"}

func (t *Translator) processText(text string) (string, error) {
	splitText := ""

	for i := 0; i < len(text); i += t.chunkSize {
		chunk := text[i : i+t.chunkSize]

		if t.modifier != nil {
			splitText = t.handleModifier(chunk, splitText)
			continue
		}

		found := false
		for _, handlerKey := range handlerOrder {
			handler := t.handlers[handlerKey]
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

	return splitText, nil
}

func (t *Translator) handleModifier(chunk, splitText string) string {
	switch *t.modifier {
	case Capital:
		if t.isBraille {
			splitText += strings.ToUpper(t.dictionary.Alphabet[chunk])
		} else {
			splitText += t.dictionary.Modifiers[string(Capital)] + t.dictionary.Alphabet[chunk]
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

func (t *Translator) brailleMode() {
	t.isBraille = true
	t.dictionary = t.dictionary.Reverse()
	t.chunkSize = 6
}
