import re
import sys

# Create lists holding the letters and numbers of each alphabet placed at the same relative index for easy conversion
standard_alphabet = [
    "a", "b", "c", "d",
    "e", "f", "g", "h",
    "i", "j", "k", "l",
    "m", "n", "o", "p",
    "q", "r", "s", "t",
    "u", "v", "w", "x",
    "y", "z", ".", ",",
    "?", "!", ":", ";",
    "-", "/", "<", ">",
    "(", ")", " "
]
standard_digits = [
    "1", "2",
    "3", "4",
    "5", "6",
    "7", "8",
    "9", "0",
]

braille_alphabet = [
    # a         b         c         d
    "O.....", "O.O...", "OO....", "OO.O..",
    # e         f         g         h 
    "O..O..", "OOO...", "OOOO..", "O.OO..",
    # i         j         k         l 
    ".OO...", ".OOO..", "O...O.", "O.O.O.",
    # m         n         o         p 
    "OO..O.", "OO.OO.", "O..OO.", "OOO.O.",
    # q         r         s         t 
    "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",
    # u         v         w         x 
    "O...OO", "O.O.OO", ".OOO.O", "OO..OO",
    # y         z         .         , 
    "OO.OOO", "O..OOO", "..OO.O", "..O...",
    # ?         !         :         ; 
    "..O.OO", "..OOO.", "..OO..", "..O.O.",
    # -         /         <         > 
    "....OO", ".O..O.", ".OO..O", "O..OO.",
    # (         )         " "      
    "O.O..O", ".O.OO.", "......"
]
braille_digits = [
    # 1         2
    "O.....", "O.O...", 
    # 3         4
    "OO....", "OO.O..", 
    # 5         6
    "O..O..", "OOO...", 
    # 7         8
    "OOOO..", "O.OO..", 
    # 9         0
    ".OO...", ".OOO..",
]

# A pattern that is used to check if the inputted string is exclusively O's and .'s meaning its braille
braille_alphabet_pattern = re.compile(r"^[O.]{6,}$")

# Loop through every character in the string and add the braille equivalent onto a new string with precedent characters when needed
def convert_to_braille(str_to_convert):
    converted_str = ""
    continued_num = False
    for letter in str_to_convert:
        try:
            if letter.isupper():
                converted_str += ".....O" #capital follows
                converted_str += braille_alphabet[standard_alphabet.index(letter.lower())]
            elif letter.isdigit() and not continued_num:
                converted_str += ".O.OOO" #number follows
                converted_str += braille_digits[standard_digits.index(letter)]
                continued_num = True
                continue
            elif letter.isdigit() and continued_num:
                converted_str += braille_digits[standard_digits.index(letter)]
                continue
            elif letter == "." and continued_num:
                converted_str += ".O...O" #there was a digit first so place a decimal follows
                converted_str += braille_alphabet[standard_alphabet.index(letter)]
                continue
            else:
                converted_str += braille_alphabet[standard_alphabet.index(letter)]

            continued_num = False
        except ValueError:
            return "Braille Contains Miss Input Please Try Again\n.....OO.O...O.OOO.O......OO...O.O.O.O.O.O.O..O.............OOO....O..OO.OO.OO..OOOO.O......OO...OO.OO..OO.O............OOO..O..OO....OO.O..OO.O............O.OO...OO.OO.OOO.O.O...OO.OOOO.\n.....OOOO.O.O.O.O.O..O..O......OO.O.O..O.............O.OOOO.O.OOO.OO.OOO...........OO.....OOOO..O......OO...OO.OO."

    return converted_str

def convert_to_standard(str_to_convert):
    converted_str = ""
    continued_num = False
    continued_capital = False
    individual_letters = [str_to_convert[i:i+6] for i in range(0, len(str_to_convert), 6)]

    for letter in individual_letters:
        if letter == ".....O":  # capital follows
            continued_capital = True
        elif continued_capital:
            converted_str += standard_alphabet[braille_alphabet.index(letter)].upper()
            continued_capital = False
        elif letter == ".O.OOO":  # number follows
            continued_num = True
        elif letter == "......":
            continued_num = False
            converted_str += " "
        elif continued_num:
            converted_str += standard_digits[braille_digits.index(letter)]
        elif letter == ".O...O":  # decimal follows
            continue
        else:
            converted_str += standard_alphabet[braille_alphabet.index(letter)]
    return converted_str

# This is the method that utilizes the previous Regex to decide which conversion needs to be made
def check_alphabet(str_to_check):
    if braille_alphabet_pattern.match(str_to_check):
        return convert_to_standard(str_to_check)
    else:
        return convert_to_braille(str_to_check)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No input strings provided.")
        sys.exit(1)
    
    # Process each input string and join them with a space
    input_string = ' '.join(sys.argv[1:])
    result = check_alphabet(input_string)
    print(result, end="")
