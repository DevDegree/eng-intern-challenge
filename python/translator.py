import sys
from braille_to_english import braille_to_english
from english_to_braille import english_to_braille

if __name__ == "__main__":
    arguments = sys.argv[1:]
    combined_text = " ".join(arguments)
    if(set(combined_text).issubset(set([".","O"]) ) ):
        result = braille_to_english(combined_text)
    else:
        result = english_to_braille(combined_text)
    print(result)