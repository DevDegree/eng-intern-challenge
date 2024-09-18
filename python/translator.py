import sys

TEXT_TO_BRAILLE = {
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
    " ": "......",
}

NUMBERS_TO_BRAILLE = {
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

BRAILLE_TO_TEXT = {
    v: k for k, v in TEXT_TO_BRAILLE.items()
}

BRAILLE_TO_NUMBERS = {
    v: k for k, v in NUMBERS_TO_BRAILLE.items()
}

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

def is_braille(text_input): 
    '''Return True if text_input is a Braille input, otherwise return False.'''
    return all(ch in ".O" for ch in text_input)

def braille_to_english(braille_input):
    '''Return the English translation of a Braille input'''
    english_chars = []
    capital_flag = False 
    number_flag = False

    for i in range(0, len(braille_input), 6):
        braille_character = braille_input[i:i+6]
        if braille_character == CAPITAL_FOLLOWS:
            capital_flag = True
        elif braille_character == NUMBER_FOLLOWS:
            number_flag = True
        elif braille_character == TEXT_TO_BRAILLE[" "]:
            english_chars.append(BRAILLE_TO_TEXT[braille_character])
            number_flag = False
        else:
            if number_flag:
                english_chars.append(BRAILLE_TO_NUMBERS[braille_character])
            elif capital_flag:
                english_chars.append(BRAILLE_TO_TEXT[braille_character].capitalize())
                capital_flag = False    
            else:
                english_chars.append(BRAILLE_TO_TEXT[braille_character])

    return "".join(english_chars)

def english_to_braille(english_input):
    '''Return the Braille translation of an English input'''
    braille_chars = []
    number_flag = False

    for ch in english_input:
        if ch.isdigit():
            if not number_flag:
                braille_chars.append(NUMBER_FOLLOWS)
                number_flag = True
            braille_chars.append(NUMBERS_TO_BRAILLE[ch])
        else:
            if ch.isupper():
                braille_chars.append(CAPITAL_FOLLOWS)
            braille_chars.append(TEXT_TO_BRAILLE[ch.lower()])
            number_flag = False

    return "".join(braille_chars)
            
def main():
    if len(sys.argv) < 2:
        print("Error: No text inputted.")
        print("Usage: python translator.py <text>")
        return
    
    text_input = " ".join(sys.argv[1:])

    if is_braille(text_input):
        print(braille_to_english(text_input))
    else:
        print(english_to_braille(text_input))

if __name__ == "__main__":
    main()