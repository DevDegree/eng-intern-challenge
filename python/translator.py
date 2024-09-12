braille_english = {
    # Letters
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    
    # Special characters
    ".....O": "cap", # Capital follows
    ".O...O": "dec", # Decimal follows
    ".O.OOO": "num", # Number follows
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " "
}

braille_english_nums = {
    # Numbers
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

english_braille = {v: k for k, v in braille_english.items()}
english_braille_nums = {v: k for k, v in braille_english_nums.items()}

def is_braille(input_string):
    return all(char in 'O.' for char in input_string)

def english_to_braille(text):
    braille_translation = []
    is_number = False
    for char in text:
        if char == " ":
            braille_translation.append(english_braille[" "])
            is_number = False
        elif char.isupper():
            braille_translation.append(english_braille["cap"])
            braille_translation.append(english_braille[char.lower()])
        elif char.isdigit() and not is_number:
            braille_translation.append(english_braille["num"])
            braille_translation.append(english_braille_nums[char])
            is_number = True
        elif char.isdigit() and is_number:
            braille_translation.append(english_braille_nums[char])
        else:
            braille_translation.append(english_braille[char])
    return ''.join(braille_translation)

def braille_to_english(braille):
    english_translation = []
    i = 0
    capitalize_next = False
    is_number = False
    
    while i < len(braille):
        braille_char = braille[i:i+6]
        if braille_char == english_braille["cap"]:
            capitalize_next = True
            i += 6
            continue
        elif braille_char == english_braille["num"]:
            is_number = True
            i += 6
            continue
        elif braille_char == english_braille[" "]:
            english_translation.append(" ")
            is_number = False
            i += 6
            continue
        
        if is_number:
            english_translation.append(braille_english_nums[braille_char])
        else:
            char = braille_english[braille_char]
            if capitalize_next:
                english_translation.append(char.upper())
                capitalize_next = False
            else:
                english_translation.append(char)
        
        i += 6
    return ''.join(english_translation)

def braille_translator(input_string):
    if is_braille(input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    import sys
    input_strings = ' '.join(sys.argv[1:])
    output = braille_translator(input_strings)
    print(output)
