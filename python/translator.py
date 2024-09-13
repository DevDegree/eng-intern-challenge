import sys, re

def eng_to_braille(phrase, eng_braille_dict):
    """Translates English to Braille. Only handles the space character, A-Z, a-z, and 0-9."""
    s = ""
    capital_next = ".....O"
    number_next = ".O.OOO"
    number_flag = False
    for c in phrase:
        if c == " ":
            number_flag = False
            s += f"{eng_braille_dict[c]}"
        elif number_flag == True:
            # Lookup dict with the right letter, by getting the character representation of a digit 1-9 + offset 64, and append
            # If the character is '0', then simply lookup dict with 'J'
            s += f"{eng_braille_dict['J']}" if c == '0' else f"{eng_braille_dict[chr(int(c) + 64)]}"
        elif c.isnumeric() and number_flag == False:
            number_flag = True
            s += f"{number_next}"
            s += f"{eng_braille_dict['J']}" if c == '0' else f"{eng_braille_dict[chr(int(c) + 64)]}"
        elif c.isupper():
            s += f"{capital_next}{eng_braille_dict[c]}"
        else:
            s += f"{eng_braille_dict[c.upper()]}"
    print(s)

def braille_to_eng(phrase, braille_eng_dict):
    """Translates Braille to English. Only handles the space character, A-Z, a-z, and 0-9."""
    s = ""
    capital_next = ".....O"
    number_next = ".O.OOO"
    number_flag = False
    capital_flag = False
    for i in range(0, len(phrase), 6):
        c = phrase[i : i+6]
        if c == "......":
            number_flag = False
            s += f"{braille_eng_dict[c]}"
        elif number_flag == True:
            # Subtract offset 64 from the int representation of a letter to get a digit and append.
            # If the letter in Braille corresponds to 'J', then simply append '0'
            s += "0" if c == ".OOO.." else f"{(ord(braille_eng_dict[c]) - 64)}"
        elif c == number_next:
            number_flag = True
        elif c == capital_next:
            capital_flag = True
        elif capital_flag == True:
            capital_flag = False
            s += f"{braille_eng_dict[c]}"
        else:
            s += f"{braille_eng_dict[c]}".lower()
    print(s)

if __name__ == '__main__':
    phrase = ' '.join(sys.argv[1:])  # Should this be stripped?

    eng_braille_dict = {
        "A": "O.....",    "B": "O.O...",    "C": "OO....",
        "D": "OO.O..",    "E": "O..O..",    "F": "OOO...",
        "G": "OOOO..",    "H": "O.OO..",    "I": ".OO...",
        "J": ".OOO..",    "K": "O...O.",    "L": "O.O.O.",
        "M": "OO..O.",    "N": "OO.OO.",    "O": "O..OO.",
        "P": "OOO.O.",    "Q": "OOOOO.",    "R": "O.OOO.",
        "S": ".OO.O.",    "T": ".OOOO.",    "U": "O...OO",
        "V": "O.O.OO",    "W": ".OOO.O",    "X": "OO..OO",
        "Y": "OO.OOO",    "Z": "O..OOO",    " ": "......"
    }
    braille_eng_dict = dict((v,k) for k,v in eng_braille_dict.items())

    if (re.search("[^O\.]", phrase)):
        eng_to_braille(phrase, eng_braille_dict)
    else:
        braille_to_eng(phrase, braille_eng_dict)
