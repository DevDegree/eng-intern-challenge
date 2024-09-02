import sys

def translate_braille_to_english(value):
    #dictionaries to map values from braille to english
    braille_to_english_alpha = {
        'O.....': 'a',
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
    }

    braille_to_english_num = {
        'O.....': '1',
        'O.O...': '2',
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9',
        '.OOO..': '0',
    }

    braille_to_english_commands = {
        '.....O': 'capital_follows',
        '.O.OOO': 'number_follows',
        '......': 'space_follows',
    }

    output = []
    cur_command = ""
    for i in range(0, len(value), 6):
        #get the braille string
        cur_str = value[i:i+6]
        english_val = ""
        #either a command or a letter
        if cur_str in braille_to_english_commands:
            if braille_to_english_commands[cur_str] == 'capital_follows':
                cur_command = 'capital_follows'
            elif braille_to_english_commands[cur_str] == 'number_follows':
                cur_command = 'number_follows'
            elif braille_to_english_commands[cur_str] == 'space_follows':
                english_val += ' '
                cur_command = 'space_follows'
        else:
            if cur_command == 'number_follows':
                english_val += braille_to_english_num[cur_str]
            elif cur_command == 'capital_follows':
                english_val += braille_to_english_alpha[cur_str].upper()
                cur_command = ""
            else:
                english_val += braille_to_english_alpha[cur_str]
        output.append(english_val)

    return ("".join(output))
    
def translate_english_to_braille(value):
    #dictionaries to map values from english to braille
    english_to_braille_alpha = {
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
    }

    english_to_braille_num = {
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        'O': '.OOO..',
    }

    english_to_braille_commands = {
        'capital_follows': '.....O',
        'number_follows': '.O.OOO'
    }

    english_to_braille_space = '......'

    reading_num = False
    output = []
    for c in value:
        braille_val = ""
        #check if character is a number first to handle multiple digit numbers
        if c.isdigit():
            if (reading_num == False):
                braille_val += english_to_braille_commands['number_follows']
                reading_num = True
            braille_val += english_to_braille_num[c]
        else:
            reading_num = False
            if c.isupper():
                braille_val += english_to_braille_commands['capital_follows'] + english_to_braille_alpha[c.lower()]
            elif c.islower():
                braille_val += english_to_braille_alpha[c]  
            elif c == ' ':
                braille_val += english_to_braille_space
        output.append(braille_val)
    
    return ("".join(output))

def translate(value):
    #get all characters in the input
    chars = []
    for c in value:
        if c not in chars:
            chars.append(c)

    #check if input is braille or english
    if (len(chars) == 2 and chars.__contains__('.') and chars.__contains__('O')):
        translation = translate_braille_to_english(value)
    else:
        translation = translate_english_to_braille(value)
        
    #print final translation to output
    print(translation)
#get user input into one string
value = (" ".join(sys.argv[1:]))
#call function to translate
translate(value)

