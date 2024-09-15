import sys

brailleTonumbers = { #generated with a for
    # nums
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7',
    'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}
alphabetToBraille: dict = {
    #letters
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
    # nums
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
    #markers
    'cap': '.....O',
    'dec': '.O...O',
    'num': '.O.OOO',
    #special chars
    # '.': '..OO.O',
    # ',': '..O...',
    # '?': '..O.OO',
    # '!': '..OOO.',
    # ':': '..OO..',
    # ';': '..O.O.',
    # '-': '....OO',
    # '/': '.O..O.',
    # '<': '.OO..O',
    # '>': 'O..OO.',
    # '(': 'O.O..O',
    # ')': '.O.OO.',
    ' ': '......',
}

#one time thing to not rewrite it
#braille_to_alphabet = {value: key for key, value in alphabetToBraille.items()}


brailleToAlphabet = {'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u',
    'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', '.....O': 'cap', '.O...O': 'dec',
    '.O.OOO': 'num', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    # '..OO..': ':', '..O.O.': ';','....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O.O..O': '(', '.O.OO.': ')'
    '......': ' '}

def isBraille(given_string):
    '''
    Verify the str is in braille by:
     - all chars are either 'O' or '.'
     - the length of the string is 0(mod 6)
     - there's no matrix/2x3 of braille that has all raised
      '''
    return all(char in 'O.' for char in given_string) and len(given_string) % 6 == 0 and any(
        char == '.' for char in given_string)
def translateToBraille(word):
    '''
    Letters to braille
    '''
    out = ''
    number_lock = False
    for char in word:
        if char==' ' and number_lock:
            number_lock = False
            out+=alphabetToBraille[' ']
            continue
        elif char.isdigit() and not number_lock:
            out+=alphabetToBraille['num']
            number_lock = True
            out+=alphabetToBraille[char]
            continue
        elif char.isupper():
            out+=alphabetToBraille['cap']
            out+=alphabetToBraille[char.lower()]
            continue
        out+=alphabetToBraille[char.lower()]
    return out
def translateToAlphabet(braille):
    '''
    braille to alphanumeric
    '''
    out = ''
    number_lock = False
    upper_case = False
    braille_chunks = [braille[i:i + 6] for i in range(0, len(braille), 6)]


    for char in braille_chunks:
        if char==alphabetToBraille['num']: #for indicating a number
            number_lock = True
            continue
        elif number_lock and char!=alphabetToBraille[' ']: #continue number
            out+=brailleTonumbers[char]
            continue
        elif number_lock and char==alphabetToBraille[' ']:#turn off number at space
            out+= brailleToAlphabet[char]
            number_lock = False
            continue
        elif char == alphabetToBraille['cap']:
            upper_case = True
            continue
        elif upper_case:
            out+=brailleToAlphabet[char].upper()
            upper_case = False
            continue
        out+=brailleToAlphabet[char]
    return out

def main():
    giventext = ' '.join(sys.argv[1:])  # the args at runtime in a str
    # print(translateToAlphabet(translateToBraille('123 456')))
    if isBraille(giventext):
        result = translateToAlphabet(giventext)
    else:
        result = translateToBraille(giventext)
    print(result)
# Abc 123 xYz
# my tests
    # if giventext == 'Hello world':
    #     hello = '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..'
    #     print(hello==b)
    # elif giventext == '42':
    #     fourtwo = '.O.OOOOO.O..O.O...'
    #     print(fourtwo==b)
    # elif giventext == '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..':
    #     print('Hello world'==a)
    #
    # elif giventext == '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....':
    #     print(a)
    #     print('Abc 123'==a)

if __name__ == '__main__':
    main()