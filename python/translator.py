"""
Shopify Eng Intern Challenge Fall - Winter 2025

Name: Falak Rastogi
Email: falakrast1@gmail.com

Terminal / command-line application that can translate Braille to English and vice versa.
"""

# Braille dictionary to convert English to Braille
braille_dict = {

    # alphabets
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

    # numbers
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

    # additionals
    " ": "......",
    "capital_follows": ".....O",
    "number_follows": ".O.OOO"
}


# English dictionary to convert Braille to English
english_dict = {braille: eng for eng, braille in braille_dict.items()}


# Function to translate English to Braille
def translate_to_braille(text: str) -> str:
    """Translates English input text to braille and returns a string of braille characters"""

    result = []
    number_mode = False
    for char in text:
        if char.isdigit() and not number_mode:
            result.append(braille_dict["number_follows"])
            number_mode = True
        elif not char.isdigit() and number_mode:
            number_mode = False

        if char.isupper():
            result.append(braille_dict["capital_follows"])
            result.append(braille_dict[char.lower()])
        else:
            result.append(braille_dict[char.lower()])

    return "".join(result)

if __name__ == '__main__':
    answer = translate_to_braille("Abc 123")
    print(answer == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")