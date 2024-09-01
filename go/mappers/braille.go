package mappers

const (
	BRAILLE_SPACE           = "......"
	BRAILLE_FULLSTOP        = "..OO.O"
	BRAILLE_CAPITAL_FOLLOWS = ".....O"
	BRAILLE_DECIMAL_FOLLOWS = ".O...O"
	BRAILLE_NUMBER_FOLLOWS  = ".O.OOO"
)

var (
	BRAILLE_TO_LETTERS = map[string]rune{
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
	BRAILLE_TO_NUMBERS = map[string]rune{
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
	BRAILLE_TO_PUNCTUATION = map[string]rune{
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
)
