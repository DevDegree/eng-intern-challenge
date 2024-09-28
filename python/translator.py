import sys

englishToBrailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital': '.....O', 'num': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

brailleToEnglishDict = {v: k for k, v in englishToBrailleDict.items()}

digit_to_letter_map = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}


def english_to_braille(text):
    result = []
    number_flag = False
    for char in text:
        if char.isupper():
            result.append(englishToBrailleDict['capital'])
            char = char.lower()
        if char.isdigit() and not number_flag:
            result.append(englishToBrailleDict['num'])
            number_flag = True
        if char == ' ':
            result.append(englishToBrailleDict[' '])
            number_flag = False
        else:
            result.append(englishToBrailleDict[char])
    return ''.join(result)


def braille_to_english(braille):
    segments = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    english_chars = [brailleToEnglishDict.get(segment, '') for segment in segments]
    result = []
    number_flag = False
    capital_flag = False
    for english_char in english_chars:
        if english_char == 'num':
            number_flag = True
            continue
        elif english_char == 'capital':
            capital_flag = True
            continue
        elif english_char == ' ':
            capital_flag = False
            number_flag = False
        if number_flag:
            if english_char.isdigit():
                result.append(english_char)
                continue
            else:
                number_flag = False
        else:
            if english_char.isdigit():
                english_char = digit_to_letter_map.get(english_char)
            if capital_flag:
                result.append(english_char.upper())
                capital_flag = False
            else:
                result.append(english_char)

    return ''.join(result)


# Main function
def main():
    if len(sys.argv) < 2:
        return

    text = ' '.join(sys.argv[1:])
    if '.' in text:
        translated_text = braille_to_english(text)
    else:
        translated_text = english_to_braille(text)

    # Print the result
    print(translated_text)


if __name__ == "__main__":
    main()
