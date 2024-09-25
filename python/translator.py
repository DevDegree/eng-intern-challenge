import sys
import re

ENGLISH_TO_BRAILLE = {
    ' ': '......', 'a': 'O.....', 'b': 'O.O...', 
    'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.',
    'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 
    'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O',
    'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 
    'CAP': '.....O',
    'NUM': '.O.OOO'
}

BRAILLE_TO_ENGLISH = dict((reversed(item) for item in ENGLISH_TO_BRAILLE.items()))

LETTER_TO_NUMBER = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 
                    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}

NUMBER_TO_LETTER = dict((reversed(item) for item in LETTER_TO_NUMBER.items()))


def braille_to_english (braille):
    """ takes braille input string, returns translated english string """
    letters = re.findall('..?.?.?.?.?', braille)
    if not letters or len(letters[-1]) % 6 != 0:
        return "Check that you have included the correct number of characters."
    
    word = ''
    capitalize = False
    number = False
    for letter in letters:
        if letter not in BRAILLE_TO_ENGLISH.keys():
            print("Could not translate '{}', check the correctness of the braille input string.".format(letter))
            sys.exit(1)
        elif BRAILLE_TO_ENGLISH[letter] not in LETTER_TO_NUMBER.keys():
            print("Could not translate '{}', check the correctness of the braille numerical characters.".format(letter))
            sys.exit(1)

        translation = BRAILLE_TO_ENGLISH[letter]

        if translation == "CAP":
            capitalize = True  # capitalizes the next character
        elif translation == "NUM":
            number = True
        elif number:
            word += LETTER_TO_NUMBER[translation]
        else:
            if capitalize:
                word += translation.upper()
            else:
                word += translation
            capitalize = False  # only capitalize the first occuring character
            if translation == " ":
                number = False

    return word


def english_to_braille (words):
    """ takes list of english strings, returns translated braille string """
    braille = ""
    for word in words:
        number = False
        for letter in word:
            if not letter.isnumeric() and letter.lower() not in ENGLISH_TO_BRAILLE.keys():
                print("'{}' is an invalid character, only use alphanumeric characters (A-Z, a-z, 0-9)".format(letter))
                sys.exit(1)

            if letter.isnumeric() and not number:
                number = True
                braille += ENGLISH_TO_BRAILLE["NUM"]
            if number:
                braille += ENGLISH_TO_BRAILLE[NUMBER_TO_LETTER[letter]]
            else:
                if letter.isupper():
                    braille += ENGLISH_TO_BRAILLE["CAP"]
                braille += ENGLISH_TO_BRAILLE[letter.lower()]

        # add a space after every word except the final one
        if words.index(word) != len(words)-1:
            braille += ENGLISH_TO_BRAILLE[" "]

    return braille


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Please provide an input string to translate.")
        sys.exit(1)

    # only braille input strings are expected to contain '.'
    if '.' in args[0]:
        print(braille_to_english(args[0]))
    else:
        print(english_to_braille(args))


if __name__ == '__main__':
    main()