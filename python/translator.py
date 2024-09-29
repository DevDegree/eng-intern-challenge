import sys

if len(sys.argv) > 1:
    input = sys.argv[1:]

    conversion = [
    ('1', 'O.....'),
    ('2', 'O.O...'),
    ('3', 'OO....'),
    ('4', 'OO.O..'),
    ('5', 'O..O..'),
    ('6', 'OOO...'),
    ('7', 'OOOO..'),
    ('8', 'O.OO..'),
    ('9', '.OO...'),
    ('0', '.OOO..'),

    ('a', 'O.....'),
    ('b', 'O.O...'),
    ('c', 'OO....'),
    ('d', 'OO.O..'),
    ('e', 'O..O..'),
    ('f', 'OOO...'),
    ('g', 'OOOO..'),
    ('h', 'O.OO..'),
    ('i', '.OO...'),
    ('j', '.OOO..'),
    ('k', 'O...O.'),
    ('l', 'O.O.O.'),
    ('m', 'OO..O.'),
    ('n', 'OO.OO.'),
    ('o', 'O..OO.'),
    ('p', 'OOO.O.'),
    ('q', 'OOOOO.'),
    ('r', 'O.OOO.'),
    ('s', '.OO.O.'),
    ('t', '.OOOO.'),
    ('u', 'O...OO'),
    ('v', 'O.O.OO'),
    ('w', '.OOO.O'),
    ('x', 'OO..OO'),
    ('y', 'OO.OOO'),
    ('z', 'O..OOO'),

    (' ', '......'),

    ('capital', '.....O'),
    ('decimal', '.O...O'),
    ('number', '.O.OOO'),
    ]

    b_map = dict(conversion)
    e_map = dict(reversed(t) for t in conversion) # Other way
    num_map = dict(reversed(t) for t in conversion[:10])
    result = ''
    if len(input) == 1 and input[0].replace('O','').replace('.','') == '':
        # Braille
        input = input[0]
        is_capital = False
        is_number = False
        for i in range(0,len(input),6):
            c = input[i:i+6]
            if e_map[c] == 'number':
                is_number = True
            elif e_map[c] == 'capital':
                is_capital = True
            elif e_map[c] == ' ':
                result += ' '
                is_number = False
            elif is_number:
                result += num_map[c]
            elif is_capital:
                result += e_map[c].upper()
                is_capital = False
            else:
                result += e_map[c]
    else:
        # English
        
        for s in input:
            if s.isnumeric():
                result += b_map['number']
            for c in s:
                if c.lower() != c: # upper case
                    result += b_map['capital']
                result += b_map[c.lower()]
            result += b_map[' ']
        result = result[:-6]
    print(result)
    

                
