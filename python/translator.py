import sys

braille_dict_symbols = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}
braille_dict_letters = {
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
    " ": "......",
}

english_dict_letters = {v: k for k, v in braille_dict_letters.items()}
english_dict_symbols = {v: k for k, v in braille_dict_symbols.items()}

braille_capital = ".....O"
braille_number = ".O.OOO"
braille_space = "......"


### English -> Braille
def e2b(eng_text):
    result = []
    in_number_seq = False

    for c in eng_text:

        ### Digit
        if c.isdigit():
            if not in_number_seq:
                result.append(braille_number)
                in_number_seq = True
            result.append(braille_dict_symbols[c])
            continue

        ### Letter
        if in_number_seq:
            in_number_seq = False

        if c.isupper():
            result.append(braille_capital)
            c = c.lower()

        result.append(braille_dict_letters.get(c, ""))  # Lookup in letters dictionary

    return "".join(result)


### Braille -> English
def b2e(braille_text):

    result = []
    b_length = len(braille_text)

    is_capital = False
    in_number_seq = False

    for i in range(0, b_length, 6):
        b = braille_text[i : i + 6]

        if b == braille_capital:
            is_capital = True
            continue

        elif b == braille_number:
            in_number_seq = True
            continue

        elif b == braille_space:
            result.append(" ")
            in_number_seq = False
            continue

        if in_number_seq:
            c = english_dict_symbols.get(b, "")
        else:
            c = english_dict_letters.get(b, "")

        if is_capital:
            c = c.upper()
            is_capital = False

        result.append(c)

    return "".join(result)


if __name__ == "__main__":
    ### Append all arguments (words) with a space
    input_text = " ".join(sys.argv[1:])

    if all(c in "O." for c in input_text):
        output_text = b2e(input_text)
    else:
        output_text = e2b(input_text)

    print(output_text)
