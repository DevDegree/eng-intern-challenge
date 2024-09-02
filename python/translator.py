import sys

# mapping of Braille to english letters and punctuation
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")", "......": " ",
}

# mapping of Braille to numbers (0-9)
braille_to_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

# reverse lookup dictionaries to convert english letters and nums to braille
english_to_braille = {v: k for k, v in braille_to_english.items()}
num_to_braille = {v: k for k, v in braille_to_num.items()}

# capitalization and numbers
capital_prefix = ".....O"  # indicates that a capital follows
number_prefix = ".O.OOO"   # indicates that a number follows
decimal_prefix = ".O...O"  # indicates that a decimal follows

# function to check if the given string is braille or english
def braille_check(string):

    # check if the string is braille, otherwise return false (english string)
    return all(c in ".O" for c in string) and len(string) % 6 == 0

# function to convert braille to english
def braille_to_eng(braille):

    english_text = ""
    braille_chars = []

    for i in range(0, len(braille), 6):
        braille_chars.append(braille[i:i + 6])

    capitalize_next = False
    is_mode = False  # flag to track if in mode

    # iterate over each braille chunk/pattern and translate it to english
    for char in braille_chars:

        # set the capital and/or number mode flags to true if the braille pattern is seen
        if char == capital_prefix:
            capitalize_next = True
            continue
        elif char == number_prefix:
            is_mode = True
            continue
        
        # translate the braille to a number if in mode
        if is_mode:
            translated_char = braille_to_num.get(char)
            if translated_char is None:
                is_mode = False  # exit number mode if not a valid number
                translated_char = braille_to_english.get(char, "")
        else: # translate to english letters or punctutation if not in mode
            translated_char = braille_to_english.get(char, "")

        if capitalize_next:
            translated_char = translated_char.upper()
            capitalize_next = False

        english_text += translated_char

    return english_text

# function to convert english to braille 
def eng_to_braille(english):

    braille_text = ""
    is_mode = False  # flag to track if in number mode

    # iterate over each character in the english string
    for char in english:

        if char.isupper():
            braille_text += capital_prefix
            char = char.lower()
            is_mode = False  # exit num mode before letters

        if char.isdigit():
            if not is_mode:  # only prepend the number prefix to the braille string if not in mode
                braille_text += number_prefix
                is_mode = True
            braille_text += num_to_braille.get(char, "") # if it is a number then get the number translation to braille
        else: # otherwise get the english letter/punctuation translation
            braille_text += english_to_braille.get(char, "")
            is_mode = False  # exit num mode after non-digit

    return braille_text

# main function to detect input and perform translation
def main():
    # join all arguments into a single string to handle multiple inputs correctly
    string = " ".join(sys.argv[1:])

    # determine if the input is braille or english
    if braille_check(string):
        result = braille_to_eng(string)
    else:
        result = eng_to_braille(string)
    
    # print the resulting converted string
    print(result)

if __name__ == "__main__":
    main()
