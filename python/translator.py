import sys

BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"

eng_to_braille_map = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..OOO.",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

eng_to_braille_number_map = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

braille_to_eng_map = dict((v,k) for k,v in eng_to_braille_map.items())

braille_to_eng_number_map = dict((v,k) for k,v in eng_to_braille_number_map.items())

def main():
    # If we have no arguments just return empty string
    if len(sys.argv) < 2:
        print("")
        quit()

    arguments = sys.argv[1:]

    # Need to check the type of conversion
    isBraille = arguments[0][0] in ['0', '.']

    # Do the conversion
    if isBraille:
        convert_to_english(arguments)
    else:
        convert_to_braille(arguments)



def convert_to_english(arguments):
    text = arguments[0]
    seperated_braille_arr = [text[i:i+6] for i in range(0, len(text), 6)]
    capital_follows = False
    number_follows = False
    for character in seperated_braille_arr:
        if character == BRAILLE_CAPITAL_FOLLOWS:
            capital_follows = True
        elif character == BRAILLE_NUMBER_FOLLOWS:
            number_follows = True
        elif capital_follows:
            english_character = braille_to_eng_map[character]
            english_character = english_character.upper()
            print(english_character, end="")    
            capital_follows = False
        elif braille_to_eng_map[character] == " ":
            english_character = braille_to_eng_map[character]
            print(english_character, end="")
            number_follows = False
        elif number_follows:
            english_number = braille_to_eng_number_map[character]
            print(english_number, end="")
        else:
            english_character = braille_to_eng_map[character]
            print(english_character, end="")

    print()


def convert_to_braille(arguments):
    text = " ".join(arguments)
    is_first_number = True
    for character in text:
        if character.isupper():
            print(BRAILLE_CAPITAL_FOLLOWS, end="")
            lower_char = character.lower()
            braille_character = eng_to_braille_map[lower_char]
            print(braille_character, end="")
        elif character == " ":
            is_first_number = True
            braille_character = eng_to_braille_map[character]
            print(braille_character, end="")
        elif character in ['1','2','3','4','5','6','7','8','9','0']:
            if is_first_number:
                print(BRAILLE_NUMBER_FOLLOWS, end="")
                is_first_number = False
            
            braille_character = eng_to_braille_number_map[character]
            print(braille_character, end="")
            
        else:    
            braille_character = eng_to_braille_map[character]
            print(braille_character, end="")
    
    print()




if __name__ == "__main__":
    main()
