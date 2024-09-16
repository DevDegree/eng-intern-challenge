import sys
import re

def is_braille(word):
    """ Checks if word is in Braille

    Valid braille words only contain O or . and are a length multiple of 6
    Keyword arguments:
    word - the string to check
    """
    
    return (bool(re.match('^[O\.]+$', word)) and len(word) % 6 == 0)

def braille_translator():
    return ""


if __name__ == "__main__":
    is_braille(sys.argv[1])