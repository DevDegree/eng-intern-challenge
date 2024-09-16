import sys

num_dict = {
    'O.....': "1",
    'O.O...': "2", 'OO....': "3", 'OO.O..': "4",
    'O..O..': "5", 'OOO...': "6", 'OOOO..': "7",
    'O.OO..': "8", '.OO...': "9", '.OOO..': "0",
    '......': " "
}
eng_dict = {
    'O.....': 'a', 'OO....': 'c', 'O.O...': 'b', 'OO.O..': 'd', 'O..O..': 'e',
    'OOOO..': 'g', 'OOO...': 'f', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'OO..O.': 'm', 'O.O.O.': 'l', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOOOO.': 'q', 'OOO.O.': 'p', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'OO..OO': 'x', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
}
inverted_num_dict = {
    '1': "O.....",
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'}
inverted_eng_dict = {
    'a': 'O.....',
    'c': 'OO....',
    'b': 'O.O...',
    'd': 'OO.O..',
    'e': 'O..O..',
    'g': 'OOOO..',
    'f': 'OOO...',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'm': 'OO..O.',
    'l': 'O.O.O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'q': 'OOOOO.',
    'p': 'OOO.O.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'x': 'OO..OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......'}


def translate_to_english(input_str):
    numberfollows = False
    capitalFollows = False
    outputstr = ''
    for i in range(0, len(input_str), 6):
        braille_letter = input_str[i:i + 6]
        if braille_letter == "......":
            outputstr += ' '
            numberfollows = False
            continue

        elif braille_letter == '.O.OOO' and not numberfollows:
            numberfollows = True
            continue

        elif braille_letter == '.O.OOO' and numberfollows:
            continue
        elif numberfollows:
            outputstr += num_dict[braille_letter]

        elif braille_letter == '.....O' and not capitalFollows:  # capital follows
            capitalFollows = True
            continue

        elif capitalFollows:
            outputstr += eng_dict[braille_letter].capitalize()
            capitalFollows = False
        else:
            outputstr += eng_dict[braille_letter]
    return outputstr


def translate_to_braille(input_str):
    outputstr = ''
    numberPrefixAdded = False
    for i in range(0, len(input_str), 1):
        eng_letter = input_str[i]
        if eng_letter.isspace():
            outputstr += '......'
            numberPrefixAdded = False
        elif eng_letter.isnumeric():
            if not numberPrefixAdded:
                outputstr += '.O.OOO'
                numberPrefixAdded = True
            outputstr += inverted_num_dict[eng_letter]
        elif eng_letter.isupper():
            outputstr += ".....O" + inverted_eng_dict[eng_letter.lower()]
        else:
            outputstr += inverted_eng_dict[eng_letter]
    return outputstr


def main():
    inputs = sys.argv[1:]
    input_str = ' '.join(inputs)
    if all(char in "O." for char in input_str):
        output = translate_to_english(input_str)
    elif all(char.isalnum() or char.isspace() for char in input_str):
        output = translate_to_braille(input_str)
    else:
        raise Exception("INVALID INPUT. ACCEPTABLE INPUT: ALPHANUMERIC (0-9; A-Z) or Braille (O and .)")

    print(output)

if __name__ == "__main__":
    main()

