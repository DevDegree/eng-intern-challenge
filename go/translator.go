package main

import (
	"fmt"
	"os"
)

// IsBraille checks if a given string consists only of Braille characters ('O' and '.').
func IsBraille(str string) bool {
	for _, r := range str {
		if r != 'O' && r != '.' {
			return false
		}
	}
	return true
}

// EnglishToBraille converts an English string to its Braille representation.
func EnglishToBraille(str string) {
	// Mapping of each alphabet letter to its Braille representation
	alpha_to_braille := [26]string{
		"O.....", "O.O...", "OO....", "OO.O..", "O..O..", // A-E
		"OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", // F-J
		"O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", // K-O
		"OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", // P-T
		"O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", // U-Y
		"O..OOO", // Z
	}

	// Mapping of each digit to its Braille representation
	num_to_braille := [10]string{
		".OOO..", "O.....", "O.O...", "OO....", "OO.O..", // 0-4
		"O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", // 5-9
	}

	// Prepare to process the input string
	rune_arr := make([]rune, 0, len(str))
	number := false

	// Iterate through each character in the input string
	for _, r := range str {
		// Handle numbers by adding a special prefix '#' to indicate numbers in Braille
		if '0' <= r && r <= '9' {
			if !number {
				rune_arr = append(rune_arr, '#')
				number = true
			}
			rune_arr = append(rune_arr, r)
			continue
		}

		number = false

		// Handle uppercase letters by adding a special prefix '^' to indicate capital letters in Braille
		if 'A' <= r && r <= 'Z' {
			rune_arr = append(rune_arr, '^')
			rune_arr = append(rune_arr, r+32) // Convert to lowercase
			continue
		}
		rune_arr = append(rune_arr, r)
	}

	new_str := string(rune_arr)

	// Convert each character in the processed string to its Braille equivalent
	for _, r := range new_str {
		if 'a' <= r && r <= 'z' {
			fmt.Print(alpha_to_braille[r-'a'])
		} else if '0' <= r && r <= '9' {
			fmt.Print(num_to_braille[r-'0'])
		}
		switch r {
		case '#':
			fmt.Print(".O.OOO") // Braille number prefix
		case '^':
			fmt.Print(".....O") // Braille capital letter prefix
		case ' ':
			fmt.Print("......") // Braille space
		}
	}
}

// BrailleToEnglish converts a Braille string back to its English representation.
func BrailleToEnglish(braille string) {
	// Mapping from Braille patterns to English characters
	braille_to_english := map[string]rune{
		"O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
		"OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
		"O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
		"OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
		"O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
		"O..OOO": 'z', ".O.OOO": '#', ".....O": '^', "......": ' ',
	}

	// Mapping from Braille patterns to digits
	braille_to_num := map[string]rune{
		".OOO..": '0', "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4',
		"O..O..": '5', "OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9',
	}

	var new_str string
	number := false
	capital := false

	// Iterate through each Braille pattern in the input string
	for i := 0; i < len(braille); i += 6 {
		end := i + 6

		if number {
			new_str += string(braille_to_num[braille[i:end]])
			continue
		}

		r := braille_to_english[braille[i:end]]
		if r == '#' {
			number = true
			continue
		} else if r == '^' {
			capital = true
			continue
		} else if r == ' ' {
			number = false
		}

		if capital {
			new_str += string(r - 32) // Convert to uppercase
		} else {
			new_str += string(r)
		}

		capital = false
	}

	fmt.Print(new_str)
}

// main is the entry point of the program, handling command-line arguments and triggering the appropriate conversion.
func main() {
	args := os.Args[1:]

	if len(args) == 1 && IsBraille(args[0]) {
		// Convert Braille to English if the input is recognized as Braille
		BrailleToEnglish(args[0])
	} else {
		// Convert English text to Braille
		var str string
		for _, arg := range args {
			str += arg + " "
		}
		str = str[:len(str)-1] // Remove trailing space
		EnglishToBraille(str)
	}

	fmt.Println()
}
