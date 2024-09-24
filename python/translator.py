# Name: Faizan Naseer
# Email: f.naseer@mail.utoronto.ca

# IMPORTANT!
# Assumption/(s) Below:
# 1. Was not sure about whether we have to use punctuation, so have used it with a logical assumption (point 3 & 4)
# 2. once number starts, only numbers should come ahead until a space is reached (given assumption)
# 3. if punctuations are used in input, overall should be in speech marks as the some punctuation could cause a terminal error
# 4. As ">" has the same braille as "o" so keep track if we get "<", otherwise convert to "o" 
#    (logical assumption for when a closing arrow is used)

# IMPORTANT!
# Observations Below:
# 1. if there are multiple inputs add space between each input
# 2. some punctuations cause errors on the terminal too, ie !, <, etc. (points to assumption 2 above)

import sys

ALPHABET_TO_BRAILLE = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", 
                       "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
                         "q": "OOOOO.", "r": "O.OOO.", "s": ".00.0.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
                           "y": "OO.OOO", "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
                             "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......", '.': '..OO.O', ',': '..O...', '?': '..O.OO', 
                             '!': '..OOO.', ':': '..OO..',';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O','>': 'O..OO.',
                               '(': 'O.O..O', ')': '.O.OO.', ' ': '......'}

BRAILLE_TO_ALPHABET = {value: key for key, value in ALPHABET_TO_BRAILLE.items() if key.isalpha()}
BRAILLE_TO_NUMBER = {value: key for key, value in ALPHABET_TO_BRAILLE.items() if key.isdigit()} 
BRAILLE_TO_PUNCTUATION = {value: key for key, value in ALPHABET_TO_BRAILLE.items() if not key.isalnum()} # Includes space


# special chars
cap_follows = ".....O"
num_follows = ".O.OOO"
space = "......"
# dec_follows = ".O...O" # Not Needed

# if not divisible by 6, definitely not braille
# if any 6 subset does not match braille letter/number then its alphabet and needs to be converted
def is_braille(input):
    if len(input) % 6 != 0:
        return False
    for i in range(0, len(input), 6):
        temp = input[i:i+6]
        if temp not in BRAILLE_TO_ALPHABET and temp not in BRAILLE_TO_NUMBER and temp not in BRAILLE_TO_PUNCTUATION and temp != cap_follows and temp != num_follows and temp != space:
            return False
    return True
            

def translate_alpha_to_braille(input):
    num_started = False
    res = ""
    for letter in input:
        if letter.isupper():
            res += cap_follows
            res += ALPHABET_TO_BRAILLE[letter.lower()]
        elif letter.isdigit():
            if not num_started:
                res += num_follows
                res += ALPHABET_TO_BRAILLE[letter]
                num_started = True
            else:
                res += ALPHABET_TO_BRAILLE[letter]
        elif letter == " " and num_started:
            res += ALPHABET_TO_BRAILLE[letter]
            num_started = False
        else:
            res += ALPHABET_TO_BRAILLE[letter]
    return res
    

def translate_braille_to_alpha(input):
    openArrowFlag = False
    openArrowCounter = 0
    res = ""
    i = 0
    while i < len(input):
        temp = input[i:i+6]
        if temp == cap_follows:
            i += 6
            res += BRAILLE_TO_ALPHABET[input[i:i+6]].upper()
        elif temp == num_follows:
            i += 6
            number = ""
            while input[i:i+6] != space and i < len(input):
                number += BRAILLE_TO_NUMBER[input[i:i+6]]
                i += 6
            i -= 6
            res += number
        else:
            if temp in BRAILLE_TO_PUNCTUATION and BRAILLE_TO_PUNCTUATION[temp] == "<":
                openArrowFlag = True
                openArrowCounter += 1
                res += "<"
            elif openArrowFlag and temp in BRAILLE_TO_PUNCTUATION and BRAILLE_TO_PUNCTUATION[temp] == ">":
                openArrowCounter -= 1
                if openArrowCounter == 0:
                    openArrowFlag = False
                res += ">"
            elif temp in BRAILLE_TO_ALPHABET:
                res += BRAILLE_TO_ALPHABET[temp]
            else:
                res += BRAILLE_TO_PUNCTUATION[temp]  
        i += 6
    return res



if __name__ == "__main__":
    # No arguments provided
    if len(sys.argv) <= 1:
        print("")
    input = ' '.join(sys.argv[1:])
    if is_braille(input):
        print(translate_braille_to_alpha(input))
    else:
        print(translate_alpha_to_braille(input))