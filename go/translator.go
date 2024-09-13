package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	// get input argument string
	args := os.Args
	if len(args) < 2 {
		log.Print("Err : Please provide input")
		return
	}
	// remove first argument of file name and concat rest of arguments
	inputString := strings.Join(args[1:], " ")
	translate(&inputString)
}

var englishToBrailleMap map[rune]string = map[rune]string{
	97:  "O.....", // a
	98:  "O.O...", // b
	99:  "OO....", // c
	100: "OO.O..", // d
	101: "O..O..", // e
	102: "OOO...", // f
	103: "OOOO..", // g
	104: "O.OO..", // h
	105: ".OO...", // i
	106: ".OOO..", // j
	107: "O...O.", // k
	108: "O.O.O.", // l
	109: "OO..O.", // m
	110: "OO.OO.", // n
	111: "O..OO.", // o
	112: "OOO.O.", // p
	113: "OOOOO.", // q
	114: "O.OOO.", // r
	115: ".OO.O.", // s
	116: ".OOOO.", // t
	117: "O...OO", // u
	118: "O.O.OO", // v
	119: ".OOO.O", // w
	120: "OO..OO", // x
	121: "OO.OOO", // y
	122: "O..OOO", // z
	49:  "O.....", // 1
	50:  "O.O...", // 2
	51:  "OO....", // 3
	52:  "OO.O..", // 4
	53:  "O..O..", // 5
	54:  "OOO...", // 6
	55:  "OOOO..", // 7
	56:  "O.OO..", // 8
	57:  ".OO...", // 9
	48:  ".OOO..", // 0
	15:  ".....O", // capital letter
	14:  ".O...O", // decimal follows
	16:  ".O.OOO", // number follows
	46:  "..OO.O", // .
	44:  "..O...", // ,
	63:  "..O.OO", // ?
	33:  "..OOO.", // !
	58:  "..OO..", // :
	59:  "..O.O.", // ;
	45:  "....OO", // -
	47:  ".O..O.", // /
	60:  ".OO..O", // <
	62:  "O..OO.", // >
	40:  "O.O..O", // (
	41:  ".O.OO.", // )
	32:  "......", // <Space>
}

func translate(input *string) {
	// check if the string is English or Braille
	isBraille := true
	var output strings.Builder

	// divide the string by 6 to check if there are enough Braille letter
	if len(*input)%6 == 0 {
		// the letter are multiplication of 6 for 2x3 matrix of 6 letter to represent character
		// check if letter is other than "O" or "." exist
		// and if it exist set isBraille false
		for _, letter := range *input {
			if letter != 79 && letter != 46 { // 79 for "O" and 46 for "."
				isBraille = false
				break
			}
		}
	} else {
		isBraille = false // for invalid isBraille input set isBraille false
	}

	if isBraille { // translate isBraille to English
		brailleToEnglish := map[string]rune{}

		// create English to Braille map
		for k, v := range englishToBrailleMap {
			if !(k > 47 && k < 58) { // exclude number from replacing a-j with 0-9
				brailleToEnglish[v] = k
			}
		}

		// to keep status if the number is encountered
		numFlag := false
		capitalFlag := false

		for i := 0; i < len(*input); i += 6 {
			// check if the braille number follows
			letter := brailleToEnglish[(*input)[i:i+6]]
			if letter == 16 {
				numFlag = true
				continue
			}
			// check if the braille capital follows
			if letter == 15 {
				capitalFlag = true
				continue
			}

			if numFlag && letter > 96 && letter < 107 { // for each successive number with number flag add

				if letter == 106 { // for J = 106 convert j to 0
					letter -= 58
				} else { // for a - i to convert to number 1 - 9
					letter -= 48
				}
			} else if capitalFlag { // if capital flag is set convert the letter to capital

				capitalFlag = false
				letter -= 32
			}

			if letter == 32 { // for each space reset num flag
				numFlag = false
			}
			// write output
			_, err := output.WriteRune(letter)
			if err != nil {
				log.Panic(err)
			}
		}

	} else { // translate English to isBraille
		// to keep status if the number is encountered
		numFlag := false

		for _, letter := range *input {
			// check if the letter is number
			if letter > 47 && letter < 58 { // check if letter is in between 0 - 9
				if !numFlag {
					// set num flag and print the value of braille Num value
					numFlag = true
					output.WriteString(".O.OOO") // print number follows for first number
				}
			}

			// check for capital letter
			if letter > 64 && letter < 91 { // check if letter is in between A - Z
				output.WriteString(".....O") // print capital follows for letter
				// add 32 to the capital letter of rune value to convert it to small letter
				letter += 32
			}

			if letter == 32 { // for each space reset num flag
				numFlag = false
			}
			// write output
			output.WriteString(englishToBrailleMap[letter])
		}
	}
	// write output to console
	fmt.Println(output.String())
}
