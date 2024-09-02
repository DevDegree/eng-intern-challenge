import argparse

UNKNOWN_PLACEHOLDER = "█"
NUM_DOTS_PER_TOKEN = 6

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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    # ">": "O..OO.", duplicated symbol with "o" - even with context, it's ambiguous
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    "CAPITAL_FOLLOWS": ".....O",
    "NUMBER_FOLLOWS": ".O.OOO",
    "DECIMAL_FOLLOWS": ".O...O"
}

number_to_braille = {
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
    ".": "..OO.O",
    " ": "......",
}

braille_to_char = {v: k for k, v in char_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}

def is_braille(payload):
    for char in payload:
        if char not in ['.', 'O']:
            return False
    return True

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="CMD-line Braille Translator")
    parser.add_argument('args', nargs='*', help='Payload to be parsed by the translator')
    args = parser.parse_args()

    # Process the arguments ---------------------------------------------
    
    payload_is_braille = len(args.args) == 1 and is_braille(''.join(args.args)) # Optimization: terminate early if more than one continuous string is passed
    output = ""

    capital_follows_toggle = False # only the next char
    number_follows_toggle = False # every char until the next space

    if payload_is_braille:
        payload = args.args[0]
        num_tokens = len(payload) // NUM_DOTS_PER_TOKEN

        for i in range(num_tokens):
            start = i * NUM_DOTS_PER_TOKEN
            end = start + NUM_DOTS_PER_TOKEN # exclusive
            token = payload[start:end]
            translated = braille_to_char[token]

            if translated == "CAPITAL_FOLLOWS":
                capital_follows_toggle = True
                continue

            if translated == "NUMBER_FOLLOWS":
                number_follows_toggle = True
                continue

            if translated == " ":
                output += " "
                number_follows_toggle = False
                continue

            if capital_follows_toggle:
                output += translated.upper()
                capital_follows_toggle = False
                continue

            if number_follows_toggle:
                output += braille_to_number[token]
                continue

            output += translated
    else:
        payload = ' '.join(args.args)
        for char in payload:
            if char == ' ':
                number_follows_toggle = False
                output += char_to_braille[char]

            elif char.isdigit():
                if number_follows_toggle:
                    output += number_to_braille[char]
                else:
                    number_follows_toggle = True
                    output += char_to_braille["NUMBER_FOLLOWS"]
                    output += number_to_braille[char]

            elif char.isupper():
                output += char_to_braille["CAPITAL_FOLLOWS"]
                output += char_to_braille[char.lower()]
            
            else:
                output += char_to_braille[char]

    print(output)

if __name__ == "__main__":
    main()
