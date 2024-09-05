import sys

# braille dictionary for alphabets
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

# braille dictionary for numbers
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# braille special symbols
braille_capital = '.....O'  # capitalization indicator
braille_number = '.O.OOO'   # number indicator
braille_space = '......'    # space

# reverse dictionaries for english translation
english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_numbers = {v: k for k, v in braille_numbers.items()}

# determining what the input text is in (either english or braille)
def is_braille(text):
    return all(char in 'O.' for char in text)


# function for translating from english to braille
def translate_to_braille(text):
    braille_output = []
    # flag to indicate if the translation is currently in number mode
    number_mode = False
    
    # iterate over each character in the input text
    for char in text:
        # check if the character is a digit
        if char.isdigit():
            # if not already in number mode, add the number indicator and set the flag
            if not number_mode:
                braille_output.append(braille_number)
                number_mode = True
            braille_output.append(braille_numbers[char])
        # check if the character is a letter
        elif char.isalpha():
            # if previously in number mode, add a space to reset number mode
            if number_mode:
                braille_output.append(braille_space)
                number_mode = False
            # if the letter is uppercase, add the capitalization indicator
            if char.isupper():
                braille_output.append(braille_capital)
                char = char.lower()
            # append the corresponding braille representation of the letter
            braille_output.append(braille_alphabet[char])
        # check if the character is a space
        elif char == ' ':
            braille_output.append(braille_space)
            number_mode = False
    
    return ''.join(braille_output)

# function for translating from braille to english
def translate_to_english(braille):
    english_output = []
    number_mode = False
    i = 0
    
    # loop through the braille string (each is 6 characs.)
    while i < len(braille):
        symbol = braille[i:i+6]
        
        # check if the symbol is a space
        if symbol == braille_space:
            english_output.append(' ')
            number_mode = False
        # check if the symbol is a capitalization indicator
        elif symbol == braille_capital:
            i += 6
            next_symbol = braille[i:i+6]
            # if the symbol is a valid letter, append its uppercase version to the output
            if next_symbol in english_alphabet:
                english_output.append(english_alphabet[next_symbol].upper())
        # check if the symbol is a number indicator
        elif symbol == braille_number:
            number_mode = True
        else:
            # if in number mode and the symbol is a valid number, append it to the output
            if number_mode and symbol in english_numbers:
                english_output.append(english_numbers[symbol])
            # if not in number mode and the symbol is a valid letter, append it to the output
            elif not number_mode and symbol in english_alphabet:
                english_output.append(english_alphabet[symbol])
        
        # move to the next braille symbol
        i += 6
    
    # join all english characters into a single string and return it
    return ''.join(english_output)


def main():
    # check to see if the input string(s) are blank 
    if len(sys.argv) < 2:
        print("please provide input to translate.")
        return
    
    # combining all arguments for multi-word input
    input_text = ' '.join(sys.argv[1:])
    
    # determing if the input is braille or english
    if is_braille(input_text):
        # translate from braille to english
        print(translate_to_english(input_text))
    else:
        # translate from english to braille
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
