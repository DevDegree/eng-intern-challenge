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
