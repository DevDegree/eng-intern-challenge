import sys

# Braille to character mappings
braille_to_char = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " "
}

braille_to_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

braille_to_mode = {
    ".....O": "capital_follows", ".O.OOO": "number_follows"
}

# Reverse mappings: Characters and numbers to Braille
char_to_braille = {char: braille for braille, char in braille_to_char.items()}
num_to_braille = {num: braille for braille, num in braille_to_num.items()}
mode_to_braille = {mode: braille for braille, mode in braille_to_mode.items()}

def translate_to_ascii(braille_input: str) -> str:
    """Translate Braille input to ASCII text considering modes for capitalization and numbers."""
    result = ""
    is_num_mode, is_capital_mode = False, False
    i = 0

    while i < len(braille_input):
        segment = braille_input[i:i+6]
        i += 6

        if segment in braille_to_mode:
            mode = braille_to_mode[segment]
            is_capital_mode = (mode == "capital_follows")
            is_num_mode = (mode == "number_follows")
        elif is_num_mode and segment in braille_to_num:
            result += braille_to_num[segment]
        elif is_capital_mode and segment in braille_to_char:
            result += braille_to_char[segment].upper()
            is_capital_mode = False  # Reset after use
        elif segment in braille_to_char:
            result += braille_to_char[segment]

    return result

def translate_to_braille(text_input: str) -> str:
    """Convert ASCII text to Braille output with modes for capital letters and numbers."""
    result = ""
    is_num_mode = False

    for char in text_input:
        if char.isdigit():
            if not is_num_mode:
                result += mode_to_braille["number_follows"]
                is_num_mode = True
            result += num_to_braille[char]
        elif char.isupper():
            result += mode_to_braille["capital_follows"] + char_to_braille[char.lower()]
        elif char == ' ':
            is_num_mode = False  # Reset num mode on space
            result += char_to_braille[char]
        else:
            result += char_to_braille[char]

    return result

def is_braille(input_string: str) -> bool:
    """Check if the input string is a valid Braille sequence."""
    return all(ch in "O." for ch in input_string) and len(input_string) % 6 == 0

if __name__ == '__main__':
    input_string = " ".join(sys.argv[1:])
    # input_string = "Abc 123 xYz"
    print(translate_to_ascii(input_string) if is_braille(input_string) else translate_to_braille(input_string))
