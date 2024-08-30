# 08-29-2024
# Albert Nguyen-Tran
# albert.nguyen.tran1@gmail.com

import sys
import re

'''
Clarifications/Assumptions:

1) Capital follows (".....O") can only be used for the next character
    - In the example Hello -> uses a "capital follows" once before the H and then returns to all lowercase
    - I will assume a character MUST come next

2) Number follows (".O.OOO") is binding until a space and always needs to be used
    - Therefore "abc123" and "456" are valid
    - But "123abc" and "456A" are not valid because all following symbols starting from a number follows must be a number until a space
        - note that the abc after 123 could get read as numbers since they have a corresponding mapping
        - therefore I asssume that only numbers MUST follow

3) The braille to english mapping for numbers is not consistent in the examples
    - In the example 42, 2 is mapped to "O.O..."
    - But in the example ABC 123, 2 is mapped to "OO...." because it seems like the number system is from 0-9 instead of 1-9 then 0
    - In the README spec, it says to include "... the numbers 0 THROUGH 9"
    - The test in the translator.test.py goes by the same numbering system
    - Therefore I will assume the number system follows the latter example where 2 is mapped to "OO...."

4) Alphabet must only consist of letters from a to z, numbers 0-9 and the ability to include spaces and capitalize

5) Based on the standard behaviour of sys.argv, only singular spaces can be translated from english to braille
'''

braille_mapping = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.','p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '0': 'O.....', '1': 'O.O...', '2': 'OO....', '3': 'OO.O..', '4': 'O..O..', '5': 'OOO...', '6': 'OOOO..', '7': 'O.OO..', '8': '.OO...', '9': '.OOO..',
    'capital_follows': '.....O',
    'number_follows': '.O.OOO',
    ' ': '......',
}

english_character_mapping = {b: s for s, b in braille_mapping.items() if not s.isdigit()}
english_number_mapping = {b: s for s, b in braille_mapping.items() if s.isdigit()}

def chunk_braille(braille):
    return [braille[i:i+6] for i in range(0, len(braille), 6)]

def braille_to_english(braille):
    # it is asserted that the length of the braille string must be a multiple 6, and if it was 0 we would have returned an empty string already
    symbols = chunk_braille(braille)
    english_translation = ""
    number_follows = False
    capital_follows = False

    for symbol in symbols:

        # space
        if symbol == '......':
            assert not capital_follows
            number_follows = False
            english_translation += english_character_mapping[symbol]
        
        # capital follows
        elif symbol == '.....O':
            assert not number_follows and not capital_follows
            capital_follows = True
        
        # number follows
        elif symbol == '.O.OOO':
            assert not number_follows and not capital_follows
            number_follows = True
        
        # is a number
        elif number_follows:
            # based on clarification 2, we must have numbers until a space
            assert symbol in english_number_mapping
            english_translation += english_number_mapping[symbol]
        
        # is a letter
        elif symbol in english_character_mapping and english_character_mapping[symbol].isalpha():
            assert not number_follows
            if capital_follows:
                english_translation += english_character_mapping[symbol].upper()
            else:
                english_translation += english_character_mapping[symbol]
            capital_follows = False
            
        # else is an invalid character
        else:
            assert symbol in braille_mapping
    
    return english_translation

def english_to_braille(words):
    allowed = re.compile(r'[\w]')
    braille_translation = ""
    number_follows = False

    for i, word in enumerate(words):
        # based on clarification 4 (e.g. "a+b{c") 
        assert len(allowed.findall(word)) == len(word)

        for c in word:
            if c.isdigit() and not number_follows:
                number_follows = True
                braille_translation += braille_mapping['number_follows']
                  
            if number_follows:
                # based on clarification 2 all symbols that follow must be digits until the next space (e.g. "123a")
                assert c.isdigit()
                braille_translation += braille_mapping[c]
            
            else:
                # based on clarification 1 capital follows only works for next character
                if c.isupper():
                    braille_translation += braille_mapping['capital_follows']
                braille_translation += braille_mapping[c.lower()]

        # reset inserting_numbers and add space if this is not the last word
        if i < len(words)-1:
            number_follows = False
            braille_translation += braille_mapping[' ']

    return braille_translation

def main():
    args = sys.argv[1:]

    if not args or (args and not args[0]):
        return ""
   
    if len(args) == 1 and len(args[0]) % 6 == 0 and all(c in {"O", "."} for c in args[0]):
        translated = braille_to_english(args[0])
    else:
        translated = english_to_braille(args)

    return translated


if __name__ == "__main__":
    translated_string = main()
    print(translated_string)