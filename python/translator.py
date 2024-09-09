import sys

# Define the Braille alphabet, numbers, and other necessary symbols
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',  # space
    'cap': '.....O',  # Capitalization symbol
    'num': '.O.OOO',  # Number symbol
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

# Reverse dictionary for translation from Braille to English
english_dict_letter = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', # Special symbols
    '......': ' ',  # Space
    '.....O': 'cap',  # Capitalization symbol
    '.O.OOO': 'num'} # Number symbol  
    

    # Braille number representations (with number flag on)
english_dict_num = {'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',

    # Special symbols
    '......': ' ',  # Space
    '.....O': 'cap',  # Capitalization symbol
    '.O.OOO': 'num',  # Number symbol
}


def is_braille(text):
    """Check if the input string is in Braille (series of 'O' and '.')."""
    return all(c in 'O.' for c in text)

def translate_to_braille(text):
    """Translate English text to Braille."""
    braille_text = []
    num_flag = False  # Track if we're translating a number
    for char in text:
        if char.isdigit():
            # Add number symbol if we haven't already done so for this number sequence
            if not num_flag:
                braille_text.append(braille_dict['num'])
                num_flag = True
            braille_text.append(braille_dict[char])
        else:
            # Reset number flag after encountering a non-number character
            num_flag = False
            if char.isalpha():
                if char.isupper():
                    # Add capital symbol before the capital letter
                    braille_text.append(braille_dict['cap'])
                braille_text.append(braille_dict[char.lower()])
            elif char == ' ':
                braille_text.append(braille_dict[' '])
    return ''.join(braille_text)

def translate_to_english(braille):
    """Translate Braille text to English."""
    english_text = []
    cap_flag = False  # Track capitalization
    num_flag = False  # Track number sequences
    i = 0
    while i < len(braille):
        # Extract a Braille cell (6 characters)
        char = braille[i:i+6]
        print(i)
        print(f"Processing Braille: {char}, cap_flag: {cap_flag}, num_flag: {num_flag}")
        
        if char == braille_dict['cap']:
            cap_flag = True  # Set flag to capitalize the next letter
        elif char == braille_dict['num']:
            num_flag = True  # Set flag to treat subsequent characters as numbers
        elif char == braille_dict[' ']:
            english_text.append(' ')  # Handle spaces
            num_flag = False  # Reset the number flag when a space is encountered
        else:
            # Debugging prints to see the state of cap_flag and num_flag
            print(f"Processing Braille: {char}, cap_flag: {cap_flag}, num_flag: {num_flag}")
            
            if cap_flag:
                # Capitalize the next letter
                letter = english_dict_letter.get(char, '')
                if letter:
                    english_text.append(letter.upper())  # Capitalize the letter
                    print(english_text)
                cap_flag = False  # Reset the cap_flag after one capital letter
            elif num_flag:
                # Translate digits until space is encountered
                digit = english_dict_num.get(char, '')
                if digit and digit.isdigit():
                    english_text.append(digit)
                else:
                    num_flag = False  # Reset number flag if it's not a digit
                    letter = english_dict_num.get(char, '')
                    if letter:
                        english_text.append(letter)
            else:
                # Translate lowercase letters
                letter = english_dict_letter.get(char, '')
                if letter:
                    english_text.append(letter)
        i += 6  # Move to the next Braille cell after processing the current letter

    print(f"Final English translation: {''.join(english_text)}")  # Debugging output
    return ''.join(english_text)

def main():
    # Combine all command line arguments into a single input string
    input_text = ' '.join(sys.argv[1:])

    # Determine if input is Braille or English (if needed)
    if is_braille(input_text):
        print(translate_to_english(input_text).strip())  # Braille to English
    else:
        print(translate_to_braille(input_text).strip())  # English to Braille

if __name__ == "__main__":
    main()
