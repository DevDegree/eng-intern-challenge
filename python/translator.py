english_to_braille_letters_dict = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

english_to_braille_nums_dict = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

def braille_to_english(braille_text):
    letters = dict((v,k) for k,v in english_to_braille_letters_dict.items())
    nums = dict((v,k) for k,v in english_to_braille_nums_dict.items())
    english_text = ""
    capitalize_next = False
    is_number = False
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]

        if braille_char == ".....O":  
            capitalize_next = True
            continue
        elif braille_char == ".O.OOO":  
            is_number = True
            continue
            
        if is_number:
            english_char = nums.get(braille_char)
            english_char = str(int(english_char))

        elif capitalize_next:
            english_char = letters.get(braille_char)
            english_char = english_char.upper()
            capitalize_next = False
        else:
            english_char = letters.get(braille_char)

        if english_char:
            english_text += english_char
        else:
            raise ValueError("Invalid Braille character: " + braille_char)

    return english_text

def english_to_braille(english_text):
    braille_text = ""
    is_number = False
    for char in english_text:
        if char.isupper():
            braille_text += ".....O"
        elif char == ' ':
            braille_text += english_to_braille_letters_dict.get(char.lower())
            is_number = False
            continue
        elif char.isdigit() and not is_number:
            braille_text += ".O.OOO"
            is_number = True       
        
        if is_number:
            braille_char = english_to_braille_nums_dict.get(str(int(char)))
        else:
            braille_char = english_to_braille_letters_dict.get(char.lower())
            is_number = False

        if braille_char:
            braille_text += braille_char
        else:
            raise ValueError("Invalid English character: " + char)

    return braille_text

def translate(text):
    x = all(c in set('.'+'O') for c in text)
    if(x):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        print(translate(text))
    else:
        print("Please provide a text to translate.")
