import unittest

from translator import BrailleToEnglishTranslation, EnglishToBrailleTranslation

class TestBrailleToEnglishTranslation(unittest.TestCase):
    def setUp(self) -> None:
        self.translator = BrailleToEnglishTranslation()
        
    def test_default(self):
        input = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        assert self.translator.translate(input) == "Abc 123 xYz"
    
    def test_number(self):
        input = ".O.OOOOO.O..O.O..."
        assert self.translator.translate(input) == "42"
    
    def test_decimal(self):
        input = ".O.OOOOO.O...O...O..OO.OO..O.."
        assert self.translator.translate(input) == "4.5"
    
    def test_lower_string(self):
        input = "O.OO..O..O..O.O.O.O.O.O.O..OO."
        assert self.translator.translate(input) == "hello"
    
    def test_capital_string(self):
        input = ".....OO..OOO.....OO....."
        assert self.translator.translate(input) == "ZA"


class TestEnglishToBrailleTranslation(unittest.TestCase):
    def setUp(self) -> None:
        self.translator = EnglishToBrailleTranslation()
    
    def test_default(self):
        input = "Abc 123 xYz"
        assert self.translator.translate(input) == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
    
    def test_number(self):
        input = "42"
        assert self.translator.translate(input) == ".O.OOOOO.O..O.O..."
    
    def test_decimal(self):
        input = "4.5"
        assert self.translator.translate(input) == ".O.OOOOO.O...O...O..OO.OO..O.."
    
    def test_lower_string(self):
        input = "hello"
        assert self.translator.translate(input) == "O.OO..O..O..O.O.O.O.O.O.O..OO."
    
    def test_capital_string(self):
        input = "ZA"
        assert self.translator.translate(input) == ".....OO..OOO.....OO....."
    

if __name__ == "__main__":
    unittest.main()