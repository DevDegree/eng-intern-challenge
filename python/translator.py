import sys

# English to Braille dictionary
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.O.O', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 
    'cap': '.....O', 'num': '.O.OOO', 
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Braille to English dictionary (does not include numbers since same mapping)
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k not in '0123456789'}

# checks if input is braille or not (is English)
def is_braille(s):
    for c in s:
        if c in '.':
            return True
        return False

def english_to_braille(english):
    braille = []
    number_mode = False
    for c in english:
        if c.isdigit():
            if not number_mode:
                braille.append(ENGLISH_TO_BRAILLE['num'])
                number_mode = True
            braille.append(ENGLISH_TO_BRAILLE[c])
        elif c.isalpha():
            if c.isupper():
                braille.append(ENGLISH_TO_BRAILLE['cap'])
            braille.append(ENGLISH_TO_BRAILLE[c.lower()])
            number_mode = False
        elif c == ' ':
            braille.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
    return ''.join(braille)

def braille_to_english(braille):
    if len(braille) % 6 != 0:
        print("Error: Invalid Braille input")
        sys.exit(1)

    english = []
    i = 0
    number_mode = False
    capital_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == '.O.OOO':  # "Number follows" symbol
            number_mode = True
            capital_mode = False
        elif symbol == '.....O':  # Capitalization symbol
            capital_mode = True
            i += 6
            continue
        elif symbol == '......':  # Space character
            english.append(' ')
            number_mode = False
            capital_mode = False
        else:
            char = BRAILLE_TO_ENGLISH.get(symbol, '')

            if number_mode and char in 'abcdefghij':  # Should show number
                # Map a-j to 1-9 and 0
                number = str(ord(char) - ord('a') + 1)
                number = '0' if number == '10' else number  # Handle 0 separately
                english.append(number)
            elif capital_mode and char: # Upper case character addition
                english.append(char.upper())
                number_mode = False
                capital_mode = False
            elif char:
                english.append(char)  # Regular character addition
                number_mode = False
                capital_mode = False
        i += 6

    return ''.join(english)

def main():
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        
        if is_braille(input_text):
            print(braille_to_english(input_text))
        else:
            print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
