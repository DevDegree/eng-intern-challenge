import sys

ALPHA_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "CAP": ".....O", "NUM": ".O.OOO", " ": "......",
}


NUM_TO_BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}


BRAILLE_TO_ALPHA = {v: k for k, v in ALPHA_TO_BRAILLE.items()}
BRAILLE_TO_NUM = {v: k for k, v in NUM_TO_BRAILLE.items()}


def is_braille_input(text):
    return all(char in 'O.' for char in text)

def braille_to_english(braille):
    result = []
    is_capital = False
    is_numeric = False
    
    for i in range(0, len(braille), 6):
        segment = braille[i:i+6]
        if segment == ALPHA_TO_BRAILLE["CAP"]:
            is_capital = True
        elif segment == ALPHA_TO_BRAILLE["NUM"]:
            is_numeric = True
        elif segment == ALPHA_TO_BRAILLE[" "]:
            is_numeric = False
            result.append(" ")
        else:
            if is_numeric:
                result.append(BRAILLE_TO_NUM[segment])
            elif is_capital:
                result.append(BRAILLE_TO_ALPHA[segment].upper())
                is_capital = False
            else:
                result.append(BRAILLE_TO_ALPHA[segment])
    
    return "".join(result)

def english_to_braille(english_text):
    result = []
    is_numeric = False
    
    for char in english_text:
        if char == " ":
            result.append(ALPHA_TO_BRAILLE[" "])
            is_numeric = False
        elif char.isdigit():
            if not is_numeric:
                is_numeric = True
                result.append(ALPHA_TO_BRAILLE["NUM"])
            result.append(NUM_TO_BRAILLE[char])
        elif char.isalpha():
            if char.isupper():
                result.append(ALPHA_TO_BRAILLE["CAP"])
            result.append(ALPHA_TO_BRAILLE[char.lower()])
            is_numeric = False
    
    return "".join(result)

def main():
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        if is_braille_input(input_text):
            print(braille_to_english(input_text))
        else:
            print(english_to_braille(input_text))
    else:
        print("Please provide an input for translation.")

if __name__ == '__main__':
    main()
