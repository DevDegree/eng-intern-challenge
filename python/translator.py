import sys

# braille dictionary
braille_dict = {
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
    "cap": ".....O", # capital letter follows
    "num": ".O.OOO", # number follows
    " ": "......", # space
}

# reverse dictionary for english lookup
english_dict = {v: k for k, v in braille_dict.items()}

def is_braille(text):
    # check if the input only contains 'O' and '.'
    return all(char in "O." for char in text)

def translate_to_braille(text):
    result = []
    num_mode = False

    for char in text:
        # turn off num mode if we see a space
        if char == " ":
            num_mode = False  
        
        # add a capital letter symbol if the character is uppercase
        if char.isupper():
            result.append(braille_dict['cap'])
            char = char.lower()
        
        # add a number symbol if the character is a digit and we haven't turned on num mode yet
        if char.isdigit() and not num_mode:
            result.append(braille_dict['num'])
            num_mode = True
        
        result.append(braille_dict[char])
    
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    cap_next = False

    while i < len(braille):
        symbol = braille[i:i+6]

        # if we need to capitalize the next letter
        if symbol == braille_dict['cap']:
            cap_next = True
        
        elif symbol == braille_dict['num']:
            pass
        
        else:
            char = english_dict[symbol]

            if cap_next:
                char = char.upper()
                cap_next = False

            result.append(char)

        i += 6

    return ''.join(result)

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))