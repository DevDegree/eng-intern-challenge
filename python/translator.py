# Nargol Lotfizadeh
# Braille Translator

import sys

# Braille to English dictionary including special symbols
braille_to_english_letter = {
    "O.....": "a",  # Braille dot pattern for 'a'
    "O.O...": "b",  # Braille dot pattern for 'b'
    "OO....": "c",  # Braille dot pattern for 'c'
    "OO.O..": "d",  # Braille dot pattern for 'd'
    "O..O..": "e",  # Braille dot pattern for 'e'
    "OOO...": "f",  # Braille dot pattern for 'f'
    "OOOO..": "g",  # Braille dot pattern for 'g'
    "O.OO..": "h",  # Braille dot pattern for 'h'
    ".OO...": "i",  # Braille dot pattern for 'i'
    ".OOO..": "j",  # Braille dot pattern for 'j'
    "O...O.": "k",  # Braille dot pattern for 'k'
    "O.O.O.": "l",  # Braille dot pattern for 'l'
    "OO..O.": "m",  # Braille dot pattern for 'm'
    "OO.OO.": "n",  # Braille dot pattern for 'n'
    "O..OO.": "o",  # Braille dot pattern for 'o'
    "OOO.O.": "p",  # Braille dot pattern for 'p'
    "OOOOO.": "q",  # Braille dot pattern for 'q'
    "O.OOO.": "r",  # Braille dot pattern for 'r'
    ".OO.O.": "s",  # Braille dot pattern for 's'
    ".OOOO.": "t",  # Braille dot pattern for 't'
    "O...OO": "u",  # Braille dot pattern for 'u'
    "O.O.OO": "v",  # Braille dot pattern for 'v'
    ".OOO.O": "w",  # Braille dot pattern for 'w'
    "OO..OO": "x",  # Braille dot pattern for 'x'
    "OO.OOO": "y",  # Braille dot pattern for 'y'
    "O..OOO": "z",  # Braille dot pattern for 'z'
    '.....O': "capital follows",
    ".O.OOO": "number follows",
    "......": " ",  # space
}

braille_to_english_char = {
    # Special symbols
    # Braille pattern for indicating the following letter is capitalized
    '.....O': "capital follows",
    ".O.OOO": "number follows",   # Braille pattern for indicating numbers follow
    "....OO": "decimal follows",  # Braille pattern for indicating a decimal point follows
    # General symbol pattern (often used for punctuation markers)
    "OOOOOO": "symbol follows",

    # Digits (based on Braille number follows rule)
    "O.....": "1",  # 1 (Braille letter 'a' in number context)
    "O.O...": "2",  # 2 (Braille letter 'b' in number context)
    "OO....": "3",  # 3 (Braille letter 'c' in number context)
    "OO.O..": "4",  # 4 (Braille letter 'd' in number context)
    "O..O..": "5",  # 5 (Braille letter 'e' in number context)
    "OOO...": "6",  # 6 (Braille letter 'f' in number context)
    "OOOO..": "7",  # 7 (Braille letter 'g' in number context)
    "O.OO..": "8",  # 8 (Braille letter 'h' in number context)
    ".OO...": "9",  # 9 (Braille letter 'i' in number context)
    ".OOO..": "O",  # O (Braille letter 'j' in number context)
    "......": " ",  # space

    # Common punctuation marks
    "..O...": ",",   # Comma
    "..OO.O": ".",   # Period
    ".O....": "'",   # Apostrophe
    "..OOO.": "!",   # Exclamation mark
    "..O.OO": "?",   # Question mark
    "..O.O.": ";",   # Semicolon
    "..OO..": ":",   # Colon
    "....OO": "-",   # Hyphen
    ".O..O.": "/",   # slash
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")"

}

# English to Braille dictionary for letters
english_to_braille_letter = {
    "a": "O.....",  # Braille dot pattern for 'a'
    "b": "O.O...",  # Braille dot pattern for 'b'
    "c": "OO....",  # Braille dot pattern for 'c'
    "d": "OO.O..",  # Braille dot pattern for 'd'
    "e": "O..O..",  # Braille dot pattern for 'e'
    "f": "OOO...",  # Braille dot pattern for 'f'
    "g": "OOOO..",  # Braille dot pattern for 'g'
    "h": "O.OO..",  # Braille dot pattern for 'h'
    "i": ".OO...",  # Braille dot pattern for 'i'
    "j": ".OOO..",  # Braille dot pattern for 'j'
    "k": "O...O.",  # Braille dot pattern for 'k'
    "l": "O.O.O.",  # Braille dot pattern for 'l'
    "m": "OO..O.",  # Braille dot pattern for 'm'
    "n": "OO.OO.",  # Braille dot pattern for 'n'
    "o": "O..OO.",  # Braille dot pattern for 'o'
    "p": "OOO.O.",  # Braille dot pattern for 'p'
    "q": "OOOOO.",  # Braille dot pattern for 'q'
    "r": "O.OOO.",  # Braille dot pattern for 'r'
    "s": ".OO.O.",  # Braille dot pattern for 's'
    "t": ".OOOO.",  # Braille dot pattern for 't'
    "u": "O...OO",  # Braille dot pattern for 'u'
    "v": "O.O.OO",  # Braille dot pattern for 'v'
    "w": ".OOO.O",  # Braille dot pattern for 'w'
    "x": "OO..OO",  # Braille dot pattern for 'x'
    "y": "OO.OOO",  # Braille dot pattern for 'y'
    "z": "O..OOO",  # Braille dot pattern for 'z'

}

# English to Braille dictionary for special characters and symbols
english_to_braille_char = {
    # Braille pattern for indicating the following letter is capitalized
    "capital follows": ".....O",
    "number follows": ".O.OOO",    # Braille pattern for indicating numbers follow
    # Braille pattern for indicating a decimal point follows
    "decimal follows": "....OO",
    "symbol follows": "OOOOOO",    # Braille pattern for general symbols

    "1": "O.....",   # 1 (Braille letter 'a' in number context)
    "2": "O.O...",   # 2 (Braille letter 'b' in number context)
    "3": "OO....",   # 3 (Braille letter 'c' in number context)
    "4": "OO.O..",   # 4 (Braille letter 'd' in number context)
    "5": "O..O..",   # 5 (Braille letter 'e' in number context)
    "6": "OOO...",   # 6 (Braille letter 'f' in number context)
    "7": "OOOO..",   # 7 (Braille letter 'g' in number context)
    "8": "O.OO..",   # 8 (Braille letter 'h' in number context)
    "9": ".OO...",   # 9 (Braille letter 'i' in number context)
    "O": ".OOO..",   # O (Braille letter 'j' in number context)

    " ": "......",   # space
    ",": "..O...",   # Comma
    ".": "..OO.O",   # Period
    "'": ".O....",   # Apostrophe
    "!": "..OOO.",   # Exclamation mark
    "?": "..O.OO",   # Question mark
    ";": "..O.O.",   # Semicolon
    ":": "..OO..",   # Colon
    "-": "....OO",   # Hyphen
    "/": ".O..O.",   # Slash
    "<": ".OO..O",   # Less than
    ">": "O..OO.",   # Greater than
    "(": "O.O..O",   # Left parenthesis
    ")": ".O.OO."    # Right parenthesis
}

input_string = ""
if len(sys.argv) > 1:
    input_string = ' '.join(sys.argv[1:])
    # print(f"Received input: {input_string}")


def is_eng(input_string):
    char = input_string[:7]
    return all(char.isalnum() or char.isspace() for char in input_string)


def translate_braille(input_string):
    ans_str = ""
    cur_char = ""
    is_caps = False
    is_num = False

    for i in range(0, len(input_string), 6):
        cur_char = input_string[i:i + 6]

        # print(braille_to_english_char.get(cur_char))
        if braille_to_english_char.get(cur_char) == "capital follows":
            is_caps = True
            continue
        if braille_to_english_char.get(cur_char) == "number follows":
            is_num = True
            continue
        if braille_to_english_char.get(cur_char) == " ":
            is_num = False

        if (is_caps):
            ans_str += braille_to_english_letter[cur_char].upper()
        elif (is_num):
            ans_str += braille_to_english_char[cur_char]
        else:
            ans_str += braille_to_english_letter[cur_char]

        is_caps = False
    print(ans_str)
    return ans_str


# print(translate_braille(input_string))

def translate_eng(input_string):
    # print("BOOO")
    ans_str = ""
    cur_char = ""
    # is_caps = False
    is_num = False
    # print(input_string)
    for i in range(0, len(input_string)):
        # ans_str += '/'
        cur_char = input_string[i]

        if cur_char == " ":
            is_num = False
            ans_str += english_to_braille_char.get(cur_char)
            continue

        elif cur_char.isdigit():
            if not is_num:
                is_num = True
                ans_str += english_to_braille_char.get("number follows")

            ans_str += english_to_braille_char.get(cur_char)
            continue

        elif cur_char.isupper():
            ans_str += english_to_braille_char.get("capital follows")
            # print(cur_char)
            ans_str += english_to_braille_letter.get(cur_char.lower())
            continue

        elif cur_char.isalpha():
            ans_str += english_to_braille_letter.get(cur_char.lower())
            continue

        else:
            ans_str += braille_to_english_char[cur_char]

    print(ans_str)
    return ans_str


# print(translate_eng(input_string))

def translate(input_string):
    if "." in input_string:
        # print("lkfl")
        translate_braille(input_string)
    else:
        translate_eng(input_string)


translate(input_string)
