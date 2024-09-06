import sys
print(sys.argv)

# dictionary used to translate letters and numbers to brail
letterNumDict = {
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
    'z': 'O..OOO'
}

#dictionary used to translate braile to numbers and letters
braileDict = {}

if sys.argv.length > 1:
    input = ' '.join(sys.argv[1:])
    if(letterOr)
    output = ""
    i = 1
    while i < sys.argv.length:
        output += braileDict[sys.argv[i]]
        if i != sys.argv.length:
            output += "......"
        i += 1
else:
    print("empty input")


def isBraille(text): 
    return text.count("O") + text.count(".") === text.len()