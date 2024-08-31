import sys

# Braille to English Letter Dictionary
braille_to_english_dict = {
    "O.....": "A", "O.O...": "B", "OO....": "C", "OO.O..": "D",
    "O..O..": "E", "OOO...": "F", "OOOO..": "G", "O.OO..": "H",
    ".OO...": "I", ".OOO..": "J", "O...O.": "K", "O.O.O.": "L",
    "OO..O.": "M", "OO.OO.": "N", "O..OO.": "O", "OOO.O.": "P",
    "OOOOO.": "Q", "O.OOO.": "R", ".OO.O.": "S", ".OOOO.": "T",
    "O...OO": "U", "O.O.OO": "V", ".OOO.O": "W", "OO..OO": "X",
    "OO.OOO": "Y", "O..OOO": "Z",

    "..OO.O": ".", "..O...": ",", "..O.OO": "?", 
    "..OOO.": "!", "..OO..": ":", "..O.O.": ";",
    "....OO": "-", ".O..O.": "/", ".OO..O": "<",  
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")",   "......": " ", 

    ".....O": "cap", ".O...O": "dec", ".O.OOO": "num"
}

# English Letter to Braille Dictionary
english_to_braille_dict = {
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..",
    "E": "O..O..", "F": "OOO...", "G": "OOOO..", "H": "O.OO..",
    "I": ".OO...", "J": ".OOO..", "K": "O...O.", "L": "O.O.O.",
    "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.", "P": "OOO.O.",
    "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
    "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO",
    "Y": "OO.OOO", "Z": "O..OOO",

    ".": "..OO.O", ",": "..O...", "?": "..O.OO", 
    "!": "..OOO.", ":": "..OO..", ";": "..O.O.",
    "-": "....OO", "/": ".O..O.", "<": ".OO..O",  
    ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......",

    "cap": ".....O", "dec": ".O...O", "num": ".O.OOO"
}

# Braille to Number Dictionary
braille_to_num_dict = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4',
    "O..O..": '5', "OOO...": '6', "OOOO..": '7', "O.OO..": '8',
    ".OO...": '9', ".OOO..": '0'
}

# Number to Braille Dictionary
num_to_braille_dict = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
    '9': ".OO...", '0': ".OOO.."
}

def is_braille(input_text):
    return all(c in 'o.' for c in input_text)


def translate_braille_to_english(braille_text):

    chunks = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    english_text = []
    is_capital_next = False
    is_number_next = False

    for chunk in chunks:
        translated_char = braille_to_english_dict[chunk]

        if translated_char == "cap":
            is_capital_next = True
        elif translated_char == "num":
            is_number_next = True
        elif translated_char == " ":
            english_text.append(braille_to_english_dict[translated_char])
            is_number_next = False
        elif not is_capital_next:
            english_text.append(translated_char.lower())
            is_capital_next = False
        elif is_number_next:
            english_text.append(braille_to_num_dict[chunk])
        else:
            english_text.append(translated_char)
    return ''.join(english_text)

def translate_english_to_braille(english_text):

    braille_text = []
    was_number_prev = False

    for char in english_text:
        if char.isdigit():
            if not was_number_prev:
                braille_text.append(".O.OOO")
                was_number_prev = True
            braille_text.append(num_to_braille_dict[char])
        elif char.isalpha():
            if char.islower():
                braille_text.append(english_to_braille_dict[char.upper()])
            else:
                braille_text.append(".....O")
                braille_text.append(english_to_braille_dict[char])
        elif char.isspace():
            braille_text.append(english_to_braille_dict[char])
            was_number_prev = False
        else:
            braille_text.append(english_to_braille_dict[char])

    return ''.join(braille_text)

def main():
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text): output_text = translate_braille_to_english(input_text)
    else: output_text = translate_english_to_braille(input_text)

    print(output_text)

if __name__ == "__main__":
    main()
