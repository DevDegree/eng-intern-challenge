import sys

braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'cap': '.....O',
    'num': '.O.OOO'
}

braille_numbers = {
    '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

english_letters = {v: k for k, v in braille_letters.items() if k not in ('cap', 'num')}
english_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_string: str) -> bool:
    """
    Determines if the function is Braille or not
    
    Parameters:
    input_string (str): The string to be checked.
    
    Returns:
    bool: True if the string is Braille, False otherwise.

    Notes:
    - Will return True if the string contains only "." and "O"
    - Input's such as OOOOOO are considnered English since all Braille characters in our dict have at least 1 "."
    - Assuming Braille can't have whitespace
    """
    return all(c in 'O.' for c in input_string) and 'O' in input_string and '.' in input_string

def to_English(braille: str) -> str:
    """ 
    Translates a Braille input to English

    Parameters:
    braille (str): input Braille string

    Returns:
    str: English string

    Note:
    - Returns empty string if the number of characters is not a multiple of 6
    - In the case that there are back to back capital indicators they will cancel eachother out
    - If the Braille sequence after a number indicator does not represent a number then it will continue and try to match that sequence with something else (a letter or another symbol)
    """
    if len(braille) % 6 != 0:
        return ''

    result = []
    i = 0
    while i < len(braille):
        braille_sequence = braille[i:i+6]
        if braille_sequence == braille_letters['cap']:
            i += 6
            braille_sequence = braille[i:i+6]
            if braille_sequence in english_letters:
                result.append(english_letters[braille_sequence].upper())
        elif braille_sequence == braille_letters['num']:
            i += 6
            while i < len(braille) and braille[i:i+6] in english_numbers:
                result.append(english_numbers[braille[i:i+6]])
                i += 6
            continue
        else:
            result.append(english_letters.get(braille_sequence, '?'))
        i += 6
    
    return ''.join(result)

def to_Braille(english: str) -> str:
    """
    Translate English text to Braille.

    Parameters:
    english (str): Input English string

    Returns: 
    Braille string
    """
    res = []
    is_num_sequence = False

    for c in english:
        if c.isdigit():
            if not is_num_sequence:
                is_num_sequence = True
                res.append(braille_letters['num'])
            res.append(braille_numbers.get(c, '?'))
        elif c == ' ':
            is_num_sequence = False
            res.append(braille_letters[' '])
        elif c.isalpha():
            if c.isupper():
                res.append(braille_letters['cap'])
            res.append(braille_letters.get(c.lower(), '?'))
        else:
            res.append(braille_letters.get(c, '?'))
    
    return ''.join(res)

def main():
    if len(sys.argv) < 2:
        print("format: python translator.py <input>")
        return

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        output = to_English(input_string)
    else:
        output = to_Braille(input_string)

    print(output)

if __name__ == "__main__":
    main()
