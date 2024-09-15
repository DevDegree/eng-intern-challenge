import sys

def is_text_braille(text: str) -> bool:
    braille_characters = ["O", "."]

    for char in text:
        if char not in braille_characters:
            return False

    return True

def translate(text: str) -> str:
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
    
    SOLUTION_STRING = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
    print(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
    

if __name__ == "__main__":
    main()
