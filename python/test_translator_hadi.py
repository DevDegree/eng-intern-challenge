import pytest
import translator
def test_simple_english_to_braille():
    input_string = "Hello world"
    expected_answer = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
    answer = translator.braille_translator(input_string)
    assert answer == expected_answer

def test_simple_braille_to_english():
    input_string = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
    expected_answer = "Abc 123"
    answer = translator.braille_translator(input_string)
    assert answer == expected_answer

def test_simple_braille_to_english2():
    input_string = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO.........."
    expected_answer = "Abc 123 "
    answer = translator.braille_translator(input_string)
    assert answer == expected_answer

def test_english_to_braille():
    input_string = "Abc 123 xYz"
    expected_output = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'
    answer = translator.braille_translator(input_string)
    assert answer == expected_output