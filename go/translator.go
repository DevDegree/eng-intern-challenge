package main

import (
	"fmt"
	"os"
	"strings"
)

var BRAILLE_MAP = map[string]int{
	"a": 0b100000, "b": 0b101000, "c": 0b110000, "d": 0b110100, "e": 0b100100,
	"f": 0b111000, "g": 0b111100, "h": 0b101100, "i": 0b011000, "j": 0b011100,
	"k": 0b100010, "l": 0b101010, "m": 0b110010, "n": 0b110110, "o": 0b100110,
	"p": 0b111010, "q": 0b111110, "r": 0b101110, "s": 0b011010, "t": 0b011110,
	"u": 0b100011, "v": 0b101011, "w": 0b011101, "x": 0b110011, "y": 0b110111,
	"z": 0b100111,
	"1": 0b100000, "2": 0b101000, "3": 0b110000, "4": 0b110100, "5": 0b100100,
	"6": 0b111000, "7": 0b111100, "8": 0b101100, "9": 0b011000, "0": 0b011100,
	".": 0b001101, ",": 0b001000, "?": 0b001011, "!": 0b001110, "-": 0b000011,
	":": 0b001100, ";": 0b001010, "(": 0b101001, ")": 0b010110, "/": 0b010010,
	"'": 0b000010, "\"": 0b001010, "*": 0b000110, "@": 0b000101, "&": 0b101101,
	" ":       0b000000,
	"capital": 0b000001,
	"number":  0b010111,
	"decimal": 0b000101,
}

var BRAILLE_REVERSE_MAP map[int]string

func init() {
	BRAILLE_REVERSE_MAP = make(map[int]string)
	for k, v := range BRAILLE_MAP {
		BRAILLE_REVERSE_MAP[v] = k
	}
}

func translateToBraille(text string) []int {
	translated := []int{}
	numberMode := false

	for _, char := range text {
		charStr := string(char)
		if charStr == " " {
			translated = append(translated, BRAILLE_MAP[" "])
			numberMode = false
		} else if char >= '0' && char <= '9' {
			if !numberMode {
				translated = append(translated, BRAILLE_MAP["number"])
				numberMode = true
			}
			translated = append(translated, BRAILLE_MAP[charStr])
		} else if charStr == "." {
			if numberMode {
				translated = append(translated, BRAILLE_MAP["decimal"])
			} else {
				translated = append(translated, BRAILLE_MAP["."])
			}
			numberMode = false
		} else {
			if numberMode {
				numberMode = false
			}
			if char >= 'A' && char <= 'Z' {
				translated = append(translated, BRAILLE_MAP["capital"])
				charStr = string(char + 32) // Convert to lowercase
			}
			translated = append(translated, BRAILLE_MAP[charStr])
		}
	}

	return translated
}

func translateToEnglish(brailleBinary []int) string {
	translated := []string{}
	numberMode := false
	capitalMode := false

	for _, brailleChar := range brailleBinary {
		if brailleChar == BRAILLE_MAP[" "] {
			translated = append(translated, " ")
			numberMode = false
			capitalMode = false
		} else if brailleChar == BRAILLE_MAP["number"] {
			numberMode = true
		} else if brailleChar == BRAILLE_MAP["decimal"] {
			translated = append(translated, ".")
		} else if brailleChar == BRAILLE_MAP["capital"] {
			capitalMode = true
		} else {
			char := BRAILLE_REVERSE_MAP[brailleChar]
			if numberMode {
				if strings.ContainsAny(char, "abcdefghij") {
					digit := (int(char[0]) - int('a') + 1) % 10
					translated = append(translated, string(rune('0'+digit)))
				} else {
					translated = append(translated, "?")
				}
			} else {
				if capitalMode {
					char = strings.ToUpper(char)
					capitalMode = false
				}
				translated = append(translated, char)
			}
		}
	}

	return strings.Join(translated, "")
}

func binaryToBrailleDots(binary int) string {
	dots := ""
	for i := 5; i >= 0; i-- {
		if binary&(1<<i) != 0 {
			dots += "O"
		} else {
			dots += "."
		}
	}
	return dots
}

func brailleDotsToBinary(dots string) int {
	binary := 0
	for i, char := range dots {
		if char == 'O' {
			binary |= 1 << (5 - i)
		}
	}
	return binary
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run translator.go <text_or_braille>")
		os.Exit(1)
	}

	input := strings.Join(os.Args[1:], " ")

	if strings.Count(input, "O")+strings.Count(input, ".") == len(input) {
		// Input is Braille dots
		brailleBinary := []int{}
		for i := 0; i < len(input); i += 6 {
			brailleBinary = append(brailleBinary, brailleDotsToBinary(input[i:i+6]))
		}
		fmt.Println(translateToEnglish(brailleBinary))
	} else {
		// Input is text
		brailleBinary := translateToBraille(input)
		for _, char := range brailleBinary {
			fmt.Print(binaryToBrailleDots(char))
		}
		fmt.Println()
	}
}
