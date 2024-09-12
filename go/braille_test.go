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
		".....OO.....O.O...OO...........O.OOOO.....O.O...OO....": "Abc 123",
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

func TestDecodeAlphanumeric(t *testing.T) {
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

func TestEncode(t *testing.T) {
	inExpect := map[string]string{
		"":            "",
		"a":           "O.....",
		"ab":          "O.....O.O...",
		"abc":         "O.....O.O...OO....",
		"Hello world": ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..",
		"42":          ".O.OOOOO.O..O.O...",
		"a1":          "O......O.OOOO.....",
		"1a":          ".O.OOOO...........O.....",
	}
	for in, expect := range inExpect {
		out, err := encode(in)
		if err != nil {
			t.Fatal(err)
		}
		if out != expect {
			t.Errorf("encode(%s) returned %s; wanted %s", in, out, expect)
		}
	}
}

func TestEncodeNumber(t *testing.T) {
	inExpect := map[string][2]string{
		"":     {"", ""},
		"123":  {"", ".O.OOOO.....O.O...OO...."},
		"a123": {"a123", ""},
		"123a": {"a", ".O.OOOO.....O.O...OO.........."},
		"123 ": {"", ".O.OOOO.....O.O...OO.........."},
	}
	for in, expect := range inExpect {
		trimmed, braille := encodeNumber([]byte(in))
		if string(trimmed) != expect[0] || string(braille) != expect[1] {
			t.Errorf("encodeNumber(%q) returned %q, %q; wanted %q, %q",
				in, trimmed, braille, expect[0], expect[1])
		}
	}
}

func TestEncodeLetter(t *testing.T) {
	inExpect := map[byte]string{
		'a': "O.....",
		'A': ".....OO.....",
	}
	for in, expect := range inExpect {
		out, err := encodeLetter(in)
		if err != nil {
			t.Fatal(err)
		}
		if string(out) != expect {
			t.Errorf("encodeLetter(%c) returned %s; wanted %s", in, out, expect)
		}
	}

	invalids := []byte{'1', ' ', '<'}
	for _, invalid := range invalids {
		if _, err := encodeLetter(invalid); err == nil {
			t.Errorf("encodeLetter accepted invalid letter %c; wanted error", invalid)
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
