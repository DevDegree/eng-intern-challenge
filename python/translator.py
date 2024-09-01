import sys


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


if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        print("Error: Not enough arguments.")
        print("Usage: python3 translator.py <words to translate>")
        print("Examples:")
        print("\t- python3 translator.py hello world")
        print("\t- python3 translator.py .O.OOOOO.O..O.O...")
        exit()