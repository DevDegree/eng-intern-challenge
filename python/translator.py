import sys

braille_syntax = {'O', '.'}

braille_decimal_code_to_char = {
    32: 'a', 40: 'b', 48: 'c', 52: 'd', 36: 'e',
    56: 'f', 60: 'g', 44: 'h', 24: 'i', 28: 'j',
    33: 'k', 42: 'l', 49: 'm', 53: 'n', 38: 'o',
    57: 'p', 61: 'q', 46: 'r', 25: 's', 30: 't',
    35: 'u', 43: 'v', 29: 'w', 51: 'x', 55: 'y',
    39: 'z', 1: 'capital', 23: 'number', 34: '.',
    0: ' '
}

follow_codes = {'capital', 'number'}

braille_decimal_code_to_number = {
    32: '1',
    40: '2',
    48: '3',
    52: '4',
    36: '5',
    56: '6',
    60: '7',
    44: '8',
    24: '9',
    28: '0'
}

char_to_braille_decimal_code = {
    braille_decimal_code_to_char[code]: code for code in braille_decimal_code_to_char
}

number_to_braille_decimal_code = {
 braille_decimal_code_to_number[code]: code for code in braille_decimal_code_to_number
}

english_to_braille_decimal_code = {}
english_to_braille_decimal_code.update(char_to_braille_decimal_code)
english_to_braille_decimal_code.update(number_to_braille_decimal_code)


def braille_binary_to_decimal_code(braile: str) -> int:
    binary_rep = braile.replace('O', '1').replace('.', '0')
    return int(binary_rep, 2)

def decimal_to_braille_binary_code(decimal: int) -> str:
    binary_rep = bin(decimal)[2:]
    binary_rep = binary_rep.zfill(6)
    braille_code = str(binary_rep).replace('1', 'O').replace('0', '.')
    return braille_code


def is_input_braille(input: str) -> bool:
    if len(input) % 6 != 0:
        return False

    for letter in input:
        if letter not in braille_syntax:
            return False

    return True


def translate_braille_code_to_english(braille: str) -> str:
    translation_so_far = ""
    next_capital = False
    next_number = False

    for i in range(0, len(braille), 6):
        code = braille[i:i + 6]
        decimal_rep = braille_binary_to_decimal_code(code)
        translated_char = braille_decimal_code_to_char.get(decimal_rep, "") if not next_number else braille_decimal_code_to_char.get(code, "")
        if translated_char in follow_codes:
            if translated_char == 'capital':
                next_capital = True
            elif translated_char == 'number':
                next_number = True
        else:
            if next_capital:
                translated_char = translated_char.upper()
                next_capital = False
            elif translated_char == ' ':
                next_number = False
            translation_so_far += translated_char
    return translation_so_far

def translate_english_to_braille_code(english: str) -> str:
    translation_so_far = ""
    is_number = False

    for letter in english:
        if letter.isdigit():
            if not is_number:
                decimal_rep = english_to_braille_decimal_code.get('number', '')
                number_follows_braille = decimal_to_braille_binary_code(decimal_rep)
                translation_so_far += number_follows_braille
                is_number = True
        elif letter.isalpha():
            is_number = False
            if letter.isupper():
                decimal_rep = english_to_braille_decimal_code.get('capital', '')
                capital_follows_braille = decimal_to_braille_binary_code(decimal_rep)
                translation_so_far += capital_follows_braille
        if letter == ' ':
            is_number = False
            decimal_rep = english_to_braille_decimal_code.get(' ', '')
            space_follows_braille = decimal_to_braille_binary_code(decimal_rep)
            translation_so_far += space_follows_braille
        else:
            letter = letter.lower()
            decimal_rep = english_to_braille_decimal_code.get(letter, '')
            letter_braille = decimal_to_braille_binary_code(decimal_rep)
            translation_so_far += letter_braille

    return translation_so_far


def translate(input_text: str) -> str:
    if is_input_braille(input_text):
        return translate_braille_code_to_english(input_text)
    else:
        return translate_english_to_braille_code(input_text)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        input_text = ' '.join(sys.argv[1:])
        translation = translate(input_text)
        print(translation)
    else:
        print("Input string not provided")
