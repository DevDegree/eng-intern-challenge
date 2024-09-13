import sys
from typing import Dict

# define mappings for english letters to braille
braille_alphabet: Dict[str, str] = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

# define mappings for numbers to braille (when preceded by the number prefix)
braille_numbers: Dict[str, str] = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# special braille symbols for capital letters, numbers, and spaces
braille_specials: Dict[str, str] = {
    'capital': '.....O',  # prefix for capital letters
    'number': '.O.OOO',   # prefix for numbers
    'space': '......'     # braille symbol for space
}

# reverse mapping for braille to english (letters and numbers combined)
braille_to_english_map: Dict[str, str] = {**braille_alphabet, **braille_numbers}

def is_braille(input_str: str) -> bool:
    """check if the input string contains only braille symbols ('O' and '.')."""
    return set(input_str).issubset({'O', '.'})

def braille_to_english(braille_str: str) -> str:
    """convert braille to english, handling capital and number modes."""
    english_output = []  # to collect the translated characters
    chunks = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    
    capital_mode = False
    number_mode = False

    # process each 6-character braille chunk
    for chunk in chunks:
        if chunk == braille_specials['capital']:
            capital_mode = True
            continue
        if chunk == braille_specials['number']:
            number_mode = True
            continue
        if chunk == braille_specials['space']:
            english_output.append(" ")
            capital_mode = number_mode = False
            continue
        
        # lookup the chunk and apply appropriate modes
        character = braille_to_english_map.get(chunk, '?')
        if number_mode:
            english_output.append(character)  # append number directly
        elif capital_mode:
            english_output.append(character.upper())  # capitalize letter
            capital_mode = False  # reset after one letter
        else:
            english_output.append(character)  # append normal letter

    return ''.join(english_output)

def english_to_braille(english_str: str) -> str:
    """convert english to braille, handling capital and number modes."""
    braille_output = []  # to collect the braille translation
    number_mode = False  # track if number mode is active

    for char in english_str:
        if char.isupper():
            braille_output.append(braille_specials['capital'])
            braille_output.append(braille_alphabet[char.lower()])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                braille_output.append(braille_specials['number'])
                number_mode = True
            braille_output.append(braille_numbers[char])
        elif char == " ":
            braille_output.append(braille_specials['space'])
            number_mode = False
        else:
            braille_output.append(braille_alphabet[char])
            number_mode = False

    return ''.join(braille_output)

def main() -> None:
    """handle input from the command line and perform translation."""
    input_str = " ".join(sys.argv[1:])  # combine command-line args into one string
    # determine if input is braille or english and translate accordingly
    if is_braille(input_str):
        sys.stdout.write(braille_to_english(input_str))
    else:
        sys.stdout.write(english_to_braille(input_str))

if __name__ == "__main__":
    main()
