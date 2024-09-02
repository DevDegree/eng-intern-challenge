import sys
from alphabets import english_alphabet, braille_alphabet


def detect_language(input_list):
    ''' 
    Assumptions:
    English input that consists of multiple words (e.g., "hello world") is always represented as separate entries in input_list.
    Braille input that consists of multiple words (e.g., ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...." -> "Abc" "123) is always a single entry in input_list
    Strings like "O.", which are invalid English and Braille, will be inputed.

    Parameters:
    input_list -- list of strings

    Returns:
    0 for English
    1 for Braille
    '''
    if (len(input_list) > 1):
        return 0
    
    if (len(input_list[0]) < 6):
        return 0
    
    unique_characters = set()
    for character in input_list[0]:
        unique_characters.add(character)
    
    if (len(unique_characters) > 2):
        return 0
    
    return 1


def merge_english_words(english_words):
    '''
    Combine separate English words into a single string

    Parameters:
    english_words -- a list of english words

    Returns:
    A string
    '''
    result = ""
    for i in range(len(english_words)):
        result += english_words[i]

        if (i != (len(english_words) - 1)):
            result += " "

    return result


def english_to_braille(sentence):
    '''
    Transform text in English to Braille

    Parameters:
    sentence -- a string representing any number of english words

    Returns
    A string
    '''
    num_added = False
    result = ""
    for character in sentence:
        if (character.isdigit() and not num_added):
            num_added = True
            result += english_alphabet['digit']

        if (character == ' '):
            num_added = False

        result += english_alphabet[character]

    return result


def braille_to_english(sentence):
    '''
    Transform text in Braille to English

    Parameters:
    sentence -- a string representing a sequence of Braille characters

    Returns
    A string    
    '''
    digit_flag = False
    capital_flag = False
    result = ""
    i = 0
    chunk = ""

    while i < len(sentence):
        chunk += sentence[i]
        i += 1

        if (len(chunk) == 6):

            english = braille_alphabet[chunk]

            if (english == 'digit'):
                digit_flag = True

            elif (english == 'capital'):
                capital_flag = True

            elif(english == ' '):
                result += english
                digit_flag = False

            elif (digit_flag):
                result += braille_alphabet[english_alphabet['digit'] + chunk]

            elif (capital_flag):
                result += english.upper()
                capital_flag = False

            else:
                result += english

            chunk = ''
        

    return result


if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        print("Error: Not enough arguments.")
        print("Usage: python3 translator.py <words to translate>")
        print("Examples:")
        print("\t- python3 translator.py hello world")
        print("\t- python3 translator.py .O.OOOOO.O..O.O...")
        exit()

    language = detect_language(sys.argv[1:])

    if (language): # is Braille
        print(braille_to_english(sys.argv[1]))

    else: # is English 
        sentence = merge_english_words(sys.argv[1:])
        print(english_to_braille(sentence))

    

