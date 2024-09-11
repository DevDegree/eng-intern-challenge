import sys

# Indicator for a number
isnumber = '.O.OOO'
# Indicator for a capital letter
iscapital = '.....O'
# Contains the braille translation to letters and numbers
braille_translations = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'
}
braille_translations_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


# Function to determine if the arguments are braille or english
def is_braille(word):
    # if any of the characters contain an english letter, number, or space, then it can't be braille
    for char in word:
        if char != 'O' and char != '.':
            return False
    return True


def braille_to_english(words):
    # For easier lookup, reverse the braille_translations dictionary
    reversed_lookup = {v: k for k, v in braille_translations.items()}
    reversed_lookup_numbers = {v: k for k, v in braille_translations_numbers.items()}
    result = ""
    add_a_digit = False
    make_capital = False
    for i in range(0,len(words), 6):
        # Grab a character
        char = words[i:i+6]

        # We can ignore the indicators 
        if char == isnumber:
            add_a_digit = True
            continue
        if char == iscapital:
            make_capital = True
            continue
        if reversed_lookup[char] == ' ':
                add_a_digit = False
        if add_a_digit == True:
            
            result += reversed_lookup_numbers[char]
        elif char in reversed_lookup:
            if make_capital == True:
                result += reversed_lookup[char].upper()
                make_capital = False
            else:
                result += reversed_lookup[char]
    return result


def english_to_braille(words):
    result = ""
    # Flag that controls the amount of number indicators to add (once per series of digits)
    add_number_indicator = False
    for char in words:
        if char.isdigit():
            if add_number_indicator == False:
                result += isnumber
                add_number_indicator = True
            result += braille_translations_numbers[char]
        elif char == ' ':
            add_number_indicator = False
            result += braille_translations[char]
        elif char.isalpha():
            if char.isupper():
                result += iscapital
            result += braille_translations[char.lower()]
    return result


def main():
    # No words provided, return
    if len(sys.argv) < 2:
        return
    # Remove first argument (filename) from the list of command line arguments
    argumentList = ' '.join(sys.argv[1:])
    # Determine if we need to translate to or from braille
    print(braille_to_english(argumentList)) if is_braille(argumentList[0]) else print(english_to_braille(argumentList))

if __name__ == "__main__":
    main()