import sys

TRANSLATION = [
    ('a', 'O.....'),
    ('b', 'O.O...'),
    ('c', 'OO....'),
    ('d', 'OO.O..'),
    ('e', 'O..O..'),
    ('f', 'OOO...'),
    ('g', 'OOOO..'),
    ('h', 'O.OO..'),
    ('i', '.OO...'),
    ('j', '.OOO..'),
    ('k', 'O...O.'),
    ('l', 'O.O.O.'),
    ('m', 'OO..O.'),
    ('n', 'OO.OO.'),
    ('o', 'O..OO.'),
    ('p', 'OOO.O.'),
    ('q', 'OOOOO.'),
    ('r', 'O.OOO.'),
    ('s', '.OO.O.'),
    ('t', '.OOOO.'),
    ('u', 'O...OO'),
    ('v', 'O.O.OO'),
    ('w', '.OOO.O'),
    ('x', 'OO..OO'),
    ('y', 'OO.OOO'),
    ('z', 'O..OOO'),
    ('1', 'O.....'),
    ('2', 'O.O...'),
    ('3', 'OO....'),
    ('4', 'OO.O..'),
    ('5', 'O..O..'),
    ('6', 'OOO...'),
    ('7', 'OOOO..'),
    ('8', 'O.OO..'),
    ('9', '.OO...'),
    ('0', '.OOO..'),
    ('-1', '.....O'), # capital follows
    ('-2', '.O...O'), # decimal follows
    ('-3', '.O.OOO'), # number follows
    ('.', '..OO.O'),
    (',', '..O...'),
    ('?', '..O.OO'),
    ('!', '..OOO.'),
    (':', '..OO..'),
    (';', '..O.O.'),
    ('-', '....OO'),
    ('/', '.O..O.'),
    ('<', '.OO..O'),
    ('>', 'O..OO.'),
    ('(', 'O.O..O'),
    (')', '.O.OO.'),
    (' ', '......')
]


def is_braille(str: str) -> bool:
    for c in str:
        if c != 'O' and c != '.' and c != ' ':
            return False
    return True


def braille_to_eng(str: str, cap: bool, number: bool) -> str:
    if number:
        for i in range(26, 36):
            if TRANSLATION[i][1] == str:
                return TRANSLATION[i][0]
    for i in range(len(TRANSLATION)):
        if TRANSLATION[i][1] == str:
            if i < 26 and cap:
                return TRANSLATION[i][0].upper()
            return TRANSLATION[i][0]
    return 'Invalid Input'


def eng_to_braille(str: str) -> str:
    for i in range(len(TRANSLATION)):
        if TRANSLATION[i][0] == str:
            return TRANSLATION[i][1]
    return ''


def translate_brailles(input: str) -> str:
    input = input.replace(' ', '')
    if len(input) % 6 != 0:
        return "Invalid input"

    cap: bool = False
    is_number: bool = False
    answer: str = ""

    for i in range(0, len(input), 6):
        braille: str = input[i:i+6]
        eng_char: str = braille_to_eng(braille, cap, is_number)
        if cap:
            cap = False
        if eng_char == '-1': # capital follows
            cap = True
        elif eng_char == '-2': # decimal follows
            if is_number:
                answer += '.'
        elif eng_char == '-3': # number follows
            is_number = True
        elif eng_char == 'Invalid Input':
            return "Invalid input"
        elif eng_char == ' ':
            answer += ' '
            is_number = False
        else:
            answer += eng_char
    return answer


def translate_eng(input: str) -> str:
    answer: str = ""
    is_number: bool = False

    for i in input:
        if i.isalpha():
            is_number = False
            if i.isupper():
                answer += '.....O'
            answer += eng_to_braille(i.lower())
        elif i.isdigit():
            if not is_number:
                is_number = True
                answer += '.O.OOO'
            answer += eng_to_braille(i)
        elif i == '.' and is_number:
            answer += '.O...O'
        else:
            is_number = False
            answer += eng_to_braille(i)
    return answer


def main():
    args = sys.argv[1:]
    str_arg: str = " ".join(args)
    if is_braille(str_arg):
        print(translate_brailles(str_arg))
    else:
        print(translate_eng(str_arg))

if __name__ == "__main__":
    main()