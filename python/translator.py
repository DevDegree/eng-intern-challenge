# import IO and testing
import sys
import unittest

# flags for special cases
braille_capital_flag = '.....O'
braille_number_flag = '.O.OOO'
braille_decimal_flag = '.O...O'

braille_size = 6

# maps to convert english to braille
braille_letters = {
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
    ' ': '......',
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
    'z': 'O..OOO'
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

# reversed maps to convert braille to english
english_letters = {c: l for l, c in braille_letters.items()}
english_numbers = {c: l for l, c in braille_numbers.items()}



# braille to english translator
def braille_to_english(text):

    # dict to store translated text and bools to track special states
    translated_text = []
    is_capital = False
    is_number = False

    # tracker to iterate through the string
    i = 0

    while i < len(text):
        # check if remaining text is still valid length
        if len(text[i:]) < braille_size:
            break

        # slice the next 6 chars to translate
        letter = text[i:i+braille_size]

        # check for flags for state changes
        if letter == braille_capital_flag:
            is_capital = True
        elif letter == braille_number_flag:
            is_number = True
        elif letter == braille_decimal_flag:
            translated_text.append('.')
        # check for number state change w/ space
        elif letter == braille_letters[' '] and is_number: #'......'
            is_number = False
            translated_text.append(' ')
        # explicitly handle the special case of > == o
        elif letter == braille_letters['>'] and is_number: #'O..OO.'
            translated_text.append('>')
        # if c is not a flag, then the letter should be translated and appended
        else:
            # handle numbers (number flag takes precedence over caps)
            if is_number and letter in english_numbers:
                translated_text.append(english_numbers[letter])
            # handle capital letters
            elif is_capital and letter in english_letters:
                is_capital = False
                upper_letter = english_letters[letter].upper()
                translated_text.append(upper_letter)
            # no special case, just translate the letter/symbol
            elif letter in english_letters:
                translated_text.append(english_letters[letter])

        # move to next segment of 6 chars to translate
        i += braille_size

    # return the final translated string
    return ''.join(translated_text)



# english to braille translator
def english_to_braille(text):

    # dict to store translated text and bool to track special state
    translated_text = []
    is_number = False

    # iterate through the string char by char
    for c in text:
        # check if a flag needs to be included before the char
        # upper case letter
        if c.isupper():
            translated_text.append(braille_capital_flag)
            # change to lowercase to access map w/ valid key
            c = c.lower()
            translated_text.append(braille_letters[c])
        # first number encountered
        elif c.isdigit() and not is_number:
            is_number = True
            translated_text.append(braille_number_flag)
            translated_text.append(braille_numbers[c])
        # NOT first number encountered
        elif c.isdigit() and is_number:
            # number flag not needed
            translated_text.append(braille_numbers[c])
        # explicitly handle some special cases
        # end of number input
        elif c == ' ' and is_number:
            is_number = False
            translated_text.append(braille_letters[c])
        # when . is decimal, not period
        elif c == '.' and is_number:
            translated_text.append(braille_decimal_flag)
        # translate as usual
        elif c in braille_letters:
            translated_text.append(braille_letters[c])

    # return the dict as a string for printing
    return ''.join(translated_text)



class TestTranslator(unittest.TestCase):
    # test english to braille translator
    def test_eng_to_braille(self):
        # empty input, space
        self.assertEqual(english_to_braille(''), '')
        self.assertEqual(english_to_braille(' '), '......')
        # regular strings w/ caps and nums
        self.assertEqual(english_to_braille('maggie is the coolest'), 'OO..O.O.....OOOO..OOOO...OO...O..O.........OO....OO.O........OOOO.O.OO..O..O........OO....O..OO.O..OO.O.O.O.O..O...OO.O..OOOO.')
        self.assertEqual(english_to_braille('mixOfCaps'), 'OO..O..OO...OO..OO.....OO..OO.OOO........OOO....O.....OOO.O..OO.O.')
        self.assertEqual(english_to_braille('CAPSCAPSCAPS'), '.....OOO.........OO..........OOOO.O......O.OO.O......OOO.........OO..........OOOO.O......O.OO.O......OOO.........OO..........OOOO.O......O.OO.O.')
        self.assertEqual(english_to_braille('1234 abcd'), '.O.OOOO.....O.O...OO....OO.O........O.....O.O...OO....OO.O..')
        self.assertEqual(english_to_braille('Hello world'), '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..')
        self.assertEqual(english_to_braille('42'), '.O.OOOOO.O..O.O...')
        self.assertEqual(english_to_braille('Abc 123'), '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....')
        # no space after number
        self.assertEqual(english_to_braille('111zzz'), '.O.OOOO.....O.....O.....O..OOOO..OOOO..OOO')
        self.assertEqual(english_to_braille('111jzzz'), '.O.OOOO.....O.....O......OOO..O..OOOO..OOOO..OOO')
        self.assertEqual(english_to_braille('1110zzz'), '.O.OOOO.....O.....O......OOO..O..OOOO..OOOO..OOO')
        # handle > vs o
        self.assertEqual(english_to_braille('1> oa'), '.O.OOOO.....O..OO.......O..OO.O.....')
        # decimal point
        self.assertEqual(english_to_braille('01.23'), '.O.OOO.OOO..O......O...OO.O...OO....')
        # period
        self.assertEqual(english_to_braille('ja.bc'), '.OOO..O.......OO.OO.O...OO....')
        # can translate 1A2B into braille, but not the other way around
        self.assertEqual(english_to_braille('1A2B'), '.O.OOOO..........OO.....O.O........OO.O...')
        # invalid input
        self.assertEqual(english_to_braille('mmm|\"*^%$'), 'OO..O.OO..O.OO..O.')
        # input braille and almost-all-braille
        self.assertEqual(english_to_braille('O.....a'), '.....OO..OO...OO.O..OO.O..OO.O..OO.O..OO.OO.....')
        self.assertEqual(english_to_braille('O.....'), '.....OO..OO...OO.O..OO.O..OO.O..OO.O..OO.O')

    # test braille to english translator
    def test_braille_to_eng(self):
        # empty input, space
        self.assertEqual(braille_to_english(''), '')
        self.assertEqual(braille_to_english('......'), ' ')
        # regular strings w/ caps and nums
        self.assertEqual(braille_to_english('OO..O.O.....OOOO..OOOO...OO...O..O.........OO....OO.O........OOOO.O.OO..O..O........OO....O..OO.O..OO.O.O.O.O..O...OO.O..OOOO.'), 'maggie is the coolest')
        self.assertEqual(braille_to_english('OO..O..OO...OO..OO.....OO..OO.OOO........OOO....O.....OOO.O..OO.O.'), 'mixOfCaps')
        self.assertEqual(braille_to_english('.....OOO.........OO..........OOOO.O......O.OO.O......OOO.........OO..........OOOO.O......O.OO.O......OOO.........OO..........OOOO.O......O.OO.O.'), 'CAPSCAPSCAPS')
        self.assertEqual(braille_to_english('.O.OOOO.....O.O...OO....OO.O........O.....O.O...OO....OO.O..'), '1234 abcd')
        self.assertEqual(braille_to_english('.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'), 'Hello world')
        self.assertEqual(braille_to_english('.O.OOOOO.O..O.O...'), '42')
        self.assertEqual(braille_to_english('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'), 'Abc 123')
        # no space after number
        self.assertEqual(braille_to_english('.O.OOOO.....O.....O.....O..OOOO..OOOO..OOO'), '111zzz')
        self.assertEqual(braille_to_english('.O.OOOO.....O.....O......OOO..O..OOOO..OOOO..OOO'), '1110zzz')
        # handle > vs o
        self.assertEqual(braille_to_english('.O.OOOO.....O..OO.......O..OO.O.....'), '1> oa')
        # decimal point
        self.assertEqual(braille_to_english('.O.OOO.OOO..O......O...OO.O...OO....'), '01.23')
        # period
        self.assertEqual(braille_to_english('.OOO..O.......OO.OO.O...OO....'), 'ja.bc')
        # check if number flag takes precedence over capital flag
        self.assertEqual(braille_to_english('.O.OOOO.....O.....O.O...O.O...'), '1122')
        self.assertEqual(braille_to_english('.O.OOOO..........OO.....O.O........OO.O...'), '1122')
        # invalid input
        self.assertEqual(braille_to_english('OO..O.OO..O.OO..O.OO.'), 'mmm')


def test_suite():
    unittest.main()


def main():
    # program was called with empty argument, do nothing
    if len(sys.argv) < 2:
        return
    
    # read input from argument + handle spaces
    translation_input = ' '.join(sys.argv[1:])
    
    # determine if string is braille or english (ie is it all O or . chars) and call corresponding function
    if all(c in '.O' for c in translation_input):
        # braille to english
        print(braille_to_english(translation_input))
    else:
        # english to braille
        print(english_to_braille(translation_input))


if __name__ == "__main__":
    main()
    #test_suite()