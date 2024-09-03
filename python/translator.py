#!/usr/bin/env python3
import sys
finalTranslation = ""

numberStarted = False

def main(sentence):
    """Main function"""
    for char in sentence:
        if char != '.' and char != 'O':  # The message is in English
            print(englishToBraille(sentence))
            return

    print(brailleToEnglish(sentence))
    return

alphabet = {'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..",
            'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.",
            'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO",
            'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO", '.': "..OO.O", ',': "..O...",
            '?': "..O.OO", '!': "..OOO.", ':': "..OO..", ';': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O",
            '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.", ' ': "......"}

alphabetNumber = {'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...",
                  '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."}


def englishToBraille(input):
    finalTranslation = ""
    numberStarted = False
    for char in input:

        if numberStarted == True and char == '.':  # decimal follows
            finalTranslation += ".O...O"
            finalTranslation += alphabet[char]
        elif char.isdigit() and not numberStarted:  # series of numbers started
            finalTranslation += ".O.OOO"
            finalTranslation += alphabetNumber[char]
            numberStarted = True
        elif char.isdigit() and numberStarted:  # Inside series of numbers
            finalTranslation += alphabetNumber[char]
        elif numberStarted and char == ' ':  # series of numbers ended
            finalTranslation += alphabet[char]
            numberStarted = False
        elif char.isalpha() and char.isupper():  # uppercase alphabet
            finalTranslation += ".....O"
            finalTranslation += alphabet[char.lower()]
        else:
            finalTranslation += alphabet[char]
    return finalTranslation


braille = {"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
           "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
           "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
           "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "..OO.O": ".", "..O...": ",",
           "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
           "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")", "......": " "}

brailleNumber = {"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
                 "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"}

def brailleToEnglish(input):
    finalTranslation = ""
    isCapital = False
    isNumber = False
    for i in range(0, len(input), 6):
        subString = input[i:i + 6]

        if subString == ".....O":  # Capital Letter follows

            isCapital = True
        elif isCapital:  # Turns character capital

            finalTranslation += braille[(subString)].upper()
            isCapital = False
        elif subString == ".O...O":  # Decimal follows
            continue # Do nothing as this is just for context and actual decimal character is same as period.
        elif subString == ".O.OOO": 			# Number follows
            isNumber = True
        elif isNumber and subString == "......": # Reached a space, so isNumber=false.
            isNumber = False
        elif isNumber:  # outputs Number
            finalTranslation += brailleNumber[subString]
        else:
            finalTranslation += braille[subString]

    return finalTranslation



if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Combine all command-line arguments into a single string
        input_text = " ".join(sys.argv[1:])
        main(input_text)
    else:
        pass

