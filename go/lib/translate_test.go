package lib

import (
	"solution/mappers"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTranslateLatinToBraille(t *testing.T) {
	t.Run("one character is translated correctly", func(t *testing.T) {
		characters := []string{"w", "o", "w"}
		for _, character := range characters {
			res, err := translateFromLatinToBraille(character)
			assert.Nil(t, err)
			assert.Equal(t, mappers.LETTERS_TO_BRAILLE[rune(character[0])], res)
		}

	})
	t.Run("word is correctly translated", func(t *testing.T) {
		word := "hello"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, "O.OO..O..O..O.O.O.O.O.O.O..OO.", res)

	})
	t.Run("capitalized word is correctly translated", func(t *testing.T) {
		word := "Hello"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, ".....OO.OO..O..O..O.O.O.O.O.O.O..OO.", res)
	})
	t.Run("number is correctly translated", func(t *testing.T) {
		word := "1"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, ".O.OOOO.....", res)

	})
	t.Run("numbers are correctly translated", func(t *testing.T) {
		word := "42"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, ".O.OOOOO.O..O.O...", res)

	})
	t.Run("decimals are correctly translated", func(t *testing.T) {
		word := "123.12"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, ".O.OOOO.....O.O...OO......OO.OO.....O.O...", res)

	})
	t.Run("punctuation is correctly translated", func(t *testing.T) {
		word := ",.:;()!?<>"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, "..O.....OO.O..OO....O.O.O.O..O.O.OO...OOO...O.OO.O.O.OO..OO.", res)

	})
	t.Run("string containing punctuation correctly translated", func(t *testing.T) {
		word := "wow!"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, ".OOO.OO..OO..OOO.O..OOO.", res)
	})
	t.Run("the whole shebang", func(t *testing.T) {
		word := "wowWow!"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, ".OOO.OO..OO..OOO.O.....O.OOO.OO..OO..OOO.O..OOO.", res)

	})

	t.Run("incorrect number", func(t *testing.T) {
		word := "123."
		res, err := translateFromLatinToBraille(word)
		assert.Equal(t, "", res)
		assert.NotNil(t, err)
	})
	t.Run("incorrect number formatting", func(t *testing.T) {
		word := "123.abc"
		res, err := translateFromLatinToBraille(word)
		assert.Equal(t, "", res)
		assert.NotNil(t, err)
	})
	t.Run("123 works", func(t *testing.T) {
		word := "123"
		res, err := translateFromLatinToBraille(word)
		assert.Nil(t, err)
		assert.Equal(t, ".O.OOOO.....O.O...OO....", res)
	})
}

func TestTranslateBrailleToLatin(t *testing.T) {
	t.Run("the whole shebang backwards", func(t *testing.T) {
		word := ".OOO.OO..OO..OOO.O.....O.OOO.OO..OO..OOO.O..OOO."
		res, err := translateFromBrailleToLatin(word)
		assert.Nil(t, err)
		assert.Equal(t, "wowWow!", res)

	})
	t.Run("numbers work too", func(t *testing.T) {
		word := ".O.OOOO.....O.O...OO...."
		res, err := translateFromBrailleToLatin(word)
		assert.Nil(t, err)
		assert.Equal(t, "123", res)
	})
}

func TestTranslate(t *testing.T) {
	t.Run("chooses the right translation", func(t *testing.T) {
		word1 := "O.OO..O..O..O.O.O.O.O.O.O..OO."
		word2 := "hello"
		res1, err1 := Translate(word1)
		res2, err2 := Translate(word2)

		assert.Nil(t, err1)
		assert.Nil(t, err2)

		assert.Equal(t, "hello", res1)
		assert.Equal(t, "O.OO..O..O..O.O.O.O.O.O.O..OO.", res2)

	})
}
