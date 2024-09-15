package main

import (
	"fmt"
	"os"
	"strings"
)

// braille alphabet mapping
var brailleMap = map[string]string{

	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",

	"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
	"5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",

	".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
	";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",

	" ": "......",
	"caps": ".....O",
	"num": ".O.OOO",
}

var reverseBrailleMap = make(map[string]string)

func init() {
	for k, v := range brailleMap {
		reverseBrailleMap[v] = k
	}
}

func isBraille(input string) bool {
	for _, char := range input {
		if char != 'O' && char != '.' {
			return false
		}
	}
	return true
}

func toBraille(input string) string {
	var result strings.Builder
	numMode := false

	for i := 0; i < len(input); i++ {
		char := string(input[i])

		if char >= "A" && char <= "Z" {
			result.WriteString(brailleMap["caps"])
			char = strings.ToLower(char)
		}

		if char >= "0" && char <= "9" {
			if !numMode {
				result.WriteString(brailleMap["num"])
				numMode = true
			}
			result.WriteString(brailleMap[char])
		} else if char == " " {
			numMode = false
			result.WriteString(brailleMap[char])
		} else {
			numMode = false
			result.WriteString(brailleMap[char])
		}
	}

	return result.String()
}

func fromBraille(input string) string {
	var result strings.Builder
	numMode := false
	i := 0

	for i < len(input) {
		if i+6 <= len(input) {
			code := input[i : i+6]

			if code == brailleMap["caps"] {
				nextChar := input[i+6 : i+12]
				if letter, ok := reverseBrailleMap[nextChar]; ok {
					result.WriteString(strings.ToUpper(letter))
				}
				i += 12
				continue
			}

			if code == brailleMap["num"] {
				numMode = true
				i += 6
				continue
			}

			if letter, ok := reverseBrailleMap[code]; ok {
				result.WriteString(letter)
				if !numMode && letter == " " {
					numMode = false 
				}
			}

			i += 6
		}
	}

	return result.String()
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("To run use: go run translator.go <string>")
		return
	}

	input := strings.Join(os.Args[1:], " ")

	if isBraille(input) {
		fmt.Println(fromBraille(input))
	} else {
		fmt.Println(toBraille(input))
	}
}
