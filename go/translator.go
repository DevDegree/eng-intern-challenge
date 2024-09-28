package main

import (
	"fmt"
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

var numMap = map[string]string{
	"1": "a",
	"2": "b",
	"3": "c",
	"4": "d",
	"5": "e",
	"6": "f",
	"7": "g",
	"8": "h",
	"9": "i",
	"0": "j",
}

var reverseNumMap = reverseMap(numMap)

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
			result, ok := reverseNumMap[englishChar]
			if ok {
				englishChar = result
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

func translateToBraille(input string) string {
	var result string
	isNumberMode := false
	for _, char := range input {
		s := string(char)
		if strings.Contains("0123456789", s) && !isNumberMode {
			result += englishToBrailleDict["number"]
			isNumberMode = true
		}
		if strings.Contains("ABCDEFGHIJKLMNOPQRSTUVWXYZ", s) {
			result += englishToBrailleDict["capitalize"]
			s = strings.ToLower(s)
		}
		if s == " " {
			s = "space"
			isNumberMode = false
		}
		if isNumberMode {
			val, ok := numMap[s]
			if ok {
				s = val
			}
		}
		result += englishToBrailleDict[s]
	}
	return result
}

func main() {
	input := os.Args[1:]

	if isBraille(input) {
		result := translateToEnglish(input[0])
		fmt.Print(result)
	} else {
		result := translateToBraille(strings.Join(input, " "))
		fmt.Print(result)
	}
}
