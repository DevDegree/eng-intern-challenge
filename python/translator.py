#dictionary that maps the alphabet to braille
alphabet_dict = {
    #numbers
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',

    #letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',

    #space, capital, decimals, numbers
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO',

    #punctuation
    '.': '..00.0', ',': '..0...', '?': '..0.00', '!': '..000.', ':': '..00..',
    ';': '..0.0.', '-': '....00', '/': '.0..0.', '<': '.00..0', '>': '0..00.', '(': '0.0..0', 
    ')': '.O.OO.', ' ' : '......'
}

#reverse dictionary (braille to alphabet)
braille_dict = {v: k for k, v in alphabet_dict.items()}


#check if command line input is in braille or english
def is_braille(text):
    return all(c in ['O', '.'] for c in text) 

#function translating english to braille
def english_to_braille(text):
    braille = []
    number_mode = False
    for char in text:
        if char.isnumeric():
            if not number_mode:
                braille.append(alphabet_dict.get('number'))
                number_mode = True
        if char.isupper():
            braille.append(alphabet_dict.get('capital'))
            char = char.lower()
        braille.append(alphabet_dict.get(char))
    return ''.join(braille)

#function translating braille to english
def braille_to_english(text):
    english = []
    i = 0
    number_mode = False
    while i < len(text):
        char = text[i:i+6]

        if char == alphabet_dict.get('capital'):
            next_char = text[i+6:i+12]
            letter = braille_dict.get(next_char)
            if letter:
                english.append(letter.upper())
            i+= 12

        elif char == alphabet_dict.get('number'):
            number_mode = True
            i += 6

        elif char == alphabet_dict.get(' '):
            number_mode = False
            english.append(' ')
            i+= 6
            
        elif number_mode:
            number = braille_dict.get(char)
            if number:
                if number == 'j':
                    english.append('0')
                elif number in 'abcdefghij':  # Map letters a-j to numbers 1-9
                    english.append(str(ord(number) - ord('a') + 1))
                else:
                    english.append(number)
            i += 6

        else: 
            english.append(braille_dict.get(char))
            i+=6
    return ''.join(english)

#check which translator is needed and call
def translator(input_str):
    if is_braille(input_str):
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

if __name__ == "__main__":
    import sys
    input_str = ' '.join(sys.argv[1:])
    translated = translator(input_str)
    print(translated)