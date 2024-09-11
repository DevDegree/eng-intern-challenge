import sys

english_to_braille = {
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
    "cap": ".....O",  # Capital sign
    "num": ".O.OOO",  # Number follows
    "dec": ".0...0",  # Decimal follows
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

# Reverse mapping for Braille to English translation.
braille_to_english = {
    val: key for key, val in english_to_braille.items() if key.isalpha() or key == " "
}
braille_to_nums = {val: key for key, val in english_to_braille.items() if key.isdigit()}



def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return
    args = sys.argv[1:]
    input_text = " ".join(args)


if __name__ == "__main__":
    main()
