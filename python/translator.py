import sys

english_to_braille = {
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

capital_follows = ".....O"
number_follows = ".O.OOO"

number_to_braille = {
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

braille_to_english = dict((i,j) for j,i in english_to_braille.items())
braille_to_number = dict((i,j) for j,i in number_to_braille.items())

def main():

    if len(sys.argv) < 2:
        print("")
        return

    args = sys.argv[1:]
    is_braille = args[0][0] in ['0', '.']

    if is_braille:
        convert_to_english(args)
    else:
        convert_to_braille(args)

def convert_to_braille(args):
    text = " ".join(args)
    first_number = True
    
    for character in text:
        if character.isupper():
            print(capital_follows, end="")
            print(english_to_braille[character.lower()], end="")
        elif character == " ":
            first_number = True
            print(english_to_braille[character], end="")
        elif character in ['1','2','3','4','5','6','7','8','9','0']:
            if first_number:
                print(number_follows, end="")
                first_number = False
            
            print(number_to_braille[character], end="")
            
        else:    
            print(english_to_braille[character], end="")
    
    print()


def convert_to_english(args):
    text = args[0]
    braille_arr = [text[i:i+6] for i in range(0, len(text), 6)]
    capital_next = False
    number_next = False
    for character in braille_arr:
        if character == capital_follows:
            capital_next = True
        elif character == number_follows:
            number_next = True
        elif capital_next:
            print(braille_to_english[character].upper(), end="")    
            capital_next = False
        elif braille_to_english[character] == " ":
            print(braille_to_english[character], end="")
            number_next = False
        elif number_next:
            print(braille_to_number[character], end="")
        else:
            print(braille_to_english[character], end="")

    print()




if __name__ == "__main__":
    main()