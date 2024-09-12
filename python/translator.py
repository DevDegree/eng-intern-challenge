import sys

# Braille mappings
BRAILLE_TO_ENG = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", "..O...": "i", "..OO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", "..OOOO": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "capital", ".O.OOO": "number"
}

ENG_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENG.items()}

# Number mappings
NUMBER_MAP = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": "..O...", "0": "..OO.."
}

def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        if char == BRAILLE_TO_ENG["capital"]:
            capitalize_next = True
        elif char == BRAILLE_TO_ENG["number"]:
            number_mode = True
        else:
            if char in BRAILLE_TO_ENG:
                if number_mode:
                    result.append(str("0123456789".index(BRAILLE_TO_ENG[char])))
                else:
                    letter = BRAILLE_TO_ENG[char]
                    if capitalize_next:
                        letter = letter.upper()
                        capitalize_next = False
                    result.append(letter)
            if char == "......":
                number_mode = False
        i += 6

    return ''.join(result)

def english_to_braille(english):
    result = []
    in_number_mode = False
    for char in english:
        if char.isupper():
            result.append(ENG_TO_BRAILLE["capital"])
            char = char.lower()
        if char.isdigit():
            if not in_number_mode:
                result.append(ENG_TO_BRAILLE["number"])
                in_number_mode = True
            result.append(NUMBER_MAP[char])
        else:
            if in_number_mode:
                in_number_mode = False
            if char == ' ':
                result.append(ENG_TO_BRAILLE[char])
            else:
                result.append(ENG_TO_BRAILLE.get(char.lower(), ''))
    return ''.join(result)

def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    result = translate(input_text)
    print(result, end='', flush=True)
