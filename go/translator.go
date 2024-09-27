package main

import (
	"log"
	"os"
	"strings"
)

var englishToBrailleDict = map[string]string{
	"a":          "O.....",
	"b":          "O.O...",
	"c":          "OO....",
	"d":          "OO.O..",
	"e":          "O..O..",
	"f":          "OOO...",
	"g":          "OOOO..",
	"h":          "O.OO..",
	"i":          ".OO...",
	"j":          ".OOO..",
	"k":          "O...O.",
	"l":          "O.O.O.",
	"m":          "OO..O.",
	"n":          "OO.OO.",
	"o":          "O..OO.",
	"p":          "OOO.O.",
	"q":          "OOOOO.",
	"r":          "O.OOO.",
	"s":          ".OO.O.",
	"t":          ".OOOO.",
	"u":          "O...OO",
	"v":          "O.O.OO",
	"w":          ".OOO.O",
	"x":          "OO..OO",
	"y":          "OO.OOO",
	"z":          "O..OOO",
	"capitalize": ".....O",
	"number":     ".O.OOO",
	"space":      "......",
}

var brailleToEnglishDict = reverseMap(englishToBrailleDict)

func reverseMap(dict map[string]string) map[string]string {
	dictReversed := make(map[string]string)
	for key, value := range dict {
		dictReversed[value] = key
	}
	return dictReversed
}

func isBraille(input []string) bool {
	if strings.Contains(input[0], ".") {
		return true
	}
	return false
}

func translateToEnglish(input string) string {
	var word string
	isNextCapitalized := false
	isNextNumber := false
	i := 0
	for i < len(input) {
		brailleChar := input[i : i+6]
		englishChar := brailleToEnglishDict[brailleChar]
		if isNextCapitalized {
			englishChar = strings.ToUpper(englishChar)
			isNextCapitalized = false
		}
		if isNextNumber {
			switch englishChar {
			case "a":
				englishChar = "1"
			case "b":
				englishChar = "2"
			case "c":
				englishChar = "3"
			case "d":
				englishChar = "4"
			case "e":
				englishChar = "5"
			case "f":
				englishChar = "6"
			case "g":
				englishChar = "7"
			case "h":
				englishChar = "8"
			case "i":
				englishChar = "9"
			case "j":
				englishChar = "0"
			default:
				isNextNumber = false
			}
		}
		if englishChar == "capitalize" {
			isNextCapitalized = true
		}
		if englishChar == "number" {
			isNextNumber = true
		}
		if englishChar == "space" {
			word += " "
		}

		if len(englishChar) == 1 {
			word += englishChar
		}
		i += 6
	}
	return word
}

func translateToBraille(input string) string { return "" }

func main() {
	input := os.Args[1:]

	if isBraille(input) {
		englishChar := translateToEnglish(input[0])
		log.Printf("Translation: %v", englishChar)
	} else {
		brailleChar := translateToBraille(input[0])
		log.Printf("Translation: %v", brailleChar)
	}

}
