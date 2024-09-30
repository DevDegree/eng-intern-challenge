import sys

# Braille to English mappings
BRAILLE_TO_ENGLISH = {
    '......': ' ',    # space
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'CAPITAL',    # special symbol for capital letters
    '.O.OOO': 'NUMBER'      # special symbol for numbers
}

# Reverse mapping for English to Braille
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# Check if the input string is in valid Braille format
def is_braille(text):
    return all(char in '.O' for char in text) and len(text) % 6 == 0

# Convert Braille text to English
def braille_to_english(braille_text):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille_text):
        symbol = braille_text[i:i+6]
        
        if symbol == ENGLISH_TO_BRAILLE['CAPITAL']:
            capitalize_next = True
        elif symbol == ENGLISH_TO_BRAILLE['NUMBER']:
            number_mode = True
        else:
            char = BRAILLE_TO_ENGLISH.get(symbol, '')
            if number_mode and char.isalpha():
                # In Braille, letters are used for digits 1-9 and 0
                char = str('0123456789'.index(char))
            elif capitalize_next:
                char = char.upper()
                capitalize_next = False
            
            if char == ' ':
                number_mode = False  # Reset number mode after space
            
            result.append(char)
        
        i += 6

    return ''.join(result)

# Convert English text to Braille
def english_to_braille(english_text):
    result = []
    number_mode = False

    for char in english_text:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['NUMBER'])
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE['jabcdefghi'[int(char)]])  # Braille uses 'j' to 'i' for numbers
        elif char.isspace():
            result.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
        else:
            if number_mode:
                number_mode = False  # Exit number mode if not a digit
            
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['CAPITAL'])
                char = char.lower()
            
            result.append(ENGLISH_TO_BRAILLE.get(char, ''))

    return ''.join(result)

# Main function that handles input and determines translation direction
def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        result = braille_to_english(input_text)
        print("\nBraille to English Translation:")
    else:
        result = english_to_braille(input_text)
        print("\nEnglish to Braille Translation:")
    
    print(result)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
