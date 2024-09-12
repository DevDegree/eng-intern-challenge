import sys

# Braille to English dictionary
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.....O': 'capital', '.O.OOO': 'number'
}

# English to Braille dictionary using the above dictionary and reverding key and value
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Number dictionary
number_trans = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
                '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}


# check whether the string input is braille or not
def is_braille(text):
    return set(text).issubset({'O', '.'}) and len(text) % 6 == 0

# translate braille into text
def braille_to_text(braille_string):
    # an empty array which lateron result will get appended to it
    result = []
    # the braille string elements will get divided in groups of 6 so each group is a character
    chunks = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    # first we assume the input is letters from a-z in lowercase unless there is a charachter indicating that a number or capital is following
    capital, number_mode = False, False

    for chunk in chunks:
        # this braille string represent captial letter is the following character
        if chunk == '.....O':
            capital = True
            # this braille string indicates that the following characters are number
        elif chunk == '.O.OOO':
            number_mode = True
            # if the number_mode variable is trigered then we will use number dictionary to translate braille to numbers
        elif number_mode:
            result.append(next((k for k, v in number_trans.items() if v == chunk), '?'))
            # set the number_mode to false again so for each character it follows the same process
            number_mode = False
    return ''.join(result).replace('?', '')

def text_to_braille(text_string):
    # an empty array which lateron result will get appended to it
    result = []
    number_mode = False

    for char in text_string:
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille['number'])
                number_mode = True
            result.append(number_trans[char])
        else:
            number_mode = False
            if char.isupper():
                result.append(english_to_braille['capital'])
                char = char.lower()
            result.append(english_to_braille.get(char, '......'))

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_text(input_string), end='')
    else:
        print(text_to_braille(input_string), end='')

if __name__ == "__main__":
    main()
