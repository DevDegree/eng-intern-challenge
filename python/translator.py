import argparse


alphabet_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",

    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",


    ".": "..OO.O", 
    ",": "..O...", 
    "?": "..O.OO", 
    "!": "..OOO.", 
    ":": "..OO..",
    ";": "..O.O.", 
    "-": "....OO", 
    "/": ".O..O.", 
    "<": ".OO..O", 
    ">": "O..OO.",
    "(": "O.O..O",
     ")": ".O.OO.", 
     " ": "......",

    "capital": ".....O", "number": ".O.OOO", "decimal": ".O...O" 
}

braille_to_alphabet = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    
 
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
    "......": " ",

    ".....O":"capital", ".O.OOO": "number", "O...O.": "decimal"
}
braille_to_number = {
    "O.....":"1", 
    "O.O...":"2", 
    "OO....": "3", 
    "OO.O..": "4", 
    "O..O..": "5", 
    "OOO...": "6", 
    "OOOO..": "7", 
    "O.OO..": "8",
    ".OO...": "9",  
    ".OOO..": "0"

}


def translate_to_braille(text):
    result = ""
    num_mode = False
    for char in text:
        if char.isupper():
            result += alphabet_to_braille["capital"] + alphabet_to_braille[char.lower()]
            num_mode = False

        elif char.isdigit():
            if not num_mode:
                result += alphabet_to_braille["number"] 
                num_mode = True
            result += alphabet_to_braille.get(char)
        
        elif char == '.':
            # Handle decimal within number mode
            if num_mode:
                result += alphabet_to_braille["decimal"]
            else:
                # If not in number mode, just add the representation of "."
                result += alphabet_to_braille[char]
        
        else:
            result += alphabet_to_braille.get(char)
            num_mode = False
    return result

def translate_to_alphabet(text):
    result = ""
    i = 0
    num_mode = False
    cap_mode = False

    while i < len(text):
        braille_char = text[i:i+6]

        # Check num_mode and cap_mode
        if braille_char == alphabet_to_braille["capital"]:
            cap_mode = True
            i += 6
            continue

        elif braille_char == alphabet_to_braille["number"]:
            num_mode = True
            i += 6
            continue
        
        elif braille_char == alphabet_to_braille["decimal"]:
            result += "."
            i += 6
            continue

        elif braille_char == alphabet_to_braille[" "]:  # Handle space
            result += " "
            num_mode = False  # Reset both modes when a space is encountered
            cap_mode = False
            i += 6
            continue

        # Translate the current Braille character to Alphabet or Number
        if num_mode:
         
            if braille_char in braille_to_number:
                char = braille_to_number[braille_char]
            else:
                num_mode = False
                char = braille_to_alphabet.get(braille_char, "")
        else:
    
            char = braille_to_alphabet.get(braille_char, "")


        if cap_mode and char.isalpha():
            char = char.upper()
            cap_mode = False  

        result += char

        i += 6

    return result


def determine_and_translate(input_text):
    if all(char in "O." for char in input_text) and len(input_text) % 6 == 0:
        return translate_to_alphabet(input_text)
    else:
        return translate_to_braille(input_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text', nargs='+', type=str)  
    args = parser.parse_args()

    translated_text = determine_and_translate(' '.join(args.text))
    print(translated_text, end='')

