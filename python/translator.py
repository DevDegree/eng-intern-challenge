import sys
from typing import List, Dict

ENGLISH_TO_BRAILLE_NON_NUMERIC: Dict[str, str] = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", " ": "......", "capital_indicator": ".....O", "number_indicator": ".O.OOO"
}

ENGLISH_TO_BRAILLE_NUMERIC: Dict[str, str] = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

BRAILLE_TO_ENGLISH_CHAR: Dict[str, str] = {value: key for key, value in ENGLISH_TO_BRAILLE_NON_NUMERIC.items()}
BRAILLE_TO_ENGLISH_NUM: Dict[str, str] = {value: key for key, value in ENGLISH_TO_BRAILLE_NUMERIC.items()}

def is_braille_code(input_string: str) -> bool:
    return set(input_string).issubset({"O", "."}) and len(input_string) % 6 == 0

def translate_braille_to_english(braille_input: str) -> str:
    def process_braille_char(char: str, flag: str) -> tuple[str, str]:
        if char in ("capital_indicator", "number_indicator"):
            return "", char
        if flag == "capital_indicator":
            return BRAILLE_TO_ENGLISH_CHAR[char].upper(), ""
        if flag == "number_indicator" and char != "......":
            return BRAILLE_TO_ENGLISH_NUM.get(char, ""), "number_indicator"
        return BRAILLE_TO_ENGLISH_CHAR[char], ""

    result: List[str] = []
    flag = ""
    for i in range(0, len(braille_input), 6):
        char, new_flag = process_braille_char(braille_input[i:i+6], flag)
        result.append(char)
        flag = new_flag or flag

    return "".join(result)

def translate_english_to_braille(english_input: str) -> str:
    def char_to_braille(char: str, in_numeric_mode: bool) -> tuple[str, bool]:
        if char.isdigit():
            return ENGLISH_TO_BRAILLE_NUMERIC[char], True
        if char.isupper():
            return ENGLISH_TO_BRAILLE_NON_NUMERIC["capital_indicator"] + ENGLISH_TO_BRAILLE_NON_NUMERIC[char.lower()], False
        return ENGLISH_TO_BRAILLE_NON_NUMERIC[char.lower()], False

    result: List[str] = []
    numeric_mode = False
    for char in english_input:
        if char.isdigit() and not numeric_mode:
            result.append(ENGLISH_TO_BRAILLE_NON_NUMERIC["number_indicator"])
            numeric_mode = True
        braille, numeric_mode = char_to_braille(char, numeric_mode)
        result.append(braille)

    return "".join(result)

def main() -> None:
    user_input = " ".join(sys.argv[1:])
    result = translate_braille_to_english(user_input) if is_braille_code(user_input) else translate_english_to_braille(user_input)
    print(result)

if __name__ == "__main__":
    main()