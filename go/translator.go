package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
)

const (
	// Non-alphanumeric Braille cells.
	capitalFollows = ".....O"
	numberFollows  = ".O.OOO"
	space          = "......"
)

var braillePattern = regexp.MustCompile("(?m)^[O.]*$")

func main() {
	if len(os.Args) < 2 {
		return
	}
	if isBraille(os.Args[1]) {
		english, err := decode(strings.Join(os.Args[1:], ""))
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(english)
	} else { // Input is English.
		braille, err := encode(strings.Join(os.Args[1:], " "))
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(braille)
	}
}

// isBraille returns true if str is a valid Braille string. A valid Braille string
// contains only 'O' (uppercase letter O), and '.' (period) characters.
func isBraille(str string) bool {
	return braillePattern.MatchString(str)
}

// decode converts a Braille string to English. braille must contain only 'O' (uppercase
// letter O), and '.' (period) characters.
func decode(braille string) (string, error) {
	cells, err := splitCells(braille)
	if err != nil {
		return "", err
	}

	english := make([]byte, 0, len(cells))

	capital := false // Next character is capitalized.
	number := false  // Next character is a number.

	for _, cell := range cells {
		switch cell {
		case capitalFollows:
			capital = true
		case numberFollows:
			number = true
		case space:
			capital = false
			number = false
			english = append(english, ' ')
		default:
			enChar, err := decodeAlphanumeric(cell, capital, number)
			if err != nil {
				return "", err
			}
			english = append(english, enChar)
		}
	}

	return string(english), nil
}

// encode converts an English string to Braille. english must contain only a-z, A-Z, 0-9,
// and ' ' (space) characters. If english contains any other characters, encode returns
// ErrInvalidChar.
func encode(english string) (string, error) {
	// TODO
	return "", nil
}

// splitCells breaks a Braille string into individual cells, 3x2 dot matrices of 'O'
// (uppercase letter O) and '.' (period) characters. If braille contains any other
// characters, or if braille does not divide evenly into cells, splitCells returns
// ErrInvalidCell.
func splitCells(braille string) ([]string, error) {
	// TODO
	return nil, nil
}

// decodeAlphanumeric converts a single Braille cell to an English character. If
// capital is true, cell is interpreted as a capital letter. If number is true, cell
// is interpreted as a number. If both capital and number are true, capital is ignored
// and cell is interpreted as a number. If cell is anything other than a letter or a
// number, decodeAlphanumeric returns ErrInvalidCell.
func decodeAlphanumeric(cell string, capital, number bool) (byte, error) {
	// TODO
	return 0, nil
}
