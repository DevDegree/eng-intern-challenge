
# define a map for braille to english
BRAILLE_TO_ENGLISH = {
    # letters
    "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D",
    "O..O..": "E", "OOO...": "F", "OOOO..": "G", "O.OO..": "H",
    ".OO...": "I", ".OOO..": "J", "O...O.": "K", "O.O.O.": "L",
    "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O", "OOO.O.": "P",
    "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
    "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X",
    "OO.OOO": "Y", "O..OOO": "Z",

    # symbols
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", 
    "..OOO.": "!", "..OO..": ":", "..O.O.": ";",
    "....OO": "-", ".O..O.": "/", ".OO..O": "<",  
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")",   
    
    # special
    "......": "space", ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number"
}

# define a map for english to braille
ENGLISH_TO_BRAILLE = {BRAILLE_TO_ENGLISH[braille]: braille for braille in BRAILLE_TO_ENGLISH}
# special case because there is a symbol that shares the same.
ENGLISH_TO_BRAILLE['O'] = 'O..OO.'

# define a map for braille to number
BRAILLE_TO_NUMBER = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4',
    "O..O..": '5', "OOO...": '6', "OOOO..": '7', "O.OO..": '8',
    ".OO...": '9', ".OOO..": '0'
}

# define a map for number to braille
NUMBER_TO_BRAILLE = {BRAILLE_TO_NUMBER[braille]: braille for braille in BRAILLE_TO_NUMBER}