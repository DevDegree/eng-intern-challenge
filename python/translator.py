
# Constants
braille_dict = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "CAP": ".....O",
    "NUM": ".O.OOO",
    " ": "......",
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

reverse_braille_letters = {v: k for k, v in braille_dict.items() if k.isalpha()}
reverse_special_characters = {
    ".O.OOO": "NUM",
    "......": " ",
}
reverse_braille_numbers = {v: k for k, v in braille_dict.items() if k.isdigit()}


def check_is_braille(s):
    """Checks if the given string consists only of the characters 'O' and '.'."""
    return all(c in "O." for c in s) and len(s) % 6 == 0


def is_capital_letter(char):
    """Checks if the given character is an uppercase letter."""
    return "A" <= char <= "Z"


def is_lower_letter(char):
    """Checks if the given character is a lowercase letter."""
    return "a" <= char <= "z"


def is_numeric(char):
    """Checks if the given character is a numeric digit."""
    return "0" <= char <= "9"


def english_to_braille(s):
    """Converts a string of English text into Braille representation."""
    numeric_state = False
    result = ""

    for char in s:
        if is_capital_letter(char):
            new_char = braille_dict["CAP"] + braille_dict[char.lower()]
        elif is_lower_letter(char):
            new_char = braille_dict[char]
        elif is_numeric(char):
            new_char = braille_dict[char]
            if not numeric_state:
                numeric_state = True
                new_char = braille_dict["NUM"] + new_char
        elif char == " ":
            if numeric_state:
                numeric_state = False
            new_char = braille_dict[" "]
        result += new_char or ""
    return result


def braille_to_english(s):
    """Converts a string of Braille representation into English text."""
    result = ""
    numeric_state = False
    skip_next = False

    for i in range(0, len(s), 6):
        if skip_next:
            skip_next = False
            continue
        char = s[i:i + 6]

        if char == braille_dict["NUM"]:
            numeric_state = True
        elif char == braille_dict[" "]:
            if numeric_state:
                numeric_state = False
            result += " "
        elif numeric_state:
            result += reverse_braille_numbers.get(char, "")
        elif char == braille_dict["CAP"]:
            i += 6
            next_char = s[i:i + 6]
            result += reverse_braille_letters.get(next_char, "").upper()
            skip_next = True
        else:
            result += reverse_braille_letters.get(char, "")

    return result


# Main Execution
import sys

input_string = " ".join(sys.argv[1:])

is_braille = check_is_braille(input_string)

result = braille_to_english(input_string) if is_braille else english_to_braille(input_string)

print(result)
