import sys

braille_to_chars = {
    "O.....": "a",
    "O.O...": 'b',
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
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " "
}

braille_to_nums = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

braille_to_follows = {
    ".....O": "capital_follows",
    ".O...O": "decimal_follows",
    ".O.OOO": "number_follows"
}

# creating inverse dictionarys for the xxxx and braille
chars_to_braille = {v: k for k, v in braille_to_chars.items()}
nums_to_braille = {v: k for k, v in braille_to_nums.items()}
follows_to_braille = {v: k for k, v in braille_to_follows.items()}


# checking if the value input is braille or english
def check_format(user_in):
    user_in = ''.join(user_in)

    if (all(char in 'O.' for char in user_in)):
        return translate_to_english(user_in)
    elif not (all(char in 'O.' for char in user_in)):
        return translate_to_braille(user_in)

def translate_to_braille(user_in): 
    braille_out = ""
    num_follows = False

    for char in user_in:
        if char.isalpha() and char.isupper():
            braille_out += follows_to_braille["capital_follows"]
            braille_out += chars_to_braille[char.lower()]
        elif char.isalpha():
            braille_out += chars_to_braille[char]
        elif char.isdigit():
            if not num_follows:
                num_follows = True
                braille_out += follows_to_braille["number_follows"]
            braille_out += nums_to_braille[char]
        elif char.isspace():
            num_follows = False
            braille_out += chars_to_braille[" "]
    return braille_out

        
def translate_to_english(user_in):
    english_out = ""
    num_follows = False
    cap_follows = False

    for index in range(0, len(user_in), 6):

        sub_braille = user_in[index:index + 6]

        if sub_braille in braille_to_follows and braille_to_follows[sub_braille] == "capital_follows":
            cap_follows = True
        elif sub_braille in braille_to_follows and braille_to_follows[sub_braille] == "number_follows":
            num_follows = True
        elif cap_follows and sub_braille in braille_to_chars:
            english_out += braille_to_chars[sub_braille].upper()
            cap_follows = False
        elif sub_braille in braille_to_chars and num_follows == False:
            english_out += braille_to_chars[sub_braille]
        elif num_follows and sub_braille in braille_to_nums:
            english_out += braille_to_nums[sub_braille]
        elif sub_braille in braille_to_chars and braille_to_chars[sub_braille] == " ":
            num_follows = False
            english_out += " "
    
    return english_out

if __name__ == '__main__':
    user_in = sys.argv[1:]
    translated = check_format(user_in)
    print(translated)

    # .....OO.....O.O...OO.....O.OOOO.....O.O...OO....OO..OO.....OOO.OOOO..OOO
    # .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
    # .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO

