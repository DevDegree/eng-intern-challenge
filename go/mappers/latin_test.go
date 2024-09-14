package mappers

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLatinMappers(t *testing.T) {
	// Using these mappers as a source of truth
	expectedLettersToBraille := map[rune]string{
		'a': "O.....",
		'b': "O.O...",
		'c': "OO....",
		'd': "OO.O..",
		'e': "O..O..",
		'f': "OOO...",
		'g': "OOOO..",
		'h': "O.OO..",
		'i': ".OO...",
		'j': ".OOO..",
		'k': "O...O.",
		'l': "O.O.O.",
		'm': "OO..O.",
		'n': "OO.OO.",
		'o': "O..OO.",
		'p': "OOO.O.",
		'q': "OOOOO.",
		'r': "O.OOO.",
		's': ".OO.O.",
		't': ".OOOO.",
		'u': "O...OO",
		'v': "O.O.OO",
		'w': ".OOO.O",
		'x': "OO..OO",
		'y': "OO.OOO",
		'z': "O..OOO",
	}
	expectedNumbersToBraille := map[rune]string{
		'1': "O.....",
		'2': "O.O...",
		'3': "OO....",
		'4': "OO.O..",
		'5': "O..O..",
		'6': "OOO...",
		'7': "OOOO..",
		'8': "O.OO..",
		'9': ".OO...",
		'0': ".OOO..",
	}
	expectedPunctuationToBraille := map[rune]string{
		'.': "..OO.O",
		',': "..O...",
		'?': "..O.OO",
		'!': "..OOO.",
		':': "..OO..",
		';': "..O.O.",
		'-': ".O..O.",
		'/': ".O..O.",
		'<': ".O.O.O",
		'>': "O..OO.",
		'(': "O.O..O",
		')': ".O.OO.",
		' ': "......",
	}

	assert.Equal(t, expectedLettersToBraille, LETTERS_TO_BRAILLE, "LETTERS_TO_BRAILLE mapping is incorrect")
	assert.Equal(t, expectedNumbersToBraille, NUMBERS_TO_BRAILLE, "NUMBERS_TO_BRAILLE mapping is incorrect")
	assert.Equal(t, expectedPunctuationToBraille, PUNCTUATION_TO_BRAILLE, "PUNCTUATION_TO_BRAILLE mapping is incorrect")
}
