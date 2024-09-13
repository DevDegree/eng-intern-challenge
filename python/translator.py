import sys

# Storing Braille to English characters
BR_to_EN_mapping = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i',
    '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', '.....O': 'cap',
    '.O.OOO': 'num', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', 
    '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')', '......': ' '
}

# Storing English to Braille characters
EN_to_BR_mapping = {x: y for y, x in BR_to_EN_mapping.items()}

# Function to check if the input string is in Braille
def is_braille(s: str) -> bool:
    accepted = {'O', '.'}
    for c in s:
        if not c in accepted:
            return False
    return True

# Function to convert Braille to English
def braille_to_english(s: str) -> str:
    is_cap = False
    is_num = False

    output = []

    # Splitting the input string into Braille segments
    braille_chars = [s[i:i+6] for i in range(0, len(s), 6)]

    for char in braille_chars:
        if (BR_to_EN_mapping[char] == 'cap'):
            is_cap = True
        elif (BR_to_EN_mapping[char] == 'num'):
            is_num = True
        elif (BR_to_EN_mapping[char] == ' '):
            output.append(' ')
            is_num = False

        if (is_cap):
            output.append(BR_to_EN_mapping[char].upper())
            is_cap = False
        elif (is_num):
            output.append(BR_to_EN_mapping[char]-38)
            is_num = False

        return ''.join(output)

# Function to convert English to Braille
def english_to_braille(s: str) -> str:
    is_num = False

    output = []

    for char in s:
        if (char.isupper()):
            output.append(EN_to_BR_mapping['cap'])
            output.append(EN_to_BR_mapping[char.lower()])
        elif (char.isdigit()):
            if (not is_num):
                output.append(EN_to_BR_mapping['num'])
                is_num = True
            output.append(EN_to_BR_mapping[chr(int(char)+96)])
        else:
            if (is_num):
                is_num = False
            output.append(EN_to_BR_mapping[char])
    return ''.join(output)

if __name__ == '__main__':
    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(braille_to_english(input_str), end='')
    else:
        print(english_to_braille(input_str), end='')
