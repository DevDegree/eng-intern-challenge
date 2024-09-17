# instead of hard coding all alphabets using . and O, it will be easier to follow what it actually is. 
# O indicates there is a bump, and . indicates its just flat.
# so, build the alphabet mappings as an array of ints that show the position of the O, or where the bump will be in real life
# positions:
# 1 2
# 3 4
# 5 6
# eg, a = [1]

alphabets = {
    'a': [1],
    'b': [1, 3],
    'c': [1, 2],
    'd': [1, 2, 4],
    'e': [1, 4],
    'f': [1, 2, 3],
    'g': [1, 2, 3, 4],
    'h': [1, 3, 4],
    'i': [2, 3],
    'j': [2, 3, 4],
    'k': [1, 5],
    'l': [1, 3, 5],
    'm': [1, 2, 5],
    'n': [1, 2, 4, 5],
    'o': [1, 4, 5],
    'p': [1, 2, 3, 5],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 3, 4, 5],
    's': [2, 3, 5],
    't': [2, 3, 4, 5],
    'u': [1, 5, 6],
    'v': [1, 3, 5, 6],
    'w': [2, 3, 4, 6],
    'x': [1, 2, 5, 6],
    'y': [1, 2, 4, 5, 6],
    'z': [1, 4, 5, 6]
}

numbers = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j'
}

puncuations = {
    '.': [3, 4, 6],
    ',': [3],
    '?': [3, 5, 6],
    '!': [3, 4, 5],
    ':': [3, 4],
    ';': [3, 5],
    '-': [5, 6],
    '/': [2, 5],
    '<': [2, 3, 6],
    '>': [1, 4, 5],
    '(': [1, 3, 6],
    ')': [2, 4, 5],
    ' ': []
}

# commands
capital_follows = [6]
# decimal_follows = [2, 6]
number_follows = [2, 4, 5, 6]
