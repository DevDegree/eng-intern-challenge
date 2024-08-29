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
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    ' ': '......'
}   


# Function to determine if the arguments are braille or english
def is_braille(word):
    for char in word:
        if char != 'O' and char != '.':
            return False
    return True


def braille_to_english(words):
    return


def english_to_braille(words):
    result = ""
    add_number_indicator = False
    for char in words:
        if char.isdigit():
            if add_number_indicator == False:
                result += isnumber
                add_number_indicator = True
            result += braille_translations[char]
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

main()


