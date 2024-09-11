package main

import (
	"fmt"
	"os"
	"strings"
)

// Braille mappings with special symbols
var brailleToEnglish = map[string]string{
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
    "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",
    // Punctuation marks
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")",
    // Special indicators
    ".....O": "cap", ".O.OOO": "num", "......": " ",
}

// Separate map for numbers to avoid duplicate keys
var brailleToEnglishNumbers = map[string]string{
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8",
    ".OO...": "9", ".OOO..": "0",
}

// English to Braille mappings 
var englishToBraille = map[string]string{
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..",
    // Punctuation marks
	".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", "(": "O.O..O", ")": ".O.OO.",
    // Special symbols
    "cap": ".....O", "num": ".O.OOO", " ": "......",
}

// Helper function to translate English to Braille
func translateEnglishToBraille(english string) string {
    var braille strings.Builder
    numberMode := false

    for _, char := range english {
        c := string(char)
        if c >= "A" && c <= "Z" {
            braille.WriteString(englishToBraille["cap"]) // Capital indicator
            c = strings.ToLower(c)
        }
        if c >= "0" && c <= "9" && !numberMode {
            braille.WriteString(englishToBraille["num"]) // Number indicator only once
            numberMode = true
        }
        if c == " " {
            braille.WriteString("......")
            numberMode = false // Reset number mode on space
            continue
        }

        if val, ok := englishToBraille[c]; ok {
            braille.WriteString(val )
        }
    }
    return braille.String()
}


// Helper function to translate Braille to English
func translateBrailleToEnglish(braille string) string {
    var english strings.Builder
    capitalized := false
    numberMode := false

    // Process the Braille string in chunks of 6 characters
    for i := 0; i < len(braille); i += 6 {
        if i+6 > len(braille) {
            break // In case the string isn't a multiple of 6, stop to avoid out-of-bounds error
        }
        brailleChar := braille[i : i+6]

        if brailleChar == ".....O" {
            capitalized = true
            continue
        }
        if brailleChar == ".O.OOO" {
            numberMode = true
            continue
        }

        var val string
        var ok bool
        if numberMode {
            // Use the number map when in number mode
            val, ok = brailleToEnglishNumbers[brailleChar]
        } else {
            // Use the regular map for letters
            val, ok = brailleToEnglish[brailleChar]
        }

        if ok {
            if capitalized {
                val = strings.ToUpper(val)
                capitalized = false // Capitalize only one letter
            }
            english.WriteString(val)
        } else if brailleChar == "......" { // Reset number mode on space
            numberMode = false
            english.WriteString(" ")
        }
    }
    return english.String()
}

// Helper function to determine if the input is Braille
func isBraille(input string) bool {
    // Ensure the input length is a multiple of 6 (quick check for braille)
    if len(input)%6 != 0 {
        return false
    }

	// Making sure braille only contains 'O' or '.'
	if strings.ContainsAny(input, "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") {
		return false
	}

    return true
}


func main() {
	// Process all arguments and output the result without trimming spaces
    for i, input := range os.Args[1:] {
        if isBraille(input) {
            // Input is Braille, translate to English
            fmt.Print(translateBrailleToEnglish(input))
        } else {
            // Input is English, translate to Braille
            fmt.Print(translateEnglishToBraille(input))
        }

		// Append a space or Braille space between arguments, but not after the last one
        if i < len(os.Args)-2 {
            if isBraille(input) {
                fmt.Print(" ") // Add a regular space between English words
            } else {
                fmt.Print("......") // Add a Braille space between Braille blocks
            }
        }
    }
}