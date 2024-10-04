import sys

englishTranslation = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
                      'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
                      'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
                      'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
                      'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
                      'z': 'O..OOO', ' ': '......'}

numberText = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
                      '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
                      '0': '.OOO..', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
                      ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
                      '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'}

brailleTranslation = {v: k for k, v in englishTranslation.items()}
brailleNumbers = { v: k for k, v in numberText.items()}
capital_char = '.....O'
number_char = '.O.OOO'


def toBraille(message):
    brailleMessage = []
    numberFlag = False
    for char in message:

        if char.isdigit():  # Check if the character is a number

            if not numberFlag:
                brailleMessage.append(number_char)
                numberFlag = True #Number flag initializes for the first number. only becomes false if it's not a number
            brailleMessage.append(numberText[char])
        elif char.isupper():  # Check for capital letters
            # Add capital prefix followed by the lowercase version of the character
            brailleMessage.append(capital_char)
            brailleMessage.append(englishTranslation[char.lower()])
            numberFlag = False
        elif char in englishTranslation:
            brailleMessage.append(englishTranslation[char])
            numberFlag = False
        else:
            # Handle unknown characters with a placeholder
            brailleMessage.append('?')

    return ''.join(brailleMessage)


def toEnglish(message):
    englishMessage = []
    numberFlag = False
    capitalFlag = False

    # Split Braille input into chunks of 6 characters (each Braille character is 6 dots)
    brailleChars = [message[i:i + 6] for i in range(0, len(message), 6)]

    for char in brailleChars:
        if char == number_char:
            numberFlag = True
        elif char == capital_char:
            capitalFlag = True

        elif char in brailleTranslation:

            if numberFlag:
                #Check if it's the space symbol. only turns the flag into false if it is a space symbol
                if char == englishTranslation[' ']:
                    numberFlag = False
                else:
                    englishMessage.append(brailleNumbers[char])

            elif capitalFlag:
                englishMessage.append(brailleTranslation[char].upper())  # Capitalize the letter
                capitalFlag = False  # Reset capital flag after use

            else:
                englishMessage.append(brailleTranslation[char])
        else:
            englishMessage.append('?')  # Handle unknown characters

    return ''.join(englishMessage)


if __name__ == '__main__':

    input = sys.argv[1]

    if len(input) < 2:
        print("Please enter a valid message")

    elif input.isalnum():
        print(toBraille(input))

    else:
        print(toEnglish(input))


