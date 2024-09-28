# Shopify Eng Intern W25 Challenge
# Braille Translator

# Dictionary for English - Braille
alphabet = {
    # Lower-case letters
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", 
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "00.00.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",

    # Numbers
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO",
    "9": ".OO...", "0": ".OOO..",

    # ___ follows
    "capital follows": ".....O",
    "decimal follows": ".O...O",
    "number follows": ".O.OOO",

    # symbols
    ".": "..OO.O", ",": "..0...", "?": "..O.OO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
    " ": "......",
}

#  read six chars at a time
#  append to temp string

input_word = input() # user input word


# English to Braille
def english_brail_translate(word):
    translated_word = "" # final translated word

    for char in word: # iterate through each character in the word

        # checks to see if char is a capital letter
        if char.isupper() and char.isalpha():
            translated_word += alphabet["capital follows"]
            translated_word += alphabet[char.lower()]

        # checks to see if char is a lowercase letter
        elif char.isalpha():
            translated_word += alphabet[char]

        # checks to see if char is a number
        elif char.isnumeric():

            # if last char is a number, don't add "number follows"
            if len(translated_word) == 0 or not translated_word[-1].isnumeric(): #not working **********
                translated_word += alphabet["number follows"]
                translated_word += alphabet[char]
            else:
                translated_word += alphabet[char]

        # check if char is a space
        elif char == " ":
            translated_word += alphabet[char]

        # last option is for char to be a decimal / space
        else:
            translated_word += alphabet["decimal follows"]
            translated_word += alphabet[char]

    print(translated_word)



# Braille to English
def brail_english_translate(word):
    translated_word = "" # final translated word
    print(word)


#  check if input is braille or english
if "." in input_word[:6] or "O" in input_word[:6]:
    brail_english_translate(input_word)
else:
    english_brail_translate(input_word)