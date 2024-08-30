# assume input is not an empty string and no mix of special symbols only spacing
def is_braille(s):
    # check if the string can be split into chunks of 6 characters each
    if len(s) % 6 != 0:
        return False
    
    # check if each chunk contains only valid Braille characters: dots (•) and spaces
    for i in range(0, len(s), 6):
        segment = s[i:i+6]
        if not all(c == 'O' or c == '.' or c == ' ' for c in segment):
            return False

    return True

def braille2eng(s):
    """
    Translate the input from Braille to English.
    """
    # split the input string into chunks of 6 characters each
    s2 = [s[i:i+6] for i in range(0, len(s), 6)]

    letter_mapping = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z'
    }
    
    number_mapping = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    }
    
    symbol_mapping = {
        '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':',
        '..O.O.': ';', '.....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>',
        'O.O..O': '(', '.O.OO.': ')', '......': ' '
    }
    
    # switch modes
    cap_fw = '.....O'   # capital letter indicator
    num_fw = '.O.OOO'   # number indicator

    res = ''
    num_mode = False  # flag to handle number mode
    cap_mode = False  # flag to handle capitalization mode

    for braille_char in s2:
        if braille_char == num_fw:
            num_mode = True # turn on number mode
        elif braille_char == cap_fw:
            cap_mode = True # turn on cap mode
        else:
            if num_mode:
                if braille_char in number_mapping:
                    res += number_mapping[braille_char]
                elif braille_char == '......':
                    res += ' ' # undefined sequence in number mode
                # exit number mode on space (explicit check)
                if braille_char == '......':
                    num_mode = False
            else:
                if braille_char in letter_mapping:
                    if cap_mode:
                        res += letter_mapping[braille_char].upper()
                        cap_mode = False # turn off cap mode after one capital letter
                    else:
                        res += letter_mapping[braille_char]
                elif braille_char in symbol_mapping:
                    res += symbol_mapping[braille_char]
                else:
                    res += ' ' # undefined sequence for letters and symbols, not assumed
                    
                # exit number mode on space (in non-number sequence path)
                if braille_char == '......':
                    num_mode = False
        
    return res

def eng2braille(s):
    """
    Translate the input from English to Braille.
    """
    letter_mapping = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO',
        'A': '.....O' + 'O.....', 'B': '.....O' + 'O.O...', 'C': '.....O' + 'OO....',
        'D': '.....O' + 'OO.O..', 'E': '.....O' + 'O..O..', 'F': '.....O' + 'OOO...',
        'G': '.....O' + 'OOOO..', 'H': '.....O' + 'O.OO..', 'I': '.....O' + '.OO...',
        'J': '.....O' + '.OOO..', 'K': '.....O' + 'O...O.', 'L': '.....O' + 'O.O.O.',
        'M': '.....O' + 'OO..O.', 'N': '.....O' + 'OO.OO.', 'O': '.....O' + 'O..OO.',
        'P': '.....O' + 'OOO.O.', 'Q': '.....O' + 'OOOOO.', 'R': '.....O' + 'O.OOO.',
        'S': '.....O' + '.OO.O.', 'T': '.....O' + '.OOOO.', 'U': '.....O' + 'O...OO',
        'V': '.....O' + 'O.O.OO', 'W': '.....O' + '.OOO.O', 'X': '.....O' + 'OO..OO',
        'Y': '.....O' + 'OO.OOO', 'Z': '.....O' + 'O..OOO',
    }

    number_mapping = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

    symbol_mapping = {
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
        ';': '..O.O.', '-': '.....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
        '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
    }

    # switch modes
    cap_fw = '.....O'   # capital letter indicator
    num_fw = '.O.OOO'   # number indicator

    res = ''
    num_mode = False  # flag to handle number mode

    for char in s:
        if char.isdigit():
            if not num_mode:
                res += num_fw  # turn on number mode
                num_mode = True
            res += number_mapping[char]
        else:
            if num_mode:
                num_mode = False  # turn off number mode
            if char in letter_mapping:
                res += letter_mapping[char]
            elif char in symbol_mapping:
                res += symbol_mapping[char]
            else:
                res += '......'  # space
    
    return res

if __name__ == "__main__":
    import sys
    s = sys.argv[1:]
    s = ' '.join(s)

    if is_braille(s):
        output = braille2eng(s)
    else:
        output = eng2braille(s)

    print(output)