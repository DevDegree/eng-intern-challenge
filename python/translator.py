import sys

b_dictionary = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',  # Special characters (?, !, / etc.) not included as per the technical requirements
} 
# Reversed dictionary for Braille -> English translation
e_dictionary = {v: k for k, v in b_dictionary.items()}


letter_to_digit  = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}
digit_to_letter = {v: k for k, v in letter_to_digit.items()}

num_indicator = '.O.OOO'
caps_indicator = '.....O'
braille_len = 6

def braille_to_eng(input):
    """Translate Braille to English text."""
    output = []
    i = 0
    num_mode = False  

    while i < len(input):
        symbol = input[i:i + braille_len]

        if symbol == caps_indicator:
            next_symbol = input[i + braille_len:i + braille_len*2]
            if next_symbol in e_dictionary:
                c = e_dictionary[next_symbol].upper()
                if num_mode and c.lower() in letter_to_digit:
                    output.append(letter_to_digit[c.lower()])
                else:
                    output.append(c)
            i += braille_len*2
        elif symbol == num_indicator:
            num_mode = True 
            i += braille_len
        else:
            if symbol in e_dictionary:
                c = e_dictionary[symbol]
                if num_mode:
                    if c in letter_to_digit:
                        output.append(letter_to_digit[c])
                    else:
                        num_mode = False 
                        output.append(c)
                else:
                    output.append(c)
            i += braille_len

    print(''.join(output))
    return 

def eng_to_braille(input):
    """Translate English text to Braille."""
    output = []
    num_mode = False 

    for c in input:
        if c.isdigit():
            if not num_mode:
                output.append(num_indicator)
                num_mode = True
            letter = digit_to_letter[c]
            braille = b_dictionary.get(letter)
            output.append(braille)
        else:
            if num_mode:
                num_mode = False  
            if c.isupper():
                output.append(caps_indicator)
            c = c.lower()
            braille = b_dictionary.get(c)
            output.append(braille)

    print(''.join(output))
    return 

def main():
    """Main function to handle command-line input."""
    input = ' '.join(sys.argv[1:])

    if '.' in input: # Every braille alphabet/number contains atleast 1 '.'
        braille_to_eng(input)
    else:
        eng_to_braille(input)

if __name__ == "__main__":
    main()
