
import sys

# Braille dictionary to help translate English into Braille
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    'capital': '.....O', 'number': '.O.OOO'
}

# reverse Braille dictionaries to help Braille into English translations
# reverse_braille_chars is for characters aside from numbers
reverse_braille_chars = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<',
    'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')', '.....O': 'capital',
    '.O.OOO': 'number'
}

# reverse_braille_nums is for numbers
reverse_braille_nums = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# list of the braille numbers
braille_nums = ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..',
    'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..']

# function to translate English to Braille
def translate_to_braille(text):
    braille_output = []
    # boolean for whether the current character is part of a number
    part_of_num = False
    for char in text:
        # case when character is uppercase
        if char.isupper():
            if part_of_num:
                part_of_num = False
            braille_output.append(braille_dict['capital'])
            braille_output.append(braille_dict[char.lower()])
        # case when character is a digit
        elif char.isdigit():
            # 
            if not part_of_num:
                braille_output.append(braille_dict['number'])
                part_of_num = True
            braille_output.append(braille_dict[char])
        # case when character is a lower case letter or special character
        else:
            part_of_num = False
            braille_output.append(braille_dict[char])
    # return the answer as one string
    return ''.join(braille_output)

# function to translate Braille to English
def translate_to_english(braille_text):
    english_output = []
    i = 0
    while i < len(braille_text):
        # case for an incoming capital letter
        if braille_text[i:i+6] == braille_dict['capital']:
            english_output.append(reverse_braille_chars[braille_text[i+6:i+12]].upper())
            i += 12
        # case for an incoming number
        elif braille_text[i:i+6] == braille_dict['number']:
            # skip the current number indicator
            i += 6
            # loop through the text to get the remaining digits of the number
            while i < len(braille_text) and braille_text[i:i+6] in braille_nums:
                english_output.append(reverse_braille_nums[braille_text[i:i+6]])
                i += 6
        # case for neither a capital character or number
        else:
            # we know it's definitely not a number so we get it from the reverse_braille_chars dictionary
            english_output.append(reverse_braille_chars[braille_text[i:i+6]])
            i += 6
    # return the answer as one string
    return ''.join(english_output)

# Detect if the string is Braille or English
def is_braille(text):
    for char in text:
        if char != 'O' and char != '.':
            return False
    return True

# main function to run the translator
def main():
    # double check the input was valid length
    if len(sys.argv) < 2:
        print("Invalid input. Please provide a text.")
        return

    # get the system input
    input_text = ' '.join(sys.argv[1:])

    # if input is in Braille use the translate to English function
    if is_braille(input_text):
        result = translate_to_english(input_text)
    # if input is in English use the translate to Braille function
    else:
        result = translate_to_braille(input_text)
    # finally display results
    print(result)

if __name__ == "__main__":
    main()
