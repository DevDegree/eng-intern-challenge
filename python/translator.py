import sys

#------ Removed one character cause of no 100% solution --------

# ">": "O..OO.", Duplicate braille from o and theres no way to tell even if context
    # For example you can check if there was an opening one "<" than allow but than if you were to make a statement like Apples > Peaches it wouldnt work

#------------------------------------------------------------------

# Defined Global Variables
SPACE = "......"
CAPITAL = ".....O"
NUMBER = ".O.OOO"
DECIMAL = ".O...O"

# Alphabet Dictionary
alphabet = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    # ">": "O..OO.", Duplicate braille from o and theres no way to tell even if context
    # For example you can check if there was an opening one "<" than allow but than if you were to make a statement like Apples > Peaches it wouldnt work
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

# Number Dictionary
number = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    ".": "..OO.O",
}


# Function to convert strings if its braille to blocks of 6
def split_string(s, block):
    return [s[i:i+block] for i in range(0, len(s), block)]

# Function to check if its braille or not
def braille_check(string: str) -> bool:
    # checks if characters is braille length
    is_correct_length = len(string) % 6 == 0
    # checks for characters that aren't . or O in string
    is_braille = all(char in ".O" for char in string)
    return is_correct_length and is_braille

#Translation Function
def translate(input_x):
    answer = []
    if braille_check(input_x):
        # Translation from braille to text
        alphabet_braille = {value: key for key, value in alphabet.items()}
        number_braille = {value: key for key, value in number.items()}

        input_x = split_string(input_x, 6)
        is_number = False
        is_capital = False
        for element in input_x:
            if element == SPACE:
                answer.append(" ")
                is_number = False
                is_capital = False
            elif element == NUMBER:
                is_number = True
            elif element == CAPITAL:
                is_capital = True
            elif is_number: 
                answer.append(number_braille.get(element, ""))
            else:
                char = alphabet_braille.get(element, "")
                if is_capital:
                    char = char.upper()
                    is_capital = False
                answer.append(char)
    else:
        # Translation from text to braille
        is_number = False
        for char in input_x:
            if char == " ":
                answer.append(SPACE) 
                is_number = False
            elif char.isdigit():
                if not is_number:
                    answer.append(NUMBER)
                    is_number = True
                answer.append(number[char])
            elif char.isupper():
                answer.append(CAPITAL)
                answer.append(alphabet[char.lower()])

            else:
                answer.append(alphabet[char])
            
    return ''.join(answer)

if __name__ == "__main__":
    args = " ".join(sys.argv[1:])
    output = translate(args)
    print(output)