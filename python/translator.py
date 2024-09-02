import textwrap
import sys

braille_dict = {
    "O....." : 'a',
    "O.O..." : 'b',
    "OO...." : 'c',
    "OO.O.." : 'd',
    "O..O.." : 'e',
    "OOO..." : 'f',
    "OOOO.." : 'g',
    "O.OO.." : 'h',
    ".O.O.." : 'i',
    ".OO..." : 'j',
    "O...O." : 'k',
    "O.O.O." : 'l',
    "OO..O." : 'm',
    "OO.OO." : 'n',
    "O..OO." : 'o',
    "OOO.O." : 'p',
    "OOOOO." : 'q',
    "O.OOO." : 'r',
    ".O.OO." : 's',
    ".OOO.." : 't',
    "O...OO" : 'u',
    "O.O.OO" : 'v',
    ".OOO.O" : 'w',
    "OO..OO" : 'x',
    "OO.OOO" : 'y',
    "O..OOO" : 'z',
    "......" : ' '
}
braille_decimal = {
    "..OO.O" : '.',
    "..O..." : ',',
    "..O.OO" : '?',
    "..OOO." : '!',
    "..OO.." : ':',
    "..O.O." : ';',
    "....OO" : '-',
    ".O..O." : '/',
    ".OO..O" : '<',
    "O..OO." : '>',
    "O.O..O" : '(',
    ".O.OO." : ')',
}
braille_numbers = {
    "O....." : '1',
    "O.O..." : '2',
    "OO...." : '3',
    "OO.O.." : '4',
    "O..O.." : '5',
    "OOO..." : '6',
    "OOOO.." : '7',
    "O.OO.." : '8',
    ".O.O.." : '9',
    ".OO..." : '0',
}
braille_special = {
    ".....O" : 'capital',
    ".O...O" : 'decimal',
    ".O.OOO" : 'number'
}

def split_string(s):
    return textwrap.wrap(s, 6)

def translate_to_english(braille):
    words = split_string(braille)
    text = []
    capital = False
    number = False
    decimal = False

    for word in words:
        if word in braille_special:
            if braille_special[word] == 'capital':
                capital = True
            if braille_special[word] == 'number':
                number = True
            if braille_special[word] == 'decimal':
                decimal = True
            continue

        if word in braille_dict:
            if number:
                char = braille_numbers[word]
                if char == ' ':
                    number = False
                    text.append(char)
                else:
                    text.append(char)
            elif decimal:
                char = braille_decimal[word]
                text.append(char)
                decimal = False
            else:
                char = braille_dict[word]
                if capital:
                    text.append(char.upper())
                    capital = False
                else:
                    text.append(char)
    return ''.join(text)
def translate_to_braille(english):
    braille = []
    number = False

    for char in english:
        if char == ' ' and number:
            number = False

        if char.isupper():
            braille.append(".....O")
            char = char.lower()

        if char in braille_dict.values():
            for key, value in braille_dict.items():
                if value == char:
                    braille.append(key)

        elif char in braille_decimal.values():
            for key, value in braille_decimal.items():
                if value == char:
                    braille.append(key)

        elif char in braille_numbers.values():
            if not number:
                braille.append(".O.OOO")
                number = True
            for key, value in braille_numbers.items():
                if value == char:
                    braille.append(key)

        elif char in braille_special.values():
            for key, value in braille_special.items():
                if value == char:
                    braille.append(key)
    return ''.join(braille)

if __name__ == "__main__":
    # input text in terminal
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        if set(text).issubset({'O', '.', ' '}):
            english = translate_to_english(text)
            print(english)
        else:
            braille = translate_to_braille(text)
            print(braille)
