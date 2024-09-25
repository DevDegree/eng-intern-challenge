import sys
from typing import Dict, List, Tuple, Callable
from functools import reduce

BRAILLE_CHAR_LEN = 6
CAPITAL_FOLLOWS, NUMBER_FOLLOWS = "<CAPITAL>", "<NUMBER>"

ENGLISH_TO_BRAILLE: Dict[str, str] = {
    **dict(zip('abcdefghijklmnopqrstuvwxyz', [
        "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..",
        "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.",
        "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO",
        "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"
    ])),
    CAPITAL_FOLLOWS: ".....O",
    NUMBER_FOLLOWS: ".O.OOO",
    " ": "......"
}

ENGLISH_DIGITS_TO_BRAILLE: Dict[str, str] = {
    **dict(zip(map(str, range(10)), [
        ".OOO..", "O.....", "O.O...", "OO....", "OO.O..",
        "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."
    ])),
    " ": "......"
}

BRAILLE_TO_ENGLISH: Dict[str, str] = {b: e for e, b in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_ENGLISH_DIGITS: Dict[str, str] = {b: e for e, b in ENGLISH_DIGITS_TO_BRAILLE.items()}

is_braille: Callable[[str], bool] = lambda text: set(text).issubset("O.")

def chunk(text: str, n: int) -> List[str]:
    """Split text into chunks of size n."""
    return [text[i:i+n] for i in range(0, len(text), n)]

def braille_to_english(text: str) -> str:
    """Convert Braille text to English."""
    if len(text) % BRAILLE_CHAR_LEN:
        raise ValueError(f"Invalid Braille input: length must be a multiple of {BRAILLE_CHAR_LEN}.")

    def process_chunk(acc: Tuple[str, bool, bool], char: str) -> Tuple[str, bool, bool]:
        result, cap_next, num_mode = acc
        if char == CAPITAL_FOLLOWS:
            return result, True, num_mode
        elif char == NUMBER_FOLLOWS:
            return result, cap_next, True
        elif num_mode and char in BRAILLE_TO_ENGLISH_DIGITS:
            return result + BRAILLE_TO_ENGLISH_DIGITS[char], False, True
        else:
            letter = BRAILLE_TO_ENGLISH[char]
            return result + (letter.upper() if cap_next else letter), False, False

    return reduce(process_chunk, chunk(text, BRAILLE_CHAR_LEN), ('', False, False))[0]

def english_to_braille(text: str) -> str:
    """Convert English text to Braille."""
    def char_to_braille(char: str) -> str:
        if char.isupper():
            return ENGLISH_TO_BRAILLE[CAPITAL_FOLLOWS] + ENGLISH_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            return ENGLISH_TO_BRAILLE[NUMBER_FOLLOWS] + ENGLISH_DIGITS_TO_BRAILLE[char]
        elif char in ENGLISH_TO_BRAILLE:
            return ENGLISH_TO_BRAILLE[char]
        else:
            raise ValueError(f"Invalid character: '{char}'. Only letters, numbers, and spaces are supported.")

    def process_text(acc: Tuple[str, bool], char: str) -> Tuple[str, bool]:
        result, in_number = acc
        if char.isdigit() and not in_number:
            return result + ENGLISH_TO_BRAILLE[NUMBER_FOLLOWS] + ENGLISH_DIGITS_TO_BRAILLE[char], True
        elif char.isdigit():
            return result + ENGLISH_DIGITS_TO_BRAILLE[char], True
        else:
            return result + char_to_braille(char), False

    return reduce(process_text, text, ('', False))[0]

def main() -> None:
    """Main function to handle command-line input and execute translation."""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>", file=sys.stderr)
        sys.exit(1)

    text = " ".join(sys.argv[1:]).strip()
    try:
        result = braille_to_english(text) if is_braille(text) else english_to_braille(text)
        print(result, end='')
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
