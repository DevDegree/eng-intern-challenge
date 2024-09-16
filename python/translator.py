import sys

special_chars = {
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO."
}

translation_dict = {
    "capital_follows": ".....O", "decimal_follows": ".O...O", "number_follows": ".O.OOO",
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

number_dict = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse mappings for braille to text conversion
braille_dict = {v: k for k, v in translation_dict.items()}
braille_number_dict = {v: k for k, v in number_dict.items()}

def input_is_braille(input_data):
    return all(ch in {'.', 'O'} for ch in input_data)

def slice_braille_string(braille_data):
    return [braille_data[i:i + 6] for i in range(0, len(braille_data), 6)]

def braille_to_text(braille_input):
    assert len(braille_input) % 6 == 0
    segments = slice_braille_string(braille_input)
    capital_next = False
    number_next = False

    for segment in segments:
        char_value = braille_dict[segment]

        if char_value == 'capital_follows':
            capital_next = True
        elif char_value == 'number_follows':
            number_next = True
        elif char_value == ' ':
            number_next = False
            print(char_value, end='')
        else:
            if number_next:
                print(braille_number_dict[segment], end='')
            elif capital_next:
                print(char_value.upper(), end='')
                capital_next = False
            else:
                print(char_value, end='')

def text_to_braille(text_input):
    parse_number = False

    for char in text_input:
        if char.isalpha():
            if char.isupper():
                print(translation_dict['capital_follows'], end='')
                print(translation_dict[char.lower()], end='')
            else:
                print(translation_dict[char], end='')
        elif char.isdigit():
            if not parse_number:
                print(translation_dict['number_follows'], end='')
                parse_number = True
            print(number_dict[char], end='')
        elif char == ' ':
            parse_number = False
            print(translation_dict[' '], end='')

def main():
    user_input = ' '.join(sys.argv[1:])

    if input_is_braille(user_input):
        braille_to_text(user_input)
    else:
        text_to_braille(user_input)

if __name__ == '__main__':
    main()