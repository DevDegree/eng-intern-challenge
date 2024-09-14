package helpers

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsLatin(t *testing.T) {

	t.Run("catch non alphabetic strings", func(t *testing.T) {
		invalidCases := []string{".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..", ".O.OOOOO.O..O.O...", "😭😭😭"}
		for _, invalidCase := range invalidCases {
			assert.False(t, IsLatin(invalidCase))
		}
	})
	t.Run("latin looks right", func(t *testing.T) {
		validCases := []string{"abc", "ced", "lmao", "hello! how are. you, :????", "aha ;3", "Wow"}
		for _, validCase := range validCases {
			assert.True(t, IsLatin(validCase))
		}

	})

}

func TestIsBraille(t *testing.T) {
	t.Run("catch non braille strings", func(t *testing.T) {
		invalidCases := []string{"oooo..oi", "oooooooOOO.", "OOO.."}
		for _, invalidCase := range invalidCases {
			assert.False(t, IsBraille(invalidCase))
		}
	})
	t.Run("braille looks right", func(t *testing.T) {
		validCases := []string{".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..", ".O.OOOOO.O..O.O..."}
		for _, validCase := range validCases {
			assert.True(t, IsBraille(validCase))
		}
	})
}
