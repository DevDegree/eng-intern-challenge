from enum import Enum

class Language (Enum):
    BRAILLE = 0
    ENGLISH = 1

class Modifier (Enum):
    CAPITAL_FOLLOWS = 0
    NUM_FOLLOWS = 1
    DECIMAL_FOLLOWS = 2

class CurrentCharState (Enum):
    NUMBER = 0
    UPPERCASE_LETTER = 1
    DECIMAL = 2
    OTHER = 3

class Dictionaries:
    braille_symbols = {'o', '.'}

    braille_to_english = {
        'o.....': 'a',
        'o.o...': 'b',
        '.o.ooo': Modifier.NUM_FOLLOWS,
        '.....o': Modifier.CAPITAL_FOLLOWS,
        '.o...o': Modifier.DECIMAL_FOLLOWS,
        '......': ' '
        #think about ideas on how to do this in a less manual / error-prone way before continuing
    }

    braille_to_num = {
        'o.....': '1',
    }

    english_to_braille = {
        'a': 'o.....',
        'b': 'o.o...',
        ' ': '......',
        Modifier.NUM_FOLLOWS: '.o.ooo',
        Modifier.CAPITAL_FOLLOWS: '.....o',
        Modifier.DECIMAL_FOLLOWS: '.o...o',
    }

    num_to_braille = {
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

def translate_braille_to_english(input):
    output = ''
    translated_char = ''
    braille_characters = separate_braille_characters(input)
    #isCapital = False
    #isNum = False
    for char in braille_characters:
        translated_char = Dictionaries.braille_to_english[char]
        if isNum and translated_char not in [Modifier.DECIMAL_FOLLOWS, ' ']:
            translated_char = Dictionaries.braille_to_num[char] #search the number dictionary instead of the letter / symbol dictionary
            output += translated_char
        elif isCapital:
            output += translated_char.upper()
            isCapital = False #only capitalize the character immediately after capital follows symbol
        else:
            if translated_char == Modifier.CAPITAL_FOLLOWS:
                isCapital = True
            elif translated_char == Modifier.NUM_FOLLOWS:
                isNum = True
            elif isNum and translated_char == ' ':
                isNum = False
                output += ' '
            elif translated_char == Modifier.DECIMAL_FOLLOWS:
                output += '.'
            else:
                output += translated_char
    return output

def translate_english_to_braille(input):
    output = ''
    translated_char = ''
    #isNum = False
    for n in range(len(input)):
        char = input[n]
        # Periods and decimals
        if char == '.':
            # If current position is not in the middle of a number
            if isNum == False:
                next_char = input[n+1]
                # If current character is a decimal at the beginning of a number
                if next_char.isnumeric():
                    isNum = True
                    output += Dictionaries.english_to_braille[Modifier.NUM_FOLLOWS]
                else:
                    output += Dictionaries.english_to_braille[char]
            # If current position is in the middle of a number
            else:
                output += Dictionaries.english_to_braille[Modifier.DECIMAL_FOLLOWS]

        # Numeric characters
        elif char.isnumeric():
            if isNum == False:
                isNum = True
                output += Dictionaries.english_to_braille[Modifier.NUM_FOLLOWS]
            output += Dictionaries.num_to_braille[char]

        # Letters and non-period punctuation
        else:
            # End of numeric characters
            if isNum == True: #Adds a space to signify the end of a number
                isNum = False
                output += Dictionaries.english_to_braille[' ']
        
            # Capitals
            if char.isupper():
                output += Dictionaries.english_to_braille[Modifier.CAPITAL_FOLLOWS]
                output += Dictionaries.english_to_braille[char.lower()]

            # Lowercase or non-period punctuation
            else:
                output += Dictionaries.english_to_braille[char]
        
    return output

def translate_input(input):
    input_language = detect_language(input)
    if input_language == Language.BRAILLE:
        return translate_braille_to_english(input)
    elif input_language == Language.ENGLISH:
        return translate_english_to_braille(input)
    
def main():
    input = input("Enter text to translate: ")
    return translate_input(input)
