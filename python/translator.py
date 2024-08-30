# written using python 3.12.4
import string
import sys

# using hashmaps/dictionaries to perform the translation from braille to english 
# time complexity should be O(1) when looking up translations, and space complexity is O(38) which can be treated is O(1)
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

# reverse the map for the braille to english translation
eng_dict = {val: key for key, val in braille_dict.items()}

# dictionary for numbers
num_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3',
    'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
    'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
    '.OOO..': '0', '.O...O': '.' # decimal can also be part of the num dictionary
}

# reverse numbers dict for the english to braille translation 
braille_num_dict = {val: key for key, val in num_dict.items()}

def translator(s: string) -> string:
    # check if input is braille or english
    engInput = False
    for char in s:
        if char not in "O.":
            engInput = True
            break

    # add one more check to make sure the input is braille (braille characters are 6 letters each). In case of inputs like "O.O."
    if len(s) % 6 != 0:
        engInput = True

    capitalLetter, number = False, False
    res = ""

    # iterate by 6 if input is braille, and by 1 if input is english
    iterator = 1 if engInput else 6
    for i in range(0, len(s), iterator):
        substring = s[i:i+iterator]
        
        s_english, s_braille = "", ""

        # logic for braille to english
        if not engInput:
            # special cases
            if substring == "......": # space. Resets the booleans for capital letters, decimals and numbers
                capitalLetter = False
                number = False
            elif substring == ".....O": # capital letter follows. set the capitalLetter boolean to true and continue to next iteration
                capitalLetter = True
                continue
            elif substring == ".O.OOO": # number follows. set number boolean to true and continue
                number = True
                continue
            elif substring == ".O...O": # decimal follows. basically the same logic as number but append a '.' to the result
                number = True

            if capitalLetter:   # a letter's capital version of itself has a ascii value of 32 less than current ascii value
                s_braille = chr(ord(eng_dict[substring]) - 32)
                capitalLetter = False
            elif number:
                s_braille = num_dict[substring]
            else:
                s_braille = eng_dict[substring]

        # logic for english letters
        else:
            if 65 <= ord(substring) <= 90: # special case for capital letters
                s_english += ".....O" + braille_dict[chr(ord(substring) + 32)]
                # s_english += braille_dict[chr(ord(substring) + 32)]
            elif 48 <= ord(substring) <= 57: # number
                if not number:  # add the number follows prior to adding the braille numbers
                    s_english += ".O.OOO"
                s_english += braille_num_dict[chr(ord(substring))]
                number = True
            elif substring == ".": # decimal
                s_english += ".O...O"
                number = True
            elif substring == " ": # end of capital letters/numbers/decimals
                capitalLetter = False
                number = False
                s_english += "......"
            else:
                s_english = braille_dict[substring]

        res += s_english if engInput else s_braille

    return res

if __name__ == "__main__":
    s = ' '.join(sys.argv[1:])
    print(translator(s))