from enum import Enum
import sys # Handles system arguments

class Language (Enum):
    BRAILLE = 0
    ENGLISH = 1

class Modifier (Enum):
    CAPITAL_FOLLOWS = 0
    NUM_FOLLOWS = 1
    DECIMAL_FOLLOWS = 2

class BrailleCharType (Enum):
    NUMBER_FOLLOWS_SYMBOL = 0
    DECIMAL_FOLLOWS_SYMBOL = 1
    CAPITAL_FOLLOWS_SYMBOL = 2
    DIGIT = 3
    CAPITAL_LETTER = 4
    OTHER = 5
    END_OF_NUMBER = 6

class EnglishCharType (Enum):
    DIGIT = 0
    DECIMAL = 1
    CAPITAL_LETTER = 2
    OTHER = 3

class BrailleOutputModifier (Enum):
    START_OF_NUMBER = 0

def invert_dictionary(dict):
    inverted_dict = {}
    for key, val in dict.items():
        inverted_dict[val] = key
    
    return inverted_dict
        
    
class Dictionaries:
    braille_symbols = {'O', '.'}
    
    english_to_braille = {
        'a': 'O.....', 
        'b': 'O.O...', 
        'c': 'OO....', 
        'd': 'OO.O..', 
        'e': 'O..O..',
        'f': 'OOO...', 
        'g': 'OOOO..', 
        'h': 'O.OO..', 
        'i': '.OO...', 
        'j': '.OOO..',
        'k': 'O...O.', 
        'l': 'O.O.O.', 
        'm': 'OO..O.', 
        'n': 'OO.OO.', 
        'o': 'O..OO.',
        'p': 'OOO.O.', 
        'q': 'OOOOO.', 
        'r': 'O.OOO.', 
        's': '.OO.O.', 
        't': '.OOOO.',
        'u': 'O...OO', 
        'v': 'O.O.OO', 
        'w': '.OOO.O', 
        'x': 'OO..OO', 
        'y': 'OO.OOO', 
        'z': 'O..OOO',
        ' ': '......',
        '1': 'O.....', 
        '2': 'O.O...', 
        '3': 'OO....', 
        '4': 'OO.O..', 
        '5': 'O..O..',
        '6': 'OOO...', 
        '7': 'OOOO..', 
        '8': 'O.OO..', 
        '9': '.OO...', 
        '0': '.OOO..',
        Modifier.NUM_FOLLOWS: '.O.OOO',
        Modifier.CAPITAL_FOLLOWS: '.....O',
        Modifier.DECIMAL_FOLLOWS: '.O...O'
    }
    
    braille_to_english = invert_dictionary(english_to_braille)

def detect_language(input):
    for char in input:
        if char not in Dictionaries.braille_symbols:
            return Language.ENGLISH
    return Language.BRAILLE

def separate_braille_characters(input):
    braille_characters = []
    char_start = 0
    char_end = 6
    input_length = len(input)
    while char_end <= input_length:
        braille_characters.append(input[char_start:char_end])
        char_start += 6
        char_end +=6
    return braille_characters

def classify_braille_char(curr_char, prev_char_type):
        # Modifiers
        if curr_char == Dictionaries.english_to_braille[Modifier.NUM_FOLLOWS]:
            return BrailleCharType.NUMBER_FOLLOWS_SYMBOL
        if curr_char == Dictionaries.english_to_braille[Modifier.DECIMAL_FOLLOWS]:
            return BrailleCharType.DECIMAL_FOLLOWS_SYMBOL
        if curr_char == Dictionaries.english_to_braille[Modifier.CAPITAL_FOLLOWS]:
            return BrailleCharType.CAPITAL_FOLLOWS_SYMBOL

        # If current character is not a modifier, check if it is impacted by a preceding modifier
        elif prev_char_type == BrailleCharType.NUMBER_FOLLOWS_SYMBOL: # previous character was number follows
            return BrailleCharType.DIGIT
        elif prev_char_type == BrailleCharType.DECIMAL_FOLLOWS_SYMBOL:
            return BrailleCharType.DIGIT # Assumes a decimal will always be followed by a number and not be the end of a number
        elif prev_char_type == BrailleCharType.CAPITAL_FOLLOWS_SYMBOL:
            return BrailleCharType.CAPITAL_LETTER
        
        # Numbers
        elif prev_char_type == BrailleCharType.DIGIT:
            if curr_char == Dictionaries.english_to_braille[' ']: # a space at the end of a string of digits signifies the end of the number
                return BrailleCharType.END_OF_NUMBER
            else:
                return BrailleCharType.DIGIT
        
        # Lowercase letters and punctuation
        else:
            return BrailleCharType.OTHER

def translate_braille_char(curr_char, char_type):
    if char_type == BrailleCharType.NUMBER_FOLLOWS_SYMBOL:
        return '' # modifier only, no translation needed
    elif char_type == BrailleCharType.DECIMAL_FOLLOWS_SYMBOL:
        return '.'
    elif char_type == BrailleCharType.CAPITAL_FOLLOWS_SYMBOL:
        return '' # modifier only, no translation needed
    elif char_type == BrailleCharType.DIGIT:
        return Dictionaries.braille_to_english[curr_char]
    elif char_type == BrailleCharType.CAPITAL_LETTER:
        return Dictionaries.braille_to_english[curr_char].upper()
    elif char_type == BrailleCharType.OTHER:
        return Dictionaries.braille_to_english[curr_char]
    elif char_type == BrailleCharType.END_OF_NUMBER:
        return ' ' # space signifies end of number in braille
    
def classify_english_char (curr_char, next_char, prev_char_type):
    modifier = None

    # Numbers
    if curr_char.isnumeric():
        # Set char_type of current character
        char_type = EnglishCharType.DIGIT
    
    # Decimals
    elif curr_char == '.' and next_char.isnumeric():
        char_type = EnglishCharType.DECIMAL

    # Capital Letters
    elif curr_char.isupper():
        char_type = EnglishCharType.CAPITAL_LETTER
    
    # Other
    else:
        char_type = EnglishCharType.OTHER
    

    # Modifiers
    # Start of numbers
    if char_type in [EnglishCharType.DIGIT, EnglishCharType.DECIMAL]:
        # Check if current character is the start of a number
        if prev_char_type not in [EnglishCharType.DIGIT, EnglishCharType.DECIMAL]: # Preceding character was not a number or decimal
            modifier = BrailleOutputModifier.START_OF_NUMBER
    
    return {"char_type": char_type, "modifier": modifier}
        
def translate_english_char (curr_char, char_type, modifier):
    output = []
    # Add NUM_FOLLOWS for the start of a number if applicable
    if modifier == BrailleOutputModifier.START_OF_NUMBER:
        output.append(Dictionaries.english_to_braille[Modifier.NUM_FOLLOWS])
    
    # Translate characters based on type
    if char_type == EnglishCharType.CAPITAL_LETTER:
        output.append(Dictionaries.english_to_braille[Modifier.CAPITAL_FOLLOWS])
        output.append(Dictionaries.english_to_braille[curr_char.lower()])
    elif char_type == EnglishCharType.DECIMAL:
        output.append(Dictionaries.english_to_braille[Modifier.DECIMAL_FOLLOWS])
    else:
        output.append(Dictionaries.english_to_braille[curr_char])
    
    return output

def translate_braille_to_english(input):
    output = []
    braille_characters = separate_braille_characters(input)
    char_type = None # state of the previous character that was translated or the current character being translated

    for char in braille_characters:
        char_type = classify_braille_char(char, char_type) # First determine whether a character's state is a modifier, a number, a capital letter, or other symbol
        char_translation = translate_braille_char(char, char_type) # Translate based on current character's identified type
        output.append(char_translation)
  
    return ''.join(output) # Join translated characters into a single string

def translate_english_to_braille(input):
    output = []
    prev_char_type = None # state of the previous character that was translated or the current character being translated
    
    for n in range(len(input)):
        curr_char = input[n]
        if n == len(input)-1:
            next_char = None
        else:
            next_char = input[n+1]
        
        curr_char_state = classify_english_char(curr_char, next_char, prev_char_type)
        char_translation = translate_english_char (curr_char, curr_char_state["char_type"], curr_char_state["modifier"])
        
        for symbol in char_translation: # Braille translation of a single English character may require 2-3 symbols
            output.append(symbol)
        
        prev_char_type = curr_char_state["char_type"]
        
    return ''.join(output) # Join translated characters into a single string

def translate_input(input):
    input_language = detect_language(input)
    if input_language == Language.BRAILLE:
        return translate_braille_to_english(input)
    elif input_language == Language.ENGLISH:
        return translate_english_to_braille(input)

if __name__ == '__main__': 
    full_input = ' '.join(sys.argv[1:])
    output = translate_input(full_input)
    print(output)