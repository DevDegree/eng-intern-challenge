# Rahaman Bappi

"""
This is a simple translator that translates a text message to braille and vice versa
"""

import sys
import dictionary

def braille_to_text(mssg_to_translate):
    """
    This function translates a braille message to text
    :param mssg_to_translate: message to translate
    """
    translated_mssg = ""
    is_capital = False
    is_number = False
    for i in range(0, len(mssg_to_translate), 6):
        character = mssg_to_translate[i:i + 6]
        is_number = False if character == dictionary.TEXT[' '] else is_number
        if character == dictionary.TEXT['CAPITAL']:
            is_capital = True
        elif character == dictionary.TEXT['NUMBER']:
            # Set is_number to True for the next character
            is_number = True
        elif is_number:
            translated_mssg += str(ord(dictionary.BRAILLE[character]) - 96)
        else:
            if is_capital:
                is_capital = False
                translated_mssg += dictionary.BRAILLE[character].upper()
            else:
                translated_mssg += dictionary.BRAILLE[character]
    print(translated_mssg)


def text_to_braille(mssg_to_translate):
    """
    This function translates a text message to braille
    :param mssg_to_translate: message to translate
    """
    translated_mssg = ""
    is_next_number = False
    for character in mssg_to_translate:
        if character.isdigit():
            translated_mssg += dictionary.TEXT['NUMBER'] if not is_next_number else ''
            is_next_number = True
            if character == '0':
                translated_mssg += dictionary.TEXT['0']
            else:
                translated_mssg += dictionary.TEXT[chr(int(character) + 96)]
        else:
            is_next_number = False
            if character.isupper():
                translated_mssg += dictionary.TEXT['CAPITAL']
            translated_mssg += dictionary.TEXT[character.lower()]
    print(translated_mssg)


if __name__ == "__main__":
    """
    This is the main function that takes the message to translate as input
    """
    message = ""

    for i in range(1, len(sys.argv)):
        if i != len(sys.argv) - 1:
            message += sys.argv[i] + " "
        else:
            message += sys.argv[i]

    if message[0] == '.':
        braille_to_text(message)
    else:
        text_to_braille(message)
