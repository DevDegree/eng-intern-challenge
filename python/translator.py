# Import sys to access command line arguments
import sys

# Constant dictionaries to lookup needed values
BRAILLE_DICT_ALPHA = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    
    "capital": ".....O",
    "number": ".O.OOO",
    " ": "......",
}

BRAILLE_DICT_NUM = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

ENGLISH_DICT_ALPHA = {v: k for k, v in BRAILLE_DICT_ALPHA.items()}

ENGLISH_DICT_NUM = {v: k for k, v in BRAILLE_DICT_NUM.items()}


def english_to_braille(message):

    output = ""
    prev_is_number = False

    # Iterate through each english character and append its corresponding braille sequence to the output
    for char in message:
        if char.isupper():
            output += BRAILLE_DICT_ALPHA["capital"] + BRAILLE_DICT_ALPHA[char.lower()]
        elif char.isdigit():
            if prev_is_number == False:
                output += BRAILLE_DICT_ALPHA["number"]
                prev_is_number = True
            output += BRAILLE_DICT_NUM[char]
        elif char == " ":
            output +=  BRAILLE_DICT_ALPHA[" "]
        else:
            output +=BRAILLE_DICT_ALPHA[char]
    
    return output


def braille_to_english(braile):
    output = ""

    # Breaking up the braille message into sequences of 6 symbols to represent a single english character/number/instruction
    sequences = [braile[i:i+6] for i in range(0, len(braile), 6)]

    capital = False
    number = False

    for seq in sequences:
        if ENGLISH_DICT_ALPHA[seq] == "capital":
            capital = True
            continue
        elif ENGLISH_DICT_ALPHA[seq] == "number":
            number = True
            continue
        elif ENGLISH_DICT_ALPHA[seq] == " ":
            number = False

        if number:
            output += ENGLISH_DICT_NUM[seq]
        elif capital:
            output += ENGLISH_DICT_ALPHA[seq].upper()
            capital = False
        else:
            output += ENGLISH_DICT_ALPHA[seq]

    return output

def main():

    message = ' '.join(sys.argv[1:])

    if len(set(message[:6])) <= 2:
        print(braille_to_english(message))
    else:
        print(english_to_braille(message))
        

if __name__ == "__main__":
    main()