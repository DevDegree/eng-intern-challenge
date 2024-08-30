import sys

# Braille dictionary based on the provided image
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '.': '.O.O.O', ',': 'O.....', '!': 'OOO...', '?': '.O.OO.', 
    '-': 'O....O', ':': 'OO.O..', ';': 'O.O...', "'": 'O....O',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Reverse dictionary for converting Braille to English
letter_dict = {v: k for k, v in braille_alphabet.items() if k.isalpha()}
punctuation_dict = {v: k for k, v in braille_alphabet.items() if k in ['.', ',', '!', '?', '-', ':', ';', "'"]}
number_dict = {
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

#Note: The provided unit test is incorrect so I left the number_dict in the correct form instead of changing it to meet unit test's output. 

def translate_to_braille(text):
    result = []
    is_number = False  # Track if we are in number mode

    for char in text:
        if char.isupper():
            result.append(braille_alphabet['capital'])
            result.append(braille_alphabet[char.lower()])
            is_number = False  # Reset number mode
        elif char.isdigit():
            if not is_number:
                result.append(braille_alphabet['number'])  # Add number indicator only once
                is_number = True  # Set number mode
            result.append(number_dict[char])
        else:
            if is_number and char == ' ':
                is_number = False  # Reset number mode if a space is found
            result.append(braille_alphabet.get(char, '......'))

    return ''.join(result)

def translate_to_english(braille):
    result = []
    is_capital = False
    is_number = False
    buffer = ''
    
    for char in braille:
        buffer += char
        if len(buffer) == 6:
            if buffer == braille_alphabet['capital']:
                is_capital = True
            elif buffer == braille_alphabet['number']:
                is_number = True
            elif buffer == '......':
                result.append(' ')
                is_number = False  # Reset number mode when a space is encountered
            else:
                if is_number:
                    # Translate using number_dict
                    char = next((key for key, value in number_dict.items() if value == buffer), '')
                else:
                    # Translate using letter_dict or punctuation_dict
                    char = letter_dict.get(buffer, '') or punctuation_dict.get(buffer, '')
                    if is_capital:
                        char = char.upper()
                        is_capital = False  # Reset capital mode immediately after use
                result.append(char)
            buffer = ''
    
    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_or_braille>")
        return
    
    # Combine all arguments into a single input string
    input_text = ' '.join(sys.argv[1:])
    
    # Determine if input is Braille or English
    if all(char in 'O.' for char in input_text.replace(' ', '')):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
