import sys

# Braille to English dictionary
braille_to_english = {
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
    '.O.OOO': 'number',  # Number follows indicator
    '.....O': 'capital',  # Capital follows indicator
    '......': ' ',        # Space
    '.O....': '.',        
    '.OO.O.': ',',        
    '.O..O.': '?',        
    '.O.OO.': '!',        
    '.O...O': ':',        
    '.OO..O': ';',        
    '....O.': '-',        
}


english_to_braille = {
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
    ' ': '......',   
    '.': '.O....',   
    ',': '.OO.O.',   
    '?': '.O..O.',   
    '!': '.O.OO.',   
    ':': '.O...O',   
    ';': '.OO..O',  
    '-': '....O.',  
    '1': 'O.....',   # Numbers are the same as letters, with the number indicator
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'capital': '.....O',  
    'number': '.O.OOO',   
}

def is_braille(input_str):
    # Braille format (contains 'O' and '.')
    return all(c == 'O' or c == '.' for c in input_str)

def braille_to_text(braille_str):
    words = braille_str.split('......')  # Split into words by Braille space
    translated_text = []
    is_capital = False
    is_number = False

    for word in words:
        chars = [word[i:i+6] for i in range(0, len(word), 6)]
        word_text = ""
        for char in chars:
            if char in braille_to_english:
                symbol = braille_to_english[char]
                if symbol == 'capital':
                    is_capital = True
                elif symbol == 'number':
                    is_number = True
                else:
                    if is_number and symbol.isalpha():
                        symbol = str(ord(symbol) - ord('a') + 1)  # Convert a-j to 1-9
                    if is_capital:
                        symbol = symbol.upper()
                        is_capital = False
                    word_text += symbol
                    if is_number and symbol == ' ':
                        is_number = False
        translated_text.append(word_text)
    
    return ' '.join(translated_text)

def text_to_braille(text_str):
    braille_translation = []
    is_number_sequence = False

    for char in text_str:
        if char.isdigit():
            if not is_number_sequence:
                braille_translation.append(english_to_braille['number'])  
                is_number_sequence = True
            braille_translation.append(english_to_braille[char])
        elif char.isalpha():
            if char.isupper():
                braille_translation.append(english_to_braille['capital'])  
                braille_translation.append(english_to_braille[char.lower()])
            else:
                braille_translation.append(english_to_braille[char])
            is_number_sequence = False  # End number sequence if we encounter a letter
        else:
            braille_translation.append(english_to_braille.get(char, '......'))  # Default to space for unknown symbols
            is_number_sequence = False  # End number sequence on spaces or punctuation

    return ''.join(braille_translation)

def main():
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(braille_to_text(input_str))
    else:
        print(text_to_braille(input_str))

if __name__ == "__main__":
    main()
