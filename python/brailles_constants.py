LATIN_ENGLISH_ALPHABET= {"OO.OO.": "N", "O..OO.": "O", "OOO.O.": "P",
    "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
    "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X",
    "OO.OOO": "Y", "O..OOO": "Z",
    "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D",
    "O..O..": "E", "OOO...": "F", "OOOO..": "G", "O.OO..": "H",
    ".OO...": "I", ".OOO..": "J", "O...O.": "K", "O.O.O.": "L",
    "OO..O.": "M"
}

ENG_TO_BRAILLE = {v: k for k, v in LATIN_ENGLISH_ALPHABET.items()}

ENG_TO_BRAILLE[" "] = "......"
ENG_TO_BRAILLE["caps"] = ".....O"
ENG_TO_BRAILLE["digit"] = ".O.OOO"
ENG_TO_BRAILLE["deci"] = ".O...O"

NUMERALS = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4',
    "O..O..": '5', "OOO...": '6', "OOOO..": '7', "O.OO..": '8',
    ".OO...": '9', ".OOO..": '0'
}

NUMBER_TO_BRAILLE = {v: k for k, v in NUMERALS.items()}

PUNCTUATED = {'.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')'}

SPECIALLY = {'..OO.O':'.','..O...':',', '..O.OO':'?', '..OOO.':'!', '..OO..':':', '..O.O.':';', '....OO':'-', 
             '.O..O.':'/', '.OO..O':'<', 'O..OO.':'>', 'O.O..O':'(', '.O.OO.':')',  }
