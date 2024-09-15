import sys

to_braille = {
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
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'cap': '.....O',
    'num': '.O.OOO',
    ' ': '......',
}
to_eng = {v: k for k, v in to_braille.items()}

def english_to_braille(input):
    output = ''
    num = False
    for c in input:
        if num:
            if c == ' ': # No longer reading a number due to space character
                num = False
        elif c.isdigit():
            output += to_braille['num']
            num = True
        elif c.isupper():
            output += to_braille['cap']
            c = c.lower()
        output += to_braille[c]
    return output

def braille_to_english(input):
    output = ''
    cap = False
    num = False

    # Divide Braille input into individual Braille characters
    chars = [input[i:i+6] for i in range(0, len(input), 6)]
    
    for c in chars:
        if to_eng[c] == 'cap':
            cap = True
            continue
        if to_eng[c] == 'num':
            num = True
            continue
        
        if num:
            output += to_eng[c]
            if to_eng[c] == ' ':
                num = False
        else:
            char = to_eng[c]
            if char < 'A' and char != ' ': # Adjusting for characters 'a' to 'j' since they are the same as the digits in Braille
                char = chr(ord(char) + 48) if char != '0' else 'j'
            if cap:
                output += char.upper()
                cap = False
            else:
                output += char
    return output

if __name__ == "__main__":
    # Error handling for incorrect program usage
    if len(sys.argv) < 2:
        print("Error: Must pass at least 1 argument.")
        sys.exit(1)
    
    result = ''

    for i in range(1, len(sys.argv)):
        input = sys.argv[i]
        if '.' in input: # Determine whether the input is in English or Braille
            if i > 1: # Add space between words
                result += ' '
            result += braille_to_english(input)
        else:
            if i > 1: # Add space between words
                result += '......'
            result += english_to_braille(input)
    print(result)
