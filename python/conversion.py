
# Number positions are:
#  1 4 
#  2 5
#  3 6

# Using information from https://www.pharmabraille.com/pharmaceutical-braille/the-braille-alphabet/
braille_to_letters = {
    1 : 'a',
    12 : 'b',
    14: 'c',
    145: 'd',
    15: 'e',
    124: 'f',
    1245: 'g',
    125: 'h',
    24: 'i',
    245: 'j',
    13: 'k',
    123: 'l',
    134: 'm',
    1345: 'n',
    135: 'o',
    1234: 'p',
    12345: 'q',
    1235: 'r',
    234: 's',
    2345: 't',
    136: 'u',
    1236: 'v',
    2456: 'w',
    1346: 'x',
    13456: 'y',
    1356: 'z',
    256: '.',
    2: ',',
    236: '?',
    235: '!',
    25: ':',
    23: ';',
    36: '-',
    34: '/',
    246: '<',
    135: '>',
    126: '(',
    345: ')'
}

letters_to_braille = {}

def charToBraille(c):
    pass