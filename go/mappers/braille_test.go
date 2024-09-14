package mappers

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBrailleMappings(t *testing.T) {
	// Source of truth for braille to Latin is here
	expectedBrailleToLetters := map[string]rune{
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
	expectedBrailleToNumbers := map[string]rune{
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
	}
	expectedBrailleToPunctuation := map[string]rune{
		"..OO.O": '.',
		"..O...": ',',
		"..O.OO": '?',
		"..OOO.": '!',
		"..OO..": ':',
		"..O.O.": ';',
		".O..O.": '-',
		".O.O.O": '<',
		"O..OO.": '>',
		"O.O..O": '(',
		".O.OO.": ')',
		"......": ' ',
	}

	assert.Equal(t, expectedBrailleToLetters, BRAILLE_TO_LETTERS, "BRAILLE_TO_LETTERS mapping is incorrect")
	assert.Equal(t, expectedBrailleToNumbers, BRAILLE_TO_NUMBERS, "BRAILLE_TO_NUMBERS mapping is incorrect")
	assert.Equal(t, expectedBrailleToPunctuation, BRAILLE_TO_PUNCTUATION, "BRAILLE_TO_PUNCTUATION mapping is incorrect")
}
