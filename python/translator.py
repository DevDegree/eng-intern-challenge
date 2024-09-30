# Name: Mihir Gediya 
# #Email ID: mihirgediya2001@gmail.com


# Here, to avoid confusion in braille code between 'o' and '.',
# I will use numbers flag when there is special character
import sys

# Braille to English translation function
def braille_to_english(braille_str):
    result = []
    flags = {'capital': False, 'decimal': False, 'number': False}

    # Split the input into chunks of 6 (each braille character is 6 dots)
    chunks = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]

    for chunk in chunks:
        if chunk in braille_flags:
            # Set the appropriate flag based on the chunk
            flag = braille_flags[chunk]
            flags[flag] = True
        elif chunk == "......":
            result.append(" ")
            flags['number'] = False  # Reset number flag after space
        else:
            # If number flag is set, use digits
            if flags['number']:
                result.append(braille_number_map.get(chunk, ""))
                result.append(braille_specials_reverse.get(chunk, ""))
            elif flags['decimal']:
                result.append(braille_specials_reverse.get(chunk, ""))
            else:
                # If capital flag is set, use uppercase characters
                ch = braille_char_map.get(chunk, "")
                result.append(ch.upper() if flags['capital'] else ch)
            
            # Reset the capital flag after using it once
            flags['capital'] = False

    print("".join(result))

# English to Braille translation function
def english_to_braille(english_str):
    result = []
    last_number = False
    specials = {',', '.', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')'}

    for ch in english_str:
        if 'A' <= ch <= 'Z':
            result.append(braille_flags_reverse['capital'])
            result.append(braille_char_map_reverse[ch.lower()])
            last_number = False
        elif 'a' <= ch <= 'z':
            result.append(braille_char_map_reverse[ch])
            last_number = False
        elif ch == " ":
            result.append("......")
            last_number = False
        elif '0' <= ch <= '9':
            if not last_number:
                result.append(braille_flags_reverse['number'])
            last_number = True
            result.append(braille_number_map_reverse[ch])
        elif ch == '.':
            result.append(braille_flags_reverse['decimal'])
            result.append(braille_specials[ch])
            last_number = True
        elif ch in specials:
            if not last_number:
                result.append(braille_flags_reverse['number'])
            result.append(braille_specials[ch])
            last_number = True


    print("".join(result))


# Braille mappings
braille_char_map = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z'
}

braille_number_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

braille_flags = {
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number'
}

braille_specials = {
    ',': '..O...', '.': '..OO.O', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

# Reverse mappings for English to Braille conversion
braille_char_map_reverse = {v: k for k, v in braille_char_map.items()}
braille_number_map_reverse = {v: k for k, v in braille_number_map.items()}
braille_flags_reverse = {v: k for k, v in braille_flags.items()}
braille_specials_reverse = {v: k for k, v in braille_specials.items()}

# Read command-line arguments
if len(sys.argv) <= 1:
    print("Invalid number of arguments passed")
    sys.exit()

input_str = " ".join(sys.argv[1:])
if len(input_str) % 6 == 0 and set(input_str).issubset({'O', '.'}):
    braille_to_english(input_str)
else:
    english_to_braille(input_str)
