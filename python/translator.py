
import string
import sys


class Translator():
    orgText = ''

    def __init__(self, orgText):
        self.orgText = orgText

    number_follows = 'number_follows'
    capital_follows = 'capital_follows'
    decimal_follows = 'decimal_follows'
    space = " "
    
    #alphabet of eng and special chars to Braille
    dic = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': 'O.O...',
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
        't': 'O...OO',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        capital_follows: '.....O',
        decimal_follows: '.O...O',
        number_follows: '.O.OOO',
        space: '......',
        '.': '..OO.O',
        ',': '..O...',
        '?': '..O.OO',
        '!': '..OOO.',
        ',': '..OO..',
        ';': '..O.O.',
        '-': '....OO',
        '/': '.O..O.',
        '<': '.OO..O',
        '>': 'O..OO.',
        '(': 'O.O..O',
        ')': '.O.OO.',
    }

    #numbers dictionary
    numbers = {
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O..OO..',
        '9': '.OO...',
        'O': '.OOO..'
    }


    # Find the char as a start on numbers
    def numberFollows(
        self, letter)-> bool: return letter == self.dic.get(
        self.number_follows, '') 

    # find the char as a Capital char
    def capitalFollows(
        self, letter) -> bool: return letter == self.dic.get(
        self.capital_follows, '')

    #find char as space
    def spaceFollows(self, letter) -> bool: return letter == self.dic.get(self.space, '')


    