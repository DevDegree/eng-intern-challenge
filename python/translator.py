import sys

braille_alphabet = {
    # Letters a to z
    'a': 'O.....',   # a
    'b': 'O.O...',   # b
    'c': 'OO....',   # c
    'd': 'OO.O..',   # d
    'e': 'O..O..',   # e
    'f': 'OOO...',   # f
    'g': 'OOOO..',   # g
    'h': 'O.OO..',   # h
    'i': '.OO...',   # i
    'j': '.OOO..',   # j
    'k': 'O...O.',   # k
    'l': 'O.O.O.',   # l
    'm': 'OO..O.',   # m
    'n': 'OO.OO.',   # n
    'o': 'O..OO.',   # o
    'p': 'OOO.O.',   # p
    'q': 'OOOOO.',   # q
    'r': 'O.OOO.',   # r
    's': '.OO.O.',   # s
    't': '.OOOO.',   # t
    'u': 'O...OO',   # u
    'v': 'O.O.OO',   # v
    'w': '.OOO.O',   # w
    'x': 'OO..OO',   # x
    'y': 'OO.OOO',   # y
    'z': 'O..OOO',   # z

    # Special Symbols
    'capital': '.....O',  # Capital letter indicator
    'decimal': '.O...O',  # decimal follows
    'number': '.O.OOO',   # Number indicator
    ' ': '......'         # Space symbol
}

braille_numbers = {
    '1': 'O.....',   # 1
    '2': 'O.O...',   # 2
    '3': 'OO....',   # 3
    '4': 'OO.O..',   # 4
    '5': 'O..O..',   # 5
    '6': 'OOO...',   # 6
    '7': 'OOOO..',   # 7
    '8': 'O.OO..',   # 8
    '9': '.OO...',   # 9
    '0': '.OOO..',   # 0
}

braille_to_english_map = {value: key for key, value in braille_alphabet.items()}

braille_to_numbers_map = {value: key for key, value in braille_numbers.items()}


def is_braille(input_str):
    """
    Checks if the input str is in braille format 
    or not

    Return -> True if braille
              False if not braille
    """

    if len(input_str) % 6 != 0:
        return False
    
    for char in input_str:
        if char not in {'O', '.'}:
            return False
    
    return True

def translate_to_braille(input_text):
    """
    Translates english input string to braille using 
    braille_alphabet map for alphabets and braille_numbers
    map for numbers. 

    Return -> Translated string in braille format 
    """

    braille_output = []
    number_mode = False  # Flag to indicate if we are in number mode

    for char in input_text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(braille_alphabet['number'])
                number_mode = True 
            braille_output.append(braille_numbers[char])

        elif char.isalpha():
            number_mode = False

            if char.isupper():
                braille_output.append(braille_alphabet['capital'])
                char = char.lower()
            braille_output.append(braille_alphabet[char])
        elif char == ' ':
            braille_output.append(braille_alphabet[' '])
            number_mode = False 

    return ''.join(braille_output)

def translate_to_english(input_text):
    """
    Translates braille input string to english using
    braille_to_english_map for alphabets and 
    braille_to_numbers_map for numbers. 

    Return -> Translated string in english format
    """
    english_output = []
    is_number_mode = False  
    is_capital_mode = False 

    for i in range(0, len(input_text), 6):
        braille_char = input_text[i:i+6]

        if braille_char == braille_alphabet['number']:
            is_number_mode = True
            continue
        if braille_char == braille_alphabet['capital']:
            is_capital_mode = True
            continue
        if braille_char == braille_alphabet[' ']:
            english_output.append(' ')
            is_number_mode = False
            continue

        # Lookup the Braille symbol in the reversed map
        decoded_char = ''
        if (is_number_mode):
            decoded_char = braille_to_numbers_map.get(braille_char, '')
        else:
            decoded_char = braille_to_english_map.get(braille_char, '')
        
        if is_number_mode:
            english_output.append(decoded_char)
        elif is_capital_mode:
            english_output.append(decoded_char.upper())
            is_capital_mode = False
        else:
            english_output.append(decoded_char)
    
    return ''.join(english_output)

def main():
    input_text = ' '.join(sys.argv[1:])

    output = ""
    
    if is_braille(input_text):
        output = translate_to_english(input_text)
    else:
        output = translate_to_braille(input_text)
    
    print(output)


if __name__ == "__main__":
    main()