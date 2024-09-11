package main

import (
        "fmt"
        "os"
        "strings"
)

func reverseMap(input map[string]string) map[string]string {
        var reversed map[string]string = make(map[string]string, len(input))

        for key, value := range input {
                reversed[value] = key
        }

        return reversed
}

var brailleNumbersToEnglish map[string]string = map[string]string{
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

var englishNumbersToBraille map[string]string = reverseMap(brailleNumbersToEnglish)

var brailleToEnglish map[string]string = map[string]string{
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",
}

var englishToBraille map[string]string = reverseMap(brailleToEnglish)

// assumptions:
//
// - braille will always be in 6 character chunks
//
// - braille will have atleast one dot character in a braille character
func isBraille(str string) bool {
        if len(str)%6 != 0 {
                return false
        }

        for _, c := range str[:6] {
                if c == '.' {
                        return true
                }
        }

        return false
}

// assumptions:
//
// - str input was validated to be braille already
func convertBrailleToEnglish(str string) (string, error) {
        var numberMode bool = false
        var capitalMode bool = false

        var buffer strings.Builder = strings.Builder{}

        for i := 0; i < len(str); i += 6 {
                var braille string = str[i : i+6]

                if capitalMode && numberMode {
                        panic("how :(")
                }

                if braille == capitalFollows {
                        capitalMode = true
                        continue
                }

                if braille == numberFollows {
                        numberMode = true
                        continue
                }

                if braille == space {
                        buffer.WriteString(" ")
                        numberMode = false
                        continue
                }

                if capitalMode {
                        value, exists := brailleToEnglish[braille]
                        if !exists {
                                return "", fmt.Errorf("invalid braille character (Capital): %s", braille)
                        }
                        buffer.WriteString(strings.ToUpper(value))
                        capitalMode = false
                        continue
                }

                if numberMode {
                        value, exists := brailleNumbersToEnglish[braille]
                        if !exists {
                                return "", fmt.Errorf("invalid braille character (Number): %s", braille)
                        }
                        buffer.WriteString(value)
                        continue
                }

                value, exists := brailleToEnglish[braille]
                if !exists {
                        return "", fmt.Errorf("invalid braille character: %s", braille)
                }

                buffer.WriteString(value)

        }

        return buffer.String(), nil
}

const (
        capitalFollows string = ".....O"
        numberFollows  string = ".O.OOO"
        space          string = "......"

        numbers             string = "1234567890"
        alphabet            string = "abcdefghijklmnopqrstuvwxyz"
        capitalizedAlphabet string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
)

func convertEnglishToBraille(str string) (string, error) {
        var buffer strings.Builder = strings.Builder{}

        var numberMode bool = false

        for _, character := range str {
                if character == ' ' {
                        buffer.WriteString(space)
                        numberMode = false
                        continue
                }

                if strings.ContainsRune(numbers, character) {
                        if !numberMode {
                                buffer.WriteString(numberFollows)
                                numberMode = true
                        }
                        buffer.WriteString(englishNumbersToBraille[string(character)])
                        continue
                }

                if strings.ContainsRune(capitalizedAlphabet, character) {
                        buffer.WriteString(capitalFollows)
                        buffer.WriteString(englishToBraille[strings.ToLower(string(character))])
                        continue
                }

                if strings.ContainsRune(alphabet, character) {
                        buffer.WriteString(englishToBraille[string(character)])
                        continue
                }

                return "", fmt.Errorf("invalid character: %c", character)
        }

        return buffer.String(), nil
}

func main() {
        var args []string = os.Args[1:]

        if len(args) == 0 {
                fmt.Println("Please provide some input 🥺")
                return
        }

        var input string = strings.Join(args, " ")

        converter := convertEnglishToBraille
        if isBraille(input) {
                converter = convertBrailleToEnglish
        }

        output, err := converter(input)

        if err != nil {
                fmt.Printf("Error: %v\n", err)
                return
        }

        fmt.Println(output)

}