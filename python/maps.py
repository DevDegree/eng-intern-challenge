braille_to_escape_characters = {
    '......':' ',
    '.....O':'cap',
    '.O.OOO':'num'
}

braille_to_alphabet = {
    'O.....':'a',
    'O.O...':'b',
    'OO....':'c',
    'OO.O..':'d',
    'O..O..':'e',
    'OOO...':'f',
    'OOOO..':'g',
    'O.OO..':'h',
    '.OO...':'i',
    '.OOO..':'j',
    'O...O.':'k',
    'O.O.O.':'l',
    'OO..O.':'m',
    'OO.OO.':'n',
    'O..OO.':'o',
    'OOO.O.':'p',
    'OOOOO.':'q',
    'O.OOO.':'r',
    '.OO.O.':'s',
    '.OOOO.':'t',
    'O...OO':'u',
    'O.O.OO':'v',
    '.OOO.O':'w',
    'OO..OO':'x',
    'OO.OOO':'y',
    'O..OOO':'z'
}

braille_to_number = {
    'O.....':'1',
    'O.O...':'2',
    'OO....':'3',
    'OO.O..':'4',
    'O..O..':'5',
    'OOO...':'6',
    'OOOO..':'7',
    'O.OO..':'8',
    '.OO...':'9',
    '.OOO..':'0'
}

escape_characters_to_braille = {value: key for key, value in braille_to_escape_characters.items()}

alphabet_to_braille = {value: key for key, value in braille_to_alphabet.items()}

number_to_braille = {value: key for key, value in braille_to_number.items()}