import sys


braille_alphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

numbers = {    
    'O.....' : '1',
    'O.O...' : '2', 
    'OO....': '3',
    'OO.O..' : '4',
    'O..O..' : '5',
    'OOO...' : '6',
    'OOOO..' : '7',
    'O.OO..' : '8',
    '.OO...' : '9',
    '.OOO..' : '0'
    }

braille_to_englishNumbers = {v: k for k, v in numbers.items()}
braille_to_englishLetters = {v: k for k, v in braille_alphabet.items()}


def braille_converter(message):
    braille = ''
    first_number = True
    for character in message:
        if character.lower() in braille_alphabet:
            if character.isalpha() and character != character.lower():
                braille += '.....O'
            braille += braille_alphabet[character.lower()]
            first_number = True
        elif character in braille_to_englishNumbers:
            if first_number:
                first_number = False
                braille += '.O.OOO'
            braille += braille_to_englishNumbers[character]
    print(braille)





def english_converter(message):
    english = ''
    capital = False
    number = False
    for i in range(0,len(message), 6):
        braille_char = message[i:i + 6]

        if braille_char == '......':
            english += ' '
            number = False

        elif braille_char == '.....O':
            capital = True
            number = False
            
            
        elif braille_char == '.O.OOO':
            number = True
            capital = False
        
        elif not number :
            # Get the next 6 characters or braille_char not in numbers
            
            if braille_char in braille_to_englishLetters:
                letter = braille_to_englishLetters[braille_char]
                english += letter.upper() if capital else letter  # Map to English character
                if capital:
                    capital = False
        elif number:
            
            if braille_char in numbers:
                english += numbers[braille_char]  # Map to English character
        

    print(english)
# .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
# .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    
    message = ' '.join(sys.argv[1:])
    if not all(char in {'O', '.'} for char in message):
        braille_converter(message)
    else:
        english_converter(message)



if __name__ == '__main__':
    main()
