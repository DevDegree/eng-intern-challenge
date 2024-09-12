// translator converts Braille to English and vice versa. The string to translate is
// passed as command-line arguments. Braille is represented as 'O' (uppercase letter O),
// and '.' (period) characters. Cells are read left to right, line by line, starting from
// the top left. Only roman characters (a-z, A-Z), numbers (0-9), and spaces (' ') are
// supported.
package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"slices"
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

	// Alphabetical Braille cells.
	letters = []string{
		"O.....", // a
		"O.O...", // b
		"OO....", // c
		"OO.O..", // ...
		"O..O..",
		"OOO...",
		"OOOO..",
		"O.OO..",
		".OO...",
		".OOO..",
		"O...O.",
		"O.O.O.",
		"OO..O.",
		"OO.OO.",
		"O..OO.",
		"OOO.O.",
		"OOOOO.",
		"O.OOO.",
		".OO.O.",
		".OOOO.",
		"O...OO",
		"O.O.OO",
		".OOO.O",
		"OO..OO",
		"OO.OOO",
		"O..OOO", // z
	}

	// Numeric Braille cells.
	numbers = []string{
		".OOO..", // 0
		"O.....", // 1
		"O.O...", // 2
		"OO....", // ...
		"OO.O..",
		"O..O..",
		"OOO...",
		"OOOO..",
		"O.OO..",
		".OO...", // 9
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
			capital = false
		}
	}

	return string(english), nil
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
		return decodeNumber(cell)
	}
	return decodeLetter(cell, capital)
}

// decodeNumber converts a single Braille cell to a numeric character (0-9), or returns
// ErrInvalidCell if cell is not a Braille number.
func decodeNumber(cell string) (byte, error) {
	if i := slices.Index(numbers, cell); i >= 0 {
		return byte('0' + i), nil
	}
	return 0, ErrInvalidCell{cell}
}

// decodeLetter converts a single Braille cell to an English letter or returns
// ErrInvalidCell if cell is not a Braille letter. If capital is true, the uppercase form
// of the letter is returned.
func decodeLetter(cell string, capital bool) (byte, error) {
	i := slices.Index(letters, cell)
	if i < 0 {
		return 0, ErrInvalidCell{cell}
	}
	c := byte('a' + i)
	if capital {
		c = byte(unicode.ToUpper(rune(c)))
	}
	return c, nil
}

// encode converts an English string to Braille. english must contain only a-z, A-Z, 0-9,
// and ' ' (space) characters. If english contains any other characters, encode returns
// ErrInvalidChar.
func encode(english string) (string, error) {
	chars := []byte(english)
	braille := make([]byte, 0, len(chars)*dotsPerCell)
	var cells []byte

	for len(chars) > 0 {
		c := chars[0]
		if unicode.IsDigit(rune(c)) {
			chars, cells = encodeNumber(chars)
			braille = append(braille, cells...)
		} else if unicode.IsLetter(rune(c)) {
			cells, err := encodeLetter(c)
			if err != nil {
				return "", err
			}
			braille = append(braille, cells...)
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

// encodeNumber converts decimal digits from the start of english to Braille and trims the
// digits from the start of english. If the number is followed by a letter, a space is
// added to the Braille string to terminate the number.
func encodeNumber(english []byte) (trimmedEnglish, braille []byte) {
	if len(english) <= 0 || !unicode.IsDigit(rune(english[0])) {
		return english, []byte{}
	}

	braille = []byte(numberFollows)
	for len(english) > 0 && unicode.IsDigit(rune(english[0])) {
		braille = append(braille, numbers[english[0]-'0']...)
		english = english[1:]
	}
	if len(english) > 0 { // Terminate number with space.
		braille = append(braille, space...)
		if english[0] == ' ' {
			english = english[1:]
		}
	}
	return english, braille
}

// encodeLetter converts an English letter to Braille. If letter is capital, the
// returned Braille string will start with a `capital follows' cell. If letter is
// invalid, encodeLetter returns nil, ErrInvalidChar.
func encodeLetter(letter byte) (braille []byte, err error) {
	if !unicode.IsLetter(rune(letter)) {
		return nil, ErrInvalidChar{letter}
	}

	if unicode.IsUpper(rune(letter)) {
		braille = append(braille, capitalFollows...)
		letter = byte(unicode.ToLower(rune(letter)))
	}
	cell := letters[letter-'a']
	braille = append(braille, cell...)
	return
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
