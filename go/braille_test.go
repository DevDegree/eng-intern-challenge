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
