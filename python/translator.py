#Shopify Winter Internship Challenge 2025
#Jeremy Thummel
#Braille Translator

entered_text = input()
braille_text_counter = 0
braille_entered = False
decoded_string = ""

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
    "CAP": ".....O",
    "DEC": ".O...O",
    "NUM": ".O.OOO",
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
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

braille_to_letter = {
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
    ".....O": "CAP",
    ".O...O": "DEC",
    ".O.OOO": "NUM",
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

braille_to_number = {
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

for current_char in entered_text:
    if current_char == 'O' or current_char == '.':
        braille_text_counter += 1

#Determine if entered text is braille
if braille_text_counter == len(entered_text):
    braille_entered = True

if braille_entered:
    current_braille_string = ""
    current_braille_string2 = "" #need this since strings are immutable
    english = ""
    next_char_cap = False
    next_char_num = False
    counter = 0

    for current_char in entered_text:
        current_braille_string = current_char
        current_braille_string2 += current_braille_string
        counter += 1

        print("totalString: "+current_braille_string2)
        if counter == 6:
            english = braille_to_letter[current_braille_string2]
            
            #Checks if special character
            if english == "CAP":
                next_char_cap = True
            elif english == "DEC":
                decoded_string += "."
                next_char_num = True
            elif english == "NUM":
                next_char_num = True
            elif english == " ":
                decoded_string += " "
                next_char_num = False

            #If normal letter or number
            else:
                if next_char_cap:
                    decoded_string += english.upper()
                    next_char_cap = False
                elif next_char_num:
                    decoded_string += braille_to_number[current_braille_string2]
                else:
                    decoded_string += english

            current_braille_string2 = ""
            current_braille_string = ""
            counter = 0

#If the user enters text that is not identified to be Braille
else:
    #numbers_start tracks if number follows braille should be outputted or not
    numbers_start = True

    for current_char in entered_text:
        if current_char == " ":
            numbers_start = True

        if current_char.isupper():
            decoded_string += ".....O"
            decoded_string += english_to_braille[current_char.lower()]
        
        elif current_char.isdigit():
            if numbers_start:
                decoded_string += ".O.OOO"

            decoded_string += english_to_braille[current_char]
            numbers_start = False

        else:
            decoded_string += english_to_braille[current_char]

print(decoded_string)