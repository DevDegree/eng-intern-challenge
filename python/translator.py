import sys
Braille_English = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", 
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", 
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number","......": " "
    }
English_Braille = {}
for braille, english in Braille_English.items():
    English_Braille[english] = braille

English_Digits = {
    "a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
    "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"
    }
Digits_Braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
    }

def is_braille(input):
    return all(char in "O." for char in input) and len(input) % 6 == 0

def translate_Braille_English(braille_string):
    english_translation = []
    digit_mode = False
    next_capital = False

    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]
        char = Braille_English[braille_char]

        if next_capital:
            english_translation.append(char.upper())
            next_capital = False
            continue  

        if digit_mode and char in English_Digits:
            char = English_Digits[char]
            english_translation.append(char)
            continue  

        if char == "capital":
            next_capital = True
            continue  

        if char == "number":
            digit_mode = True
            continue
        
        if char == " ":
            english_translation.append(" ")
            digit_mode = False
            continue  
        
        english_translation.append(char)

    return ''.join(english_translation)

def translate_English_Braille(english_string):
    braille_translation = []
    digit_mode = False

    for char in english_string:
        if char.isupper():
            braille_translation.append(English_Braille["capital"])
            braille_translation.append(English_Braille[char.lower()])
            continue
            
        if char.isdigit():
            if not digit_mode:
                braille_translation.append(English_Braille["number"])
                digit_mode = True
            braille_translation.append(Digits_Braille[char])
            continue

        if char == " ":
            braille_translation.append(English_Braille[char])
            continue

        braille_translation.append(English_Braille[char])
    
    return ''.join(braille_translation)

def main():
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        translated = translate_Braille_English(input_string)
    else:
        translated = translate_English_Braille(input_string)
    print(translated)

if __name__ == "__main__":
    main()