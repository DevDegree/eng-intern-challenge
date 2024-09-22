
import argparse

def isBraille(text):
    if len(text) % 6 != 0:
        return False
    i = 0
    while i < len(text):
        if text[i:i+6] not in brailleToLetter:
            return False
        i += 6
    return True

def brailleToText(braille):
    text = []
    i = 0
    while i < len(braille):
        if braille[i:i+6] == letterToBraille['cap']:
            i += 6
            text.append(brailleToLetter[braille[i:i+6]].upper())
            i += 6
        elif braille[i:i+6] == letterToBraille['num'] or braille[i:i+6] == letterToBraille['dec']:
            if braille[i:i+6] == letterToBraille['dec']:
                i += 6
                if braille[i:i+6] == letterToBraille['.']:
                    text.append('.')
                    i += 6
                else:
                    raise Exception('Invalid Braille, period must be after "decimal follows" sign')
            i += 6 # skip the num sign
            while i < len(braille) and braille[i:i+6] != letterToBraille[' ']:
                if braille[i:i+6] == letterToBraille['j']:
                    text.append('0')
                elif braille[i:i+6] == letterToBraille['dec']:
                    i += 6
                    if braille[i:i+6] == letterToBraille['.']:
                        text.append('.')
                    else:
                        raise Exception('Invalid Braille, period must be after "decimal follows" sign')
                else:
                    text.append(str(ord(brailleToLetter[braille[i:i+6]]) - ord('a') + 1))
                i += 6
        else:
            text.append(brailleToLetter[braille[i:i+6]])
            i += 6
    return ''.join(text) # a little faster on time

def textToBraille(text):
    braille = []
    i = 0
    while i < len(text):
        if text[i].isupper():
            braille.append(letterToBraille['cap'])
            braille.append(letterToBraille[text[i].lower()])
            i += 1
        elif text[i].isdigit() or (text[i] == '.' and i + 1 < len(text) and text[i + 1].isdigit()):
            if text[i] == '.':
                braille.append(letterToBraille['dec'])
                braille.append(letterToBraille['.'])
                i += 1
            braille.append(letterToBraille['num'])
            while i < len(text) and (text[i].isdigit() or text[i] == '.'):
                if text[i] == '.':
                    braille.append(letterToBraille['dec'])
                    braille.append(letterToBraille['.'])
                else:
                    if text[i] == '0':
                        braille.append(letterToBraille['j'])
                    else:
                        braille.append(letterToBraille[str(chr(ord('a') + int(text[i]) - 1))])
                i += 1
        else:
            braille.append(letterToBraille[text[i]])
            i += 1
    return ''.join(braille)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to demonstrate command-line argument parsing.")
    
    # Allow for multiple inputs, each of which can include spaces
    parser.add_argument("inputs", nargs='*', type=str, help="Multiple pieces of data to be processed, which may include spaces.")
    args = parser.parse_args()
    inputs = ' '.join(args.inputs)

    letterToBraille = {
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
        'cap': '.....O',
        'dec': '.O...O',
        'num': '.O.OOO',
        ' ': '......',
        '.': '..OO.O',
        ',': '..O...',
    }
    brailleToLetter = {v: k for k, v in letterToBraille.items()}
    if isBraille(inputs):
        print(brailleToText(inputs))
    else:
        print(textToBraille(inputs))