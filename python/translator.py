import sys

## Dictionary containing english letters as keys and their braille string as the value
english_to_braille_letters = {
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
    " ": "......",
}

## dictionary containing the numbers as key and their braille version as the value
numbers_to_braille = {
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

## list comprehension to translate from braille text to english text
braille_numbers_to_numbers = {v: k for k,v in numbers_to_braille.items()}
braille_letters_to_english = {v: k for k,v in english_to_braille_letters.items()}

## grabs the arguments given to the program whilst ignoring script name
args = sys.argv[1:]

## boolean value that stores whether or not our arguments are braille or english
braille = False

## Checks if our string only contains the braille values
if set(args[0]) == {"O","."}:
    braille = True

## Braille case
if braille:
    english_word = ""
    ## joins all braille arguments by spaces
    braille_strings = "......".join(args)
    ## partitions the braille string into a list of letters 
    braille_characters = [braille_strings[i:i + 6] for i in range(0,len(braille_strings),6)]
    number = 0
    capital = 0
    for i in braille_characters:
        ## checks if a number will follow
        if i == ".O.OOO":
            number = 1
        ## checks if we currently are converting a number and then checks if we have reached a space
        ## and adds a space to our string
        elif number == 1 and i == "......":
            number = 0
            english_word += " "
        ## adds another digit to our current string
        elif number == 1:
            english_word += braille_numbers_to_numbers[i]
        ## checks if the value is capital follows
        elif i == ".....O":
            capital = 1
        ## adds capital letter to string 
        elif capital == 1:
            english_word += braille_letters_to_english[i].upper()
            capital = 0
        ## adds any other character to the string
        else:
            english_word += braille_letters_to_english[i]
    
    print(english_word)

else:
    ## adds a space in between our english arguments
    english_words = " ".join(args)
    braille_string = ""
    number = 0
    for i in english_words:
        ## checks if our character is an upper case letter
        if i.isupper():
            braille_string += ".....O"
            braille_string += english_to_braille_letters[i.lower()]
            ## checks if the character is a number
        elif i.isnumeric() and number == 0:
            number = 1
            braille_string += ".O.OOO"
            braille_string += numbers_to_braille[i]
        ## checks if our character is a space and our boolean number is true
        elif i == " " and number == 1:
            number = 0
            braille_string += english_to_braille_letters[i]
        ## checks if our value is a number and number equals 1
        elif i.isnumeric():
            braille_string += numbers_to_braille[i]
        else:
            braille_string += english_to_braille_letters[i]
        
    print(braille_string)
    


