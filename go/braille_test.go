package main

import "testing"

func TestIsBraille(t *testing.T) {
	brailles := []string{"", ".", "O", "..", ".O", "O.", "OO", ".O.", "..O"}
	for _, braille := range brailles {
		if !isBraille(braille) {
			t.Errorf("isBraille rejected valid Braille string %s", braille)
		}
	}

	notBrailles := []string{"x", ".x", "x.", "Ox", "xO",
		".....OO.....O.O...OO...........O.OOOO..DEADBEEF...O.O...OO..........OO..OO.....OOO.OOOO..OOO"}
	for _, notBraille := range notBrailles {
		if isBraille(notBraille) {
			t.Errorf("isBraille accepted invalid Braille string %s", notBraille)
		}
	}
}

func TestDecode(t *testing.T) {
	inExpect := map[string]string{
		"":                               "",
		"O.....":                         "a",
		".....OO...........O.O...":       "A b",
		".O.OOOO.....O.O.........O.....": "12 a",
	}
	for in, expect := range inExpect {
		out, err := decode(in)
		if err != nil {
			t.Fatal(err)
		}
		if out != expect {
			t.Errorf("decode(%s) returned %s; wanted %s", in, out, expect)
		}
	}
}

func TestSplitCells(t *testing.T) {
	inExpect := map[string][]string{
		"":                   {},
		"O.....O.O...":       {"O.....", "O.O..."},
		"OO....OO.O..O..O..": {"OO....", "OO.O..", "O..O.."},
	}
	for in, expect := range inExpect {
		out, err := splitCells(in)
		if err != nil {
			t.Fatal(err)
		}
		if !sliceEq(out, expect) {
			t.Errorf("splitCells(%s) returned %v; wanted %v", in, out, expect)
		}
	}

	invalids := []string{"..xx..", "OOOOOO....."}
	for _, invalid := range invalids {
		if _, err := splitCells(invalid); err == nil {
			t.Errorf("splitCells accepted invalid Braille string %s; wanted error", invalid)
		}
	}
}

type decodeAlphanumericParams struct {
	cell            string
	capital, number bool
}

func TestDecodeAlphaNumeric(t *testing.T) {
	inExpect := map[decodeAlphanumericParams]byte{
		{"O.....", false, false}: 'a',
		{"O.....", true, false}:  'A',
		{"O.....", false, true}:  '1',
		{"O.....", true, true}:   '1',
	}
	for in, expect := range inExpect {
		out, err := decodeAlphanumeric(in.cell, in.capital, in.number)
		if err != nil {
			t.Fatal(err)
		}
		if out != expect {
			t.Errorf("decodeAlphanumeric(%v) returned %c; wanted %c", in, out, expect)
		}
	}

	invalids := []string{capitalFollows, numberFollows, space, ".O.O.", ".O.O.O."}
	for _, invalid := range invalids {
		if _, err := decodeAlphanumeric(invalid, false, false); err == nil {
			t.Errorf("decodeAlphanumeric accepted non-alphanumeric cell %s; wanted error", invalid)
		}
	}
}

// sliceEq returns true if s1 and s2 are the same length and contain the same elements.
func sliceEq[E comparable](s1, s2 []E) bool {
	if len(s1) != len(s2) {
		return false
	}
	for i := range s1 {
		if s1[i] != s2[i] {
			return false
		}
	}
	return true
}
