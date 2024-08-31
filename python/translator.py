#first step is to determine whether the String is Braille or English
#can do this by scanning for letters other than . or O
#also, if it is Braille, then we need to validate that the input is divisible by 6
#will need to create 2 hashmaps. one will map english to braille, the other will map braille to english.

import sys

converter = {
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
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "O": ".OOO..",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

#didn't map capital follows, decimal follows, and number follows
#what is the difference between decimal follows and number follows? decimal is "." which is different from the "." in a normal string

if len(sys.argv) != 1:
    print("Please pass only 1 argument")
    sys.exit(1)

input_string = sys.argv[0]
is_brail = True
return_string = ""

for letter in input_string:
    if letter != "O" and letter != ".":
        is_brail = False
        break

if is_brail:
    if len(input_string) % 6 != 0:
        print("Brail string must be divisible by 6")
        sys.exit(1)
else:
    number_sequence = False
    for letter in input_string:
        if letter.isupper():
            return_string += ".....O"
            return_string += converter[letter]
        elif letter == " ":
            number_sequence = False
            return_string += converter[letter]
        elif letter == "." and number_sequence == True:
            return_string += ".O...O"
        elif letter in "0123456789":
            if number_sequence == False:
                number_sequence = True
                return_string += ".O.OOO"
            return_string += converter[letter]
        elif letter not in converter:
            print("The following character: " + letter + ", cannot be converted to Braille")
            sys.exit(1)
        else:
            return_string += converter[letter]
        

print(return_string)