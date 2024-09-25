import sys

BRAILLE_LENGTH = 6
char_to_braille = {
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
    "capital_follows": ".....O",
    "decimal_follows": ".O...O",
    "number_follows": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".O.O.O",
    ">": "O.O.O.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

# Create reverse mapping
braille_to_chars = {}
for char, braille in char_to_braille.items():
    if braille not in braille_to_chars:
        braille_to_chars[braille] = []
    braille_to_chars[braille].append(char)

def english_to_braille(text):
    output = []
    number_mode = False
    for char in text:
        if char.isupper():
            # Add capital follows symbol
            output.append(char_to_braille['capital_follows'])
            char = char.lower()
            if char in char_to_braille:
                output.append(char_to_braille[char])
            else:
                # Handle characters not in the mapping
                output.append('?')
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                output.append(char_to_braille['number_follows'])
                number_mode = True
            if char in char_to_braille:
                output.append(char_to_braille[char])
            else:
                output.append('?')
        elif char == ' ':
            output.append(char_to_braille[' '])
            number_mode = False
        else:
            if char in char_to_braille:
                output.append(char_to_braille[char])
            else:
                output.append('?')
            number_mode = False
    return ''.join(output)

def braille_to_english(braille_text):
    output = []
    number_mode = False
    capitalize_next = False
    # Split the braille text into symbols of length 6
    symbols = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    for symbol in symbols:
        if symbol == char_to_braille['number_follows']:
            number_mode = True
            continue
        elif symbol == char_to_braille['capital_follows']:
            capitalize_next = True
            continue
        elif symbol == char_to_braille[' ']:
            output.append(' ')
            number_mode = False
            continue
        else:
            chars = braille_to_chars.get(symbol, [])
            if number_mode:
                # Look for a digit
                digit = next((c for c in chars if c.isdigit()), None)
                if digit:
                    output.append(digit)
                    continue
            # Not in number mode or no digit found
            char = next((c for c in chars if not c.isdigit() and c not in ['capital_follows', 'number_follows']), None)
            if char:
                if capitalize_next:
                    output.append(char.upper())
                    capitalize_next = False
                else:
                    output.append(char)
            else:
                output.append('?')
    return ''.join(output)

# process command line arguments
def get_input():
    text = sys.argv[1:]
    input_string = " ".join(text)
    return input_string

def detect_language(input_text):
    if all(char in {'O', '.'} for char in input_text) and len(input_text) % BRAILLE_LENGTH == 0:
        return "braille"
    return "english"

def main():
    text = get_input()
    language = detect_language(text)
    if language == "english":
        braille_text = english_to_braille(text)
        print(braille_text.strip())
    else:
        english_text = braille_to_english(text)
        print(english_text.strip())

if __name__ == "__main__":
    main()
