import sys


CAPITAL = '.....O'
NUMBER = '.O.OOO'
SPACE = "......"


ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......'
}
BRAILLE_TO_ALPHABET = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}
BRAILLE_TO_NUMBER = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}


def braille_to_english(input_text):

    # We need to split the input text into every 6 characters

    chunks = []

    for i in range(0, len(input_text), 6):
        chunks.append(input_text[i:i+6])

    digit_flag = False

    b = 0

    while b < len(chunks):

        if chunks[b] == CAPITAL:
            print(BRAILLE_TO_ALPHABET[chunks[b+1]].upper(), end='')
            b += 2

        # we need to make sure if we have encountered a number encoding then every chunk after is a number until we encounter a space

        elif chunks[b] == NUMBER:
            digit_flag = True
            print(BRAILLE_TO_NUMBER[chunks[b+1]], end='')
            b += 2

        else:
            if digit_flag == True:
                print(BRAILLE_TO_NUMBER[chunks[b]], end='')
                b += 1
            else:
                if chunks[b] == SPACE:
                    digit_flag = False
                print(BRAILLE_TO_ALPHABET[chunks[b]], end='')
                b += 1

    print()


def english_to_braille(input_text):

    digit_flag = False

    for i in input_text:
        if i.lower() != i:
            braille_text = ".....O" + ENGLISH_TO_BRAILLE[i.lower()]
            print(braille_text, end='')

        elif i.isdigit():

            if digit_flag == False:
                braille_text = ".O.OOO" + ENGLISH_TO_BRAILLE[i]
                digit_flag = True
            else:
                braille_text = ENGLISH_TO_BRAILLE[i]
            print(braille_text, end='')

        else:

            if i == ' ':
                braille_text = ENGLISH_TO_BRAILLE[i]
                digit_flag = False
            else:
                braille_text = ENGLISH_TO_BRAILLE[i]

            print(braille_text, end='')

    print()


def main():

    input_text = " ".join(sys.argv[1:])

    # We need to check if input text is in english or braille

    if all(c in 'O.' for c in input_text) and len(input_text) % 6 == 0:
        # Call the braille to english function
        braille_to_english(input_text)
    else:
        # Call the english to braille function
        english_to_braille(input_text)


if __name__ == "__main__":
    main()
