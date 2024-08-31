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

if is_brail:
    if len(input_string) % 6 != 0:
        print("Brail string must be divisible by 6")
        sys.exit(1)
    
    number_follows = False
    capital_follows = False
    for i in range(0, len(input_string), 6):
        # print(input_string[i:i+6])
        if input_string[i:i+6] not in converter and input_string[i:i+6] not in num_map:
            pass
        elif capital_follows == True:
            #need to actually check if the braille is an alphabet character. (cannot capitalize a number or other token)
            if converter[input_string[i:i+6]] in "abcdefghijklmnopqrstuvwxyz":
                return_string.append(converter[input_string[i:i+6]].lower())
            else:
                print("Cannot capitalize: " + converter[input_string[i:i+6]])
                sys.exit(1)
        elif input_string[i:i+6] == "......":
            number_follows = False
            return_string += converter[input_string[i:i+6]]
        # elif input_string[i:i+6]

else:
    number_follows = False
    for letter in input_string:
        if letter.isupper():
            return_string += ".....O"
            return_string += converter[letter.lower()]
        elif letter == " ":
            number_follows = False
            return_string += converter[letter]
        elif letter == "." and number_follows == True:
            return_string += ".O...O"
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