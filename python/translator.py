
import sys

# This code pretends that memory is limited so, instead of using 2 dictionaries, the use of unicode is privileged
# If memory is not a problem, it is possible to use a dictionary to convert english to braille and braille to numbers etc.

dictionary = {"O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e', "OOO...": 'f', 
              "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i',".OOO..": 'j',"O...O.": 'k',"O.O.O.": 'l',
              "OO..O.": 'm', "OO.OO.": 'n',"O..OO.": 'o',"OOO.O.": 'p',"OOOOO.": 'q',"O.OOO.": 'r',
              ".OO.O.": 's', ".OOOO.": 't',"O...OO": 'u',"O.O.OO": 'v',".OOO.O": 'w',"OO..OO": 'x', 
              "OO.OOO": 'y',"O..OOO": 'z', "......": ' '}

capital_marker = ".....O"
number_marker = ".O.OOO"
space_marker = "......"

def translate(string_to_translate: str):
    if string_to_translate.count("..") > 0 or string_to_translate.count(".O.") > 0:
        return translate_to_english(string_to_translate)
    return translate_to_braille(string_to_translate)

def translate_to_braille(string_to_translate: str):         
    return "translated_string"

def translate_to_english(string_to_translate: str):
    capital_follows = False
    number_follows = False
    translated_string = ""
    for i in range(int(len(string_to_translate) / 6)):
        word = string_to_translate[i * 6 : (i + 1) * 6]
        if word == capital_marker:
            capital_follows = True
        elif word == number_marker:
            number_follows = True
        else:
            if word == space_marker:
                number_follows = False
            if number_follows:
                translated_string += str(ord(dictionary[word]) - ord('a') + 1)
            elif capital_follows:
                translated_string += dictionary[word].upper()
                capital_follows = False                
            else:
                translated_string += dictionary[word]
    return translated_string


if __name__ == '__main__':
    separator = ' '
    print(translate(separator.join(sys.argv[1:])))
