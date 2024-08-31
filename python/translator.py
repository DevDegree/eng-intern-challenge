"""
Shopify Eng Intern Challenge Fall - Winter 2025

Name: Falak Rastogi
Email: falakrast1@gmail.com

Terminal / command-line application that can translate Braille to English and vice versa.
"""
import sys

# Dictionary to convert alphabets to Braille
eng_to_braille = {
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
    " ": "......"  # space
}

# Dictionary to convert Braille to alphabets
braille_to_eng = {braille: eng for eng, braille in eng_to_braille.items()}

# Dictionary to convert numbers to Braille
num_to_braille = {
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
}

# Dictionary to convert Braille to numbers
braille_to_num = {braille: eng for eng, braille in num_to_braille.items()}

# Dictionary containing "Capital follows" and "Number follows"
additionals = {
    "capital_follows": ".....O",
    "number_follows": ".O.OOO"
}

# Function to translate English to Braille
def translate_to_braille(text: str) -> str:
    """Translates English input text to braille and returns a string of braille characters"""

    result = []
    number_mode = False

    for char in text:
        if char.isdigit():  # If it's a number and we are not already in number mode
            if not number_mode:
                number_mode = True
                result.append(additionals["number_follows"])
            result.append(num_to_braille[char])
        elif char == " ":  # In case of a space
            number_mode = False
            result.append(eng_to_braille[char])
        elif char.isupper():  # In case of a capital letter
            result.append(additionals["capital_follows"])
            result.append(eng_to_braille[char.lower()])
        else:
            result.append(eng_to_braille[char.lower()])

    return "".join(result)


# Function to translate Braille to English
def translate_to_english(text: str) -> str:
    """Translates Braille input to English and returns a string of English characters"""

    result = []
    i = 0
    length = len(text)
    number_mode = False

    while i < length:
        chunk = text[i:i+6]
        if chunk == additionals["capital_follows"]:
            i += 6
            chunk = text[i:i+6]
            result.append(braille_to_eng[chunk].upper())
        elif chunk == additionals["number_follows"]:
            number_mode = True
        elif chunk == '......':  # space
            number_mode = False
            result.append(braille_to_eng[chunk])
        else:
            if number_mode:
                result.append(braille_to_num[chunk])
            else:
                result.append(braille_to_eng[chunk])

        i += 6
    return "".join(result)


def translate_language(input_text: str) -> bool:
    """Returns True to translate to English, False to translate to Braille"""
    for char in input_text:
        if char not in ['.', 'O']:
            return False
    return True


def main() -> None:
    input_text = ' '.join(sys.argv[1:])

    if translate_language(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))


if __name__ == '__main__':
    main()
