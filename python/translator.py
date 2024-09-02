import sys

# Braille mappings 
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-':'....OO', '/': '.O..O.', '<':'.OO..O', '>':'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.'
}

# Reverse mapping for Braille to English
english_dict = {}
for k,v in braille_dict.items():
    if v not in english_dict:
        english_dict[v] = [k]
    else:
        english_dict[v].append(k) 

# Special Braille prefixes
number_follows = '.O.OOO'    # Number follows 
capital_follows = '.....O'    # Capital follows 

def is_braille(text):
    # Check if input text is Braille 
    return all(c in 'O.' for c in text) and len(text)%6 == 0

def braille_to_english(braille):
    # Split input into groups of 6 for each Braille character
   
    result = []
    is_number = False
    i = 0

    while i < len(braille):
        char = braille[i:i+6]

        if char == capital_follows:
            # Apply capitalization to the next character
            i += 6
            next_char = braille[i:i+6]
            possible_translations = english_dict[next_char]
            if not possible_translations[0].isdigit():
                num = 0
            else:
                num = 1
            result.append(english_dict[next_char][1-num].upper() if is_number else english_dict[next_char][num].upper())
            
        elif char == number_follows:
            # Enter number mode
            is_number = True
        else:
            # Append character normally
            possible_translations = english_dict[char]
            if possible_translations[0].isdigit():
                num = 0
            else:
                num = 1
            result.append(english_dict[char][num] if is_number else english_dict[char][1-num])
            if char == '......':
                is_number = False
        
        i += 6

    return ''.join(result).strip()

def english_to_braille(english):
    result = []
    is_number = False
    for char in english:
        if char.isdigit():
            if not is_number:
                result.append(number_follows)
            is_number = True
            result.append(braille_dict[char])
        elif char.isalpha() and char.isupper():
            if is_number:
                result.append('......')
            result.append(capital_follows)
            result.append(braille_dict[char.lower()])
        else:
            if is_number:
                result.append('......')
                is_number = False
            result.append(braille_dict[char])

    return ''.join(result)

def main():
    # Get input from the command line
    if len(sys.argv) < 2:
        print("Usage: python translator.py <braille/english text>")
        return

    results = []
    for arg in sys.argv[1:]:
        if is_braille(arg):
            results.append(braille_to_english(arg))
        else:
            results.append(english_to_braille(arg))

    # Join results with a Braille space separator
    output = '......'.join(results)
    print(output)

if __name__ == "__main__":
    main()
