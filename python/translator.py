import sys

# maps for translation
braille_to_english_charmp = {
    # letters
    "o.....": "a", "o.o...": "b", "oo....": "c", "oo.o..": "d", "o..o..": "e",
    "ooo...": "f", "oooo..": "g", "o.oo..": "h", ".oo...": "i", ".ooo..": "j",
    "o...o.": "k", "o.o.o.": "l", "oo..o.": "m", "oo.oo.": "n", "o..oo.": "o",
    "ooo.o.": "p", "ooooo.": "q", "o.ooo.": "r", ".oo.o.": "s", ".oooo.": "t",
    "o...oo": "u", "o.o.oo": "v", ".ooo.o": "w", "oo..oo": "x", "oo.ooo": "y",
    "o..ooo": "z",
}

english_to_braille_charmp = {

}

braille_to_english_numbermp = {
    # numbers
    ".ooo..": "0", "o.....": "1", "o.o...": "2", "oo....": "3", "oo.o..": "4", "o..o..": "5",
    "ooo...": "6", "oooo..": "7", "o.oo..": "8", ".oo...": "9",
}
english_to_braille_numbermp = {

}

braille_to_english_symblmp = {
    # synmbols
    "..oo.o": ".", "..o...": ",", "..o.oo": "?", "..ooo.": "|", "..oo.": ":", "..o.o.": ";",
    "....oo": "-", ".o..o.": "/", ".oo..o": "<", "o..oo.": ">", "o.o..o": "(", ".o.oo.": ")",
    "......": " "
}

english_to_braille_symblmp = {

}

braille_to_english_specialmp = {
    ".....o": "CAPS", ".o...o": "DEC", ".o.ooo": "NUM"
}
english_to_braille_specialmp = {

}


# set up reversed maps from hardcoded maps
def setup_reversed_mps():
    generate_reversed_charmp()
    generate_reversed_nummp()
    generate_reversed_symbmp()
    generate_reversed_specialmp()


# reverse char map
def generate_reversed_charmp():
    for key, value in braille_to_english_charmp.items():
        english_to_braille_charmp[value] = key


# reverse number map
def generate_reversed_nummp():
    for key, value in braille_to_english_numbermp.items():
        english_to_braille_numbermp[value] = key


# reverse symbol map
def generate_reversed_symbmp():
    for key, value in braille_to_english_symblmp.items():
        english_to_braille_symblmp[value] = key


# reverse special map
def generate_reversed_specialmp():
    for key, value in braille_to_english_specialmp.items():
        english_to_braille_specialmp[value] = key


# Check if input text is in braille--
# True if braille false if not braille
def is_braille(inp_text: str):
    braille_txt = inp_text.lower()
    braille_char_set = {"o", "."}

    is_valid_braille = True

    # validate length
    if len(braille_txt) % 6 != 0:
        is_valid_braille = False

    if is_valid_braille:
        # validate characters
        for char in braille_txt:
            if char not in braille_char_set:
                is_valid_braille = False
    return is_valid_braille


"""
Convert English text to Braille.

Args:
    text (str): The English text to convert.

Returns:
    str: A string representing the text in Braille.
"""


def convert_english_to_braille(inp_text: str):
    result = ""
    num_lock = False
    dec = False
    for char in inp_text:
        mp_char = char.lower()
        original_char = char

        curr_braille = ""

        if mp_char in english_to_braille_charmp:
            if original_char.isupper():
                curr_braille += english_to_braille_specialmp["CAPS"]
            curr_braille += english_to_braille_charmp[mp_char]
        elif mp_char in english_to_braille_numbermp:
            if not num_lock:
                curr_braille += english_to_braille_specialmp["NUM"]
                num_lock = True
            curr_braille += english_to_braille_numbermp[mp_char]
        else:
            if mp_char == " ":
                num_lock = False
                dec = False
            elif mp_char == "." and num_lock:
                curr_braille += english_to_braille_specialmp["DEC"]
            curr_braille += english_to_braille_symblmp[mp_char]

        result += curr_braille

    return result.upper()


"""
Convert Braille to English.

Args:
    text (str): The braille text to convert.

Returns:
    str: A string representing the text in English.
"""


def convert_braille_to_english(inp_text: str):
    # special symbol controller
    caps_on = False
    num_on = False
    dec_on = False

    space = english_to_braille_symblmp[" "]
    decimal_follows = english_to_braille_specialmp["DEC"]

    result = ""
    for i in range(0, len(inp_text), 6):
        curr_pattern = inp_text[i:i + 6]
        # number logic
        if num_on:
            curr_char = ""
            if dec_on:
                # this should always be a period -- incase of decimals
                curr_char = braille_to_english_symblmp[curr_pattern]
                dec_on = False
            else:
                # assume we don't have decimals
                if curr_pattern != decimal_follows and curr_pattern != space:
                    curr_char = braille_to_english_numbermp[curr_pattern]
                elif curr_pattern == space:
                    result += " "
                    num_on = False
                    dec_on = False
                else:
                    dec_on = True
        else:
            # other characters and symbol logic
            curr_char = ""
            if curr_pattern in braille_to_english_charmp:
                curr_char = braille_to_english_charmp[curr_pattern]
                if caps_on:
                    curr_char = curr_char.capitalize()
                    caps_on = False
            elif curr_pattern in braille_to_english_symblmp:
                curr_char = braille_to_english_symblmp[curr_pattern]
                if curr_char == " ":
                    dec_on = False
                    num_on = False
            else:
                special_command = braille_to_english_specialmp[curr_pattern]
                if special_command == "CAPS":
                    caps_on = True
                elif special_command == "NUM":
                    num_on = True
                else:
                    dec_on = True

        result += curr_char

    return result


def convertText(inp_text: str):
    if is_braille(inp_text):
        braille_text = inp_text.lower()
        result = convert_braille_to_english(braille_text)
    else:
        result = convert_english_to_braille(inp_text)

    return result


def main():
    setup_reversed_mps()

    # get the text from command line and clean text
    text = " ".join(sys.argv[1:])
    text = text.strip()

    # convert text to appropriate format
    converted_text = convertText(text)

    print(converted_text)


# main guard
if __name__ == "__main__":
    main()
