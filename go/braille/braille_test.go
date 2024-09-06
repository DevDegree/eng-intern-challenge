package braille_test

import (
	"errors"
	"testing"

	"solution/braille"
)

func TestTranslate_braille(t *testing.T) {
	tests := []struct {
		label string
		input string
		want  string
		err   error
	}{
		{"empty", "", "", nil},
		{"space", "......", " ", nil},
		{"letter", "O.....", "a", nil},
		{"capital", ".....OO.....", "A", nil},
		{"bad capital (no letter)", ".....O", "", braille.ErrBadCapital},
		{"bad capital (not letter)", ".....O......", "", braille.ErrBadCapital},
		{"number (single digit)", ".O.OOOO.....", "1", nil},
		{"number (multiple digits)", ".O.OOOO.....O.O...", "12", nil},
		{"bad number (no digit)", ".O.OOO", "", braille.ErrBadNumber},
		{"bad number (not digit)", ".O.OOOO..OOO", "", braille.ErrBadNumber},
		{"mix", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO", "Abc 123 xYz", nil},
	}

	for _, test := range tests {
		got, err := braille.Translate(test.input)
		if got != test.want {
			t.Errorf("[%s]: got: %q, want: %q", test.label, got, test.want)
		}
		if !errors.Is(err, test.err) {
			t.Errorf("[%s]: got err: %v, want err: %v", test.label, err, test.err)
		}
	}
}

func TestTranslate_english(t *testing.T) {
	tests := []struct {
		label string
		input string
		want  string
		err   error
	}{
		{"bad symbol", "À?", "", braille.ErrBadSymbol},
		{"space", " ", "......", nil},
		{"letter", "a", "O.....", nil},
		{"capital", "A", ".....OO.....", nil},
		{"number", "1", ".O.OOOO.....", nil},
		{"mix", "Abc 123 xYz", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO", nil},
	}

	for _, test := range tests {
		got, err := braille.Translate(test.input)
		if got != test.want {
			t.Errorf("[%s]: got: %q, want: %q", test.label, got, test.want)
		}
		if !errors.Is(err, test.err) {
			t.Errorf("[%s]: got err: %v, want err: %v", test.label, err, test.err)
		}
	}
}
