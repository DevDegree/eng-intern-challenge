import sys

# Braille translation dictionaries
ENGLISH_TO_BRAILLE_CODES = {
  'a': "O.....", 'b': "O.O...", 'c': "OO....",
  'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
  'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...",
  'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
  'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
  'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
  's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO",
  'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
  'y': "OO.OOO", 'z': "O..OOO", ' ': "......",
}
ENGLISH_TO_BRAILLE_NUMERALS = {
  '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", 
  '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
  '9': ".OO...", '0': ".OOO.."
}
CAP_BRAILLE = ".....O"
NUMBER_BRAILLE = ".O.OOO"


def swap_keys_and_values(dictionary: dict) -> dict:
    return {value: key for key, value in dictionary.items()}


def check_is_braille(value: str) -> bool:
    # Check if input only contains Braille characters (O or . or space)
    return all(c in 'O. ' for c in value)


def translate_braille_to_eng(value: str) -> str:
    BRAILLE_TO_ENG_CHARS = swap_keys_and_values(ENGLISH_TO_BRAILLE_CODES)
    BRAILLE_TO_ENG_NUMS = swap_keys_and_values(ENGLISH_TO_BRAILLE_NUMERALS)
    NUM_CHARS_IN_SYMBOL = 6

    curr_symbol = ""
    translated_str = ""
    is_next_capital = False
    is_next_number = False

    if len(value) % NUM_CHARS_IN_SYMBOL != 0:
        raise ValueError("Invalid Braille length.")

    for i in range(len(value)):
        curr_symbol += value[i]

        if len(curr_symbol) == NUM_CHARS_IN_SYMBOL:
            if curr_symbol == CAP_BRAILLE:
                is_next_capital = True
            elif curr_symbol == NUMBER_BRAILLE:
                is_next_number = True
            elif is_next_capital and curr_symbol in BRAILLE_TO_ENG_CHARS:
                translated_str += BRAILLE_TO_ENG_CHARS[curr_symbol].upper()
                is_next_capital = False
            elif is_next_number and curr_symbol in BRAILLE_TO_ENG_NUMS:
                translated_str += BRAILLE_TO_ENG_NUMS[curr_symbol]
            elif (curr_symbol in BRAILLE_TO_ENG_CHARS and not is_next_number) or (is_next_number and curr_symbol == ENGLISH_TO_BRAILLE_CODES[' ']):
                translated_str += BRAILLE_TO_ENG_CHARS[curr_symbol]
                is_next_number = False
            else:
                raise ValueError("Invalid Braille symbol.")

            curr_symbol = ""

    return translated_str


def translate_eng_to_braille(value: str) -> str:
    translated_str = ""
    number_mode = False

    for i in range(len(value)):
        char = value[i]

        if char in ENGLISH_TO_BRAILLE_CODES:
            translated_str += ENGLISH_TO_BRAILLE_CODES[char]
            number_mode = False
        elif char.isupper():
            translated_str += CAP_BRAILLE + ENGLISH_TO_BRAILLE_CODES[char.lower()]
            number_mode = False
        elif char in ENGLISH_TO_BRAILLE_NUMERALS:
            if not number_mode:
                translated_str += NUMBER_BRAILLE
                number_mode = True
            translated_str += ENGLISH_TO_BRAILLE_NUMERALS[char]
        else:
            raise ValueError(f"Invalid character: {char}")

    return translated_str


def main():
    if len(sys.argv) < 2:
        sys.exit("Need to provide at least one argument.")

    input_value = ' '.join(sys.argv[1:])

    try:
        if check_is_braille(input_value):
            print(translate_braille_to_eng(input_value))
        else:
            print(translate_eng_to_braille(input_value))
    except ValueError as e:
        sys.exit(f"Input is invalid! {e}")
    except Exception as e:
        sys.exit(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
