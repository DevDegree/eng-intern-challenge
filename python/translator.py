import sys

conversion = [
    ['a','O.....'],
    ['b','O.O...'],
    ['c','OO....'],
    ['d','OO.O..'],
    ['e','O..O..'],
    ['f','OOO...'],
    ['g','OOOO..'],
    ['h','O.OO..'],
    ['i','.OO...'],
    ['j','.OOO..'],
    ['k','O...O.'],
    ['l','O.O.O.'],
    ['m','OO..O.'],
    ['n','OO.OO.'],
    ['o','O..OO.'],
    ['p','OOO.O.'],
    ['q','OOOOO.'],
    ['r','O.OOO.'],
    ['s','.OO.O.'],
    ['t','.OOOO.'],
    ['u','O...OO'],
    ['v','O.O.OO'],
    ['w','.OOO.O'],
    ['x','OO..OO'],
    ['y','OO.OOO'],
    ['z','O..OOO'],
    ['1','O.....'],
    ['2','O.O...'],
    ['3','OO....'],
    ['4','OO.O..'],
    ['5','O..O..'],
    ['6','OOO...'],
    ['7','OOOO..'],
    ['8','O.OO..'],
    ['9','.OO...'],
    ['0','.OOO..'],
    ['cap','.....O'],
    #['dec','.O...O'],
    ['num','.O.OOO'],
    # ['.','..OO.O'],
    # [',','..O...'],
    # ['?','..O.OO'],
    # ['!','..OOO.'],
    # [':','..OO..'],
    # [';','..O.O.'],
    # ['_','....OO'],
    # ['/','.O..O.'],
    # ['<','.OO..O'],
    # ['>','O..OO.'],
    # ['(','O.O..O'],
    # [')','.O.OO.'],
    [' ','......'], 
]

e_to_b = {} # english to braille map
b_to_e = {} # braille to english map

for pair in conversion:
    character, braille = pair
    e_to_b[character] = braille
    # new key
    if braille not in b_to_e: 
        b_to_e[braille] = [character]
    # existing key
    else:
        b_to_e[braille].append(character)

def is_cap(char):
    return (char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def is_num(char):
    return (char in "1234567890")

def english_to_braille(inp):
    ans = ""
    in_num_segment = False # whether we are processing a sequence of numbers
    for char in inp:
        # if end of a number sequence
        if (is_num(char) == False and in_num_segment):
            in_num_segment = False
        # if number
        if (is_num(char) == True):  
            if (not in_num_segment):
                ans += e_to_b['num']
                in_num_segment = True
            ans += e_to_b[char]
        # if capital
        elif (is_cap(char) == True):
            ans += e_to_b['cap']
            ans += e_to_b[char.lower()]
        else:
            ans += e_to_b[char]
    print(ans)

def braille_to_english(inp):
    ans = ""
    is_capital = False # whether next symbol is captial
    in_num_segment = False # whether we are processing a sequence of numbers
    inp_split = []
    for i in range(0, len(inp), 6):
        inp_split.append(inp[i:i+6])

    for braille in inp_split:
        if b_to_e[braille][0] == 'cap':
            is_capital = True
        elif b_to_e[braille][0] == 'num':
            in_num_segment = True
        # if end of number segment
        elif b_to_e[braille][0] == ' ' and in_num_segment:
            in_num_segment = False
            ans += b_to_e[braille][0]
        elif is_capital:
            ans += b_to_e[braille][0].upper()
            is_capital = False
        elif in_num_segment:
            ans += b_to_e[braille][1]
        else:
            ans += b_to_e[braille][0]

    print(ans)


inp_str = ""
for i in range(1, len(sys.argv)):
    inp_str += str(sys.argv[i]) + " "

inp_str = inp_str.strip()

if ((inp_str.count('O')+inp_str.count('.')) == len(inp_str)):
    braille_to_english(inp_str) 
else:
    english_to_braille(inp_str)