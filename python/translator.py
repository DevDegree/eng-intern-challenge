import sys

# braille dictionary to have letters correspond to braille sequence
braille_dict = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO',
        'capital': '.....O', # capitaal Signifier
        'number': '.O.OOO',  # number Signifier
        ' ': '......',  # space
        '0': '.O.O..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
        '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
        '8': 'O.OO..', '9': '.OO...'
    }

# reverses braille dictionary to have braille sequences correspond to english equivalent
english_dict = {v: k for k, v in braille_dict.items()}  

def english_to_braille(text):
    """
    Translates English text to braille string

    text: String
    """
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit() and not number_mode:
            result.append(braille_dict['number'])  # charaaacter is a num
            number_mode = True
        elif char.isalpha() and number_mode:
            number_mode = False
        
        if char.isupper():
            result.append(braille_dict['capital'])  # chaaracter needs to be capitalized
            result.append(braille_dict[char.lower()])
        elif char == " ":
            result.append(braille_dict[' '])  # spaace
        else:
            result.append(braille_dict[char])
    
    return ''.join(result)

def braille_to_english(braille):
    """
    Translates braille string to English text

    braille: String
    """
    result = []
    i = 0
    number_mode = False
    capital_mode = False
    
    while i < len(braille):
        braille_char = braille[i:i+6]

        # checks for signifiers (i.e. next character is a capital or number)
        if braille_char == braille_dict['capital']:
            capital_mode = True
            i += 6
            continue
        elif braille_char == braille_dict['number']:
            number_mode = True
            i += 6
            continue
        

        if number_mode:
            result.append(str(english_dict[braille_char]))
            number_mode = False                 # resets after appending num
        elif capital_mode:
            result.append(english_dict[braille_char].upper())
            capital_mode = False                # resets after appending caapital
        else:
            result.append(english_dict[braille_char])
        
        i += 6
    
    return ''.join(result)

def detect_and_translate(input_str):
    """
    Detects whether string is english and needs to be translated to braille or 
    is braille and needs to be translated to english

    input_str: String
    """
    if all(c in "O." for c in input_str) and len(input_str) % 6 == 0:
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide string to translate.")
        sys.exit(1)

    # remove script name & join arguments
    input_str = ' '.join(sys.argv[1:])
    
    # call translator
    detect_and_translate(input_str)