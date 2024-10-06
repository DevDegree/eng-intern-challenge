# Shopify - eng-inter-challenge
# Braille Translator
# Author: Eldin Bautista
# Description: Translates English text to Braille and vice versa

# Braille Alphabet Dictionary
braille_alphabet_dict = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 
    'z': "O..OOO"
}

# Braille Number Dictionary
braille_number_dict = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
}

# Braille Symbols Dictionary
braille_symbol_dict = {
    ' ': "......",    # Space
    '.': "..OO.O",    
    ',': "..O...",    
    '?': "..O.OO",    
    '!': "..OOO.",    
    ':': "..OO..",    
    ';': "..O.O.",    
    '-': "....OO",    
    '/': ".O..O.",    
    '<': ".OO..O",    
    '>': "O..OO.",    
    '(': "O.O..O",    
    ')': ".O.OO",     
    '*': ".....O",    # Capital follows
    '&': ".O...O",    # Decimal follows
    '#': ".O.OOO"     # Number follows
}

# Translate English to Braille
def translate_to_braille(english_text):
    braille_translation = []
    number_mode = False
    
    for char in english_text:
        if char.isdigit():  # Handle numbers
            if not number_mode:
                braille_translation.append(braille_symbol_dict['#'])  # Activate number mode
                number_mode = True
            braille_translation.append(braille_number_dict[char])
        elif char.isalpha():  # Handle alphabet
            if char.isupper():  # Handle capital letters
                braille_translation.append(braille_symbol_dict['*'])  # Capital follows
                braille_translation.append(braille_alphabet_dict[char.lower()])
            else:
                braille_translation.append(braille_alphabet_dict[char])
            number_mode = False  # Exit number mode after letters
        elif char in braille_symbol_dict:  # Handle punctuation and space
            braille_translation.append(braille_symbol_dict[char])
            if char == ' ':  # Reset number mode after a space
                number_mode = False
        else:
            braille_translation.append('?')  # Handle unknown characters

    return "".join(braille_translation)

# Translate Braille to English
def translate_to_english(braille_text):
    english_translation = []
    number_mode = False
    capital_mode = False
    i = 0

    while i < len(braille_text):
        symbol = braille_text[i:i + 6]

        if symbol == braille_symbol_dict['#']:  # Number follows
            number_mode = True  # Enter number mode
            i += 6
            continue

        elif symbol == braille_symbol_dict['*']:  # Capital follows
            capital_mode = True #Enter capital mode
            i += 6
            continue

        if symbol == braille_symbol_dict[' ']:  # Handle space
            english_translation.append(' ')  # Add a space to the English translation
            number_mode = False  # Exit number mode after a space
            i += 6
            continue

        if number_mode:
            # Check if the symbol is valid for numbers
            digit_symbol = next((key for key, value in braille_number_dict.items() if value == symbol), None)
            if digit_symbol:
                english_translation.append(digit_symbol)
            else:
                english_translation.append('?')  # Handle invalid Braille symbol for digits
        else:
            # Handle alphabet and punctuation
            letter = next((key for key, value in braille_alphabet_dict.items() if value == symbol), None)
            if letter:
                if capital_mode:
                    letter = letter.upper()  # Capitalize the letter
                    capital_mode = False  # Reset capital mode after applying
                english_translation.append(letter)
            else:
                punctuation = next((key for key, value in braille_symbol_dict.items() if value == symbol), None)
                if punctuation:
                    english_translation.append(punctuation)
                else:
                    english_translation.append('?')  # Handle invalid Braille symbol for letters

        i += 6  # Move to the next Braille symbol

    return "".join(english_translation)


# Function to automatically detect and translate
def detect_and_translate(input_text):
    # If input contains only Braille symbols (O and .), assume it's Braille and translate to English
    if all(char in ['O', '.', ' '] for char in input_text):
        return translate_to_english(input_text.replace(" ", ""))
    else:
        return translate_to_braille(input_text)


# Main program to handle user input
def main():
    input_text = input()
    output = detect_and_translate(input_text)
    print(output)


if __name__ == "__main__":
    main()