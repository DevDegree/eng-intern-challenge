import sys

# Define Braille alphabet mappings for letters and numbers separately
ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "cap": ".....O", "num": ".O.OOO", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Separate Braille-to-English mappings for letters and numbers
BRAILLE_TO_LETTERS = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k.isalpha()}
BRAILLE_TO_NUMBERS = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k.isdigit()}

def is_braille(input_text):
    # A very basic heuristic: If the input contains only 'O', '.', and whitespace, it is likely Braille
    valid_braille_chars = {'O', '.', ' '}
    return all(char in valid_braille_chars for char in input_text)

def translate_to_braille(text):
    result = []
    num_mode = False

    for char in text:
        if char.isdigit():
            if not num_mode:
                result.append(ENGLISH_TO_BRAILLE["num"])
                num_mode = True
            result.append(ENGLISH_TO_BRAILLE[char])
        else:
            if num_mode:
                num_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE["cap"])
                char = char.lower()
            result.append(ENGLISH_TO_BRAILLE.get(char, "......"))

    return ''.join(result)

def translate_to_english(braille):
    symbols = [braille[i:i+6] for i in range(0, len(braille), 6)]
    result = []
    cap_mode = False
    num_mode = False

    for symbol in symbols:
        if symbol == ENGLISH_TO_BRAILLE["cap"]:
            cap_mode = True
            continue
        elif symbol == ENGLISH_TO_BRAILLE["num"]:
            num_mode = True
            continue

        # Handle space reset for modes
        if symbol == "......":
            result.append(' ')
            cap_mode = False
            num_mode = False
            continue

        # Check for symbol to char mapping
        if num_mode:
            # Expect numbers only in num mode
            char = BRAILLE_TO_NUMBERS.get(symbol, "?")
            result.append(char)
        else:
            # Expect letters when not in num mode
            char = BRAILLE_TO_LETTERS.get(symbol, "?")
            if cap_mode:
                if char.isalpha():
                    result.append(char.upper())
                else:
                    result.append(char)  # Treat any non-letter as normal
                cap_mode = False
            else:
                result.append(char)

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return

    text = ' '.join(sys.argv[1:])

    # Determine if input is Braille or English
    if is_braille(text):
        print(translate_to_english(text))
    else:
        print(translate_to_braille(text))

if __name__ == "__main__":
    main()
