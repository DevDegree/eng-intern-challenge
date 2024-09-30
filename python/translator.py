import sys

# map for alphabet to braille (punctuation included)
ALPHA_BRAILLE = {
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
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......" 
}

# map for number to braille
NUM_BRAILLE = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...", 
    "0": ".OOO.." 
}

# create the reverse of the above maps
BRAILLE_ALPHA = {ALPHA_BRAILLE[i]: i for i in ALPHA_BRAILLE}
BRAILLE_NUM = {NUM_BRAILLE[i]: i for i in NUM_BRAILLE}

# special characters to keep track of
CAPS_CHAR = ".....O"
NUM_CHAR = ".O.OOO"
SPACE_CHAR = "......"

# translating braille to english
def braille_eng(input_text):
    num_flag = False
    caps_flag = False
    translated_text = ""

    # iterate through 6 spaces at a time
    for b in range(0, len(input_text), 6):

        # convert 6 spaces to one braille character
        braille_char = input_text[b : b+6]
        if braille_char == SPACE_CHAR:
            translated_text += " "
            num_flag = False
            continue

        if braille_char == CAPS_CHAR:
            caps_flag = True
            continue

        if braille_char == NUM_CHAR:
            num_flag = True
            continue

        if num_flag:
            translated_text += BRAILLE_NUM[braille_char]
            continue

        text_code = ord(BRAILLE_ALPHA[braille_char])

        # capitalized alphabet has ASCII code that is 32 less than uncapitalized counterpart
        if caps_flag:
            text_code -= 32
            caps_flag = False
        
        translated_text += chr(text_code)

    return translated_text

# translating english to braille
def eng_braille(input_text):
    num_flag = False
    translated_text = ""

    for c in input_text:
        if c in "1234567890":

            # to prevent adding multiple number denoters
            if not num_flag:
                translated_text += NUM_CHAR
                num_flag = True
            
            translated_text += NUM_BRAILLE[c]
            continue
        
        if c == SPACE_CHAR:
            translated_text += " "
            num_flag = False
            continue
        
        # check if char is capitalized
        if ord(c) in range(65, 91):
            translated_text += CAPS_CHAR
            translated_text += ALPHA_BRAILLE[c.lower()]
            continue
            
        translated_text += ALPHA_BRAILLE[c]

    return translated_text


def main():
    input_text = " ".join(sys.argv[1:])
    if all(c in 'O.' for c in input_text):
        print(braille_eng(input_text))
    else:
        print(eng_braille(input_text))


if __name__ == "__main__":
    main()