
import sys

# Solution to brallie challenge 
#  A dictionary of the braile to english 
# A method that accepts the converting string 
# remeber if we know A to j we already know most of all the other characters
# This condition doesnt apply to numbers and punctuation marks 

english_to_braille = {
    'a': 'O.....',  # A
    'b': 'O.O...',  # B
    'c': 'OO....',  # C
    'd': 'OO.O..',  # D
    'e': 'O..O..',  # E
    'f': 'OOO...',  # F
    'g': 'OOOO..',  # G
    'h': 'O.OO..',  # H
    'i': '.OO...',  # I
    'j': '.OOO..',  # J
    'k': 'O...O.',  # K
    'l': '0.O.O.',  # L
    'm': 'OO..O.',  # M
    'n': 'OO.OO.',  # N
    'o': 'O..OO.',  # O
    'p': 'OOO.O.',  # P
    'q': 'OOOOO.',  # Q
    'r': 'O.OOO.',  # R
    's': '.OO.O.',  # S
    't': '.OOOO.',  # T
    'u': 'O...OO',  # U
    'v': 'O.O.OO',  # V
    'w': '.OOO.O',  # W special character 
    'x': 'OO..OO',  # X
    'y': 'OO.OOO',  # Y
    'z': 'O..OOO',  # Z

  

    # Numbers, prefixed by a number sign
    '1': 'O.....',  # 1 (same as 'a')
    '2': 'O.O...',  # 2 (same as 'b')
    '3': 'OO....',  # 3 (same as 'c')
    '4': 'OO.O..',  # 4 (same as 'd')
    '5': 'O..O..',  # 5 (same as 'e')
    '6': 'OOO...',  # 6 (same as 'f')
    '7': 'OOOO..',  # 7 (same as 'g')
    '8': 'O.OO..',  # 8 (same as 'h')
    '9': '.OO...',  # 9 (same as 'i')
    '0': '.OOO..',  # 0 (same as 'j')

    # Special symbols (need sortting )
    ' ': '......',  # Space
    '.': '.O..OO',  # Period
    ',': '.O....',  # Comma
    '?': '.O...O',  # Question mark
    '!': '.OO.O.',  # Exclamation mark
    ':': '.O..O.',  # Colon
    ';': '.OO...',  # Semicolon
    '-': '..O..O',  # Dash
    '/': '..OO..',  # Slash
    '<': 'O..O.O',  # Less than
    '>': '....OO',  # Greater than
    '(': 'OO...O',  # Left parenthesis
    ')': '..O.OO',  # Right parenthesis

}
char_num_punct={
    'capital_follows': '.....O',  # Capital follows (dot 6)
    'decimal_follows': '.O...O',  # Decimal follows (dots 4, 6)
    'number_follows': '.O.O0O',   # Number follows (dots 3, 4, 5, 6)
}

# braille_to_english = {
#     'O.....': 'a',  # Braille for 'a'
#     'OO....': 'b',  # Braille for 'b'
#     'O.O...': 'c',  # Braille for 'c'
#     'O..OO.': 'd',  # Braille for 'd'
#     'O...O.': 'e',  # Braille for 'e'
#     # Add the rest of the alphabet

#     # Numbers, prefixed by a number sign (handled separately)
#     'O.....': '1',  # Braille for '1'
#     'OO....': '2',  # Braille for '2'
#     # Add more numbers

#     # Special symbols
#     '......': ' ',  # Space
#     '.O..OO': '.',  # Period
#     '.O....': ',',  # Comma
#     '.O...O': '?',  # Question mark
#     # Add more punctuation
# }



# Top method that controls if its a text or in braille and delegates a fucntion to carry out the task of translation 
def Translate(text):
    # Check if the first character equals to a dot (need to revise this logic)
    if text[0]== '.':
        Braille_to_english(text)
    else:
        Translate_to_english(text)

def Translate_to_english(text):
    braille=''
    for i in range(0, len(text)):
        # Track previous char incase we need to switch 
        current_char = text[i]
        previous_char = text[i-1] if i > 0 else '' 

        if current_char.isupper():
            print(current_char)
            braille+=char_num_punct['capital_follows']
            # converting to lower because it doesnt have capital letters in the dictionary 
            braille+=english_to_braille[current_char.lower()]
        elif current_char== ' ':
            print(current_char)
            braille+=english_to_braille[current_char.lower()]
        elif current_char.isdigit():
            print(current_char)
            # Check if the previous character is not a digit or space to add 'number_follows'
            if previous_char == '' or not previous_char.isdigit():
                braille += char_num_punct['number_follows']
            # add the braille for the current digit
            braille += english_to_braille[current_char]
        else:
            print(current_char)
            braille+=english_to_braille[text[i].lower()]       
    print(braille)

def Braille_to_english(text):
    english_text = ''
    i = 0
    is_capital = False
    is_number = False

    while i < len(text):
        current_chunk = text[i:i+6]
 
        # Check for capital indicator 

        if current_chunk == char_num_punct['capital_follows']:
            print("cap")
            is_capital = True
            i += 6 
            continue

        # Check for number indicator
        elif current_chunk == char_num_punct['number_follows']:
            print("number follows")
            is_number = True
            i += 6
            continue

        # Handle spaces
        elif current_chunk == english_to_braille[' ']:
            english_text += ' '
            i += 6  # Move past the space

            # Immediately check the next chunk to see if it's a capital or number indicator
            next_chunk = text[i:i+6]
            if next_chunk == char_num_punct['capital_follows']:
                is_capital = True
                i += 6  # Move past the capital indicator
                continue
            elif next_chunk == char_num_punct['number_follows']:
                is_number = True
                i += 6  # Move past the number indicator
                continue

            # If no special indicator follows, reset flags
            is_capital = False
            is_number = False
            continue

        # Translate numbers if number flag is set
        if is_number:
            for digit, braille in english_to_braille.items():
                if braille == current_chunk and digit.isdigit():
                    english_text += digit
                    break
            i += 6
            continue

        # Translate letters and capital letters
        for letter, braille in english_to_braille.items():
            if braille == current_chunk and not letter.isdigit():
                if is_capital:
                    english_text += letter.upper()
                    is_capital = False  # Reset the capital flag after one letter
                else:
                    english_text += letter
                break

        # Move to the next Braille chunk
        i += 6

    print(english_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
    else:
        input_text = ' '.join(sys.argv[1:])  # Join all arguments into one string
        result = Translate(input_text)
    
