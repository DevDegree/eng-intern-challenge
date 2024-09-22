
import sys
import re
# Braille to English dictionary using '.' for unraised dots and 'O' for raised dots
braille_to_english = {
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",
        ".....O": "capital",
        ".O.OOO": "number",
        "......": " "
    }
# English to braille dictionary
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
        "capital": ".....O",
        "number": ".O.OOO",
        "space": "......"
}
# translate the english string to braille string
# it can handle these situations:
# 1. 123Abc -> not allowed
# 2. 123 Abc -> a braille number follows symbol + a branville string of "123" + a branville string of a space  + a braille capital follows symbol + a branville string of "Abc"
# 3. abc 123 123 -> a braille capital follows symbol + a branville string of "abc"  + a branville string of a space + a braille number follows symbol + a branville string of "123" + a branville string of a space + a branville string of "123"
# 4. A1b -> not allowed
# 5. 1 2 -> a braille number follows symbol + a branville string of "1" + a branville string of a space + a braille number follows symbol + a branville string of "2"
# 6. 1b2 -> not allowed
def translate_english_to_braille(s):
    if not check_word(s):
        raise Exception("Invalid input: you should separate alphabets and numbers with a space.") 
    # define a number switch, when it is true, it indicates the following characters are all numbers
    # when it is false, it indicates the following characters are not numbers
    is_number = False
    result = ""
    # for loop each character in the input string
    for char in s:
        if char.isalpha(): # if the character is a alphabet
            if is_number:
                is_number = False
            if char.isupper():
                result += english_to_braille["capital"] #if it is a capital, add a Braille capital follows symbol
            result += english_to_braille[char.lower()] # add the corresponding english character braille string
        elif char.isdigit(): # if the character is a number
            if not is_number: # if the number switch is closed, which means the previous character is not a number resulting in a Braille number follows symbol added into the result
                result += english_to_braille["number"] 
                is_number = True 
            # in order to get the graville string of '1',
            # 1. translate '1' to 'a'
            # 2. get english_to_braille['a']
            # since the braille string of '1' is the same as the braille string of 'a'
            result += english_to_braille[chr(ord(char) + 48)] # add the corresponding number character braille string
        elif char == " ": # if a space is encountered
            if is_number: 
                is_number = False # close the number switch if it is open
            result += english_to_braille["space"] # add a space braille string
        else: # if the character is not a english character or a number character or a space, raise an exception
            raise Exception("Invalid input: only english character, number and space could be included in the input string.")
    return result

# check if a string has a word that containts alphbets and numbers in it
def check_word(s):
    pattern = r'(?=.*[A-Za-z])(?=.*\d)'
    str_list = s.split(" ")
    for word in str_list:
        # if a word contains characters and numbers
        # return False
        if bool(re.search(pattern, word)) == True:
            return False
    return True


# translate the braille string to english string
# it can handle these situations:
# 1. First meet a braille number follows symbol, then a braille capital follows symbol is encountered  before a space symbol -> it prioritizes to translate the following character to numbers
# 2. Meet a braille number follows symbol again before a space symbol -> ignore the extra braille number follows symbol 
def translate_braille_to_english(s):
    result = ""
    is_capital = False
    is_number = False
    for i in range(0, len(s), 6):
        braille_char = s[i:i+6]
        if braille_char not in braille_to_english:
            raise Exception("Invalid input: only braille english character, number and space could be included in the input string.")
       
        translated_char =  braille_to_english[braille_char]
        if translated_char == "number":
            is_number = True
        elif translated_char == "capital":
            if not is_number:
                is_capital = True
        elif translated_char == " ":
            if is_number:
                is_number = False
            result += " "
        else:
            if is_capital == True:
                result += translated_char.upper()
                is_capital = False
            elif is_number == True:
                # translate 'a' to '1', ord('a') - ord('1') = 48
                # ord('1') = ord('a') - 48
                result += chr(ord(translated_char) - 48)
            else:
                result += translated_char
    return result

# check if the input consists only of braille symbols
def is_braille(s):
    if len(s) % 6 != 0:
        return False
    return all(char in "O." for char in s)

             
def main():
    if len(sys.argv) < 2: 
        print("Usage: python translator.py <string to translate>")
        return
    input = " ".join(sys.argv[1:])
    if is_braille(input):
        print(translate_braille_to_english(input))
    else:
        print(translate_english_to_braille(input))


if __name__ == "__main__":
    main()
