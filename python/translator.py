import sys

braille_characters = {
    'a': '0.....', 'b': '0.0...', 'c': '00....', 'd': '00.0..', 'e': '0..0..', 
    'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.0.0...', 'j': '.000..',
    'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.', 
    'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.0.0.0.', 't': '.0000.',
    'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000', 
    'z': '0..000', ' ': '......'}

braille_numbers = {'1': '0.....', '2': '0.0...', '3': '00....', '4': '00.0..', '5': '0.0...', 
                   '6': '000...', '7': '0000..', '8': '0.00..', '9': '.0.0...', '0': '.000..'}

CAPITAL_FOLLOWS = '.....0'
NUMBER_FOLLOWS = '.0.000'

def isbraille(text: str) -> bool:
    return set(text) <= {'0', '.'}

def convert_to_braille(text: str) -> str:
    braille = ''
    num_fols = False

    for alph in text:
        if alph == ' ':
            num_fols = False

        if alph.isnumeric():
            if not num_fols:
                braille += NUMBER_FOLLOWS
                num_fols = True
            braille += braille_numbers[alph]
        else:
            if alph.isupper():
                braille += CAPITAL_FOLLOWS
                braille += braille_characters[alph.lower()]
            else:
                braille += braille_characters[alph]
    
    return braille

def convert_to_alphabet(text: str) -> str:
    english = ''

    capital_fol = False
    number_fol = False

    for i in range(0, len(text), 6):
        if text[i: i+6] == CAPITAL_FOLLOWS:
            capital_fol = True
        elif text[i: i+6] == NUMBER_FOLLOWS:
            number_fol = True
        elif text[i: i+6] == '......':
            number_fol = False
        else:
            if number_fol == True:
                for num, braille in braille_numbers.items():
                    if text[i: i+6] == braille:
                        english += num
            else:
                for alph, braille in braille_characters.items():
                    if text[i: i+6] == braille:
                        if capital_fol:
                            english += alph.capitalize()
                            capital_fol = False
                        else:
                            english += alph
    
    return english

def main():
    text = ' '.join(sys.argv[1:])
    if len(text) < 2:
        sys.exit(0)

    if isbraille(text):
        print(convert_to_alphabet(text))
    else:
        print(convert_to_braille(text))


if __name__ == "__main__":
    main()