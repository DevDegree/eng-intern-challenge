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
			res, err := translate_from_latin_to_braille(character)
			assert.Nil(t, err)
			assert.Equal(t, mappers.LETTERS_TO_BRAILLE[rune(character[0])], res)
		}

	})
	t.Run("word is correctly translated", func(t *testing.T) {
		word := "hello"
		res, err := translate_from_latin_to_braille(word)
		assert.Nil(t, err)
		assert.Equal(t, "", res)

	})
	t.Run("capitalized word is correctly translated", func(t *testing.T) {
		word := "Hello"
		res, err := translate_from_latin_to_braille(word)
		assert.Nil(t, err)
		assert.Equal(t, "", res)
	})
	t.Run("number is correctly translated", func(t *testing.T) {
		word := "1"
		res, err := translate_from_latin_to_braille(word)
		assert.Nil(t, err)
		assert.Equal(t, "", res)

	})
	t.Run("numbers are correctly translated", func(t *testing.T) {
		word := "123"
		res, err := translate_from_latin_to_braille(word)
		assert.Nil(t, err)
		assert.Equal(t, "", res)

	})
	t.Run("punctuation is correctly translated", func(t *testing.T) {
		word := ",.:;()!?<>"
		res, err := translate_from_latin_to_braille(word)
		assert.Nil(t, err)
		assert.Equal(t, "", res)

	})
	t.Run("string containing punctuation correctly translated", func(t *testing.T) {
		word := "wow!"
		res, err := translate_from_latin_to_braille(word)
		assert.Nil(t, err)
		assert.Equal(t, "", res)
	})
}
