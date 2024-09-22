package main

import (
	"errors"
	"fmt"
	"io"
	"os"
	"strings"
)

type symbol = string

type biMap[K comparable, V comparable] struct {
	encoding   map[K]V
	decoding   map[V]K
	encodeName string
	decodeName string
}

func newBrailleBiMap[K comparable](decoding map[symbol]K, encodeName string) biMap[K, symbol] {
	encoding := make(map[K]symbol, len(decoding))
	for k, v := range decoding {
		encoding[v] = k
	}

	return biMap[K, symbol]{
		encoding:   encoding,
		decoding:   decoding,
		encodeName: encodeName,
		decodeName: "braille symbol",
	}
}

func (bMap biMap[K, V]) encode(key K) (value V, err error) {
	if value, found := bMap.encoding[key]; found {
		return value, nil
	}
	return value, fmt.Errorf("unsupported %s", bMap.encodeName)
}

func (bMap biMap[K, V]) decode(value V) (key K, err error) {
	if key, found := bMap.decoding[value]; found {
		return key, nil
	}
	return key, fmt.Errorf("unsupported %s", bMap.decodeName)
}

type brailleMode int

const (
	brailleModeNone brailleMode = iota
	brailleModeCapital
	brailleModeNumber
)

func (mode brailleMode) String() string {
	switch mode {
	case brailleModeNone:
		return "none"
	case brailleModeCapital:
		return "capital follows"
	case brailleModeNumber:
		return "number follows"
	default:
		return ""
	}
}

type char rune

// toLower returns the lowercase of this char.
// This char must be within 'A' to 'Z'.
func (c char) toLower() char {
	return c + 'a' - 'A'
}

// toUpper returns the uppercase of this char.
// This char must be within 'a' to 'z'.
func (c char) toUpper() char {
	return c + 'A' - 'a'
}

// encode returns the braille mode to insert if any and the braille symbol
// encoded, or an error if the encoding has violated the rules, given isNumber
// which indicates whether a number is being encoded.
func (c char) encode(isNumber bool) (modeToInsert brailleMode, symbol symbol, err error) {
	switch {
	case c >= '0' && c <= '9':
		if !isNumber {
			modeToInsert = brailleModeNumber
		}
		symbol, _ = symbolWithDigit.encode(c)
	case c >= 'A' && c <= 'Z':
		modeToInsert = brailleModeCapital
		c = c.toLower()
		fallthrough
	default:
		if isNumber {
			err = errors.New("number prematurely ended")
		} else {
			symbol, err = symbolWithLetter.encode(c)
		}
	}

	return modeToInsert, symbol, err
}

var symbolWithLetter = newBrailleBiMap(map[string]char{"O.....": 'a',
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
	"......": ' '}, "character")

var symbolWithDigit = newBrailleBiMap(map[symbol]char{
	"O.....": '1',
	"O.O...": '2',
	"OO....": '3',
	"OO.O..": '4',
	"O..O..": '5',
	"OOO...": '6',
	"OOOO..": '7',
	"O.OO..": '8',
	".OO...": '9',
	".OOO..": '0',
	"......": ' ',
}, "character")

var symbolWithMode = newBrailleBiMap(map[symbol]brailleMode{
	".....O": brailleModeCapital,
	".O.OOO": brailleModeNumber,
}, "braille mode")

// decodeMode attempts to decode the given braille symbol into a braille
// mode. If succeeded, updates this brailleMode if it was brailleModeNone
// else returns an error, otherwise returns nil.
func (mode *brailleMode) decodeMode(symbol symbol) error {
	newMode, err := symbolWithMode.decode(symbol)
	if err != nil {
		return nil
	}
	if *mode != brailleModeNone {
		return fmt.Errorf("two consecutive modes: %v, %v", *mode, newMode)
	}
	*mode = newMode
	return nil
}

// decode returns a character by decoding the given braille symbol according
// to this braille mode. This braille mode may be changed after invoking
// this method.
// Returns an error if the given braille symbol cannot be decoded.
func (mode *brailleMode) decode(symbol symbol) (c char, err error) {
	switch *mode {
	case brailleModeCapital:
		if c, err = symbolWithLetter.decode(symbol); err == nil {
			*mode = brailleModeNone
			c = c.toUpper()
		}
	case brailleModeNone:
		c, err = symbolWithLetter.decode(symbol)
	case brailleModeNumber:
		if c, err = symbolWithDigit.decode(symbol); err == nil && c == ' ' {
			*mode = brailleModeNone
		}
	}
	return c, err
}

type BrailleTranslator[WR io.Writer] struct {
	Writer WR
}

// NewBrailleTranslator returns a new BrailleTranslator with the given writer.
func NewBrailleTranslator[WR io.Writer](writer WR) BrailleTranslator[WR] {
	return BrailleTranslator[WR]{Writer: writer}
}

// writeRune writes the given char to the embedded writer.
func (bc BrailleTranslator[WR]) writeRune(c char) error {
	if _, err := bc.Writer.Write([]byte{byte(c)}); err != nil {
		return fmt.Errorf("failed to write rune '%c': %w", c, err)
	}
	return nil
}

// writeSymbol writes the given braille symbol to the embedded writer.
func (bc BrailleTranslator[WR]) writeSymbol(symbol symbol) error {
	if _, err := bc.Writer.Write([]byte(symbol)); err != nil {
		return fmt.Errorf("failed to write string \"%s\": %w", symbol, err)
	}
	return nil
}

// translateBraille translates the given braille to alphanumeric
// characters/spaces and writes to the embedded writer.
// Any IO or malformation error will halt the translation.
func (bc BrailleTranslator[WR]) translateBraille(braille string) (err error) {
	mode := brailleModeNone
	var c char

	for i := 0; i < len(braille); i += 6 {
		if i+6 > len(braille) {
			// malformed braille sequence
			return fmt.Errorf("braille prematurely ended: %s", braille[i:])
		}

		symbol := braille[i : i+6]

		wrapErr := func(e error) error {
			return fmt.Errorf("failed to convert braille symbol \"%s\" at position %d of \"%s\": %w", symbol, i, braille, e)
		}

		oldMode := mode
		if err = mode.decodeMode(symbol); err != nil {
			return wrapErr(err)
		}
		if oldMode != mode {
			continue
		}

		if c, err = mode.decode(symbol); err == nil {
			err = bc.writeRune(c)
		}

		if err != nil {
			return wrapErr(err)
		}
	}

	return nil
}

// translateAlphanumeric translates the given alphanumeric words
// into braille and writes to the embedded writer.
// Any IO or malformation error will halt the translation.
func (bc BrailleTranslator[WR]) translateAlphanumeric(words ...string) (err error) {
	for wordIdx, word := range words {
		// a new word always ends the previous number
		isNumber := false

		if wordIdx > 0 {
			// inserts a space before converting any non-first word
			if err = bc.writeSymbol(symbolWithLetter.encoding[' ']); err != nil {
				return fmt.Errorf("failed to convert character ' ': %w", err)
			}
		}

		for runeOffset, r := range word {
			c := char(r)
			wrapErr := func(e error) error {
				return fmt.Errorf("failed to convert character '%c' at position %d of \"%s\": %w", r, runeOffset, word, e)
			}
			modeToInsert, symbol, err := c.encode(isNumber)
			if err != nil {
				return wrapErr(err)
			}
			switch modeToInsert {
			case brailleModeNumber:
				isNumber = true
				fallthrough
			case brailleModeCapital:
				err = bc.writeSymbol(symbolWithMode.encoding[modeToInsert])
			}
			if err == nil {
				err = bc.writeSymbol(symbol)
			}
			if err != nil {
				return wrapErr(err)
			}
		}
	}

	return nil
}

// Translate translates the given strings from braille to words or vice versa
// and writes the result to the embedded writer based on heuristics.
// Any IO or malformation error will halt the translation.
func (bc BrailleTranslator[WR]) Translate(args ...string) error {
	switch len(args) {
	case 0:
		return errors.New("empty input")
	case 1:
		only := args[0]
		if strings.Contains(only, ".") {
			// assume sane input
			bc.translateBraille(only)
		} else {
			bc.translateAlphanumeric(args...)
		}
	default:
		bc.translateAlphanumeric(args...)
	}

	return nil
}

func main() {
	bc := NewBrailleTranslator(os.Stdout)
	bc.Translate(os.Args[1:]...)
}
