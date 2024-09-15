import sys

alphadict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

numdict = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def get_key(val, dictionary):
    return next((key for key, value in dictionary.items() if val == value), None)

def translate(input_string):
    is_braille = set(input_string).issubset({'O', '.'})
    output = ""
    
    if not is_braille:
        # English to Braille
        last_was_num = False
        for char in input_string:
            if char in numdict:
                if not last_was_num:
                    output += ".O.OOO"
                    last_was_num = True
                output += numdict[char]
            else:
                if char.isupper():
                    output += ".....O"
                char = char.lower()
                output += alphadict.get(char, '')
                last_was_num = False
    else:
        # Braille to English
        braille_chars = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
        num_next = cap_next = False
        for braille_char in braille_chars:
            if braille_char == ".O.OOO":
                num_next = True
            elif braille_char == "......":
                num_next = False
                output += " "
            elif braille_char == ".....O":
                cap_next = True
            elif num_next:
                output += get_key(braille_char, numdict) or ''
            else:
                letter = get_key(braille_char, alphadict) or ''
                if cap_next:
                    letter = letter.upper()
                    cap_next = False
                output += letter

    return output

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
    else:
        input_string = ' '.join(sys.argv[1:])
        print(translate(input_string))