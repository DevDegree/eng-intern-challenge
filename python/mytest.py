import unittest
from python.translator import to_braille, to_english

class TestBrailleTranslator(unittest.TestCase):

    def test_to_braille(self):
        # lowercase
        self.assertEqual(to_braille('a'), 'O.....')
        self.assertEqual(to_braille('b'), 'O.O...')

        # uppercase
        self.assertEqual(to_braille('H'), '.....OO.OO..')
        self.assertEqual(to_braille('X'), '.....OOO..OO')

        # numbers
        self.assertEqual(to_braille('1'), '.O.OOOO.....')
        self.assertEqual(to_braille('123'), '.O.OOOO.....O.O...OO....')

        # sentences
        self.assertEqual(to_braille('Hello world'), '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..')
        self.assertEqual(to_braille('A B C'), '.....OO................OO.O..............OOO....')
        self.assertEqual(to_braille('Helena at Shopify 24'), '.....OO.OO..O..O..O.O.O.O..O..OO.OO.O...........O......OOOO............O.OO.O.O.OO..O..OO.OOO.O..OO...OOO...OO.OOO.......O.OOOO.O...OO.O..')

    def test_to_english(self):
        # lowercase
        self.assertEqual(to_english('OOO.O.'), 'p')
        self.assertEqual(to_english('OOOO..'), 'g')

        # uppercase
        self.assertEqual(to_english('.....OO.....'), 'A')
        self.assertEqual(to_english('.....OO..OOO'), 'Z')

        # numbers
        self.assertEqual(to_english('.O.OOOO.....'), '1')
        self.assertEqual(to_english('.O.OOOO.....OO....OO.O..'), '134')

        # sentences
        self.assertEqual(to_english('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'), 'Abc 123')
        self.assertEqual(to_english('.O.OOOO.....O.O...OO...............OO..........OO.O........OOO...........O.OOOOO.O..O..O..OOO.........OO.O..O..O..OOO...'), '123 ABC 456 def')

if __name__ == '__main__':
    unittest.main()
