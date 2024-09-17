import sys

# Dictionary containing the Latin and Braille characters
latin_to_braille = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
}

arabic_numbers_to_braille = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
}

braille_to_latin = {v: k for k, v in latin_to_braille.items()}
braille_to_arabic_numbers = {v: k for k, v in arabic_numbers_to_braille.items()}


def determine_language(sentence):
    braille = True

    for char in sentence:
        # Toggle braille to false if a normal latin character appears
        if (char.lower() in latin_to_braille or char in arabic_numbers_to_braille) and char != 'O' and char != ".":
            braille = False

    if braille:
        braille_to_english(sentence)
    else:
        english_to_braille(sentence)


def braille_to_english(sentence):
    result = ""
    capital_follows = False
    number_follows = False

    for i in range(0, len(sentence), 6):
        # slice out a fragment
        fragment = sentence[i:i + 6]

        if fragment == ".....O":
            capital_follows = True
        elif fragment == ".O.OOO":
            number_follows = True
        elif number_follows:
            result += str(braille_to_arabic_numbers[fragment])
        elif fragment == "......":  # space character
            result += " "
            number_follows = False
        elif capital_follows:
            result += (braille_to_latin[fragment]).upper()
            capital_follows = False
        else:  # for lowercase letters
            result += (braille_to_latin[fragment])
    print(result)


def english_to_braille(sentence):
    result = ""
    number_follows = False

    for i in range(len(sentence)):
        # slice out a fragment
        fragment = sentence[i]

        if fragment.lower() in latin_to_braille:  # covers all letters
            if fragment.isupper():
                letter = fragment.lower()
                result += ".....O" + latin_to_braille[letter]
            else:
                result += latin_to_braille[fragment]
        elif fragment == " ":  # covers spaces
            result += "......"
            number_follows = False
        elif fragment in arabic_numbers_to_braille and not number_follows:  # covers all numbers
            number_follows = True
            result += ".O.OOO" + str(arabic_numbers_to_braille[fragment])
        else:
            result += str(arabic_numbers_to_braille[fragment])

    print(result)


if __name__ == "__main__":
    input_sentence = ' '.join(sys.argv[1:])

    determine_language(input_sentence)
