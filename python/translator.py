import argparse

character_map = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    'capital': ".....O",
    'number': ".O.OOO",
    ' ': "......"
}

number_map = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0'
}

inverted_character_map = {v: k for (k, v) in character_map.items()}
inverted_number_map = {v: k for (k, v) in number_map.items()}


def to_english(command: str) -> str:
    """ Converts the given Braille string <command> to English. """
    statement = ''
    capitalize = False
    number = False

    while command:
        i, j = 0, 6
        char = inverted_character_map.get(command[i:j])
        if char == 'capital':
            capitalize = True
            i += 6
            command = command[i:]
            continue
        elif char == 'number':
            number = True
            i += 6
            command = command[i:]
            continue
        elif char == ' ':
            statement += char
            i += 6
            command = command[i:]
            number = False
            continue

        if capitalize:
            statement += char.upper()
            i += 6
            command = command[i:]
            capitalize = False
        elif number:
            statement += number_map.get(char)
            i += 6
            command = command[i:]
        else:
            statement += char
            i += 6
            command = command[i:]
    return statement


def to_braille(command: list[str]) -> str:
    """ Converts the strings in <command> to Braille. """
    statement = ''
    number = False
    for word in command:
        for char in word:
            if char.isupper():
                statement += character_map.get("capital")
                statement += character_map.get(char.lower())
            elif char.isnumeric() and number:
                statement += character_map.get(inverted_number_map.get(char))
            elif char.isnumeric() and not number:
                statement += character_map.get("number")
                statement += character_map.get(inverted_number_map.get(char))
                number = True
            else:
                statement += character_map.get(char)
        statement += character_map.get(' ')
    return statement[:-6]


if __name__ == "__main__":
    """ Parses a set of command-line arguments to English or Braille. """
    # Create a parser and add a variable argument.
    parser = argparse.ArgumentParser(
        description="A script that converts English to Braille, and vice-versa.")
    parser.add_argument('arg', nargs="*", help="The provided argument.")

    # Parse the command.
    cmd = parser.parse_args()

    # Determine if English or Braille, then print the corresponding output.
    argument = ' '.join(cmd.arg)
    if '.' in argument:
        print(to_english(argument))
    else:
        print(to_braille(cmd.arg))
