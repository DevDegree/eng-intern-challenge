from translation_dictionaries import *
def determine_lang(given_string : str) -> str:
    """
    Determines the language of the input string (Braille or English).
    Errors regarding specific invalid character inputs are addressed in
    the translation functions.

    Args:
        given_string (str): The string to be analyzed.

    Returns:
        str: "BRAILLE" if the input is Braille, otherwise "ENGLISH".
    """

    # Strings indivisible by the standard size of 1 Braille symbol must be English
    if len(given_string) % BR_SIZE != 0:
        return "ENGLISH"

    # Braille strings may contain only the symbols '.' and 'O'
    for char in given_string:
        if char != "." and char != "O":
            return "ENGLISH"

    return "BRAILLE"

def to_english(br_text : str) -> str:
    """
    Translates Braille text to English.

    Args: br_text (str): The Braille string to be translated to English.

    Returns:
        str: The corresponding English text.
    """

    type = STANDARD_DEF  # Keeps track of current mode (e.g. standard, uppercase, numeric).
    eng_chars = []  # Stores translated English characters.
    i = 0  # Index to iterate over Braille text.

    # Loop through Braille text in chunks of standard Braille symbol size.
    while (i + (BR_SIZE - 1)) < len(br_text):
        br_symbol = ""

        # Extract one Braille symbol at a time.
        for j in range(BR_SIZE):
            br_symbol += br_text[i]
            i += 1

        # Look up the Braille symbol in the dictionary.
        try:
            eng_symbol = b_to_e[br_symbol]
        except KeyError:
            print("Invalid Braille Text Provided")
            exit(2)  # Exit if the Braille symbol is invalid.

        # Symbols immediately after space characters should be of standard type.
        if eng_symbol[STANDARD_DEF] == " ":
            type = STANDARD_DEF
            eng_chars.append(eng_symbol[type])
            continue
        else:
            try:
                index_check = eng_symbol[type]
            except IndexError:
                print("Invalid Braille Text Provided")
                exit(2)  # Expected type does not match current symbol.

        # Append the English character based on the current type.
        if type == NUM:
            eng_chars.append(eng_symbol[type])

        elif eng_symbol[STANDARD_DEF] == "CAP FOLLOWS":
            type = UPPER

        elif eng_symbol[STANDARD_DEF] == "NUM FOLLOWS":
            type = NUM

        else:
            eng_chars.append(eng_symbol[type])
            type = STANDARD_DEF

    # Join the translated English characters into a single string.
    translated = "".join(eng_chars)
    return translated


def to_braille(eng_text: str) -> str:
    """
    Translates English text to Braille.

    Args:
        eng_text (str): The English string to be converted to Braille.

    Returns:
        str: the corresponding Braille text (using '.' and 'O')
    """
    type = STANDARD_DEF  # Keeps track of the current mode (standard, upper case, numeric).
    br_symbols = []  # Stores translated Braille symbols.

    # Iterate over each character in the English text converting and appending relevant symbols
    for char in eng_text:
        if char.islower():
            br_symbols.append(e_to_b[char])
            type = STANDARD_DEF

        elif char.isupper():
            # If the character is uppercase, append a "CAP FOLLOWS" marker and then the Braille symbol
            br_symbols.append(e_to_b["CAP FOLLOWS"])
            br_symbols.append(e_to_b[char])
            type = STANDARD_DEF

        elif char.isdigit():
            # If the character is a digit, switch to numeric mode and append the appropriate symbols.
            if type == NUM:
                br_symbols.append(e_to_b[char])
            else:
                br_symbols.append(e_to_b["NUM FOLLOWS"])
                br_symbols.append(e_to_b[char])
                type = NUM

        elif char == " ":
            br_symbols.append(e_to_b[char])
            type = STANDARD_DEF
        else:
            print("Invalid English Text Provided")
            exit(3)  # Exit if a nonalphanumeric or non-space-character is encountered.

    # Join the Braille symbols into a single string.
    translated = "".join(br_symbols)
    return translated

def translate(given_string : str) -> str:
    """
    Translates a given string from English to Braille or vice versa.

    Args:
        given_string (str): The input string to be translated (could be English or Braille)

    Returns:
        str: The translated string (either Braille or English).
    """

    # Determine whether the input is in Braille or English and call the appropriate function
    if determine_lang(given_string) == "ENGLISH":
        return to_braille(given_string)
    elif determine_lang(given_string) == "BRAILLE":
        return to_english(given_string)
    else:
        print("ERROR: INVALID INPUTS")
        exit(4) # Exit if inputs cannot be classified


