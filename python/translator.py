import sys


# braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y',
    'O..OOO': 'Z',
    '......': ' '
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# special symbols
NUMBER_SYMBOL = '.O.OOO'
CAPITAL_SYMBOL = '.....O'
# number mappings
NUMBER_MAPPING = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0'
}


def english_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_SYMBOL)
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[list(NUMBER_MAPPING.keys())[list(NUMBER_MAPPING.values()).index(char)]])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(CAPITAL_SYMBOL)
            result.append(ENGLISH_TO_BRAILLE[char.upper()])
        elif char == ' ':
            number_mode = False
            result.append(ENGLISH_TO_BRAILLE[char])
        else:
            raise ValueError(f"unsupported character: {char}")
    
    return ''.join(result)


def braille_to_english(braille):
    result = []
    i = 0
    number_mode = False
    capitalize_next = False
    
    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == NUMBER_SYMBOL:
            number_mode = True
        elif symbol == CAPITAL_SYMBOL:
            capitalize_next = True
        else:
            char = BRAILLE_TO_ENGLISH[symbol]
            if number_mode and char in NUMBER_MAPPING:
                result.append(NUMBER_MAPPING[char])
            else:
                if number_mode:
                    number_mode = False
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)
        
        i += 6
    
    return ''.join(result)


def is_braille(text):
    # check if the text is valid braille
    return all(c in '.O' for c in text) and len(text) % 6 == 0


def translate(text):
    # determine if input is braille or english and translate accordingly
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    
    if len(args) == 0:
        print("usage: python translator.py <text_to_translate>")
        return
    
    # join all arguments into a single string
    input_text = ' '.join(args)
    try:
        # translate and print without trailing newline
        print(translate(input_text), end='')
    except ValueError as e:
        print(f"error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()