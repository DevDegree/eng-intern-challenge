import sys

english_braille_map = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
    "9": ".OO...", "0":".OOO..", "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", 
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", 
    "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", " ": "......",
}
braille_english_map = {}
for key, value in english_braille_map.items():
    braille_english_map[value] = key

        
def english_to_braille(english):
    braille = ""
    number_follows = False
    for char in english:
        if  char.isupper():
            braille += ".....O"
        elif char.isnumeric() and number_follows == False:       # check if numeric
            braille += ".O.OOO"
            number_follows = True
        elif char == " ":
            number_follows = False

        braille += english_braille_map[char.lower()]
    return braille
    
def braille_to_english(braille):
    english = ""
    number_follows = False
    capital_follows = False
    braille_list = [(braille[i:i+6]) for i in range(0, len(braille), 6)]
    for char in braille_list:
        if char == ".O.OOO":
            number_follows = True
            continue
        if char == ".....O":
            capital_follows = True
            continue
        if number_follows:
            number = ord(braille_english_map[char]) - 96
            english += str(number)
        elif capital_follows:
            english += braille_english_map[char].upper()
            capital_follows = False
        else:
            if char == "......":
                number_follows = False
            english += braille_english_map[char]
    return english 

def main():
    args = " ".join(sys.argv[1:])
    if args.find(".") == -1:        # if there are no periods, it is english
        print(english_to_braille(args))
    else:
        print(braille_to_english(args))
        
if __name__ == "__main__":
    main()
