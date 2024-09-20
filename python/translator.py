import argparse
import re


def translate(string):
    english_pattern = r"^(?!O)[A-Za-z0-9]"
    float_pattern = r'[-+]?\d*\.\d+'
    braille_alphabet_and_special_characters = {
        "A": "O.....",
        "B": "O.O...",
        "C": "OO....",
        "D": "OO.O..",
        "E": "O..O..",
        "F": "OOO...",
        "G": "OOOO..",
        "H": "O.OO..",
        "I": ".OO...",
        "J": ".OOO..",
        "K": "O...O.",
        "L": "O.O.O.",
        "M": "OO..O.",
        "N": "OO.OO.",
        "O": "O..OO.",
        "P": "OOO.O.",
        "Q": "OOOOO.",
        "R": "O.OOO.",
        "S": ".OO.O.",
        "T": ".OOOO.",
        "U": "O...OO",
        "V": "O.O.OO",
        "W": ".OOO.O",
        "X": "OO..OO",
        "Y": "OO.OOO",
        "Z": "O..OOO",
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "0": ".OOO..",
        ".": "..OO.O",
        ",": "..O...",
        "?": "..O.OO",
        "!": "..OOO.",
        ":": "..OO..",
        ";": "..O.O.",
        "-": "..O..O",
        "/": "..O..O",
        "<": ".O.O..",
        ">": ".O..O.",
        "(": ".O..OO",
        ")": ".O.OO.",
        "capital follows": ".....O",
        "decimal follows": ".O...O",  # Corrected representation
        "number follows": ".O.OOO",
        " ": "......"
    }
    res = ""
    to_continue = 0
    number_flag = 0
    decimal_flag = 0
    match = re.search(float_pattern, string)
    position = match.start() if match else len(string)
    braille_to_english = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
        '..OO..': ':', '..O.O.': ';', '..O..O': '/', '.O.O..': '<', '.O..O.': '>',
        '.O..OO': '(', '.O.OO.': ')', '.....O': 'capital follows', '.O...O': 'decimal follows',
        '.O.OOO': 'number follows', '......': 'space'
    }
    if re.match(english_pattern, string):
        for index, value in enumerate(string):
            if value.isalpha() and value.isupper():
                res += braille_alphabet_and_special_characters['capital follows']
                res += braille_alphabet_and_special_characters[value]
            elif value.isalpha() and value.islower():
                value = value.upper()
                res += braille_alphabet_and_special_characters[value]
            elif ord(value) in range(48, 58) and not match:
                res += braille_alphabet_and_special_characters['number follows']
                res += braille_alphabet_and_special_characters[value]
                to_continue = index + 1
                number_flag = 1
                break
            elif value.isspace():
                res += braille_alphabet_and_special_characters[' ']
        while to_continue < len(string) and number_flag == 1:  # there could be letters after an integer
            if string[to_continue].isdigit():
                res += braille_alphabet_and_special_characters[string[to_continue]]
            elif string[to_continue].isupper():
                res += braille_alphabet_and_special_characters['capital follows']
                res += braille_alphabet_and_special_characters[string[to_continue]]
            elif string[to_continue].isspace():
                res += braille_alphabet_and_special_characters[' ']
            elif string[to_continue].isalpha() and string[to_continue].islower():
                value = string[to_continue].upper()
                res += braille_alphabet_and_special_characters[value]
            to_continue += 1
        while match and position < len(string):
            if decimal_flag == 0:
                res += braille_alphabet_and_special_characters['decimal follows']
            if string[position] != '.':
                res += braille_alphabet_and_special_characters[string[position]]
            position += 1
            decimal_flag = 1
        return res
    else:  # input length will be multiples of 6 , coz braille is a 6-character script
        res = ""
        capital_flag = False
        number_flag = False
        decimal_flag = False

        for i in range(0, len(string), 6):
            braille_character = string[i:i + 6]
            english_char = braille_to_english[braille_character]

            if english_char == "capital follows":
                capital_flag = True
                continue

            elif english_char == "number follows":
                number_flag = True
                continue

            elif english_char == "space":  # reset all flags for potential new type of word
                capital_flag = False
                number_flag = False
                decimal_flag = False
                res += " "
                continue

            elif english_char == "decimal follows":
                decimal_flag = True
                continue

            elif decimal_flag:
                res += braille_to_english[braille_character]
                res += '.'
                decimal_flag = False

            elif number_flag:
                number_map = {'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
                              'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'}
                if braille_character in number_map:
                    res += number_map[braille_character]
                else:
                    res += braille_to_english[braille_character]

            elif capital_flag:
                res += braille_to_english[braille_character].upper()
                capital_flag = False
            else:
                res += english_char

        return res


def main():
    parser = argparse.ArgumentParser(description="English To Braille and Vice-Versa")
    parser.add_argument("input", help="Input String", nargs='+')
    args_obj = parser.parse_args()
    result = translate(' '.join(args_obj.input))
    print(result)


if __name__ == "__main__":
    main()
