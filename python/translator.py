import sys

# Braille to English Letter Dictionary
braille_to_english_letter = {
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
english_letter_to_braille = {
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
braille_to_number = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4',
    "O..O..": '5', "OOO...": '6', "OOOO..": '7', "O.OO..": '8',
    ".OO...": '9', ".OOO..": '0'
}

# Number to Braille Dictionary
number_to_braille = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
    '9': ".OO...", '0': ".OOO.."
}

# Check if Input is Braille
def is_braille(input):
    return all(c in 'o.' for c in input)

# Translate Braille to English
def braille_to_english(input):
    
    # Split the input into 6-character chunks
    letters = [input[i:i+6] for i in range(0, len(input), 6)]

    english = []
    capital_next = False
    number_next = False

    for letter in letters:
        translated_letter = braille_to_english_letter[letter]

        if translated_letter == "cap":
            capital_next = True
        elif translated_letter == "num":
            number_next = True
        elif translated_letter == " ":
            english.append(braille_to_english_letter[translated_letter])
            number_next == False
        elif not capital_next:
            english.append(translated_letter.lower())
            capital_next = False
        elif number_next:
            english.append(braille_to_number[letter])
        else:
            english.append(translated_letter)
    return ''.join(english)

# Translate English to Braill
def english_to_braille(input):
     
    braille = []
    number_prev = False
    
    for char in input:
        if char.isdigit():
            if not number_prev:
                braille.append(".O.OOO")
                number_prev = True
            braille.append(number_to_braille[char])
        elif char.isalpha():
            if char.islower():
                braille.append(english_letter_to_braille[char.upper()])
            else:
                braille.append(".....O")
                braille.append(english_letter_to_braille[char])
        elif char.isspace():
            braille.append(english_letter_to_braille[char])
            number_prev = False;
        else:
            braille.append(english_letter_to_braille[char])
    
    return ''.join(braille)

def main():
    input = ' '.join(sys.argv[1:])

    if is_braille(input):
        output = braille_to_english(input)
    else:
        output = english_to_braille(input)

    print(output)

if __name__ == "__main__":
    main()

