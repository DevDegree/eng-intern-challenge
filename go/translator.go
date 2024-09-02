package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	capFollows        = "capFollows"
	numFollows        = "numFollows"
	braileSpace       = "......"
	brailleCapFollows = ".....O"
	brailleNumFollows = ".O.OOO"
	brailleLength     = 6
)

var englishToBrailleMap = map[string]string{
	"a":        "O.....",
	"b":        "O.O...",
	"c":        "OO....",
	"d":        "OO.O..",
	"e":        "O..O..",
	"f":        "OOO...",
	"g":        "OOOO..",
	"h":        "O.OO..",
	"i":        ".OO...",
	"j":        ".OOO..",
	"k":        "O...O.",
	"l":        "O.O.O.",
	"m":        "OO..O.",
	"n":        "OO.OO.",
	"o":        "O..OO.",
	"p":        "OOO.O.",
	"q":        "OOOOO.",
	"r":        "O.OOO.",
	"s":        ".OO.O.",
	"t":        ".OOOO.",
	"u":        "O...OO",
	"v":        "O.O.OO",
	"w":        ".OOO.O",
	"x":        "OO..OO",
	"y":        "OO.OOO",
	"z":        "O..OOO",
	"1":        "O.....",
	"2":        "O.O...",
	"3":        "OO....",
	"4":        "OO.O..",
	"5":        "O..O..",
	"6":        "OOO...",
	"7":        "OOOO..",
	"8":        "O.OO..",
	"9":        ".OO...",
	"0":        ".OOO..",
	" ":        braileSpace,
	capFollows: brailleCapFollows,
	numFollows: brailleNumFollows,
}

var brailleToEnglishAlphabetMap = map[string]string{
	"O.....":          "a",
	"O.O...":          "b",
	"OO....":          "c",
	"OO.O..":          "d",
	"O..O..":          "e",
	"OOO...":          "f",
	"OOOO..":          "g",
	"O.OO..":          "h",
	".OO...":          "i",
	".OOO..":          "j",
	"O...O.":          "k",
	"O.O.O.":          "l",
	"OO..O.":          "m",
	"OO.OO.":          "n",
	"O..OO.":          "o",
	"OOO.O.":          "p",
	"OOOOO.":          "q",
	"O.OOO.":          "r",
	".OO.O.":          "s",
	".OOOO.":          "t",
	"O...OO":          "u",
	"O.O.OO":          "v",
	".OOO.O":          "w",
	"OO..OO":          "x",
	"OO.OOO":          "y",
	"O..OOO":          "z",
	braileSpace:       " ",
	brailleCapFollows: capFollows,
	brailleNumFollows: numFollows,
}

var brailleToEnglishNumberMap = map[string]string{
	"O.....": "1",
	"O.O...": "2",
	"OO....": "3",
	"OO.O..": "4",
	"O..O..": "5",
	"OOO...": "6",
	"OOOO..": "7",
	"O.OO..": "8",
	".OO...": "9",
	".OOO..": "0",
}

func englishToBraille(english string) string {
	bs := []byte(english)
	ret := ""
	isNum := false

	for _, b := range bs {
		if b >= 'A' && b <= 'Z' {
			ret += englishToBrailleMap[capFollows]
			b = byte(unicode.ToLower(rune(b)))
		}

		if b >= '0' && b <= '9' {
			if !isNum {
				ret += englishToBrailleMap[numFollows]
			}
			isNum = true
		} else {
			isNum = false
		}

		ret += englishToBrailleMap[string(b)]
	}

	return ret
}

func brailleToEnglish(braille string) string {
	bs := []byte(braille)
	ret := ""
	isCap := false
	isNum := false

	for i := 0; i < len(bs); i += brailleLength {
		word := string(bs[i : i+brailleLength])
		if word == brailleCapFollows {
			isCap = true
			continue
		} else if word == brailleNumFollows {
			isNum = true
			continue
		} else if word == braileSpace {
			isNum = false
		}

		if isCap {
			ret += strings.ToUpper(brailleToEnglishAlphabetMap[word])
			isCap = false
		} else if isNum {
			ret += brailleToEnglishNumberMap[word]
		} else {
			ret += brailleToEnglishAlphabetMap[word]
		}
	}

	return ret
}

func main() {
	args := os.Args[1:]
	fmt.Println(englishToBraille(strings.Join(args, " ")))
}
