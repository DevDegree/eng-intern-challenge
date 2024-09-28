import sys

braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital', '.O.OOO': 'number'
}

english_to_braille = {value: key for key, value in braille_to_english.items()}

number_map = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

"""
Chunk the input text string into a list of strings of length equal to size
"""
def chunk(text, size):
    return [text[i:i+size] for i in range(0, len(text), size)]

"""
Check if every character in the input text string is either O or . and
if the length of text is divisible by 6
"""
def is_braille(text):
    return all(character in 'O.' for character in text) and len(text) % 6 == 0

"""
Translates Braille to English
"""
def braille_to_eng(text):
    result = []
    symbols = chunk(text, 6)
    capitalize_next = False
    number_mode = False

    for symbol in symbols:
        if symbol == braille_to_english['capital']:
            capitalize_next = True
        elif symbol == braille_to_english['number']:
            number_mode = True
        else:
            char = braille_to_english[symbol]
            if number_mode and char in number_map:
                result.append(number_map[char])
            else:
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)
                number_mode = False

    return ''.join(result)

"""
Translates English to Braille
"""
def eng_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(english_to_braille['capital'])
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['number'])
                number_mode = True
            char = [key for key, value in number_map.items() if value == char][0]
        else:
            number_mode = False

        result.append(english_to_braille[char])

    return ''.join(result)

"""
Determine whether to translate English to Braille or Braille to English
"""
def translate(text):
    if is_braille(text):
        return braille_to_eng(text)
    else:
        return eng_to_braille(text)

input_text = sys.argv[1]
print(translate(input_text))
