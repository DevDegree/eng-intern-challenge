#first step is to determine whether the String is Braille or English
#can do this by scanning for letters other than . or O
#also, if it is Braille, then we need to validate that the input is divisible by 6
#will need to create 2 hashmaps. one will map english to braille, the other will map braille to english.

#later need to create a check if 2 decimal points in a number (this should fail)

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
    " ": "......",
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
    "..OO.O": ".", #normal period
    # ".O...O": ".", #decimal follows
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
    "......": " "
}

num_map = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
    ".O...O": ".", #decimal follows
}

#didn't map capital follows, decimal follows, and number follows
#what is the difference between decimal follows and number follows? decimal is "." which is different from the "." in a normal string

if len(sys.argv) < 2:
    print("Please pass at least 1 argument")
    sys.exit(1)

input_string = ""
for i, word in enumerate(sys.argv):
    if i == 0:
        continue
    input_string += word
    if i != len(sys.argv) - 1:
        input_string += " "

is_brail = True
return_string = ""

for letter in input_string:
    if letter != "O" and letter != ".":
        is_brail = False
        break

if is_brail and len(input_string) %6 != 0 and len(input_string) < 6:
    is_brail = False
    #treat as english if only O and . are in the String but it is less than 6 characters

if is_brail:
    if len(input_string) % 6 != 0:
        print("Braille string must be divisible by 6")
        sys.exit(1)
    
    number_follows = False
    capital_follows = False
    decimal_follows = False
    for i in range(0, len(input_string), 6):
        curr_character = input_string[i:i+6]
        # print(curr_character)
        #need to add a few more conditions for exit below
        if curr_character not in converter and curr_character not in num_map and curr_character != ".....O" and curr_character != ".O.OOO":
            print("The following character does not exist: " + curr_character)
            sys.exit(1)
        elif curr_character == ".....O":
            capital_follows = True
        elif curr_character == ".O.OOO":
            number_follows = True
        elif capital_follows == True:
            #need to actually check if the braille is an alphabet character. (cannot capitalize a number or other token)
            if converter[curr_character] in "abcdefghijklmnopqrstuvwxyz":
                return_string += converter[curr_character].upper()
                capital_follows = False
            else:
                print("Cannot capitalize: " + converter[curr_character])
                sys.exit(1)
        elif curr_character == "......":
            number_follows = False
            decimal_follows = False
            return_string += converter[curr_character]
        elif number_follows == True:
            if curr_character in num_map:
                if curr_character == ".O...O":
                    if decimal_follows == True:
                        print("Cannot have more than 1 decimal in a number")
                        sys.exit(1)
                    else:
                        decimal_follows = True
                return_string += num_map[curr_character]
            else:
                print("The following is not a decimal when it should be: " + curr_character)
                sys.exit(1)
        else:
            return_string += converter[curr_character]

else:
    number_follows = False
    decimal_follows = False
    for letter in input_string:
        if letter.isupper():
            return_string += ".....O"
            return_string += converter[letter.lower()]
        elif letter == " ":
            number_follows = False
            decimal_follows = False
            return_string += converter[letter]
        elif letter == "." and number_follows == True:
            if decimal_follows == False:
                return_string += ".O...O"
                decimal_follows = True
            else:
                print("Cannot have two decimals in a number")
                sys.exit(1)
        elif letter in "0123456789":
            if number_follows == False:
                number_follows = True
                return_string += ".O.OOO"
            return_string += converter[letter]
        elif letter not in converter:
            print("The following character: " + letter + ", cannot be converted to Braille")
            sys.exit(1)
        else:
            return_string += converter[letter]
        

print(return_string)

# ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
# ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"