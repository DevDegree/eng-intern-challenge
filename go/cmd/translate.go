package cmd

import (
	"fmt"
	"os"
	"regexp"
	"strings"

	"github.com/spf13/cobra"
)

type Dictionary struct {
	Alphabet  map[string]string
	Numbers   map[string]string
	Symbols   map[string]string
	Modifiers map[string]string
}

func (d *Dictionary) Reverse() Dictionary {
	return Dictionary{
		Alphabet:  reverseMap(d.Alphabet),
		Numbers:   reverseMap(d.Numbers),
		Symbols:   reverseMap(d.Symbols),
		Modifiers: reverseMap(d.Modifiers),
	}
}

var dictionary = Dictionary{
	Alphabet: map[string]string{
		"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
		"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
		"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
		"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
		"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
		"z": "O..OOO",
	},
	Numbers: map[string]string{
		"0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
		"5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
	},
	Symbols: map[string]string{
		" ": "......",
	},
	Modifiers: map[string]string{
		"capital": ".....O", "decimal": ".O...O", "number": ".O.OOO",
	},
}

var rootCmd = &cobra.Command{
	Use:   "translator",
	Short: "Translator is a tool to translate between text and braille",
	Run: func(cmd *cobra.Command, args []string) {
		output := []string{}

		for _, arg := range args {
			translated, err := translate(arg, len(args) == 1 && isBraille(args[0]))
			if err != nil {
				fmt.Println("Error:", err)
				continue
			}

			output = append(output, translated)
		}

		fmt.Println(strings.Join(output, dictionary.Symbols[" "]))
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func translate(text string, isBraille bool) (string, error) {
	var splitText, modifier string
	increment := 1
	if isBraille {
		increment = 6
		dictionary = dictionary.Reverse()
	}

	for i := 0; i < len(text); i += increment {
		chunk := text[i : i+increment]

		if modifier != "" {
			splitText += handleModifier(chunk, modifier, isBraille)
			modifier = ""
			continue
		}

		val, found := handleChunk(chunk, isBraille, &modifier)
		if !found {
			return "", fmt.Errorf("character %s not found in dictionary", chunk)
		}
		splitText += val
	}

	return splitText, nil
}

func handleModifier(chunk, modifier string, isBraille bool) string {
	switch modifier {
	case "capital":
		if isBraille {
			return strings.ToUpper(dictionary.Alphabet[chunk])
		}
		return dictionary.Modifiers["capital"] + dictionary.Alphabet[chunk]
	case "decimal":
		if val, ok := dictionary.Numbers[chunk]; ok {
			if isBraille {
				return "." + val
			}
			return dictionary.Modifiers["decimal"] + val
		}
	case "number":
		if val, ok := dictionary.Numbers[chunk]; ok {
			return val
		}
	}
	return dictionary.Symbols[chunk]
}

func handleChunk(chunk string, isBraille bool, modifier *string) (string, bool) {
	handlers := map[string]func(string) (string, bool){
		"Alphabet": func(chunk string) (string, bool) { val, ok := dictionary.Alphabet[chunk]; return val, ok },
		"Symbols":  func(chunk string) (string, bool) { val, ok := dictionary.Symbols[chunk]; return val, ok },
		"Modifiers": func(chunk string) (string, bool) {
			val, ok := dictionary.Modifiers[chunk]
			if ok {
				*modifier = val
			}
			return "", ok
		},
	}

	if !isBraille {
		handlers["Lowercase"] = func(chunk string) (string, bool) {
			val, ok := dictionary.Alphabet[strings.ToLower(chunk)]
			if ok {
				*modifier = "capital"
				return dictionary.Modifiers["capital"] + val, true
			}
			return "", false
		}

		handlers["Numbers"] = func(chunk string) (string, bool) {
			val, ok := dictionary.Numbers[chunk]
			if ok {
				*modifier = "number"
				return dictionary.Modifiers["number"] + val, true
			}
			return "", false
		}
	}

	for _, handler := range handlers {
		if val, ok := handler(chunk); ok {
			return val, true
		}
	}
	return "", false
}

func reverseMap(m map[string]string) map[string]string {
	output := make(map[string]string)
	for k, v := range m {
		output[v] = k
	}
	return output
}

func isBraille(text string) bool {
	exp := regexp.MustCompile(`^[.O]+$`)
	return exp.MatchString(text)
}
