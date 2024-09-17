import sys

braille_dict = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'capital_follows': '.....O',
    'decimal_follows': '.O...O',
    'number_follows': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

braille_numbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

def translate_to_eng(text):
    """
    Translates a given text from Braille to English.

    Args:
        text (str): The Braille text to be translated.

    Returns:
        str: The translated English text.
    """

    eng_result = ''
    capital_next = False
    number_next = False

    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]

        if(number_next):
            for key, value in braille_numbers.items():
                if(value == braille_char):
                    eng_result += key
                    break
            if(braille_char == braille_dict[' ']):
                number_next = False
        else:
            for key, value in braille_dict.items():
                if(value == braille_char):
                    if(capital_next):
                        eng_result += key.upper()
                        capital_next = False
                    elif(key == 'capital_follows'):
                        capital_next = True
                    elif key == 'number_follows':
                        number_next = True
                    elif key == 'decimal_follows':
                        eng_result += '.'                    
                    else:
                        eng_result += key
                    break
    return eng_result

def translate_to_braille(text):
    """
    Translates the given text into Braille.

    Args:
        text (str): The text to be translated.

    Returns:
        str: The translated text in Braille.
    """

    braille_result = ''
    number_next = False
    for letter in text:
        if(letter.isupper()):
            braille_result += braille_dict['capital_follows']
            braille_result += braille_dict[letter.lower()]
        else:
            if(number_next and letter == ' '):
                number_next = False
                braille_result += braille_dict[letter]
            elif((not number_next) and letter in braille_numbers.keys()):
                number_next = True
                braille_result += braille_dict['number_follows']
                braille_result += braille_numbers[letter]
            elif(number_next):
                braille_result += braille_numbers[letter]
            else:
                braille_result += braille_dict[letter]
        
    return braille_result

def main():
    """
    Translates the given text to either English or Braille based on the presence of certain characters.

    The function takes the text to be translated as command line arguments and prints the translated result.

    Args:
        None

    Returns:
        None
    """
    args = sys.argv[1:]
    
    if(len(args) < 1):
        print("Error: Please enter a text to translate")
        return

    text = args[0]
    for i in range(1, len(args)):
        text += ' ' + args[i]

    result = ''
    if(text.find('.') != -1 or (text.find('0') != -1 and text.find('.') != -1)):
        result = translate_to_eng(text)
    else:
        result = translate_to_braille(text)
    print(result)

if __name__ == "__main__":
    main()