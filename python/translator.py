import sys  # necessary for command line execution


def translate(inp):
    """
    Translate from Braille to English or vice-versa.
    Accepts alphanumeric strings and valid Braille-like strings only
    and returns the appropriate converted string.
    Can be executed from command line.

    Args:
        inp (str): a Braille-like string or alphanumeric string.

    Returns:
        output (str: the string resulting from translation.

    Raises:
        ValueError: if the input is not a valid Braille-like string.

    """
    braille_to_english = {
        "O.....": 'a',
        "O.O...": 'b',
        "OO....": 'c',
        "OO.O..": 'd',
        "O..O..": 'e',
        "OOO...": 'f',
        "OOOO..": 'g',
        "O.OO..": 'h',
        ".O....": 'i',
        ".O.O..": 'j',
        "O...O.": 'k',
        "O.O.O.": 'l',
        "OO..O.": 'm',
        "OO.OO.": 'n',
        "O..OO.": 'o',
        "OOO.O.": 'p',
        "OOOOO.": 'q',
        "O.OOO.": 'r',
        ".OO.O.": 's',
        ".OOOO.": 't',
        "O...OO": 'u',
        "O.O.OO": 'v',
        ".OOO.O": 'w',
        "OO..OO": 'x',
        "OO.OOO": 'y',
        "O..OOO": 'z',
        "......": ' '
    }
    english_to_braille = {
        'a': "O.....",
        'b': "O.O...",
        'c': "OO....",
        'd': "OO.O..",
        'e': "O..O..",
        'f': "OOO...",
        'g': "OOOO..",
        'h': "O.OO..",
        'i': ".O....",
        'j': ".O.O..",
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
        ' ': "......"
    }
    number_to_braille = {
        '1': "O.....",
        '2': "O.O...",
        '3': "OO....",
        '4': "OO.O..",
        '5': "O..O..",
        '6': "OOO...",
        '7': "OOOO..",
        '8': "O.OO..",
        '9': ".OO...",
        '0': ".OOO.."
    }
    braille_to_number = {
        "O.....": '1',
        "O.O...": '2',
        "OO....": '3',
        "OO.O..": '4',
        "O..O..": '5',
        "OOO...": '6',
        "OOOO..": '7',
        "O.OO..": '8',
        ".OO...": '9',
        ".OOO..": '0'
    }
    modifier_braille = [".....O", ".O.OOO"]

    def check_braille(text):
        for char in text:
            if char != "." and char != "O":
                return False

        return True

    def braille_to_english_key(braille):
        return braille_to_english[braille]

    def english_to_braille_key(character):
        char = character.lower()
        return english_to_braille[char]

    def number_to_braille_key(number):
        return number_to_braille[number]

    def braille_to_number_key(character):
        return braille_to_number[character]

    def convert_braille_to_english(braille):
        output = []
        number_mode = False
        caps_mode = False
        captured_string = []

        for char in braille:
            captured_string.append(char)
            # Parse through 6 characters at a time.
            # Then form a Braille string to figure out what it is in English.
            if len(captured_string) == 6:
                converted_string = ""
                string = "".join(captured_string)

                if caps_mode:
                    converted_string = braille_to_english_key(string).upper()
                    caps_mode = False

                elif number_mode:
                    if string == "......":  # stop adding numbers if space is found
                        number_mode = False
                        converted_string = ' '

                    else:
                        converted_string = braille_to_number_key(string)

                elif string == modifier_braille[0]:  # if next capital
                    caps_mode = True

                elif string == modifier_braille[1]:  # if next number
                    number_mode = True

                else:
                    converted_string = braille_to_english_key(string)
                output.append(converted_string)
                captured_string = []

        return "".join(output)

    def convert_english_to_braille(english):
        output = []
        number_mode = False

        for char in english:
            if char == ' ':
                output.append(english_to_braille_key(char))
                number_mode = False

            elif number_mode:  # adding numbers
                output.append(number_to_braille_key(char))

            elif not number_mode and char.isdigit():  # add numbers from now on, not characters
                output.append(modifier_braille[1])
                output.append(number_to_braille_key(char))
                number_mode = True

            elif char.isupper():
                number_mode = False  # interrupt number adding, go back to characters
                output.append(modifier_braille[0])
                output.append(english_to_braille_key(char))

            else:
                number_mode = False
                output.append(english_to_braille_key(char))

        return "".join(output)

    inp = str(inp)
    is_braille = check_braille(inp)

    if is_braille:
        try:
            if len(inp) % 6 == 0:
                return convert_braille_to_english(inp)

        except ValueError as e:
            print(e)

    else:
        return convert_english_to_braille(inp)


if __name__ == "__main__":  # for running in command line
    input_text = " ".join(sys.argv[1:])  # captures all arguments provided
    input_text = str(input_text)
    result = translate(input_text)
    print(result)
