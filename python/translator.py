
"""
This module contains the solution to the Shopify Engineering Internship Technical Challange.
The problem is to convert ASCII characters to Braille and vice versa.
"""
import sys

# For the purposes of this program, ascii will be letters and special characters, numbers will be listed seperately
ascii2braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    "(": "O.O..O",
    ")": ".O.OO.",
    'UPPERCASE': ".....O",
    'NUMERIC': ".O.OOO"
}

num2braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...'
}

braille2ascii = {b: a for a, b in ascii2braille.items()}
braille2num = {b: n for n, b in num2braille.items()}


def ascii_to_braille(input_ascii: str) -> str:
    """
    Function that converts an ASCII string to Braille string.

    Parameters
    ----------
    - ascii: ascii string to convert to braille

    Returns
    -------
    - braille: braille version of the input ascii string
    """
    braille: str = ""
    numeric: bool = False

    for char in input_ascii:
        # Check if character is uppercase
        if char.isupper():
            braille += ascii2braille['UPPERCASE']
            braille += ascii2braille[char.lower()]

        # Check if character is numeric
        elif char.isnumeric():
            # Set numeric flag if not already set and add numeric braille character, then add the number
            # if numeric flag is already set, just add the number
            if not numeric:
                braille += ascii2braille['NUMERIC']
                numeric = True
            braille += num2braille[char]

        # Else convert character to braille
        else:
            if char == " ": numeric = False     # Reset numeric flag if character is space
            braille += ascii2braille[char]

    return braille


def braille_to_ascii(input_braille: str) -> str:
    """
    Function that converts a Braille character to ASCII.

    Parameters
    ----------
    - braille: braille string to convert to ascii

    Returns
    -------
    - ascii: ascii version of the input braille string
    """
    ascii: str = ""
    uppercase: bool = False
    numeric: bool = False

    # Split braille string into 6 character chunks
    for braille in [input_braille[i:i+6] for i in range(0, len(input_braille), 6)]:
        # Set flag for uppercase to convert the next character to uppercase
        if braille == ascii2braille['UPPERCASE']:
            uppercase = True

        # Set flag for numeric to convert all following characters until space to numeric
        elif braille == ascii2braille['NUMERIC']:
            numeric = True

        # Convert braille to ascii according to the flags
        else:
            if uppercase:
                ascii += braille2ascii[braille].upper()
                uppercase = False
            elif numeric:
                ascii += braille2num[braille]
            else:
                if braille == ascii2braille[' ']: numeric = False   # Reset numeric flag if character is space
                ascii += braille2ascii[braille]

    return ascii


def main() -> str:
    """
    Main function that reads input from command line, converts it to Braille or ASCII.  Then, prints it to the console.
    """
    # Combine all command line arguments into a single string
    input_string: str = ' '.join(sys.argv[1:])

    # Check if input is ASCII or Braille
    if any(char not in ['.', 'O'] for char in set(input_string)):
        # Convert ASCII to Braille
        out_string: str = ascii_to_braille(input_string)
    else:
        # Convert Braille to ASCII
        out_string: str = braille_to_ascii(input_string)

    print(out_string)

if __name__ == "__main__":
    main()