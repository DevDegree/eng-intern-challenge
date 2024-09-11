package main

import (
	"fmt"
	"os"
	"strings"
)


const (
	capitalFollows = ".....O"
	numberFollows  = ".O.OOO"
	space          = "......"
)


var engToBraille = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
	"z": "O..OOO", " ": space, "capital_follows": capitalFollows, "number_follows": numberFollows,
}


var characterToNumber = map[string]string{
	"a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
	"f": "6", "g": "7", "h": "8", "i": "9", "j": "0",
}


var brailleToEng map[string]string
var numberToCharacter map[string]string


func init() {
	brailleToEng = make(map[string]string)
	for key, value := range engToBraille {
		brailleToEng[value] = key
	}
    numberToCharacter = make(map[string]string)
    for key, value := range characterToNumber {
        numberToCharacter[value] = key
    }
}


func brailleToEnglish(braille string) string {
    var result strings.Builder
    capitalizeFlag := false
    numberFlag := false
    for i := 0; i < len(braille); i += 6 {
        if i+6 > len(braille) {
            break
        }
        char := braille[i : i+6]
        switch char {
        case capitalFollows:
            capitalizeFlag = true
        case numberFollows:
            numberFlag = true
        case space:
            result.WriteString(" ")
            numberFlag = false
        default:
            if character, ok := brailleToEng[char]; ok {
                if numberFlag {
                    if num, exists := characterToNumber[character]; exists {
                        result.WriteString(num)
                        continue
                    }
                    numberFlag = false
                }
                if capitalizeFlag {
                    character = strings.ToUpper(character)
                    capitalizeFlag = false
                }
                result.WriteString(character)
            }
        }
    }
    return result.String()
}


func englishToBraille(text string) string {
    var result strings.Builder
    numberFlag := false
    for _, char := range text {
        switch {
        case char >= '0' && char <= '9':
            if !numberFlag {
                result.WriteString(numberFollows)
                numberFlag = true
            }
            result.WriteString(engToBraille[numberToCharacter[string(char)]])
        case char >= 'a' && char <= 'z' || char >= 'A' && char <= 'Z':
            if numberFlag {
                result.WriteString(space)
                numberFlag = false
            }
            if char >= 'A' && char <= 'Z' {
                result.WriteString(capitalFollows)
                char += 32 
            }
            result.WriteString(engToBraille[string(char)])
        case char == ' ':
            result.WriteString(space)
            numberFlag = false
        }
    }
    return result.String()
}


func translate(input string) string {
    for _, c := range input {
        if c != 'O' && c != '.' {
            return englishToBraille(input)
        }
    }
    return brailleToEnglish(input)
}


func main() {
	if len(os.Args) < 2 {
		os.Exit(1)
	}
	input := strings.Join(os.Args[1:], " ")
	fmt.Println(translate(input))
}
