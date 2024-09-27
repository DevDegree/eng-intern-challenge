import sys

def is_braille(string):
    english_char = False
    for c in string:
        if c != 'O' and c != '.':
            english_char = True
            break
    if english_char:
        print(to_braille(string))
    else:
        print(to_english(string))

def to_english(string):
    BRAILLE_ENGLISH_LETTER_MAP = {
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
        "..OO.O": '.',
        "..O...": ',',
        "..O.OO": '?',
        "..OO..": ':',
        "..O.O.": ';',
        "....OO": '-',
        ".O..O.": '/',
        ".OO..O": '<',
        "O.O..O": '(',
        ".O.OO.": ')',
        "......": ' '
}
    BRAILLE_ENGLISH_NUMBER_MAP = {
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
        "..O...": ',',
        "..O.OO": '?',
        "..OO..": ':',
        "..O.O.": ';',
        "....OO": '-',
        ".O..O.": '/',
        ".OO..O": '<',
        "O..OO.": '>',
        "O.O..O": '(',
        ".O.OO.": ')',
        "......": ' '
    }
    CAPITAL_FOLLOWS = ".....O"
    DECIMAL_FOLLOWS = ".O...O"
    NUMBER_FOLLOWS = ".O.OOO"
    SPACE = "......"
    english_str = ''
    number_mode = False
    capital_mode = False
    for i in range(6, len(string) + 1, 6):
        if i == len(string):
            curr_c = string[i - 6:]
        else:
            curr_c = string[i - 6: i]
        if curr_c == CAPITAL_FOLLOWS:
            capital_mode = True
        elif capital_mode:
            english_str += (BRAILLE_ENGLISH_LETTER_MAP[curr_c]).upper()
            capital_mode = False
        elif number_mode:
            if curr_c == SPACE:
                number_mode = False
                english_str += ' '
            elif curr_c == DECIMAL_FOLLOWS:
                english_str += '.'
            else: 
                english_str += BRAILLE_ENGLISH_NUMBER_MAP[curr_c]
        elif curr_c == NUMBER_FOLLOWS:
            number_mode = True
        else:
            english_str += BRAILLE_ENGLISH_LETTER_MAP[curr_c]
    return english_str
        
def to_braille(string):
    ENGLISH_BRAILLE_MAP = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        '.': '..OO.O',
        ',': '..O...',
        '?': '..O.OO',
        ':': '..OO..',
        ';': '..O.O.',
        '-': '....OO',
        '/': '.O..O.',
        '<': '.OO..O',
        '>': 'O..OO.',
        '(': 'O.O..O',
        ')': '.O.OO.',
        ' ': '......',
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..'
}
    CAPITAL_FOLLOWS = ".....O"
    DECIMAL_FOLLOWS = ".O...O"
    NUMBER_FOLLOWS = ".O.OOO"
    SPACE = "......"
    braille_str = ''
    number_mode = False

    for i in range(len(string)):
        if string[i] == ' ':
            number_mode = False
        elif string[i].isnumeric() and not number_mode:
            braille_str += NUMBER_FOLLOWS
            number_mode = True
        elif string[i].isupper():
            braille_str += CAPITAL_FOLLOWS
        elif number_mode and string[i] == '.':
            braille_str += DECIMAL_FOLLOWS
            continue
        braille_str += ENGLISH_BRAILLE_MAP[string[i].lower()]
    return braille_str

if __name__ == "__main__":
    args = sys.argv[1:]
    input = ' '.join(args)
    is_braille(input)
