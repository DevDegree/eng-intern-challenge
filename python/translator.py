import sys

def main():
    if len(sys.argv) < 2:
        print("Pass English or Braille")
        sys.exit(1)

    original = ""
    for arg in sys.argv[1:]:
        original += arg + " "

    # Remove the trailing space
    original = original.strip()

    # Convert to entry to list of char
    char_array = list(original)

    if char_array[0].isdigit() or char_array[0].isalpha():
        print(word_to_braille(char_array))
    else: print(braille_to_word(original))

def word_to_braille(char_array): # converts english to braille
    english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..' }
    # Special symbols
    braille_capital = '.....O'
    braille_number = '.O.OOO'

    result = ''
    in_number_sequence = False

    for char in char_array:
        if char.isupper():
            result += braille_capital
            char = char.lower()
        
        if char.isdigit():
            if not in_number_sequence:
                result += braille_number
                in_number_sequence = True
            result += english_to_braille.get(char, '')
        else:
            in_number_sequence = False
            result += english_to_braille.get(char, '')
    
    return result



def braille_to_word(original): # coverts braille to english
    braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z', '......': ' '}
    
    # Special symbols
    braille_capital = '.....O'
    braille_number = '.O.OOO'

    result = ''
    i = 0
    length = len(original)
    in_number_sequence = False
    in_capital_sequence = False
    
    while i < length:
        # Extract the next 6-character substring
        braille_char = original[i:i+6]
        # capital 
        if braille_char == braille_capital:
            in_capital_sequence = True
            i += 6
            continue
        # number
        if braille_char == braille_number:
            in_number_sequence = True
            i += 6
            continue
        
        if braille_char in braille_to_english:
            char = braille_to_english[braille_char]
            
            if in_number_sequence:
                # Convert letters 'a' to 'j' into digits '1' to '0'
                if char == 'a':
                    result += '1'
                elif char == 'b':
                    result += '2'
                elif char == 'c':
                    result += '3'
                elif char == 'd':
                    result += '4'
                elif char == 'e':
                    result += '5'
                elif char == 'f':
                    result += '6'
                elif char == 'g':
                    result += '7'
                elif char == 'h':
                    result += '8'
                elif char == 'i':
                    result += '9'
                elif char == 'j':
                    result += '0'
                
            else:
                if in_capital_sequence:
                    result += char.upper()  # Capitalize the character
                    in_capital_sequence = False  # Reset capital sequence flag
                else:
                    result += char
        i += 6

    return result

if __name__ == "__main__":
    main()


