# Rahaman Bappi

"""
This file contains the dictionary for the translator
"""

TEXT = dict()
TEXT['a'] = 'O.....' # also '1'
TEXT['b'] = 'O.O...' # also '2'
TEXT['c'] = 'OO....' # also '3'
TEXT['d'] = 'OO.O..' # also '4'
TEXT['e'] = 'O..O..' # also '5'
TEXT['f'] = 'OOO...' # also '6'
TEXT['g'] = 'OOOO..' # also '7'
TEXT['h'] = 'O.OO..' # also '8'
TEXT['i'] = '.O.O..' # also '9'
TEXT['j'] = '.OOO..'
TEXT['k'] = 'O...O.'
TEXT['l'] = 'O.O.O.'
TEXT['m'] = 'OO..O.'
TEXT['n'] = 'OO.OO.'
TEXT['o'] = 'O..OO.'
TEXT['p'] = 'OOO.O.'
TEXT['q'] = 'OOOOO.'
TEXT['r'] = 'O.OOO.'
TEXT['s'] = '.OO.O.'
TEXT['t'] = '.OOOO.'
TEXT['u'] = 'O...OO'
TEXT['v'] = 'O.O.OO'
TEXT['w'] = '.OOO.O'
TEXT['x'] = 'OO..OO'
TEXT['y'] = 'OO.OOO'
TEXT['z'] = 'O..OOO'

# Misc

TEXT[' '] = '......'
TEXT['CAPITAL'] = '.....O'
TEXT['NUMBER'] = '.O.OOO'
TEXT['0'] = '.OOO..'

# Reverse dictionary

BRAILLE = dict()
for key, value in TEXT.items():
    BRAILLE[value] = key