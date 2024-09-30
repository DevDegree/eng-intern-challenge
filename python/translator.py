import sys
from typing import List

CHARACTERS_TO_BRAILLE = {
    # Standard characters to handle
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
    # Special sequences for capitalization or digits
    # as defined in the tech spec.
    "CAPITAL_FOLLOWS": ".....O",
    "NUMBER_FOLLOWS":  ".O.OOO",
    # NOTE: these are added for potential future use
    # as the tech spec. does not define their useage
    # the inclusion of them could be considered UB
    # thus they have been removed for now
    # ".": "..OO.O",
    # ",": "..O...",
    # "?": "..O.OO",
    # "!": "..OOO.",
    # ":": "..OO..",
    # ";": "..O.O.",
    # "-": "....OO",
    # "/": ".O..O.",
    # "<": ".OO..O",
    # ">": "O..OO.",
    # "(": "O.O..O",
    # ")": ".O.OO.",
}

DIGIT_TO_CHARACTER = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "0": "j"
}

BRAILLE_TO_CHARACTERS = {v:k for k,v in CHARACTERS_TO_BRAILLE.items()}

CHARACTERS_TO_DIGITS = {v:k for k,v in DIGIT_TO_CHARACTER.items()}

# take in list of word, return string
def text_to_braille(text: List[str]) -> str:
    '''
    Converts a list of words into a braille string

    Args:
        text (List[str]): A list of words to be converted into braille

    Returns:
        str: A string where each word is represented in braille, seperated by braille spaces
    '''
    # store result as array of words
    braille_words = []

    for word in text:
        braille_word = ""

        # set word_is_digits flag based on first character of the word
        # if the character is a digit, assume all others in word as 
        # also digits as defined in tech spec.
        word_is_digits = False
        if word[0].isdigit():
                braille_word += CHARACTERS_TO_BRAILLE["NUMBER_FOLLOWS"]
                word_is_digits = True

        for character in word:
            # if character is capitalized add "capitalize follow" to the 
            # result sequence to the result 
            if character.isupper():
                braille_word += CHARACTERS_TO_BRAILLE["CAPITAL_FOLLOWS"]
                character = character.lower()

            # if the word is a digit, convert this digit 
            # to the associated charater
            if word_is_digits:
                character = DIGIT_TO_CHARACTER[character]

            # add the character in braille to current word result
            braille_word += CHARACTERS_TO_BRAILLE[character]
        
        # add our word to results list
        braille_words.append(braille_word)

    # join our result using the space character as 
    # defined in our table and return string
    return CHARACTERS_TO_BRAILLE[" "].join(braille_words)

def braille_to_text(braille: str) -> str:
    '''
    Converts a braille string back into text

    Args:
        braille (str): A braille string where each character is represented by the established sequences

    Returns:
        str: The text this braille respresents
    '''
    result = ""

    # control flags
    capitalize_following = False
    word_is_digits = False

    # split braille into chunks of 6 characters, as each chunk of 6
    # is one character, or one control character 
    for chunk in range(0, len(braille), 6):
        # extract our single character
        braille_character = braille[chunk:chunk+6]

        # check if character is number sequence, if true toggle flag and continue
        if braille_character == CHARACTERS_TO_BRAILLE["NUMBER_FOLLOWS"]:
            word_is_digits = True
            continue
        # if character is capitalize sequence, toggle flag and continue
        elif braille_character == CHARACTERS_TO_BRAILLE["CAPITAL_FOLLOWS"]:
            capitalize_following = True
            continue
        # if character is space, take this time to untoggle word_is_digits 
        elif braille_character == CHARACTERS_TO_BRAILLE[" "]:
            word_is_digits = False
        
        # get associated character
        character = BRAILLE_TO_CHARACTERS[braille_character]

        # if character is supposed to be digit, map this character
        # to the associated digit
        if word_is_digits:
            character = CHARACTERS_TO_DIGITS[character]
        
        # if capitalization flag was set, capitalize character
        if capitalize_following:
            character = character.capitalize()
            capitalize_following = False

        # add character to result
        result += character
    
    return result

if __name__ == "__main__":
    input = sys.argv[1::]

    if len(input) == 1 and all(point == '.' or point == 'O' for point in input[0]):
        result = braille_to_text(input[0])
    else:
        result = text_to_braille(input)

    print(result, end="")