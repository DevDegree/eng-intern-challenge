"""Braille Translator."""
 
import sys 
 
# Braille to English dictionary 
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......', "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", 
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
    "O.O..O": "(", ".O.OO.": ")", "......": " "
} 

# English to Braille dictionary 
english_dict = {v: k for k, v in braille_dict.items()} 

# Special symbols
braille_capital = '.....O'
braille_number = '.O.OOO'

def is_braille(s):
    """Determine if the input string is in Braille format."""
    return all(c in 'O.' for c in s)

def translate_braille_to_english(braille): 
    """Convert Braille to English text."""
    result = []
    i, number_mode = 0, False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_capital:
            i += 6
            result.append(english_dict[braille[i:i+6]].upper())
        elif symbol == braille_number:
            number_mode = True
        else:
            char = english_dict.get(symbol, f"[{symbol}]")
            if number_mode and char.isalpha():
                char = str(ord(char) - ord('a') + 1)
            result.append(char)
            number_mode = False
        i += 6
    return ''.join(result)

def translate_english_to_braille(english):
    """Convert English text to Braille."""
    result = []
    number_mode = False
    for char in english:
        if char.isdigit():
            if not number_mode:
                result.append(braille_number)
                number_mode = True
            result.append(braille_dict[char])
        elif char.isalpha():
            if char.isupper():
                result.append(braille_capital)
            result.append(braille_dict[char.lower()])
            number_mode = False
        else:
            result.append(braille_dict[char])
            number_mode = False
    return ''.join(result)


def main():
    # Check if the input is Braille or English
    input_text = " ".join(sys.argv[1:])
    # Check if the input is Braille or English
    if is_braille(input_text):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))


if __name__ == "__main__": 
    main()
