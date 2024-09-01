import sys

def solution(input):
    # English Characters to Braille
    chars = {
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
    }

    # Numbers to Braille
    nums = {
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        'O': '.OOO..',
    }

    # Braille to English Characters
    braille_chars = {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f',
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z'
    }

    # Braille to Numbers
    braille_nums = {
        'O.....': '1',
        'O.O...': '2',
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9',
        '.OOO..': 'O'
    }

    TRANSLATE_TO_BRAILLE = False

    # Due to the restrictions of the question, if the string contains a period
    # It has to be a sequence of braille. We can further verify it by making sure
    # The length of the sequence is a multiple of 6.
    for char in input:
        if char == '.' and len(input) % 6 == 0:
            TRANSLATE_TO_BRAILLE = True
            break

    output = "" # Store the output

    if TRANSLATE_TO_BRAILLE:
        
        # Translate ENGLISH to BRAILLE
        digit = False
        capital = False

        for i in range(0,len(input),6):
            char = input[i:i+6]

            # If the sequence is a space
            if char == '......':
                output += " "
                digit = False
            
            # If the sequence designates that a "capital follows" 
            elif char == '.....O':
                capital = True

            # If the sequence designates that a "number follows" 
            elif char == '.O.OOO':
                digit = True
            
            # If this sequence is a digit as declared by number follows
            elif digit:
                output += braille_nums[char]

            # Else this sequence is a character
            else:
                if capital:
                    output += str.upper(braille_chars[char])
                else:
                    output += braille_chars[char]
                capital = False

    else:

        # Translate BRAILLE to ENGLISH
        digit = False

        for char in input:
            
            # If the character is space
            if char == ' ':
                output += '......'
                digit = False

            # If this current sequence is digits as declared by number follows
            elif digit:
                output += nums[char]

            # If the character is alpha numeric
            elif str.isalpha(char):

                # If the character is a capital
                if str.upper(char) == char:
                    output += '.....O' + chars[str.lower(char)]
                # If the character is lowercase
                else:
                    output += chars[char]

            # If the character is a digit
            elif str.isdigit(char):
                output += '.O.OOO' + nums[char]
                digit = True
    
    return output

if __name__ == "__main__":
    print(solution(" ".join(sys.argv[1:])), end='')