import sys
import unittest

# flags for special cases

braille_capital_flag = '.....O'
braille_number_flag = '.O.OOO'
braille_decimal_flag = '.O...O'

# maps to convert english to braille

braille_letters = {
    ' ': '......',
    'a': 'O......',
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
    '()': 'O.O..O',
    ')': '.O.OO.'
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



# braille to english
def braille_to_english(text):
    translated_text=[]
    return ''



# english to braille
def english_to_braille(text):
    translated_text=[]
    is_number = False

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
        # space indicates end of number input
        elif c == ' ' and is_number:
            is_number = False
            translated_text.append(braille_letters[c])
        # no special case
        else:
            translated_text.append(braille_letters[c])

    # return the dict as a string for printing
    return ''.join(translated_text)



'''
edge cases
    english encountered in braille string?
        translate entire string as english
    incomplete braille letter at end of string
        ignore trailing 1-5 characters (6 would be another braille letter)
    inalid braille letter found in string
        ignore, print nothing for this letter
    unrecognized/invalid english letter found in string
        ignore, print nothing for this letter
    empty string as argument
        print nothing
    forgetting to put space-flag after numbers conclude (invalid braille to english)
        treat as usual braille (if letters A to J, translate into numbers - else, translate as letters/symbols as usual?)
'''

'''
other notes: overall
    global vars for flags (capitals/numbers/decimals) and the chunk size, 6
    use a dict to append substrings to the end_translation string and then join it all together at the end

other notes: english to braille
    use bools to track capitals/numbers/decimals
    slice the string in chunks of 6 (i:i+6)
    if encounter a . then must check if period or decimal (number flag true?)

other notes: braille to english
    just read in the next char, check for flags in the char (capitals/numbers/decimals)
    append accordingly
    number flag only matters if next braille letter is A to J (decimal point, symbols unchanged)
'''


class TestTranslator(unittest.TestCase):
    def test_eng_to_braille(self):
        self.assertEqual(english_to_braille(' '), '......')
        self.assertEqual(english_to_braille('maggie is the coolest'), 'OO..O.O......OOOO..OOOO...OO...O..O.........OO....OO.O........OOOO.O.OO..O..O........OO....O..OO.O..OO.O.O.O.O..O...OO.O..OOOO.')
        self.assertEqual(english_to_braille('mixOfCaps'), 'OO..O..OO...OO..OO.....OO..OO.OOO........OOO....O......OOO.O..OO.O.')
        self.assertEqual(english_to_braille('CAPSCAPSCAPS'), '.....OOO.........OO...........OOOO.O......O.OO.O......OOO.........OO...........OOOO.O......O.OO.O......OOO.........OO...........OOOO.O......O.OO.O.')
        #self.assertEqual(english_to_braille('1234 abcd'), '.O.OOOO.....O.O...OO....OO.O........O.....O.O...OO....OO.O..')
        self.assertEqual(english_to_braille('Hello world'), '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..')
        self.assertEqual(english_to_braille('42'), '.O.OOOOO.O..O.O...')

        #def test_braille_to_eng(self):
            #self.assertEqual()
        #unittest.main()

def test_suite():
    unittest.main()

def main():
    translation_input = sys.argv[1]
    
    # determine if string is braille or english (ie is it all O or . chars) and call corresponding function
    # braille to english
    if all(c in '.O' for c in translation_input):
        print(braille_to_english(translation_input))
    # english to braille
    else:
        print(english_to_braille(translation_input))


if __name__ == "__main__":
    #main()
    test_suite()