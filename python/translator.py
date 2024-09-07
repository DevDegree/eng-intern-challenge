import sys

# Braille dictionary for letters, capital indicator, and numbers
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",
    "cap": ".....O", "num": ".O.OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse dictionary to decode Braille to English
english_dict = {v: k for k, v in braille_dict.items()}


def text_to_braille(text: str) -> str:
    """
    Translates text to Braille

    Paramaters
    ----------
    text : str
        English text

    Returns
    -------
    str
        Text representation of Braille
    """
    output = []
    number = False
    for char in text:
        if number:
            if char == " ":
                number = False
        else:
            if char.isupper():
                output.append(braille_dict["cap"])
                char = char.lower()
            if char.isdigit():
                output.append(braille_dict["num"])
                number = True
        output.append(braille_dict[char])
    return "".join(output)


def braille_to_text(braille: str) -> str:
    """
    Translates Braille to text

    Parameters
    ----------
    braille : str
        Text representation of Braille
    
    Returns
    -------
    str 
        Text translated from Braille
    """
    output = []
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == ".....O":
            next_symbol = braille[i+6:i+12]
            output.append(english_dict[next_symbol].upper())
            i += 12
        elif symbol == ".O.OOO":
            i += 6
            while i < len(braille) and braille[i:i+6] in english_dict:
                next_symbol = braille[i:i+6]
                output.append(english_dict[next_symbol])
                i += 6
        else:
            output.append(english_dict[symbol])
            i += 6
    return "".join(output)


def main():
    if len(sys.argv) < 2:
        print("Please provide an input string to translate.")
        sys.exit(1)

    input_str = "".join(sys.argv[1:])
    
    if all(c in "O." for c in input_str) and len(input_str) % 6 == 0:
        join_char = english_dict[" "]
        print(braille_to_text(join_char.join(sys.argv[1:])))
    else:
        join_char = " "
        print(text_to_braille(join_char.join(sys.argv[1:])))

if __name__ == "__main__":
    main()
