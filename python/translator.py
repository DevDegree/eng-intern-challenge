
import sys

braille_dict_alpha_small = {
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
}
alpha_small_to_braille = {value: key for key, value in braille_dict_alpha_small.items()}

braille_dict_numb = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}
numb_to_braille = {value: key for key, value in braille_dict_numb.items()}

braille_dict_alpha_big = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
}
big_alphabet_to_braille = {value: key for key, value in braille_dict_alpha_big.items()}

Decimal_Follows = ".O.OOO"
Capital_Follows = ".....O"


def Braille_Or_English(args):
    for arg in args:
        if "." in arg:
            return "Braille"
        else:
            return "English"


def English_To_Braille(args):
    braille_string = ""
    number_folows_flag = False
    for arg in args:
        word = arg
        temp_string = ""
        for i in range(len(word)):
            # smaller alphabet case
            if not word[i].isdigit():
                if word[i].isupper():
                    temp_string += Capital_Follows
                temp_string += braille_dict_alpha_small[word[i].lower()]
            # number case
            else:
                if number_folows_flag == False:
                    temp_string += Decimal_Follows
                    number_folows_flag = True
                temp_string = temp_string + (braille_dict_numb[word[i]])
        if (len(args) > 1) and (arg != args[-1]):
            temp_string += "......"
        braille_string = braille_string + (temp_string)
    return braille_string


def Braille_To_English(args):
    list_of_braille_characters = []
    english_word = ""
    num_follows = False
    capital_follows = False
    arg = args[0]
    num_follows_value = ".O.OOO"
    cap_follows_value = ".....O"
    for i in range(0, len(arg), 6):
        braille_value = arg[i : i + 6]
        list_of_braille_characters.append(braille_value)
    for i in range(len(list_of_braille_characters)):
        wrd = list_of_braille_characters[i]
        # num follows flag
        if wrd == num_follows_value:
            num_follows = True
        # number case
        elif num_follows == True and (wrd in numb_to_braille):
            english_word += numb_to_braille[wrd]
        # capital follows  flag
        elif wrd == cap_follows_value:
            capital_follows = True
        # capital alphabet case
        elif capital_follows == True and (wrd in big_alphabet_to_braille):
            english_word += big_alphabet_to_braille[wrd]
            capital_follows = False
        # small alphabet case
        elif (
            num_follows == False
            and capital_follows == False
            and wrd in alpha_small_to_braille
        ):
            english_word += alpha_small_to_braille[wrd]
        # space case
        elif wrd == "......":
            english_word += " "
            num_follows = False
    return english_word


def main():
    args = sys.argv[1:]
    language = Braille_Or_English(args)
    if language == "English":
        return English_To_Braille(args)
    else:
        return Braille_To_English(args)


print(main())
