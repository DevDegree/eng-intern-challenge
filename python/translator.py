import sys

# The English language includes characters
# from 'a' to 'z', digits '0' to '9', and some
# special characters including '.' and whitespace.

# Our Braille representation includes characters
# '.' and 'O'

# Each Braille alphabet is a 6-length combination
# of '.' and 'O' symbols. Therefore the Braille
# language will always be a multiple of 6.

# "a" to "j" and "1" to "O" have same Braille
# representation. So does "O" and ">". So we
# can't use bidirectional maps here.

english_to_braille = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "0" : ".OOO..",
    "capital_follows" : ".....O",
    "number_follows" : ".O.OOO",
    " " : "......",
}

braille_to_english = {
    "O....." : ("a", "1"),
    "O.O..." : ("b", "2"),
    "OO...." : ("c", "3"),
    "OO.O.." : ("d", "4"), 
    "O..O.." : ("e", "5"),
    "OOO..." : ("f", "6"),
    "OOOO.." : ("g", "7"),
    "O.OO.." : ("h", "8"),
    ".OO..." : ("i", "9"),
    ".OOO.." : ("j", "0"),
    "O...O." : ("k"),
    "O.O.O." : ("l"),
    "OO..O." : ("m"),
    "OO.OO." : ("n"),
    "O..OO." : ("o"),
    "OOO.O." : ("p"),
    "OOOOO." : ("q"),
    "O.OOO." : ("r"),
    ".OO.O." : ("s"),
    ".OOOO." : ("t"),
    "O...OO" : ("u"),
    "O.O.OO" : ("v"),
    ".OOO.O" : ("w"),
    "OO..OO" : ("x"),
    "OO.OOO" : ("y"),
    "O..OOO" : ("z"),
    ".....O" : ("capital_follows"),
    ".O.OOO" : ("number_follows"),
     "......": (" "),
}

CAPITAL = "capital_follows"
NUMBER = "number_follows"

IDX = 0
DIGIT_IDX = 1

def is_braille(text: str) -> bool:
    if len(text) % 6 != 0:
        return False

    for char in text:
        if char not in {'O', '.'}:
            return False
    
    return True

def convert_to_english(text: str) -> str:
    solution = ""
    capital_flag = False
    number_flag = False

    # splits the Braille text into sections, each of length 6
    number_of_chunks = len(text) // 6
    chunks = [text[6 * i: 6 * i + 6] for i in range(number_of_chunks)]

    for chunk in chunks:
        if braille_to_english[chunk] == CAPITAL:
            capital_flag = True
        elif braille_to_english[chunk] == NUMBER:
            number_flag = True
        elif braille_to_english[chunk] == " ":
            number_flag = False
            solution += braille_to_english[chunk][IDX]
        else:
            # we are dealing with a chunk that is either
            # an alphabet or a digit

            if number_flag:
                solution += braille_to_english[chunk][DIGIT_IDX]
            else:
                if capital_flag:
                    solution += braille_to_english[chunk][IDX].upper()
                    capital_flag = False
                else:
                    solution += braille_to_english[chunk][IDX]

    return solution


def convert_to_braille(text: str) -> str:
    solution = ""
    number_flag = True

    for char in text:
        if char.isupper():
            solution +=  english_to_braille[CAPITAL]+ english_to_braille[char.lower()]
            number_flag = True
        elif char.isdigit():
            solution +=  (english_to_braille[NUMBER] if number_flag else "") + english_to_braille[char]
            number_flag = False
        else:
            # char is a lower case alphabet, or space
            solution += english_to_braille[char]
            number_flag = True

    return solution

# We want the number_flag that helps us insert the "number_follows" alphabet
# to be True once we finish parsing digits. And number_flag to be False when
# we are currently parsing digits.


def main():
    # if there are some arguments
    if len(sys.argv) > 1:
        sys.argv.pop(0) # pop out the program name

        arguments = sys.argv
        input_string = " ".join(arguments)
        
        if is_braille(input_string):
            output_string = convert_to_english(input_string)
        else:
            # input_string is in English
            output_string = convert_to_braille(input_string)
        
        print(output_string)

if __name__ == "__main__":
    main()
