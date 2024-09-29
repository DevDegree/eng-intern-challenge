# Shopify Eng Intern W25 Challenge
# Braille Translator
# Yasmeen Elkheir

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

    # Decimals
    ".": "..OO.O", ",": "..0...", "?": "..O.OO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
    " ": "......",
}

# English to Braille
def english_brail_translate(word):
    translated_word = "" # To store final translated word
    is_number = False

    for char in word: # Iterate through each character in the word

        # Checks to see if char is a capital letter
        if char.isupper() and char.isalpha():
            translated_word += alphabet["capital follows"]
            translated_word += alphabet[char.lower()]

        # Checks to see if char is a lowercase letter
        elif char.isalpha():
            translated_word += alphabet[char]

        # Checks to see if char is a number
        elif char.isnumeric():
            # Add "number follows" only at the start of a number sequence
            if not is_number:
                translated_word += alphabet["number follows"]
                is_number = True
            translated_word += alphabet[char]

        # Check if char is a space
        elif char == " ":
            translated_word += alphabet[char]
            is_number = False

        # Last option is for char to be a decimal
        else:
            translated_word += alphabet["decimal follows"]
            translated_word += alphabet[char]

    print(translated_word)



# Braille to English
def brail_english_translate(word):
    translated_word = "" # Final translated word
    is_upper = False
    is_number = False
    is_decimal = False

    # Iterate over the word six chars at a time
    for i in range(0, len(word), 6):
        curr_digit = word[i: i+6]
        
        for char, braille in alphabet.items():
            if braille == curr_digit:

                # Indicator for next char to be a decimal
                if  char == "decimal follows":
                    is_decimal = True 

                # Indicator for next char to be a number
                elif char == "number follows":
                    is_number = True

                # Indicator for next char to be uppercase
                elif char == "capital follows":
                    is_upper = True
                
                # Turns letter to uppercase if last braille string indicated so
                if char.isalpha():
                    if is_upper:
                        translated_word += char.upper()
                        is_upper = False
                    else:
                        translated_word += char

                # Checks if the braille should be a number
                elif is_number:
                    if char.isnumeric():
                        translated_word += char
                    break

                # Checks for decimals
                elif is_decimal:
                    if not char.isalpha() and not char.isnumeric():
                        translated_word += char
                    is_decimal = False
                    break

                # Reset `is_number` when a space is encountered
                elif char == " ":
                    translated_word += char
                    is_number = False 
                    break

    print(translated_word)


input_word = input() # User input word

#  Check if input is braille or english
if "." in input_word[:6] or "O" in input_word[:6]:
    brail_english_translate(input_word)
else:
    english_brail_translate(input_word)