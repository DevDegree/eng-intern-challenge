import sys

braille_to_english = {
    "O.....": 'a',
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": 'h',
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z"
}

braille_num_to_english = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

BRAILLE_CAPITAL = ".....O"
BRAILLE_NUMBER = ".O.OOO"
BRAILLE_SPACE = "......"


english_to_braille = {v: k for k, v in braille_to_english.items()}
english_num_to_braille = {v: k for k, v in braille_num_to_english.items()}

def is_braille(input_text):
    return input_text[0][0] in ['O', '.']

def translate_to_braille(input_text):
    text = "".join(input_text)
    result = []
    first_of_numbers = True
    for char in text:
        if char.isupper():
            result.append(BRAILLE_CAPITAL)
            char = char.lower()
            result.append(english_to_braille[char])
        elif char.isdigit():
            if first_of_numbers:
                result.append(BRAILLE_NUMBER)
                first_of_numbers = False
            result.append(english_num_to_braille[char])
        elif char == " ":
            first_of_numbers = True
            result.append(BRAILLE_SPACE)
        else:
            result.append(english_to_braille[char])
    return "".join(result)

def translate_to_english(braille):
    result = []
    braille = braille[0]
    is_capital = False
    is_number = False
    braille_text = [braille[i:i+6] for i in range(0, len(braille), 6)]
    for symbol in braille_text:
        if symbol == BRAILLE_CAPITAL:
            is_capital = True
        elif symbol == BRAILLE_NUMBER:
            is_number = True
        elif symbol == BRAILLE_SPACE:
            is_number == False
            result.append(" ")
        elif is_number:
            char = braille_num_to_english[symbol]
            result.append(char)
        elif is_capital:
            char = braille_to_english[symbol]
            char = char.upper()
            is_capital = False
            result.append(char)
        else:
         result.append(braille_to_english[symbol])
    return "".join(result)

def main():
    input_text = " ".join(sys.argv[1:])

    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))
        
if __name__ == '__main__':
    main()