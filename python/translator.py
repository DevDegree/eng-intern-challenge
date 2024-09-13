import sys

braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0", "......": " "
}

english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......"
}

def is_braille(input_str):
    for char in input_str:
        if char != 'O' and char != '.':
            return False
    return True

def translate_to_english(braille_text):
    result = []
    i = 0
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        if braille_char in braille_to_english:
            result.append(braille_to_english[braille_char])
        else:
            result.append('?')
        i += 6
    return ''.join(result)

def translate_to_braille(english_text):
    result = []
    is_number = False
    for char in english_text:
        if char == ' ':
            result.append('......')
            is_number = False
            continue
        
        if char.isdigit():
            if not is_number:
                result.append('.O.OOO')
                is_number = True
            result.append(english_to_braille[char])
        else:
            char_lower = char.lower()
            if char.isupper():
                result.append('.....O')
            result.append(english_to_braille[char_lower])
            is_number = False
    
    return ''.join(result)

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))
