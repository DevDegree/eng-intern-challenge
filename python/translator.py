import sys


BRAILLE_LENGTH = 6


def is_braille(s):
    s_no_space = s.replace(' ', '')
    return all(c in 'O.' for c in s_no_space) and not len(s_no_space) % BRAILLE_LENGTH


def translate_to_english(s, letter_mapping, number_mapping, special_mapping):
    answer = ""
    is_capital = False
    is_number = False
    for i in range(0, len(s), BRAILLE_LENGTH):
        braille_letter = s[i:i+BRAILLE_LENGTH]
        cur_letter = ""
        if braille_letter in special_mapping.values():
            if braille_letter == special_mapping['capital']:
                is_capital = True
            elif braille_letter == special_mapping['number']:
                is_number = True
            else:
                is_number = False
                cur_letter = ' '
        elif is_number:
            if braille_letter in number_mapping:
                cur_letter = number_mapping[braille_letter]
        elif braille_letter in letter_mapping:
            if is_capital:
                cur_letter = letter_mapping[braille_letter].upper()
                is_capital = False
            else:
                cur_letter = letter_mapping[braille_letter]
        else:
            return "There's an invalid Braille letter"
        answer += cur_letter
    return answer


def translate_to_braille(s, letter_mapping, number_mapping, special_mapping):
    ans = ""
    is_number = False
    for c in s:
        if c == ' ':
            ans += special_mapping['space']
            if is_number:
                is_number = False
        elif c.isalpha():
            if c.isupper():
                ans += special_mapping['capital']
                ans += letter_mapping[c.lower()]
            else:
                ans += letter_mapping[c]
        elif c.isnumeric():
            if not is_number:
                ans += special_mapping['number']
                is_number = True
            ans += number_mapping[c]
    return ans


def main():
    input_string = ' '.join(sys.argv[1:])
    output = ""

    braille_letter_mapping = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
        'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
        'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
        '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
        'OO.OOO': 'y', 'O..OOO': 'z',
    }

    braille_number_mapping = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    }

    english_letter_mapping = {value: key for key, value in braille_letter_mapping.items()}
    english_number_mapping = {value: key for key, value in braille_number_mapping.items()}

    special_mapping = {
        'space': '......', 'capital': '.....O', 'number': '.O.OOO'
    }

    if is_braille(input_string):
        output = translate_to_english(input_string, braille_letter_mapping, braille_number_mapping, special_mapping)
    else:
        output = translate_to_braille(input_string, english_letter_mapping, english_number_mapping, special_mapping)

    print(output)


if __name__ == '__main__':
    main()