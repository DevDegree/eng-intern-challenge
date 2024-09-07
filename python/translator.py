import sys

# Dictionary for mapping English letters to their corresponding Braille symbols
char_to_braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", "cap": ".....O", "num": ".O.OOO"
}

# Dictionary for mapping numbers (0-9) to their corresponding Braille symbols
num_to_braille_alphabet = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......", "cap": ".....O", "num": ".O.OOO"
}

# Reverse dictionary for converting Braille symbols back to English letters
braille_to_char_alphabet = {v: k for k, v in char_to_braille_alphabet.items()}

# Reverse dictionary for converting Braille symbols back to numbers
braille_to_num_alphabet = {v: k for k, v in num_to_braille_alphabet.items()}

def is_braille(input_string):
    """
    checks if a string only contains chars '0' and '.'
    if true, means that the string is a braille string
    """
    return all(char in "O." for char in input_string)

def english_to_braille_convert(input):
    """
    converts the input string from English to braille
    """
    result = []
    is_num = False
    for char in input:
        if char.isdigit():
            if not is_num:
                # If the character is the first digit in a number sequence, add braille symbol for num mode
                is_num = True
                result.append(char_to_braille_alphabet["num"])
            result.append(num_to_braille_alphabet[char])
        else:
            if is_num:
                is_num = False
            if char.isupper():
                result.append(char_to_braille_alphabet["cap"])
                char = char.lower()
            result.append(char_to_braille_alphabet[char])
    return ''.join(result)

def braille_to_english_convert(input):
    """
    converts the input string from braille to English
    """
    result = []
    is_num = False
    is_cap = False
    index = 0
    while (index < len(input)):
        symbol = input[index:index+6] # get the substring corresponding to a letter or a number
        index += 6
        if not is_num:
            char = braille_to_char_alphabet[symbol]
            # first check if the symbol represents is_cap or is_num
            # if it is, set the corresponding flag and continue to the next symbol
            if char == "cap":
                is_cap = True
                continue
            if char == "num":
                is_num = True
                continue
            if is_cap:
                char = char.upper()
                is_cap = False # cap flag only applies to the next letter
            result.append(char)
        else:
            char = braille_to_num_alphabet[symbol]
            if char == " ":
                # if a white space is encountered, it means num mode is finished
                is_num = False
            result.append(char)
    return ''.join(result)

def translate(input_string):
    """
    converts the input string from English to Braille or from Braille to English
    it assumes that the input is a valid English or Braille string according to
    the requirements in the problem description
    """
    if is_braille(input_string):
        return braille_to_english_convert(input_string)
    else:
        return english_to_braille_convert(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input to translate.")
    else:
        input_string = ' '.join(sys.argv[1:])
        translated_string = translate(input_string)
        sys.stdout.write(translated_string)