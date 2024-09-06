package braille

type symbol struct {
	kind    symbolKind
	braille string
	english rune
}

type symbolKind int

const (
	symbolKindUnknown symbolKind = iota
	symbolKindNumberFollows
	symbolKindCapitalFollows
	symbolKindSpace
	symbolKindDigit
	symbolKindLetter
)

var (
	alphabet = [...]symbol{
		{kind: symbolKindNumberFollows, braille: ".O.OOO"},
		{kind: symbolKindCapitalFollows, braille: ".....O"},
		{kind: symbolKindSpace, braille: "......", english: ' '},
		{kind: symbolKindDigit, braille: "O.....", english: '1'},
		{kind: symbolKindDigit, braille: "O.O...", english: '2'},
		{kind: symbolKindDigit, braille: "OO....", english: '3'},
		{kind: symbolKindDigit, braille: "OO.O..", english: '4'},
		{kind: symbolKindDigit, braille: "O..O..", english: '5'},
		{kind: symbolKindDigit, braille: "OOO...", english: '6'},
		{kind: symbolKindDigit, braille: "OOOO..", english: '7'},
		{kind: symbolKindDigit, braille: "O.OO..", english: '8'},
		{kind: symbolKindDigit, braille: ".OO...", english: '9'},
		{kind: symbolKindDigit, braille: ".OOO..", english: '0'},
		{kind: symbolKindLetter, braille: "O.....", english: 'a'},
		{kind: symbolKindLetter, braille: "O.O...", english: 'b'},
		{kind: symbolKindLetter, braille: "OO....", english: 'c'},
		{kind: symbolKindLetter, braille: "OO.O..", english: 'd'},
		{kind: symbolKindLetter, braille: "O..O..", english: 'e'},
		{kind: symbolKindLetter, braille: "OOO...", english: 'f'},
		{kind: symbolKindLetter, braille: "OOOO..", english: 'g'},
		{kind: symbolKindLetter, braille: "O.OO..", english: 'h'},
		{kind: symbolKindLetter, braille: ".OO...", english: 'i'},
		{kind: symbolKindLetter, braille: ".OOO..", english: 'j'},
		{kind: symbolKindLetter, braille: "O...O.", english: 'k'},
		{kind: symbolKindLetter, braille: "O.O.O.", english: 'l'},
		{kind: symbolKindLetter, braille: "OO..O.", english: 'm'},
		{kind: symbolKindLetter, braille: "OO.OO.", english: 'n'},
		{kind: symbolKindLetter, braille: "O..OO.", english: 'o'},
		{kind: symbolKindLetter, braille: "OOO.O.", english: 'p'},
		{kind: symbolKindLetter, braille: "OOOOO.", english: 'q'},
		{kind: symbolKindLetter, braille: "O.OOO.", english: 'r'},
		{kind: symbolKindLetter, braille: ".OO.O.", english: 's'},
		{kind: symbolKindLetter, braille: ".OOOO.", english: 't'},
		{kind: symbolKindLetter, braille: "O...OO", english: 'u'},
		{kind: symbolKindLetter, braille: "O.O.OO", english: 'v'},
		{kind: symbolKindLetter, braille: ".OOO.O", english: 'w'},
		{kind: symbolKindLetter, braille: "OO..OO", english: 'x'},
		{kind: symbolKindLetter, braille: "OO.OOO", english: 'y'},
		{kind: symbolKindLetter, braille: "O..OOO", english: 'z'},
	}
	numberFollowsSymbol  = alphabet[0]
	capitalFollowsSymbol = alphabet[1]
	spaceSymbol          = alphabet[2]
	digitSymbols         = alphabet[3:13]
	letterSymbols        = alphabet[13:]
)
