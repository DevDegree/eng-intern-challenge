
import sys

# constant values:
num_start = ord("0") - ord(" ")
num_end = ord("9") - ord(" ")
dot_index = ord(".") - ord(" ")
# mapping ascii orders to braille
order_maps_braille = [
    "......",  # Space
    "..OOO.",  # !
    "",  # "
    "",  # #
    "",  # $
    "",  # %
    "",  # &
    "",  # '
    "O.O..O",  # (
    ".O.OO.",  # )
    "",  # *
    "",  # +
    "..O...",  # ,
    "....OO",  # -
    "..OO.O",  # .
    ".O..O.",  # /
    ".OOO..",  # 0
    "O.....",  # 1
    "O.O...",  # 2
    "OO....",  # 3
    "OO.O..",  # 4
    "O..O..",  # 5
    "OOO...",  # 6
    "OOOO..",  # 7
    "O.OO..",  # 8
    ".OO...",  # 9
    "..OO..",  # :
    "..O.O.",  # ;
    ".OO..O",  # <
    "",  # =
    "O..OO.",  # >
    "..O.OO",  # ?
    "",  # @
    "O.....",  # A
    "O.O...",  # B
    "OO....",  # C
    "OO.O..",  # D
    "O..O..",  # E
    "OOO...",  # F
    "OOOO..",  # G
    "O.OO..",  # H
    ".OO...",  # I
    ".OOO..",  # J
    "O...O.",  # K
    "O.O.O.",  # L
    "OO..O.",  # M
    "OO.OO.",  # N
    "O..OO.",  # O
    "OOO.O.",  # P
    "OOOOO.",  # Q
    "O.OOO.",  # R
    ".OO.O.",  # S
    ".OOOO.",  # T
    "O...OO",  # U
    "O.O.OO",  # V
    ".OOO.O",  # W
    "OO..OO",  # X
    "OO.OOO",  # Y
    "O..OOO",  # Z
]
# capital follows, decimals follows, numbers follows
braille_instructions = [
    ".....O",
    ".O...O",
    ".O.OOO",
    "......",
]
# mapping braille to letter
braille_maps_chars = {
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
}
braille_maps_symbols = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}


# the mapping should be from the braille pattern into the ascii decimals
# main function definition
def translate(text):
    if len(text) == 0:
        print(text)
    if isBraille(text):
        print(toEnglish(text))
    else:
        print(toBraille(text))


# helper function: return the translated texting from Braille to English
def toEnglish(text):
    count = len(text) // 6
    result = []
    capital = False
    number = False
    decimal = False
    i = 0
    while i < count:
        braille_char = text[i * 6 : i * 6 + 6]
        if braille_char in braille_instructions:
            if braille_char == braille_instructions[0]:  # capital follows
                capital = True
            if braille_char == braille_instructions[1]:
                decimal = True
            if not number and braille_char == braille_instructions[2]:  # number follows
                number = True
            if braille_char == braille_instructions[-1]:  # deactivate the number mode
                result.append(" ")
                number = False
            i += 1
            continue
        # assumption: if there are two char with same braille representation, consider the letter first
        if braille_char in braille_maps_chars:
            char = braille_maps_chars[braille_char]
        elif char in braille_maps_symbols:
            char = braille_maps_symbols[braille_char]
        else:
            raise Exception(
                "We could not find a translation for",
                braille_char,
                "please input a valid braille string",
            )
        i += 1
        if decimal:
            result.append(char)  # regular char
            decimal = False
        elif number:
            num = (ord(char) - ord("a") + 1) % 10
            result.append(str(num))  # number
        elif capital:
            result.append(char.capitalize())  # capitalized char
            capital = False
        else:
            result.append(char)  # regular char
    return "".join(result)


# helper function: return the translated texting from English to Braille
def toBraille(text):
    result = []
    prev_number = False
    for i in range(len(text)):
        if text[i].isupper():  # capital letter
            result.append(braille_instructions[0])
        order = ord(text[i].capitalize()) - ord(" ")
        if prev_number and order == dot_index:  # has a decimal number
            result.append(braille_instructions[1])
        elif not prev_number and order in range(
            num_start, num_end
        ):  # start of the number
            result.append(braille_instructions[2])
            prev_number = True
        elif prev_number and (
            order < num_start or order > num_end
        ):  # end of the number
            prev_number = False
        braille_char = order_maps_braille[order]
        result.append(braille_char)
    return "".join(result)


# helper function: return true if the texting is Braille
def isBraille(text):
    if len(text) < 6 or len(text) % 6 != 0:
        return False
    for i in range(0, 6):
        if text[i] != "." and text[i] != "O":
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_texts = sys.argv[1:]
        s = " ".join(input_texts)
        translate(s)
