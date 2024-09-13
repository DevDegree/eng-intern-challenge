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
		if len(args) == 1 && isBraille(args[0]) {
			translated, err := translateToEnglish(args[0])
			if err != nil {
				fmt.Println("Error:", err)
				return
			}
			fmt.Println(translated)
		} else {
			var output []string
			for _, arg := range args {
				translated, err := translateToBraille(arg)
				if err != nil {
					fmt.Println("Error:", err)
					continue
				}
				output = append(output, translated)
			}
			fmt.Println(strings.Join(output, dictionary.Symbols[" "]))
		}
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func translateToEnglish(text string) (string, error) {
	var splitText, modifier string
	reversedDictionary := dictionary.Reverse()

	for i := 0; i < len(text); i += 6 {
		if i+6 > len(text) {
			return "", fmt.Errorf("text length is not a multiple of 6")
		}
		chunk := text[i : i+6]

		if modifier != "" {
			switch modifier {
			case "capital":
				splitText += strings.ToUpper(reversedDictionary.Alphabet[chunk])
			case "decimal":
				if val, ok := reversedDictionary.Numbers[chunk]; ok {
					splitText += fmt.Sprintf("%s.", val)
				}
			case "number":
				if " " == reversedDictionary.Symbols[chunk] {
					splitText += " "
				} else if val, ok := reversedDictionary.Numbers[chunk]; ok {
					splitText += val
					continue
				}
			}
			modifier = ""
			continue
		}

		if val, ok := reversedDictionary.Alphabet[chunk]; ok {
			splitText += val
		} else if val, ok := reversedDictionary.Symbols[chunk]; ok {
			splitText += val
		} else if val, ok := reversedDictionary.Modifiers[chunk]; ok {
			modifier = val
		} else {
			return "", fmt.Errorf("braille character %s not found in dictionary", chunk)
		}
	}

	return splitText, nil
}

func translateToBraille(text string) (string, error) {
	var splitText, modifier string

	for i := 0; i < len(text); i++ {
		chunk := text[i : i+1]

		if modifier != "" {
			switch modifier {
			case "capital":
				splitText += dictionary.Modifiers["capital"] + dictionary.Alphabet[chunk]
				i += 6
			case "decimal":
				if val, ok := dictionary.Numbers[chunk]; ok {
					splitText += dictionary.Modifiers["decimal"] + val
				}
			case "number":
				if " " == chunk {
					splitText += dictionary.Symbols[" "]
				} else if val, ok := dictionary.Numbers[chunk]; ok {
					splitText += val
					continue
				}
			}
			modifier = ""
			continue
		}

		if val, ok := dictionary.Alphabet[chunk]; ok {
			splitText += val
		} else if val, ok := dictionary.Alphabet[strings.ToLower(chunk)]; ok {
			splitText += dictionary.Modifiers["capital"] + val
		} else if val, ok := dictionary.Numbers[chunk]; ok {
			splitText += dictionary.Modifiers["number"] + val
			modifier = "number"
		} else if val, ok := dictionary.Symbols[chunk]; ok {
			splitText += val
		} else if val, ok := dictionary.Modifiers[chunk]; ok {
			modifier = val
		} else {
			return "", fmt.Errorf("braille character %s not found in dictionary", chunk)
		}
	}

	return splitText, nil
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
