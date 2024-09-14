import sys

# mapping from braille to english (only letters because like 'a' and 1 have same braille so in the dict it will overwrite keys and values)
braille_to_eng_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",

    ".....O": "capital follows",  # Capital follows symbol
    ".O.OOO": "number follows",   # Number follows symbol
    "......": " "                 # Space
}

# braille mapping for numbers (only valid after "number follows" symbol)
braille_numbers_map = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

numbers_braille_map = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

eng_to_braille_map = {v: k for k, v in braille_to_eng_map.items() if v not in ['captial follows', 'number follows']}

# detecting input type
def is_braille(input_str):
    braille_unique_chars = {"O", "."}
    return set(input_str).issubset(braille_unique_chars)

# braille to english
def braille_to_eng(input_str):
    result_str = []
    i = 0
    is_number = False
    while i < len(input_str):
        char_braille = input_str[i:i+6] # reading the input 6 characters at a time

        # checking for capital or number follows
        if char_braille == ".....O": # capital follows
            result_str.append(braille_to_eng_map[input_str[i+6:i+12]].upper())
            i += 12 # going 12 chars (captial follows + captial char) ahead
        elif char_braille == ".O.OOO": # number follows
            is_number = True
            i += 6
        else:
            if is_number:
                # translate as a number
                result_str.append(braille_numbers_map[char_braille])
            else:
                result_str.append(braille_to_eng_map[char_braille])
            i += 6
    return ''.join(result_str)


# english to braille
def eng_to_braille(input_str):
    result_str = []
    in_num_mode = False # to check for contiguous num chars so that we don't put "number follows" after every num char
    # example: 42 shouldn't become "num follows" + 4 + "num follows" + 2. it should be "num follows" + 4 + 2

    for char in input_str:
        if char.isdigit():
            if not in_num_mode:
                result_str.append(".O.OOO") # number follows
                in_num_mode = True # Now we enter number mode
            result_str.append(numbers_braille_map[char]) # converting the num to braille
        else:
            if in_num_mode:
                in_num_mode = False  # we exit number mode when we next char is a non-digit
            if char.isupper():
                result_str.append(".....O")  # Capital follows
                result_str.append(eng_to_braille_map[char.lower()])  # Lowercase conversion
            else:
                result_str.append(eng_to_braille_map[char])
    return ''.join(result_str)


def main():
    cmd_line_args = sys.argv[1:]

    input_str = ' '.join(cmd_line_args)

    if is_braille(input_str):
        result = braille_to_eng(input_str) # input is braille so translate to english
    else:
        result = eng_to_braille(input_str) # input is english so translate to braille
    
    print(result)

if __name__ == "__main__":
    main()