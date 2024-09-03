import sys

# Mapping braille combinations to alphabet characters and spaces
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

# Constants
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
# Reverse BRAILLE_TO_ENGLISH to get mapping in other direction
ENGLISH_TO_BRAILLE = {val: key for key, val in BRAILLE_TO_ENGLISH.items()}

def english_to_braille(english):
    result = []
    # We use this boolean flag to track if track we're dealing with a number in our English set of words
    # This is needed, as the first 10 lower case letters and numbers share braille combinations
    number_flag = False

    for char in english:
        # If we encounter a numerical digit
        if char.isdigit():
            if not number_flag:
                result.append(NUMBER_FOLLOWS)
                number_flag = True
            # We use an ASCII table to convert a given digit to its corresponding letter
            # ASCII decimal code for 'a' is 97, so we use an offset of 96
            # 'j' and '0' is a special case
            letter = 'j' if char == '0' else chr(int(char) + 96)
            result.append(ENGLISH_TO_BRAILLE[letter])
        # If we encounter a space character
        elif char == ' ':
            if number_flag:
                number_flag = False
            result.append(ENGLISH_TO_BRAILLE[' '])
        # If we encounter a letter
        else:
            if char.isupper():
                result.append(CAPITAL_FOLLOWS)
                char = char.lower()      
            result.append(ENGLISH_TO_BRAILLE[char])

    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    # We use a capital boolean flag since lowercase and uppercase for the same letter shares 
    # the same braille combination. We use a number boolean flag for the same reason described previously.
    number_flag = False
    capital_flag = False

    while i < len(braille):
        combination = braille[i:i+6]
        # If we encounter a 'number follows' combination
        if combination == NUMBER_FOLLOWS:
            number_flag = True
        # If we encounter a 'capital follows' combination
        elif combination == CAPITAL_FOLLOWS:
            capital_flag = True
        # We encounter a space, digit or letter combination
        else:
            char = BRAILLE_TO_ENGLISH[combination]
            if char == ' ':
                number_flag = False
            elif capital_flag:
                char = char.upper()
                capital_flag = False
            elif number_flag:
                # We use an ASCII table to convert a given letter to its corresponding digit
                # ASCII decimal code for 'a' is 97, so we use an offset of 96
                # 'j' and '0' is a special case
                if 97 <= ord(char) and ord(char) <= 106:
                    char = '0' if ord(char) == 106 else str(ord(char) - 96)
            result.append(char)
        i += 6

    return ''.join(result)

if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    # All valid, non-empty braille strings must have a '.' character
    if '.' in input_string: 
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))
