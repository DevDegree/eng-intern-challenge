# Braille to English and English to Braille dictionary
braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", " ": "......",
    "capital": ".....O", 
    "number": ".O.OOO",
    "decimal": "O..O.O",
    ".": ".O.O..", ",": "O.....", "?": "O.O..O", "!": "O.O.O.", 
    ":": "O..O.O", ";": "O.O..O", "-": "O..O..", 
    "/": "O.O..O", "<": "OOO...", ">": ".OOO.O", "(": "O...OO", ")": ".OOO.O"
}


braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_numbers = {v: k for k, v in braille_numbers.items()}

def translate(input_text):
    braille_symbols = set(braille_alphabet.values()) | set(braille_numbers.values())
    input_is_braille = all(symbol in braille_symbols for symbol in input_text.split())
    
    result = []
    capital_mode = False
    number_mode = False

    if input_is_braille:
        braille_chars = input_text.split()

        for braille_char in braille_chars:
            if braille_char == braille_alphabet['capital']:
                capital_mode = True
            elif braille_char == braille_alphabet['number']:
                number_mode = True
            elif braille_char == "......":
                result.append(" ")
                number_mode = False
            else:
                if number_mode:
                    english_char = english_numbers[braille_char]
                else:
                    english_char = english_alphabet[braille_char]
                    if capital_mode:
                        english_char = english_char.upper()
                        capital_mode = False
                
                result.append(english_char)

    else:
        for char in input_text:
            if char.isupper():
                result.append(braille_alphabet['capital'])
                result.append(braille_alphabet[char.lower()])
            elif char.isdigit():
                if not number_mode:
                    result.append(braille_alphabet['number'])
                    number_mode = True
                result.append(braille_numbers[char])
            elif char == " ":
                result.append(braille_alphabet[" "])
                number_mode = False
            else:
                result.append(braille_alphabet[char])
                number_mode = False

    return " ".join(result) if not input_is_braille else "".join(result)

