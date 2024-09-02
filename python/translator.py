import sys

eng_to_braille = { # Dictionary that stores the alphabet letters as keys and their Braille representations as values
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
    " ": "......"
}


num_to_braille = { # Dictionary that stores the Numbers as keys and their Braille representations as values
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

braille_to_eng = {v:k for k, v in eng_to_braille.items()}

braille_to_num = {v:k for k, v in num_to_braille.items()}

def is_braille(input_str: str) -> bool:
    for char in input_str:
        if char not in {'O', '.', ' '}:
            return False
    return True

def english_to_braille(phrase):
    
    # Translates an English phrase to Braille.
    
    result = ""
    number_follows = False

    for c in phrase:
        if c.isupper():
            result += ".....O"  # Braille capitalization indicator
            c = c.lower()
        elif c.isnumeric():
            if not number_follows:
                result += ".O.OOO"  # Braille number indicator
                number_follows = True
            result += num_to_braille[c]
            continue
        elif c == " ":
            number_follows = False  # Resets the number flag on space

        result += eng_to_braille[c]
    
    return result


def braille_to_english(phrase):
    
    # Translates a Braille phrase to English.
  
    result = ""
    str = ""
    number_follows = False
    capital_follows = False

    for c in phrase:
        str += c
        if len(str) == 6:
            if str == ".O.OOO":
                number_follows = True
            elif str == ".....O":
                capital_follows = True
            elif str == "......":
                number_follows = False
                result += " "
            else:
                if number_follows:
                    result += braille_to_num.get(str, "?")
                elif capital_follows:
                    result += braille_to_eng.get(str, "?").upper()
                    capital_follows = False
                else:
                    result += braille_to_eng.get(str, "?")
            str = ""
    
    return result



def translatePhrase(phrase):
    
    # Determines if the phrase is in english or in braille then translates them accordingly.
   
    if not is_braille(phrase):
        return english_to_braille(phrase)
    else:
        return braille_to_english(phrase)




if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(translatePhrase(" ".join(sys.argv[1:])))
    else:
        print("Please enter a valid input")