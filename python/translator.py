import sys

# braile dictionaries

ENGLISH_BRAILLE_DICT = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", "capital": ".....O", "decimal": ".O...O", "number": ".O.OOO", ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.", "(": "O.O..O", ")": ".O.OO.", " ": "......"}

NUMBER_BRAILLE_DICT = {"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......"}

BRAILLE_NUMBER_DICT = {v: k for k, v in NUMBER_BRAILLE_DICT.items()}

BRAILLE_ENGLISH_DICT = {v: k for k, v in ENGLISH_BRAILLE_DICT.items()}


# check if a string is braille or english where braille is represented by dots and Os
def is_braille(s):
    '''
    Check if a string is braille or english

    Args:
        s: string
    
    Returns:
        True if the string is braille, False otherwise
    '''
    for i in s:
        if i not in ['.', 'O']:
            return False
    return True



def braile_to_english(s):
    '''
    Translate braille to english

    Args:
        s: string
    
    Returns:
        English translation of the braille string
    '''

    result = ""
    Capital = False
    Number = False
    for i in range(0, len(s), 6):
        # get the 6 characters
        letter = s[i:i+6]
        # loop through the dictionary
        if letter in BRAILLE_ENGLISH_DICT:
            if BRAILLE_ENGLISH_DICT[letter] == "capital":
                Capital = True
                continue
            elif BRAILLE_ENGLISH_DICT[letter] == "number":
                Number = True
                continue
            if Capital:
                result += BRAILLE_ENGLISH_DICT[letter].upper()
                Capital = False
            elif Number and BRAILLE_ENGLISH_DICT[letter] == " ":
                result += BRAILLE_ENGLISH_DICT[letter]
                Number = False
            elif Number:
                result += BRAILLE_NUMBER_DICT[letter]
            else:
                result += BRAILLE_ENGLISH_DICT[letter]
    
    return result


# Translate english to braile

def english_to_braille(s):
    '''
    Translate english to braille

    Args:
        s: string

    Returns:
        Braille translation of the english string
    '''
    result = ""
    number = False
    for i in s:
        if i.isupper():
            result += ENGLISH_BRAILLE_DICT["capital"]
            result += ENGLISH_BRAILLE_DICT[i.lower()]
        elif i.isdigit():
            if not number:
                result += ENGLISH_BRAILLE_DICT["number"]
                number = True
            result += NUMBER_BRAILLE_DICT[i]
        elif i == " ":
            result += ENGLISH_BRAILLE_DICT[i]
            number = False
        else:
            result += ENGLISH_BRAILLE_DICT[i]

    return result

# Test cases
# print(braile_to_english(".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.."))
# print(english_to_braille("Hello world") == ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

def main():
    if len(sys.argv) < 2:
        print("Please provide an input string to be translated.")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    print(input_text)

    if is_braille(input_text):
        print(braile_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == '__main__':
    main()

