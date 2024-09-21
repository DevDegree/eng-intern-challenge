package main

// Struct to represent translation state
type Translator struct {
	AlphaE2B    map[rune]string
	NumberE2B   map[rune]string
	PunctE2B    map[rune]string
	AlphaB2E    map[string]rune
	NumberB2E   map[string]rune
	PunctB2E    map[string]rune
	Symbols     map[rune]string
	taskMap     map[string]func(rune) string // Task map for different scenarios
	numberMode  bool
	capitalMode bool
}
