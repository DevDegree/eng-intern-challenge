package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
	"unicode"
)

const (
	// Number of dots per Braille cell.
	dotsPerCell = 3 * 2

	// Non-alphanumeric Braille cells.
	capitalFollows = ".....O"
	numberFollows  = ".O.OOO"
	space          = "......"
)

var (
	braillePattern = regexp.MustCompile("(?m)^[O.]*$")

	// Braille cell -> English letter.
	letters = map[string]byte{
		"O.....": 'a',
		"O.O...": 'b',
		"OO....": 'c',
		"OO.O..": 'd',
		"O..O..": 'e',
		"OOO...": 'f',
		"OOOO..": 'g',
		"O.OO..": 'h',
		".OO...": 'i',
		".OOO..": 'j',
		"O...O.": 'k',
		"O.O.O.": 'l',
		"OO..O.": 'm',
		"OO.OO.": 'n',
		"O..OO.": 'o',
		"OOO.O.": 'p',
		"OOOOO.": 'q',
		"O.OOO.": 'r',
		".OO.O.": 's',
		".OOOO.": 't',
		"O...OO": 'u',
		"O.O.OO": 'v',
		".OOO.O": 'w',
		"OO..OO": 'x',
		"OO.OOO": 'y',
		"O..OOO": 'z',
	}

	// Braille cell -> number.
	numbers = map[string]byte{
		"O.....": '1',
		"O.O...": '2',
		"OO....": '3',
		"OO.O..": '4',
		"O..O..": '5',
		"OOO...": '6',
		"OOOO..": '7',
		"O.OO..": '8',
		".OO...": '9',
	}
)

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
	chars := []byte(english)
	braille := make([]byte, 0, len(chars)*dotsPerCell)
	for len(chars) > 0 {
		c := chars[0]
		if unicode.IsDigit(rune(c)) {
			braille = append(braille, encodeNumber(&chars)...)
		} else if unicode.IsLetter(rune(c)) {
			braille = append(braille, encodeLetter(c)...)
			chars = chars[1:]
		} else if c == ' ' {
			braille = append(braille, space...)
			chars = chars[1:]
		} else {
			return "", ErrInvalidChar{c}
		}
	}
	return string(braille), nil
}

// encodeNumber converts decimal digits from the start of english to Braille and
// trims the digits from the start of english. If the number is followed by a letter,
// a space is added to the returned Braille string to terminate the number.
func encodeNumber(english *[]byte) (braille []byte) {
	// TODO
	return nil
}

// encodeLetter converts an English letter to Braille. If letter is capital, the
// returned Braille string will start with a `number follows' cell.
func encodeLetter(letter byte) (braille []byte) {
	// TODO
	return nil
}

// splitCells breaks a Braille string into individual cells, 3x2 dot matrices of 'O'
// (uppercase letter O) and '.' (period) characters. If braille contains any other
// characters, or if braille does not divide evenly into cells, splitCells returns
// ErrInvalidCell.
func splitCells(braille string) ([]string, error) {
	cells := make([]string, 0, len(braille)%dotsPerCell)
	for len(braille) >= dotsPerCell {
		cell := braille[:dotsPerCell]
		if !isBraille(cell) {
			return cells, ErrInvalidCell{cell}
		}
		cells = append(cells, cell)
		braille = braille[dotsPerCell:]
	}
	if len(braille) > 0 { // Trailing partial cell.
		return cells, ErrInvalidCell{braille}
	}
	return cells, nil
}

// decodeAlphanumeric converts a single Braille cell to an English character. If
// capital is true, cell is interpreted as a capital letter. If number is true, cell
// is interpreted as a number. If both capital and number are true, capital is ignored
// and cell is interpreted as a number. If cell is anything other than a letter or a
// number, decodeAlphanumeric returns ErrInvalidCell.
func decodeAlphanumeric(cell string, capital, number bool) (byte, error) {
	if number {
		return decodeNumeric(cell)
	}
	return decodeAlpha(cell, capital)
}

// decodeNumeric converts a single Braille cell to a numeric character (0-9), or returns
// ErrInvalidCell if cell is not a Braille number.
func decodeNumeric(cell string) (byte, error) {
	if c, ok := numbers[cell]; ok {
		return c, nil
	}
	return 0, ErrInvalidCell{cell}
}

// decodeAlpha converts a single Braille cell to an English letter or returns
// ErrInvalidCell if cell is not a Braille letter. If capital is true, the uppercase form
// of the letter is returned.
func decodeAlpha(cell string, capital bool) (byte, error) {
	c, ok := letters[cell]
	if !ok {
		return 0, ErrInvalidCell{cell}
	}
	if capital {
		c = byte(unicode.ToUpper(rune(c)))
	}
	return c, nil
}

type ErrInvalidCell struct {
	cell string
}

func (e ErrInvalidCell) Error() string {
	return fmt.Sprintf("invalid Braille cell: %s", e.cell)
}

type ErrInvalidChar struct {
	c byte
}

func (e ErrInvalidChar) Error() string {
	return fmt.Sprintf("invalid English character: %c", e.c)
}