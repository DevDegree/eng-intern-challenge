import sys

braille_to_english = {
    # Letters
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", 
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", 
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z",
    
    # Capital symbol
    ".....O": "capital",

    # Number symbol
    ".O.OOO": "number",

    # Space
    "......": " "
}

english_to_braille = {
    # Letters
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO",

    # Capital symbol
    "capital": ".....O",

    # Number symbol
    "number": ".O.OOO",

    # Space
    " ": "......"
}

def is_braille(input_str):
    return all(c in 'O.' for c in input_str)


def translate_braille_to_english(braille_str):
    result = []
    i = 0
    is_capital = False
    is_number = False
    
    while i < len(braille_str):
        # each braille symbol is 6 characters
        symbol = braille_str[i:i+6]
        
        if symbol == ".....O":  # Capital symbol
            is_capital = True
        elif symbol == ".O.OOO":  # Number symbol
            is_number = True
        elif symbol == "......":  # Space symbol
            result.append(' ')
            is_number = False
        else:
            if is_number:  # number mode
                # Translate letters a-j to numbers 1-0
                letter = braille_to_english.get(symbol, '')
                if letter in "abcdefghij":
                    number_translation = str("abcdefghij".index(letter) + 1) if letter != "j" else "0"
                    result.append(number_translation)
            elif is_capital:  # capital mode
                result.append(braille_to_english.get(symbol, '').upper())
                is_capital = False
            else:
                result.append(braille_to_english.get(symbol, ''))
        
        i += 6
    return ''.join(result)

def translate_english_to_braille(english_str):
    result = []
    is_number_mode = False
    
    for char in english_str:
        if char.isupper():
            result.append(english_to_braille["capital"])
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():  
            if not is_number_mode:
                result.append(english_to_braille["number"])
                is_number_mode = True
            if char == "0":
                result.append(english_to_braille["j"])
            else:
                result.append(english_to_braille["abcdefghij"[int(char) - 1]])
        elif char == " ":
            result.append(english_to_braille[" "])
            is_number_mode = False
        else:
            result.append(english_to_braille[char])
    
    return ''.join(result)

if __name__ == "__main__":
    # Join all arguments
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        print(translate_braille_to_english(input_str))
    else:
        print(translate_english_to_braille(input_str))
