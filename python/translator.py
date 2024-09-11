# There was several assumptions made in my implementation:
# 1. I have assumed that the code is expected to be worked on by multiple developers in the future. Therefore, the focus of the code was not just on solving the problem, but also on ensuring clarity, extendability, and seperation of concerns.
# 2. The program expects to also receive invalid inputs thus the program should be able to handle invalid inputs and provide a meaningful error message.
# 3. Any other rules not in the specification should be considered invalid (ex: only space, number and alphabet is allowed, only a letter is allowed to be followed after a capital code unless there is a space).
# 4. Any of the ambigiouty should be considered invalid (ex: in english only a number is allowed to be followed after a number until there is a space).
# 5. As specified in the requirements, Braille Alphabet are only limited to the 26 letters of the English alphabet, the numbers 0-9 and a space.

import sys

# Constants
VALID_ENGLISH_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
VALID_BRAILLE_CHARS = set(".O")
LETTER_BRAILLE_MAP = {
  'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
  'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
  'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
  'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
  'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
  'O..OOO': 'z'
}
NUMBER_BRAILLE_MAP = {
  'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
  'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}
CAPITAL_BRAILLE_CODE = '.....O'
NUMBER_BRAILLE_CODE = '.O.OOO'
SPACE_BRAILLE_CODE = '......'
REVERSE_BRAILLE_MAP = {**{v: k for k, v in LETTER_BRAILLE_MAP.items()}, **{v: k for k, v in NUMBER_BRAILLE_MAP.items()}}
REVERSE_BRAILLE_MAP[' '] = SPACE_BRAILLE_CODE


def braille_to_english(braille: str) -> str:
    """
    Translates a Braille code string into English.

    Parameters:
    braille (str): A string of Braille characters where each character is represented as a 6-dot code.

    Returns:
    str: The translated English string.
    """
    translated_text = []
    i = 0
    while i < len(braille):
        current_code = braille[i:i + 6]
        if current_code == CAPITAL_BRAILLE_CODE:
            i += 6
            next_code = braille[i:i + 6]
            translated_text.append(LETTER_BRAILLE_MAP[next_code].upper())
        elif current_code == NUMBER_BRAILLE_CODE:
            i += 6
            while i < len(braille):
                number_code = braille[i:i + 6]
                if number_code == SPACE_BRAILLE_CODE:
                    translated_text.append(" ")
                    break
                i += 6
                translated_text.append(NUMBER_BRAILLE_MAP[number_code])
        elif current_code == SPACE_BRAILLE_CODE:
            translated_text.append(" ")
        else:
            translated_text.append(LETTER_BRAILLE_MAP[current_code])
        i += 6
    return ''.join(translated_text)


def english_to_braille(english: str) -> str:
    """
    Translates an English string into Braille code.

    Parameters:
    english (str): A string of English characters (letters, digits, and spaces).

    Returns:
    str: The translated Braille string.
    """
    translated_text = []
    is_number_mode = False

    for char in english:
        if char.isdigit():
            if not is_number_mode:
                is_number_mode = True
                translated_text.append(NUMBER_BRAILLE_CODE)
        elif char == ' ':
            is_number_mode = False
        elif char.isalpha() and char.isupper():
            translated_text.append(CAPITAL_BRAILLE_CODE)
        translated_text.append(REVERSE_BRAILLE_MAP[char.lower()])
    
    return ''.join(translated_text)


def validate_braille(braille: str) -> list[str]:
    """
    Validates a Braille string to ensure it follows correct encoding.
      The rules are:
      - The length of the code should be a multiple of 6.
      - The code should only contain Braille characters mentioned in the specification.
      - Only letter code should be right after the capital follow code.
      - A number code should be followed by a number code until a space code.

    Parameters:
    braille (str): A string of Braille characters.

    Returns:
    list[str]: A list of error messages if the Braille string is invalid, otherwise an empty list.
    """
    if len(braille) % 6 != 0:
      return ["The length of the code is not a multiple of 6."]
    if not set(braille).issubset(VALID_BRAILLE_CHARS):
      return ["Invalid characters found in the code."]
    issues = []
    i = 0
    while i < len(braille):
        current_code = braille[i:i + 6]
        if current_code == CAPITAL_BRAILLE_CODE:
            i += 6
            next_code = braille[i:i + 6]
            if next_code not in LETTER_BRAILLE_MAP:
                issues.append("Expected a letter Braille code after the capital Braille code.")
        elif current_code == NUMBER_BRAILLE_CODE:
            i += 6
            while i < len(braille):
                number_code = braille[i:i + 6]
                i += 6
                if number_code == SPACE_BRAILLE_CODE:
                    break
                if number_code not in NUMBER_BRAILLE_MAP:
                    issues.append("Expected a number Braille code after the number Braille code until a space code.")
        elif current_code in LETTER_BRAILLE_MAP or current_code == SPACE_BRAILLE_CODE:
            pass
        else:
            issues.append(f"Invalid Braille code: {current_code}.")
        i += 6
    return issues


def validate_english(english: str) -> list[str]:
    """
    Validates an English string to ensure it contains only valid characters.
      The rules are:
      - Only letters, digits, and spaces are allowed.
      - Only a number is allowed to be followed after a number until a space.
    Parameters:
    english (str): A string of English characters (letters, digits, and spaces).

    Returns:
    list[str]: A list of error messages if the English string is invalid, otherwise an empty list.
    """
    if not set(english.lower()).issubset(VALID_ENGLISH_CHARS):
        return ["Invalid characters found in the code."]
    issues = []
    is_number_mode = False
    for char in english:
        if char == ' ':
            is_number_mode = False
        elif char.isdigit():
            is_number_mode = True
        elif is_number_mode:
            issues.append("Expected only numbers after a digit until the next space.")
    return issues


def detect_code_type(code: str) -> str:
    """
    Detects whether the input string is Braille or English based on validation results.

    Parameters:
    code (str): The input code, which can either be Braille or English.

    Returns:
    str: "braille" if the code is valid Braille, "english" if the code is valid English.

    Raises:
    ValueError: If the code is neither valid Braille nor valid English.
    """
    braille_issues = validate_braille(code)
    if not braille_issues:
        return "braille"

    english_issues = validate_english(code)
    if not english_issues:
        return "english"
    
    # If neither is valid, raise an error with detailed messages
    error_message = "The code is neither valid Braille nor English:\n"
    if braille_issues:
        error_message += "Braille issues:\n  " + "\n  ".join(braille_issues) + "\n"
    if english_issues:
        error_message += "English issues:\n  " + "\n  ".join(english_issues)
    
    raise ValueError(error_message)


def translate(code: str) -> str:
    """
    Translates the input code from Braille to English or from English to Braille.

    Parameters:
    code (str): The input code, either Braille or English.

    Returns:
    str: The translated code in the opposite format (Braille to English or English to Braille).

    Raises:
    ValueError: If the input code is neither valid Braille nor valid English.
    """
    code_type = detect_code_type(code)
    if code_type == "braille":
        return braille_to_english(code)
    elif code_type == "english":
        return english_to_braille(code)


def get_input_from_args() -> str:
    """
    Retrieves the input code from command-line arguments.

    Returns:
    str: The code input provided as command-line arguments.

    Raises:
    ValueError: If no input code is provided.
    """
    if len(sys.argv) < 2:
        raise ValueError("Please provide the code to translate.")
    return " ".join(sys.argv[1:])

if __name__ == "__main__":
    input_code = get_input_from_args()
    print("result")
