import sys

# dictionary of all braille characters -> very good for braille to english
braille_dictionary = {
    "O....." : {'lower': "a", 'upper': "A", 'number': 1},
    "O.O..." : {'lower': "b", 'upper': "B", 'number': 2},
    "OO...." : {'lower': "c", 'upper': "C", 'number': 3},
    "OO.O.." : {'lower': "d", 'upper': "D", 'number': 4},
    "O..O.." : {'lower': "e", 'upper': "E", 'number': 5},
    "OOO..." : {'lower': "f", 'upper': "F", 'number': 6},
    "OOOO.." : {'lower': "g", 'upper': "G", 'number': 7},
    "O.OO.." : {'lower': "h", 'upper': "H", 'number': 8},
    ".OO..." : {'lower': "i", 'upper': "I", 'number': 9},
    ".OOO.." : {'lower': "j", 'upper': "J", 'number': 0},
    "O...O." : {'lower': "k", 'upper': "K", 'number': None},
    "O.O.O." : {'lower': "l", 'upper': "L", 'number': None},
    "OO..O." : {'lower': "m", 'upper': "M", 'number': None},
    "OO.OO." : {'lower': "n", 'upper': "N", 'number': None},
    "O..OO." : {'lower': "o", 'upper': "O", 'number': None},
    "OOO.O." : {'lower': "p", 'upper': "P", 'number': None},
    "OOOOO." : {'lower': "q", 'upper': "Q", 'number': None},
    "O.OOO." : {'lower': "r", 'upper': "R", 'number': None},
    ".OO.O." : {'lower': "s", 'upper': "S", 'number': None},
    ".OOOO." : {'lower': "t", 'upper': "T", 'number': None},
    "O...OO" : {'lower': "u", 'upper': "U", 'number': None},
    "O.O.OO" : {'lower': "v", 'upper': "V", 'number': None},
    ".OOO.O" : {'lower': "w", 'upper': "W", 'number': None},
    "OO..OO" : {'lower': "x", 'upper': "X", 'number': None},
    "OO.OOO" : {'lower': "y", 'upper': "Y", 'number': None},
    "O..OOO" : {'lower': "z", 'upper': "Z", 'number': None},
    "......" : {'lower': " ", 'upper': " ", 'number': " "},
}

# no puntuation added in the dictionary, not listed as a requirement in the question...but can scale very easily to this!
    #   "..OO.O" : {'lower' : '.', 'upper': '.', 'number': '.'},
    #   "..O..." : {'lower' : ',', 'upper': ',', 'number': ','},
    #   "..O.OO" : {'lower' : '?', 'upper': '?', 'number': '?'},
    #   "..OOO." : {'lower' : '!', 'upper': '!', 'number': '!'},
    #   "..OO.." : {'lower' : ';', 'upper': ';', 'number': ';'},
    #   "..O.O." : {'lower' : ':', 'upper': ':', 'number': ':'},
    #   "....OO" : {'lower' : '-', 'upper': '-', 'number': '-'},
    #   ".O..O." : {'lower' : "/", 'upper': "/", 'number': "/"},
    #   ".OO..O" : {'lower' : "<", 'upper': "<", 'number': "<"},
    #   "O..OO." : {'lower' : ">", 'upper': ">", 'number': ">"},
    #   "O.O..O" : {'lower' : "(", 'upper': "(", 'number': "("},
    #   ".O.OO." : {'lower' : ")", 'upper': ")", 'number': ")"},

# this is needed for the english to braille translation, as the dictionary above can't run in O(1) here..,
char_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
}

# can add more punctuation here, but not listed as a requirement in the question, like so:
    # '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.", ';': "..OO..",
    # ':': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O", '>': "O..OO.",
    # '(': "O.O..O", ')': ".O.OO."

capital_follows = ".....O"
decimal_follows = ".O...O" # when is this used? not specified in the question
number_follows = ".O.OOO"

# checks if the text is braille or anglais
def braille_check(text):
    if len(text) % 6 != 0:
        return False
    else:
        # we know we have a multiple of 6 characters, on the right track...
        # check if all characters are in the dictionary (just Os and .s)
        return all(char in "O." for char in text)
# O(n) time complexity, n = len(text)

def braille_to_english(text):
    result = []
    i = 0
    mode = 'lower'

    while i < len(text):
        braille_charac = text[i:i+6]
        # we need to check if the upcoming braille represents a uppercase, 
            # number, or punctuation
        if braille_charac == capital_follows:
            # uppercase follows
            mode = 'upper'
            i += 6
            continue
        elif braille_charac == number_follows:
            # number follows
            mode = 'number'
            i += 6
            continue
        elif braille_charac == "......":
            # we get a space, so we don't need to go back to lower!
            result.append(' ')
            mode = 'lower'
            i += 6
            continue
        if braille_charac in braille_dictionary:
            temp_char = braille_dictionary[braille_charac].get(mode)
            if temp_char is not None:
                if isinstance(temp_char, int):
                    result.append(str(temp_char))
                else:
                    result.append(temp_char)
            else:
                break # invalid character - should we exit the loop or continue? need more direction here
        i += 6
        if mode != 'number':
            mode = 'lower'
    return ''.join(result)
# O(n)

def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isupper():
            result.append(capital_follows)
            result.append(char_to_braille[char.lower()])
            number_mode = False
        elif char.isdigit():
            if not number_mode: 
                result.append(number_follows)
                number_mode = True
            result.append(char_to_braille[char])
        elif char in char_to_braille:
            result.append(char_to_braille[char])
            number_mode = False
        else:
            break # invalid character
    return ''.join(result)
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)  # Exit the script indicating that it was not used correctly

    # Concatenates all provided arguments into a single input string
    input_string = " ".join(sys.argv[1:])  # This ensures natural phrase input handling

    if not input_string.strip():
        # input is empty
        sys.exit(1)

    if braille_check(input_string):  # Check if input is Braille
        output = braille_to_english(input_string)
    else:
        output = english_to_braille(input_string)

    if output:
        print(output)  # Output the translation result

if __name__ == "__main__":
    main()