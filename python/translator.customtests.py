import unittest
import subprocess
import sys

class TestBrailleTranslator(unittest.TestCase):

    def runTranslator(self, inputText):
        result = subprocess.run([sys.executable, "translator.py", inputText], capture_output=True, text=True)
        return result.stdout.strip()

    def testEnglishToBraille(self):
        self.assertEqual(self.runTranslator("Hello world"), 
                         ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

    def testBrailleToEnglish(self):
        self.assertEqual(self.runTranslator(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."), 
                         "Hello world")

    def testNumbers(self):
        self.assertEqual(self.runTranslator("42"), 
                         ".O.OOOOO.O..O.O...")
        self.assertEqual(self.runTranslator(".O.OOOOO.O..O.O..."), 
                         "42")

    def testFullAlphabet(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        brailleAlphabet = self.runTranslator(alphabet)
        self.assertEqual(self.runTranslator(brailleAlphabet), alphabet)

    def testCapitalization(self):
        self.assertEqual(self.runTranslator("Hello World"), 
                         ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..")

    def testMixedContent(self):
        self.assertEqual(self.runTranslator("Abc 123"), 
                         ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
        self.assertEqual(self.runTranslator(".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."), 
                         "Abc 123")

    def testAllNumbers(self):
        numbers = "0123456789"
        brailleNumbers = self.runTranslator(numbers)
        self.assertEqual(self.runTranslator(brailleNumbers), numbers)

    def testMultipleWords(self):
        sentence = "The quick brown fox jumps over the lazy dog"
        brailleSentence = self.runTranslator(sentence)
        self.assertEqual(self.runTranslator(brailleSentence), sentence)

    def testCapitalFollows(self):
        self.assertEqual(self.runTranslator("AbC"), 
                         ".....OO.....O.O........OOO....")

    def testNumberFollows(self):
        self.assertEqual(self.runTranslator("a12 b34"), 
                         "O......O.OOOO.....O.O.........O.O....O.OOOOO....OO.O..")
    def testMixedCaseAndNumbers(self):
        self.assertEqual(self.runTranslator("Hello123 World456"), 
                         ".....OO.OO..O..O..O.O.O.O.O.O.O..OO..O.OOOO.....O.O...OO...............O.OOO.OO..OO.O.OOO.O.O.O.OO.O...O.OOOOO.O..O..O..OOO...")

    def testEmptyInput(self):
        self.assertEqual(self.runTranslator(""), "")

if __name__ == '__main__':
    unittest.main()