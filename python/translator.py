import sys

# Braille to English mapping
BRAILLE_TO_ENG = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',

    '.....O': 'capital next', '.O.OOO': 'number next'
}

# Reverse mapping from English letters to Braille
ENG_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENG.items()}

# Number mapping from Braille letters to numbers when in number mode
NUM_MAPPING = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def braille_to_eng_translate(braille):
    """
    Convert braille string to English text.
    
    :param braille: str
    :rtype: str
    """
    i = 0
    result = []
    cap_next_char = False
    in_num_mode = False

    while i < len(braille):
        cur_char = braille[i:i+6]

        if cur_char == ENG_TO_BRAILLE["capital next"]: # capital next
            cap_next_char = True
        elif cur_char == ENG_TO_BRAILLE['number next']: # number next
            in_num_mode = True
        elif cur_char in BRAILLE_TO_ENG:
            letter = BRAILLE_TO_ENG[cur_char]
            if in_num_mode and letter in NUM_MAPPING:
                result.append(NUM_MAPPING[letter])
            else:
                if cap_next_char:
                    letter = letter.upper()
                    cap_next_char = False
                result.append(letter)
                if letter == ' ':
                    in_num_mode = False
        i += 6

    return ''.join(result)

def eng_to_braille_translate(english):

    """
    Convert English text to braille string.
    
    :param english: str
    :rtype: str
    """
    result = [] # List to store converted Braille letters

    in_number_mode = False # Flag to indicate if the next letter is a number

    for char in english:
        if char.isupper(): # Check if the character is uppercase
            result.append(ENG_TO_BRAILLE['capital next'])
            char = char.lower()

        if char.isdigit(): # Check if the character is a digit
            if not in_number_mode:
                # If the character is a digit and not currently in number mode, add the 'number next' character
                result.append(ENG_TO_BRAILLE['number next'])
                in_number_mode = True
            char = list(NUM_MAPPING.keys())[list(NUM_MAPPING.values()).index(char)]
        elif in_number_mode:
            # If the character is not a digit and currently in number mode, add the 'number next' character
            in_number_mode = False

        result.append(ENG_TO_BRAILLE[char])

    return ''.join(result)


def translate_str(input_string):
    """
    Translates input string to other language.
    :param input_string: str
    :rtype: str
    """
    if set(input_string).issubset({'O', '.'}): # Check if the input string is in Braille
        return braille_to_eng_translate(input_string)
    else: # Translate English to Braille
        return eng_to_braille_translate(input_string)


if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    result = translate_str(input_string)
    sys.stdout.write(result)
    sys.stdout.flush()