package main

import (
	"os"
	"regexp"
	"strings"
)

var translation map[string]string
var special map[string]string

func main() {
	// Read and join command line arguments to form message
	message := strings.Join(os.Args[1:], " ")

	// Translation table
	translation = map[string]string{
		"a": "O.....",
		"b": "O.O...",
		"c": "OO....",
		"d": "OO.O..",
		"e": "O..O..",
		"f": "OOO...",
		"g": "OOOO..",
		"h": "O.OO..",
		"i": ".OO...",
		"j": ".OOO..",
		"k": "O...O.",
		"l": "O.O.O.",
		"m": "OO..O.",
		"n": "OO.OO.",
		"o": "O..OO.",
		"p": "OOO.O.",
		"q": "OOOOO.",
		"r": "O.OOO.",
		"s": ".OO.O.",
		"t": ".OOOO.",
		"u": "O...OO",
		"v": "O.O.OO",
		"w": ".OOO.O",
		"x": "OO..OO",
		"y": "OO.OOO",
		"z": "O..OOO",
		"1": "O.....",
		"2": "O.O...",
		"3": "OO....",
		"4": "OO.O..",
		"5": "O..O..",
		"6": "OOO...",
		"7": "OOOO..",
		"8": "O.OO..",
		"9": ".OO...",
		"0": ".OOO..",
		".": "..OO.O",
		",": "..O...",
		"?": "..O.OO",
		"!": "..OOO.",
		":": "..OO..",
		";": "..O.O.",
		"_": "....OO",
		"/": ".O..O.",
		"<": ".OO..O",
		">": "O..OO.",
		"(": "O.O..O",
		")": ".O.OO.",
		" ": "......",
	}

	special = map[string]string{
		"cap": ".....O",
		"dec": ".O...O",
		"num": ".O.OOO",
	}

	// Determine the direction of translation
	pattern := `^[a-zA-Z0-9 ]+$`
	re := regexp.MustCompile(pattern)

	if re.MatchString(message) {
		println(translateToBraille(message))
	} else {
		println(translateToEnglish(message))
	}
}

func translateToBraille(message string) string {
	result := ""
	flagNum := false

	for _, char := range message {
		if char >= 'A' && char <= 'Z' {
			result += special["cap"]
			char = char + 32
		}

		if char >= 'a' && char <= 'z' {
			result += translation[string(char)]
		} else if char >= '0' && char <= '9' {
			if !flagNum {
				result += special["num"]
				flagNum = true
			}
			result += translation[string(char)]
		} else if char == ' ' {
			result += translation[string(char)]
			flagNum = false
		} else if char == '.' {
			if flagNum {
				result += special["dec"]
			} else {
				result += translation[string(char)]
			}
		} else if translation[string(char)] != "" {
			result += translation[string(char)]
		}
	}

	return result
}

func translateToEnglish(message string) string {
	result := ""
	flagCap := false
	flagNum := false

	for i := 0; i < len(message); i += 6 {
		char := message[i : i+6]

		if char == special["cap"] {
			flagCap = true
			continue
		} else if char == special["dec"] {
			result += "."
			continue
		} else if char == special["num"] {
			flagNum = true
			continue
		} else if char == translation[" "] {
			result += " "
			flagNum = false
			continue
		} else if flagNum {
			for k, v := range translation {
				if v == char && k >= "0" && k <= "9" {
					result += k
					break
				}
			}
		} else {
			for k, v := range translation {
				if v == char && (k < "0" || k > "9") {
					if flagCap {
						result += strings.ToUpper(k)
						flagCap = false
					} else {
						result += k
					}
					break
				}
			}
		}
	}
	return result
}
