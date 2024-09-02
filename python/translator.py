import sys
from alphabets import english_alphabet


def detect_language(input_list):
    ''' 
    Assumptions:
    Each word in an input English phrase (e.g., "hello world") is a separate item in input_list.

    Arguments:
    input_list -- list of strings

    Returns:
    0 for English
    1 for Braille
    '''
    if (len(input_list) > 1):
        return 0
    
    characters = set()
    for character in input_list[0]:
        characters.add(character)
    
    if (len(characters) > 2):
        return 0
    
    return 1


def english_to_braille(sentence):
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


def merge_english_words(english_words):
    '''
    '''
    result = ""
    for i in range(len(english_words)):
        result += english_words[i]

        if (i != (len(english_words) - 1)):
            result += " "

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
        pass

    else: # is English 
        sentence = merge_english_words(sys.argv[1:])
        print(english_to_braille(sentence))

