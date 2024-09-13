package dictionary

type Dictionary struct {
	Alphabet  map[string]string
	Numbers   map[string]string
	Symbols   map[string]string
	Modifiers map[string]string
}

// Init initializes the dictionary with the default values - meaning (letter, braille) pairs
func Init() Dictionary {
	return Dictionary{
		Alphabet: map[string]string{
			"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
			"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
			"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
			"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
			"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
			"z": "O..OOO",
		},
		Numbers: map[string]string{
			"0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
			"5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
		},
		Symbols: map[string]string{
			" ": "......",
		},
		Modifiers: map[string]string{
			"capital": ".....O", "decimal": ".O...O", "number": ".O.OOO",
		},
	}
}

// Reverse returns a new dictionary with the keys and values reversed
func (d *Dictionary) Reverse() Dictionary {
	return Dictionary{
		Alphabet:  reverseMap(d.Alphabet),
		Numbers:   reverseMap(d.Numbers),
		Symbols:   reverseMap(d.Symbols),
		Modifiers: reverseMap(d.Modifiers),
	}
}

func reverseMap(m map[string]string) map[string]string {
	output := make(map[string]string)
	for k, v := range m {
		output[v] = k
	}
	return output
}
