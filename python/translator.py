import sys

base_mapping = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO..", " ": "......", ".": "..OO.O", ",": "..O...", "?": "..O.OO",
    "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", "(": "O.O..O", ")": ".O.OO.", "Capital follows": ".....O",
    "Number follows": ".O.OOO"
}

english_to_braille = base_mapping
braille_to_english = {v: k for k, v in base_mapping.items()}


def translate_to_braille(english):
    output = []
    number_state = False

    for char in english:
        if char.isupper():
            output.append(english_to_braille["Capital follows"])
            output.append(english_to_braille[char.lower()])
            number_state = False
        elif char.isdigit():
            if not number_state:
                output.append(english_to_braille["Number follows"])
                number_state = True
            output.append(english_to_braille[char])
        elif char == ' ':
            output.append(english_to_braille[char])
            number_state = False
        else:
            output.append(english_to_braille[char])

        print(char)

    return ''.join(output)


def main():
    input_string = sys.argv[1]

    if all(char in 'O.' for char in input_string):
        print("oops")
    else:
        print(translate_to_braille(input_string))


if __name__ == "__main__":
    main()
