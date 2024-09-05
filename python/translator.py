import sys

alphaDict = {
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
    'z': '0..000'
}
numericDict = {
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
}

modifierDict = {
    'capital': '.....0', # put two in front of word to capitalize word
    'decimal': '.0...0',
    'number': '.0.000'
}

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789,?!:;-/<>() '

def isBraille(input): # checks if input string is braille or english
    if any((char in chars) for char in input):
        return False
    else:
        return True


if __name__ == '__main__':

    input = sys.argv[1]

    print(input)

    if (isBraille(input)):
        print ('Braille')
    elif (not isBraille(input)):
        print ('English')



