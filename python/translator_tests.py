"""
Braille Translator Tests

"""


# imports
from translator import Translator




# Unit Tests
def test_unit(t: Translator) -> None:
    assert t.is_braille("ewfnoiweaskoijxcv") == False
    assert t.is_braille("O.O.O.") == True
    assert t.english_to_braille("abc") == "O.....O.O...OO...."
    assert t.braille_to_english("O.....O.O...OO....") == "abc"




# Integration Tests
def test_integration(t: Translator) -> None:
    # translator must be invertible
    invertible = "hello"
    invertible = t.braille_to_english(t.english_to_braille(invertible))
    assert invertible == "hello"

    # all numbers
    numbers = "1234567890"
    numbers = t.braille_to_english(t.english_to_braille(numbers))
    assert numbers == "1234567890"

    # provided tests ----------------------------------------------
    hello = "Hello world"
    hello = t.english_to_braille(hello)
    assert hello == ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
    
    forty_two = "42"
    forty_two = t.english_to_braille(forty_two)
    assert forty_two == ".O.OOOOO.O..O.O..."
    
    braille = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
    braille = t.braille_to_english(braille)
    assert braille == "Abc 123"




# Acceptance Tests
def test_acceptance(t: Translator) -> None:
    # random uppercases
    capital = "hElLo ThErE"
    capital = t.braille_to_english(t.english_to_braille(capital))
    assert capital == "hElLo ThErE"
    
    # arbitrary spacing
    space = "i   love             shopify"
    space = t.braille_to_english(t.english_to_braille(space))
    assert space == "i   love             shopify"
    
    # mixed numbers and letters
    alphanumeric = "lcJJAWOIFJ329 2839"
    alphanumeric = t.braille_to_english(t.english_to_braille(alphanumeric))
    assert alphanumeric == "lcJJAWOIFJ329 2839"

    # all letters of alphabet
    alphabet = "the quick brown fox jumped over the lazy dog"
    alphabet = t.braille_to_english(t.english_to_braille(alphabet))
    assert alphabet == "the quick brown fox jumped over the lazy dog"




def run_tests():
    t = Translator()
    test_unit(t)
    test_integration(t)
    test_acceptance(t)




if __name__ == '__main__':
    run_tests()
