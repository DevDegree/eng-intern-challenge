import sys

from enum import Enum

class TypeLetter(Enum):
    NUMBER = 1
    LETTER = 2
    CAPS = 3
    NUMBER_ONE = 4


def constructDictionnary():
        dictionnary = { 'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
                        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
                        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
                        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
                        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
                        'z': 'O..OOO', ' ': '......', 'caps': '.....O', 'num': '.O.OOO' }
        reversed_dictionnary = {}
        for key, value in dictionnary.items():
            reversed_dictionnary[value] = key

        
        return (dictionnary, reversed_dictionnary)

def brailleCalculator(letter, braille_to_ascii, letter_type):

    temp = braille_to_ascii[letter]
    if (temp == 'caps'):
        return ("",  TypeLetter.CAPS)
    elif temp == ' ':
        return (temp, TypeLetter.LETTER)
    elif temp == "num":
        return ("", TypeLetter.NUMBER)
    else:
        if letter_type == TypeLetter.CAPS:
            return (chr(ord(temp) -32), TypeLetter.LETTER)
        elif letter_type == TypeLetter.NUMBER:
            if temp == 'j':
                return ('0', TypeLetter.NUMBER)
            return (chr(ord(temp) -48), TypeLetter.NUMBER)
        return (temp, letter_type)
    
def asciiCalculator(letter, ascii_to_braille, letter_type):

    if letter >= 'A' and letter <= 'Z':
        return (ascii_to_braille['caps'] + ascii_to_braille[letter.lower()], TypeLetter.LETTER)
    elif letter == '0':
        if letter_type == TypeLetter.LETTER:
            return (ascii_to_braille['num'] + ascii_to_braille[chr(ord(letter) + 58)], TypeLetter.NUMBER)
        return ascii_to_braille[chr(ord(letter) + 58)], TypeLetter.NUMBER
    elif letter >= '1' and letter <= '9':
        if letter_type == TypeLetter.LETTER:
            return (ascii_to_braille['num'] + ascii_to_braille[chr(ord(letter) + 48)], TypeLetter.NUMBER)
        return ascii_to_braille[chr(ord(letter) + 48)], TypeLetter.NUMBER

    return (ascii_to_braille[letter], TypeLetter.LETTER)

def checkTypeInput(word):
    if len(word) % 6 == 0:
        for i in word:
            if i != 'O' and i != '.':
                return False
    else:
        return False
    return True

def translateWord(word, is_braille, ascii_to_braille, braille_to_ascii):
    letter_type = TypeLetter.LETTER
    answer = ""
    i = 0
    while i < len(word):
        if is_braille:
            temp, letter_type =  brailleCalculator(word[i:i+6], braille_to_ascii, letter_type)
            answer += temp
            i += 6
        else:
            temp, letter_type =  asciiCalculator(word[i], ascii_to_braille, letter_type)
            answer += temp
            i += 1
    return answer

def mainFonction(word):
    is_braille = checkTypeInput(word)
    ascii_to_braille, braille_to_ascii = constructDictionnary()
    answer = translateWord(word, is_braille, ascii_to_braille, braille_to_ascii)
    print(answer)

if __name__ == '__main__':
    mainFonction(" ".join(sys.argv[1:]))
         