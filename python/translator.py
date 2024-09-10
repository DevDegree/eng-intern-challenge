"""
This is my assessment.
"""
import sys

braille_dict_letter = {
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

braille_dict_number = {
    ' ': '......',  # space character
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
}

caps = '.....O'
nums = '.O.OOO'


def translator(sample):
    """
    >>> translator('Hello world')
    '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'
    >>> translator('42')
    '.O.OOOOO.O..O.O...'
    >>> translator('Abc 123')
    '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'
    >>> translator('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....')
    'Abc 123'
    >>> translator('.O.OOOOO.O..O.O...')
    '42'
    >>> translator('Abc 123 A')
    '.....OO.....O.O...OO...........O.OOOO.....O.O...OO...............OO.....'
    """

    def braille_to_english(braille):
        """

        :param braille:
        :return:
        """
        braille_in_list = [braille[i: i + 6] for i in range(0, len(braille), 6)]
        letter_list = list(braille_dict_letter.keys())
        braille_list_letter = list(braille_dict_letter.values())

        number_list = list(braille_dict_number.keys())
        braille_list_number = list(braille_dict_number.values())

        numlock = False
        caplock = False

        english = ''

        for i in braille_in_list:
            if i == '......':
                numlock = False

            if i == caps:
                caplock = True
            elif i == nums:
                numlock = True
            elif caplock:
                position = braille_list_letter.index(i)
                english += letter_list[position].upper()
                caplock = False
            elif numlock:
                position = braille_list_number.index(i)
                english += number_list[position]
            else:
                position = braille_list_letter.index(i)
                english += letter_list[position]

        return english

    def english_to_braille(english):
        """

        :param english:
        :return:
        """

        braille_text = ''
        numlock = False
        for i in english:
            if i == ' ':
                numlock = False
            if i.isupper():
                braille_text += caps + braille_dict_letter[i.lower()]
            elif i.isnumeric():
                if numlock:
                    braille_text += braille_dict_number[i]
                else:
                    braille_text += nums + braille_dict_number[i]
                    numlock = True
            else:
                braille_text += braille_dict_letter[i]
        return braille_text

    def is_braille(text):
        """

        :param text:
        :return:
        """
        valid_chars = {'O', '.'}
        for char in text:
            if char not in valid_chars:
                return False
        # Check if the text is a valid Braille pattern
        if len(text) % 6 != 0:
            return False
        return True

    if is_braille(sample):
        return braille_to_english(sample)
    else:
        return english_to_braille(sample)


sys.argv.pop(0)
argument = ' '.join(sys.argv)
print(translator(argument))
