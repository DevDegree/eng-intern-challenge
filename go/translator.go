package main

import (
	"fmt"
)

type Language int

const (
	English = iota + 1
	Braille
)

func main() {
	// Read input
	// Identify language
	// Get data from the language using codification
	// Convert into the other language
	// Print the result and only the result
	var input string

	_, err := fmt.Scanln(&input)

	if err != nil {
		fmt.Println("Error reading from the input: ", err)
	}
	fmt.Println("Input: ", input)
	if languageIdentifier(input) == English {
		englishToBraille(input)
	}
	brailleToEnglish(input)
}

func languageToString(l Language) string {
	if l == English {
		return "English"
	}
	if l == Braille {
		return "Braille"
	}

	return "Unknown"
}

func languageIdentifier(input string) Language {
	for _, char := range input {
		if char != '0' && char != '.' {
			return English
		}
	}
	return Braille
}

func englishToBraille(input string) string { return nil }

func brailleHelper(input string) string {
	brailleMap := make(map[string]string)
	brailleMap["0....."] = "a" // also 1
	brailleMap["0.0..."] = "b" // also 2
	brailleMap["00...."] = "c" // also 3
	brailleMap["00.0.."] = "d" // also 4
	brailleMap["0..0.."] = "e" // also 5
	brailleMap["000..."] = "f" // also 6
	brailleMap["0000.."] = "g" // also 7
	brailleMap["0.00.."] = "h" // also 8
	brailleMap[".00..."] = "i" // also 9
	brailleMap[".000.."] = "j" // also 0
	brailleMap["0...0."] = "k"
	brailleMap["0.0.0."] = "l"
	brailleMap["00..0."] = "m"
	brailleMap["00.00."] = "n"
	brailleMap["0..00."] = "o"
	brailleMap["000.0."] = "p"
	brailleMap["00000."] = "q"
	brailleMap["0.000."] = "r"
	brailleMap[".00.0."] = "s"
	brailleMap[".0000."] = "t"
	brailleMap["0...00"] = "u"
	brailleMap["0.0.00"] = "v"
	brailleMap[".000.0"] = "w"
	brailleMap["00..00"] = "x"
	brailleMap["00.000"] = "y"
	brailleMap["0..000"] = "z"
	brailleMap[".....0"] = "Capital letter follows"
	brailleMap[".0.000"] = "Number follows"
	brailleMap[".0...0"] = "Decimal follows"
	brailleMap["..00.0"] = "."
	brailleMap["..0..."] = ","
	brailleMap["..0.00"] = "?"
	brailleMap["..00.."] = ":"
	brailleMap["..0.0."] = ";"
	brailleMap["....00"] = "-"
	brailleMap[".0..0."] = "/"
	brailleMap[".0.0.0"] = "<"
	brailleMap["0.0.0."] = ">"
	brailleMap["0.0..0"] = "("
	brailleMap[".0.00."] = ")"
	brailleMap["......"] = " "

	return brailleMap[input]
}

func brailleToEnglish(input string) string { return nil }

func brailleDecoder(input string) {
	str := ""
	capitalNext := false
	numberNext := false
	decimalNext := false
	for i := 0; i < len(input); i += 6 {
		if i+6 > len(input) {
			break
		}

		brailleCell := input[i : i+6]

		if brailleCell == ".....0" {
			capitalNext = true
			continue
		}
		if brailleCell == ".0.000" {
			numberNext = true
			continue
		}
		if brailleCell == ".0...0" {
			decimalNext = true
			continue
		}

		if capitalNext {

		}

		str += brailleHelper(input[i : i+6])

	}

}
