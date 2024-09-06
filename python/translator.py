import sys
print(sys.argv)

# dictionary used to translate letters and numbers to brail
letNumDict = {
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
    ' ': '......',
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
    'A': '.....OO.....',
    'B': '.....OO.O...',
    'C': '.....OOO....',
    'D': '.....OOO.O..',
    'E': '.....OO..O..',
    'F': '.....OOOO...',
    'G': '.....OOOOO..',
    'H': '.....OO.OO..',
    'I': '.....O.OO...',
    'J': '.....O.OOO..',
    'K': '.....OO...O.',
    'L': '.....OO.O.O.',
    'M': '.....OOO..O.',
    'N': '.....OOO.OO.',
    'O': '.....OO..OO.',
    'P': '.....OOOO.O.',
    'Q': '.....OOOOOO.',
    'R': '.....OO.OOO.',
    'S': '.....O.OO.O.',
    'T': '.....O.OOOO.',
    'U': '.....OO...OO',
    'V': '.....OO.O.OO',
    'W': '.....O.OOO.O',
    'X': '.....OOO..OO',
    'Y': '.....OOO.OOO',
    'Z': '.....OO..OOO'
}

#dictionary used to translate braile to numbers and letters
brailleDict = {v: k for k, v in letNumDict}

def isBraille(text): 
    return text.count("O") + text.count(".") == text.len()


def main():
    print(brailleDict)

    if sys.argv.length > 1:
        input = ' '.join(sys.argv[1:])
        if isBraille:
            print('braille')
        else:
            print('letnum')
            # output = ""
            # i = 1
            # while i < sys.argv.length:
            #     output += braileDict[sys.argv[i]]
            #     if i != sys.argv.length:
            #         output += "......"
            #     i += 1
    else:
        print("empty input")

if __name__ == "__main__":
    main()