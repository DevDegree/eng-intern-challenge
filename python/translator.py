import sys
from constants.translator import BRAILLE_MAPPING, NUMBER_MAPPING

# Invert the BRAILLE_MAPPING and NUMBER_MAPPING dictionaries for reverse lookup
ENGLISH_TO_BRAILLE_MAPPING = {v: k for k, v in BRAILLE_MAPPING.items()}
NUMBER_TO_BRAILLE_MAPPING = {v: k for k, v in NUMBER_MAPPING.items()}


def is_braille(phrase: str) -> bool:
    """
    Check if the input string is in Braille format.

    Args:
        phrase (str): The input string to check.

    Returns:
        bool: True if the string is in Braille format, False otherwise.
    """
    return all(char in "O." for char in phrase)


def braille_to_english(phrase: str) -> str:
    """
    Convert a Braille string to English text.

    Args:
        phrase (str): The Braille string to convert.

    Returns:
        str: The translated English text.
    """
    index = 0
    caps_lock = False
    number_mode = False
    english_text = ""

    # Process each 6-character Braille segment
    for _ in range(len(phrase) // 6):
        segment = phrase[index : index + 6]
        if segment in BRAILLE_MAPPING:
            if BRAILLE_MAPPING[segment] == "NUM":
                number_mode = True
            elif BRAILLE_MAPPING[segment] == "CAPS":
                caps_lock = True
            elif BRAILLE_MAPPING[segment] == " ":
                number_mode = False
                english_text += " "
            else:
                char = BRAILLE_MAPPING[segment]
                if caps_lock:
                    english_text += char.upper()
                    caps_lock = False
                elif number_mode:
                    english_text += NUMBER_MAPPING[segment]
                else:
                    english_text += char
        index += 6

    return english_text


def english_to_braille(phrase: str) -> str:
    """
    Convert an English string to Braille.

    Args:
        phrase (str): The English string to convert.

    Returns:
        str: The translated Braille string.
    """
    braille_text = ""
    number_mode = False

    # Process each character in the English phrase
    for char in phrase:
        if char.isnumeric() and char in NUMBER_TO_BRAILLE_MAPPING:
            if not number_mode:
                braille_text += ENGLISH_TO_BRAILLE_MAPPING["NUM"]
            braille_text += NUMBER_TO_BRAILLE_MAPPING[char]
            number_mode = True
        elif char.lower() in ENGLISH_TO_BRAILLE_MAPPING:
            if char.isupper():
                braille_text += ENGLISH_TO_BRAILLE_MAPPING["CAPS"]
                char = char.lower()
            braille_text += ENGLISH_TO_BRAILLE_MAPPING[char]
            number_mode = False

    return braille_text


def run_tests():
    """
    Run predefined test cases to verify the correctness of the conversion functions.
    """
    test_cases = [
        (
            "Hello world",
            ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..",
            False,
        ),
        ("42", ".O.OOOOO.O..O.O...", False),
        (".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "Abc 123", True),
    ]

    for i, (input_str, expected_output, is_braille_flag) in enumerate(test_cases, 1):
        if is_braille_flag:
            result = braille_to_english(input_str)
        else:
            result = english_to_braille(input_str)

        print(f"Test Case {i}:")
        print(f"Input: {input_str}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {result}")
        print(f"Test {'Passed' if result == expected_output else 'Failed'}\n")


def main():
    """
    Main function to handle user input or run tests.
    If command-line arguments are provided, it will convert the input.
    Otherwise, it runs the predefined test cases.
    """
    if len(sys.argv) > 1:
        phrase = " ".join(sys.argv[1:])
        if is_braille(phrase):
            print(braille_to_english(phrase))
        else:
            print(english_to_braille(phrase))
    else:
        run_tests()


if __name__ == "__main__":
    main()
