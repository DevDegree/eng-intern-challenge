from enum import Enum

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
    END_OF_NUMBER = 1
    START_AND_END_OF_NUMBER = 2
    
class Dictionaries:
    braille_symbols = {'o', '.'}

    braille_to_english = {
        'o.....': 'a',
        'o.o...': 'b',
        '.o.ooo': Modifier.NUM_FOLLOWS,
        '.....o': Modifier.CAPITAL_FOLLOWS,
        '.o...o': Modifier.DECIMAL_FOLLOWS,
        '......': ' ',
        '..o...': '.'
        #think about ideas on how to do this in a less manual / error-prone way before continuing
    }

    braille_to_digit = {
        'o.....': '1',
    }

    english_to_braille = {
        'a': 'o.....',
        'b': 'o.o...',
        ' ': '......',
        '.': '..o...',
        Modifier.NUM_FOLLOWS: '.o.ooo',
        Modifier.CAPITAL_FOLLOWS: '.....o',
        Modifier.DECIMAL_FOLLOWS: '.o...o',
    }

    digit_to_braille = {
        '1': 'o.....',
    }


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

def classify_braille_char(curr_char, char_type):
        # Modifiers
        if curr_char == Dictionaries.english_to_braille[Modifier.NUM_FOLLOWS]:
            return BrailleCharType.NUMBER_FOLLOWS_SYMBOL
        if curr_char == Dictionaries.english_to_braille[Modifier.DECIMAL_FOLLOWS]:
            return BrailleCharType.DECIMAL_FOLLOWS_SYMBOL
        if curr_char == Dictionaries.english_to_braille[Modifier.CAPITAL_FOLLOWS]:
            return BrailleCharType.CAPITAL_FOLLOWS_SYMBOL

        # If current character is not a modifier, check if it is impacted by a preceding modifier
        elif char_type == BrailleCharType.NUMBER_FOLLOWS_SYMBOL: # previous character was number follows
            return BrailleCharType.DIGIT
        elif char_type == BrailleCharType.DECIMAL_FOLLOWS_SYMBOL:
            return BrailleCharType.DIGIT # Assumes a decimal will always be followed by a number and not be the end of a number
        elif char_type == BrailleCharType.CAPITAL_FOLLOWS_SYMBOL:
            return BrailleCharType.CAPITAL_LETTER
        
        # Numbers
        elif char_type == BrailleCharType.DIGIT:
            if curr_char == Dictionaries.english_to_braille[' ']: # a space at the end of a number signifies the end of the number
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
        return Dictionaries.braille_to_digit[curr_char]
    elif char_type == BrailleCharType.CAPITAL_LETTER:
        return Dictionaries.braille_to_english[curr_char].upper()
    elif char_type == BrailleCharType.OTHER:
        return Dictionaries.braille_to_english[curr_char]
    elif char_type == BrailleCharType.END_OF_NUMBER:
        return '' # modifier only, no translation needed
    
def classify_english_char (curr_char, next_char, prev_char_type):
    modifier = None

    # Start and middle of numbers
    if curr_char.isnumeric():
        # Check if current character is the start of a number
        if prev_char_type not in [EnglishCharType.DIGIT, EnglishCharType.DECIMAL]: # Preceding character was a number or decimal
            
            # Check if current character is also the end of a number
            if not next_char.isnumeric() and next_char != '.':
                modifier = BrailleOutputModifier.START_AND_END_OF_NUMBER
            
            else:
                modifier = BrailleOutputModifier.START_OF_NUMBER

        # Set char_type of current character
        char_type = EnglishCharType.DIGIT
    
    # End of numbers
    elif prev_char_type == EnglishCharType.DIGIT and not curr_char.isnumeric(): # Assumes a number will never end with a decimal character
        modifier = BrailleOutputModifier.END_OF_NUMBER
    
    # Decimals
    elif curr_char == '.' and next_char.isnumeric():
        # Check if decimal is the start of a number
        if prev_char_type != EnglishCharType.DIGIT:
            modifier = BrailleOutputModifier.START_OF_NUMBER
        
        char_type = EnglishCharType.DECIMAL

    # Capital Letters
    elif curr_char.isupper():
        char_type = EnglishCharType.CAPITAL_LETTER
    
    
    # Other
    else:
        char_type = EnglishCharType.OTHER
    
    return {"char_type": char_type, "modifier": modifier}
        
def translate_english_char (curr_char, char_type, modifier):
    output = []
    # Add NUM_FOLLOWS for the start of a number if necessary
    if modifier in [BrailleOutputModifier.START_AND_END_OF_NUMBER, BrailleOutputModifier.START_OF_NUMBER]:
        output.append(Dictionaries.english_to_braille[Modifier.NUM_FOLLOWS])
    
    # Translate characters based on type
    if char_type == EnglishCharType.CAPITAL_LETTER:
        output.append(Dictionaries.english_to_braille[Modifier.CAPITAL_FOLLOWS])
        output.append(Dictionaries.english_to_braille[curr_char.lower()])
    elif char_type == EnglishCharType.DECIMAL:
        output.append(Dictionaries.english_to_braille[Modifier.DECIMAL_FOLLOWS])
    elif char_type == EnglishCharType.DIGIT:
        output.append(Dictionaries.digit_to_braille[curr_char])
    elif char_type == EnglishCharType.OTHER:
        output.append(Dictionaries.english_to_braille[curr_char])

    # Add space to signify end of number if necessary
    if modifier in [BrailleOutputModifier.START_AND_END_OF_NUMBER, BrailleOutputModifier.END_OF_NUMBER]:
        output.append(Dictionaries.english_to_braille[' '])
    
    return output

def translate_braille_to_english(input):
    output = []
    braille_characters = separate_braille_characters(input)
    char_type = None # state of the current character being translated

    for char in braille_characters:
        char_type = classify_braille_char(char, char_type) # First determine whether a character's state is a modifier, a number, a capital letter, or other symbol
        char_translation = translate_braille_char(char, char_type) # Translate based on current character's identified state

        output.append(char_translation)
  
    return ''.join(output) # Join translated characters into a single string

def translate_english_to_braille(input):
    output = []
    char_type = None
    
    for n in range(len(input)):
        curr_char = input[n]
        if n == len(input)-1:
            next_char = None
        else:
            next_char = input[n+1]
        
        char_type_and_modifier = classify_english_char(curr_char, next_char, char_type)
        char_translation = translate_english_char (curr_char, char_type_and_modifier["char_type"], char_type_and_modifier["modifier"])
        
        for symbol in char_translation: # Braille translation of a single English character may require 2-3 symbols
            output.append(symbol)
        
    return ''.join(output) # Join translated characters into a single string

def translate_input(input):
    input_language = detect_language(input)
    if input_language == Language.BRAILLE:
        return translate_braille_to_english(input)
    elif input_language == Language.ENGLISH:
        return translate_english_to_braille(input)
    
def main():
    inp = input("Enter text to translate: ")
    print (translate_input(inp))
    return translate_input(inp)

main()