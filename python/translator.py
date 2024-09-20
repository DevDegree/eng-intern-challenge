import sys

# Dictionary
letters_to_braille = {
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
    "w": ".OO.OO",
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
    "capital": ".....O",
    "number": ".O.OOO",
    " ": "......",
}

braille_to_letters = {b: l for l, b in letters_to_braille.items() if l.isalpha()}
braille_to_numbers = {b: n for n, b in letters_to_braille.items() if n.isdigit()}


# Check if input is Braille
def is_braille(string):
    s = string.replace(" ", "")

    if len(s) % 6 != 0:  # Braille is divisible by 6
        return False

    for symbol in s:  # Check that only Braille symbolacters O and . are present
        if symbol not in ("O", "."):
            return False
    return True


# Convert Braille to english
def translate_braille(braille):
    result = []
    is_num = False  # Flag to see if we should enter number mode
    is_cap = False  # Flag to see if the next symbol should be capitalized
    i = 0

    while i < len(braille):
        symbol = braille[i : i + 6]  # A symbol is 6 Braille digits

        if symbol == letters_to_braille[" "]:
            result.append(" ")
            is_num = False  # Reset number mode flag after a space
        elif symbol == letters_to_braille["capital"]:
            is_cap = True
        elif symbol == letters_to_braille["number"]:
            is_num = True
        else:
            if is_num:  # Number mode. fetch corresponding number
                symbol = braille_to_numbers.get(symbol, "")
            else:
                symbol = braille_to_letters.get(
                    symbol, ""
                )  # Letter mode. fetch corresponding letter
            if symbol:
                if is_cap:
                    symbol = (
                        symbol.upper()
                    )  # If capitalization flag set, capitalize the symbol and reset the flag
                    is_cap = False
                result.append(symbol)
        i += 6  # Move onto the next Braille symbol

    return "".join(result)  # Join the results into a final string


# Convert english to Braille
def translate_english(text):
    result = []
    is_num = False  # Flag to see if we should enter number mode

    for symbol in text:
        if symbol == " ":
            result.append(letters_to_braille[" "])
            is_num = False  # Reset number mode flag after a space
        elif symbol.isdigit():
            if not is_num:  # If not yet in number mode, append number sign
                result.append(letters_to_braille["number"])
                is_num = True  # Set number mode flag
            result.append(letters_to_braille[symbol])
        else:
            if is_num:  # Leaving number mode, reset the flag
                is_num = False
            if (
                symbol.isupper()
            ):  # If symbol is upper case, add capital symbol and the Braille lower case letter
                result.append(letters_to_braille["capital"])
                result.append(letters_to_braille[symbol.lower()])
            else:
                if (
                    symbol in letters_to_braille
                ):  # if symbol is in the dictionary, append the symbol
                    result.append(letters_to_braille[symbol])
                else:
                    result.append(
                        "......"
                    )  # Append space if the symbol cannot be found in the dictionary

    return "".join(result)  # Join the results into a final string


def main(string):
    if is_braille(string):
        print(translate_braille(string))
    else:
        print(translate_english(string))


if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    main(input)
