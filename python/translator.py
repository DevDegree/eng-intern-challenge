eng_to_bra = {'a': 'O.....',
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
              '1': 'O.....',
              '2': 'O.O...',
              '3': 'OO....',
              '4': 'OO.O..',
              '5': 'O..O..',
              '6': 'OOO...',
              '7': 'OOOO..',
              '8': 'O.OO..',
              '9': '.OO...',
              '0': '.OOO..',
              '.': '..OO.O',
              ',': '..O...',
              '?': '..O.OO',
              '!': '..OOO.',
              ':': '..OO..',
              ';': '..O.O.',
              '-': '....OO',
              '/': '.O..O.',
              '<': '.OO..O',
              '>': 'O..OO.',
              '(': 'O.O..O',
              ')': '.O.OO.',
              ' ': '......'
              }
alpha_bra_to_eng = {'O.....': 'a',
              'O.O...': 'b',
              'OO....': 'c',
              'OO.O..': 'd',
              'O..O..': 'e',
              'OOO...': 'f',
              'OOOO..': 'g',
              'O.OO..': 'h',
              '.OO...': 'i',
              '.OOO..': 'j',
              'O...O.': 'k',
              'O.O.O.': 'l',
              'OO..O.': 'm',
              'OO.OO.': 'n',
              'O..OO.': 'o',
              'OOO.O.': 'p',
              'OOOOO.': 'q',
              'O.OOO.': 'r',
              '.OO.O.': 's',
              '.OOOO.': 't',
              'O...OO': 'u',
              'O.O.OO': 'v',
              '.OOO.O': 'w',
              'OO..OO': 'x',
              'OO.OOO': 'y',
              'O..OOO': 'z',
              '..OO.O': '.',
              '..O...': ',',
              '..O.OO': '?',
              '..OOO.': '!',
              '..OO..': ':',
              '..O.O.': ';',
              '....OO': '-',
              '.O..O.': '/',
              '.OO..O': '<',
              'O..OO.': '>',
              'O.O..O': '(',
              '.O.OO.': ')',
              '......': ' ',}
num_bra_to_eng = {
              'O.....': '1',
              'O.O...': '2',
              'OO....': '3',
              'OO.O..': '4',
              'O..O..': '5',
              'OOO...': '6',
              'OOOO..': '7',
              'O.OO..': '8',
              '.OO...': '9',
              '.OOO..': '0'}

CAPITAL_FOLLOWS = '.....O'
DECIMAL_FOLLOWS = '.O...O'
NUMBER_FOLLOWS = '.O.OOO'

def isEnglish(input_string):
    if(not (all(char in {'.', 'O'} for char in input_string)) and len(input_string) % 6 == 0):
        return True

    for i in range(0, len(input_string), 6):
        letter = input_string[i:i+6]
        if letter not in alpha_bra_to_eng and letter != CAPITAL_FOLLOWS and letter != DECIMAL_FOLLOWS and letter != NUMBER_FOLLOWS:
            return True
    return False

#main program start
input_string = input()

output = ''
if isEnglish(input_string):
    is_number = False
    for c in input_string:
        if c >= 'A' and c <= 'Z':
            output += CAPITAL_FOLLOWS
            c = c.lower()
        elif c == '.':
            output += DECIMAL_FOLLOWS
        elif c >= '0' and c <= '9':
            if not is_number:
                output += NUMBER_FOLLOWS
                is_number = True
        elif c == ' ':
            is_number = False
        #print(eng_to_bra.get(c))
        output += eng_to_bra.get(c)
else:
    is_capital = False
    is_decimal = False
    is_number = False
    for i in range(0, len(input_string), 6):
        cur_seq = input_string[i:i+6]

        if cur_seq == CAPITAL_FOLLOWS:
            is_capital = True
            continue
        elif cur_seq == DECIMAL_FOLLOWS:
            is_decimal = True
            continue
        elif cur_seq == NUMBER_FOLLOWS:
            is_number = True
            continue

        if is_number:
            cur_char = num_bra_to_eng.get(cur_seq)
        else:
            cur_char = alpha_bra_to_eng.get(cur_seq)
        
        if is_capital:
            cur_char = cur_char.capitalize()
            is_capital = False
        elif is_decimal:
            cur_char = '.'
            is_decimal = False
        
        if cur_char == ' ':
            is_number = False
        
        output += cur_char

print(output)
            

#create two maps, 1 -> English to Braille, 2 -> Braille to English
#First assume input is braille
#if we find a 6 letter combo that is not in the Braille alphabet, then we know it is english

#if it is braille, loop through 6 characters at a time and translate using map (take note of capital follows, decimal follows, and numbers follows)
#what is decimal follows??
    
#if it is english, loop through each character at a time and translate using map (take note of capitals, numbers, and spaces)
    
