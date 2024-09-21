import argparse

braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".O.O..": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
}

braille_digits = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".O.O..": "9", ".OOO..": "0"
}

english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".O.O..", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", 
    ' ': "......"  # braille for space
}


english_to_braille.update({
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".O.O..", "0": ".OOO.."
})

# get arguments from user
def parse_arguments():
    parser = argparse.ArgumentParser(description="Translate between Braille and English.")
    parser.add_argument("texts", nargs='+', help="Texts to be translated.")
    return parser.parse_args()

# checks if the input is in braille or not
def is_braille(text):
    return all(c in 'O1.' for c in text.replace(' ', ''))

# translate from braille to english
def translate_braille_to_english(text):
    english_text = []
    braille_chars = [text[i:i + 6] for i in range(0, len(text), 6)]
    
    capital_mode = False
    number_mode = False

    for braille in braille_chars:
        if braille == ".....O":  # for capital sign
            capital_mode = True
            continue
        elif braille == ".O.OOO":  # for number sign
            number_mode = True
            continue
        elif braille in braille_to_english:
            if number_mode and braille in braille_digits:
                char = braille_digits[braille]
            else:
                char = braille_to_english[braille]

            if capital_mode:
                char = char.upper()
                capital_mode = False
            
            english_text.append(char)
        elif braille == "......":  # for space
            english_text.append(" ")
            number_mode = False
        else:
            english_text.append('?') # for unknown

    return ''.join(english_text)

# translate from english to braille
def translate_english_to_braille(text):
    braille_text = []
    number_mode = False

    for char in text:
        if char == ' ':
            braille_text.append("......")
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                braille_text.append(".O.OOO")
                number_mode = True
            braille_text.append(english_to_braille[char])
        elif char.isalpha():
            if char.isupper():
                braille_text.append(".....O")
            braille_text.append(english_to_braille[char.lower()])
            number_mode = False
        else:
            braille_text.append('??????')

    return ''.join(braille_text) 

def main():
    args = parse_arguments() # get the text from user
    text = ' '.join(args.texts)  # combine the text into one string.

    # Check if input is in braille or english and display result
    if is_braille(text):
        result = translate_braille_to_english(text)
    else:
        result = translate_english_to_braille(text)

    print(result)

if __name__ == "__main__":
    main()