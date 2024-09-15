import sys

to_braille = {
    'a': '0.....',
    'b': '0.0...',
    'c': '00....',
    'd': '00.0..',
    'e': '0..0..',
    'f': '000...',
    'g': '0000..',
    'h': '0.00..',
    'i': '.00...',
    'j': '.000..',
    'k': '0...0.',
    'l': '0.0.0.',
    'm': '00..0.',
    'n': '00.00.',
    'o': '0..00.',
    'p': '000.0.',
    'q': '00000.',
    'r': '0.000.',
    's': '.00.0.',
    't': '.0000.',
    'u': '0...00',
    'v': '0.0.00',
    'w': '.000.0',
    'x': '00..00',
    'y': '00.000',
    'z': '0..000',
    '1': '0.....',
    '2': '0.0...',
    '3': '00....',
    '4': '00.0..',
    '5': '0..0..',
    '6': '000...',
    '7': '0000..',
    '8': '0.00..',
    '9': '.00...',
    '0': '.000..',
    'cap': '.....0',
    'num': '.0.000',
    ' ': '......',
}
to_eng = {v: k for k, v in to_braille.items()}

def english_to_braille(input):
    output = ''
    num = False
    for c in input:
        if num: # No longer reading a number due to space character
            if c == ' ':
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
    if len(sys.argv) != 2:
        print("Error: Pass 1 string argument.")
        sys.exit(1)
    
    input = sys.argv[1]
    
    if set(input) <= {'0', '.'}: # Determine whether the input is in English or Braille
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))