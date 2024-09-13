
import sys

# Braille to English mapping using "O" and "." for representation
braille_to_english = {
    'O.....': ('a', '1'), 'O.O...': ('b', '2'), 'OO....': ('c', '3'), 'OO.O..': ('d', '4'),
    'O..O..': ('e', '5'), 'OOO...': ('f', '6'), 'OOOO..': ('g', '7'), 'O.OO..': ('h', '8'),
    '.OO...': ('i', '9'), '.OOO..': ('j', '0'), 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm',
    'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's',
    '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.O.O.O': '<', 'O.O.O.': '>',
    'O.O..O': '(', '.O.OO.': ')'
}
# English to Braille mapping
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.O.O.O', '>': 'O.O.O.',
    '(': 'O.O..O', ')': '.O.OO.'
}

"""

When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.

"""

# Indicates that a capital follows
capital_sign = '.....O'  

# Indicates that a number follows
number_sign = '.O.OOO'  

# Indicates that a decimal follows
decimal_sign = '.O...O' 


def to_english(braille_string):
    
    text_output = ''
    braille_chunks = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    
    # Special symbols
    capital_sign = '.....O'
    number_sign = '.O.OOO'
    decimal_sign = '.O...O'
    
    is_number_mode = False
    is_capital_mode = False
    
    for chunk in braille_chunks:
        if chunk == '......':
            text_output += ' '  
            is_number_mode = False  # Reset number mode on space
        elif chunk == number_sign:
            is_number_mode = True  # Enter number mode
        elif chunk == capital_sign:
            is_capital_mode = True  # Enter capital mode
        elif chunk == decimal_sign:
            text_output += '.'  
            is_number_mode = False  # End number mode after decimal
        else:
            if is_number_mode:
                
                char = braille_to_english.get(chunk, ('', ''))[1]  
                text_output += char
                continue  
            elif is_capital_mode:
                
                char = braille_to_english.get(chunk, '')
                if isinstance(char, tuple):
                    char = char[0]  
                text_output += char.upper()
                is_capital_mode = False  
            else:
                
                char = braille_to_english.get(chunk, '')
                if isinstance(char, tuple):
                    char = char[0]  
                text_output += char
    
    return text_output

def to_braille(text_string):
    
    braille_output = ''
    is_number_mode = False

    for char in text_string:
        if char == ' ':
            is_number_mode = False
            braille_output += '......'  
        elif char.isdigit():
            if not is_number_mode:
                braille_output += number_sign  # Start number mode
                is_number_mode = True
            braille_output += english_to_braille.get(char, '......')
        elif char.isalpha():
            if char.isupper():
                braille_output += capital_sign  # Add capital sign
                char = char.lower()  
            if is_number_mode:
                braille_output += '......'  # End number mode
                is_number_mode = False
            braille_output += english_to_braille.get(char, '......')
        elif char == '.':
            braille_output += decimal_sign
        else:
            braille_output += english_to_braille.get(char, '......')

    return braille_output

def detect_mode(text_string):
    """Detect if the text is Braille or English."""
    if all(char in "O." for char in text_string):
        return 'to_english'
    return 'to_braille'
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        return

    text = " ".join(sys.argv[1:])

    mode = detect_mode(text)
    
    if mode == 'to_braille':
        print(to_braille(text))
    elif mode == 'to_english':
        print(to_english(text))

if __name__ == '__main__':
    main()