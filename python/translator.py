import sys
from translation_to_braille import translate_to_braille
from translation_to_english import translate_to_english

def is_text_braille(text: str) -> bool:
    braille_characters = ["O", "."]

    for char in text:
        if char not in braille_characters:
            return False

    return True

def translate(text: str) -> str:
    print(" we are in here")
    if not is_text_braille(text):
        return translate_to_braille(text)
    
    return translate_to_english(text)
     
def main():
    args = sys.argv[1:]
    string_to_be_translated = ""

    for i, arg in enumerate(args):
        if i == len(args) - 1:
            string_to_be_translated += arg
        else:
            string_to_be_translated += arg + " "

    print(translate(string_to_be_translated))

if __name__ == "__main__":
    main()
