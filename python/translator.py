import sys

code_table_temp = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    '#': '001111',
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
    '0': '010110',
    ' ': '000000',
    '.': '010011',
    ',': '010000',
    '?': '011001',
    '!': '011010',
    ':': '010010',
    ';': '011000',
    '-': '001001',
    '/': '001100',
    '<': '010101',
    '>': '101010',
    '(': '110001',
    ')': '001110',
    'decimal': '000101',
    'capital': '000001',
    'number': '001111'}

code_table = dict()

for k, v in code_table_temp.items():
    new_v = v[0] + v[3] + v[1] + v[4] + v[2] + v[5]
    code_table[k] = new_v

r_code_table = dict()
r_code_table_num = dict()
for k, v in code_table.items():
    new_val = ''
    for i in v:
        new_val += 'O' if i == '1' else '.'
    if k.isnumeric():
        r_code_table_num[new_val] = k
    else:
        r_code_table[new_val] = k

# ---
curr_number = False

def print_from_table(c):
    global code_table
    for code in code_table[c]:
        print('O' if code == '1' else '.',end="")

def print_char(c): 
    global curr_number
    if c.isalpha():
        if c.isupper():
            print_from_table('capital')
            c = c.lower()
    elif c.isnumeric():
        if not curr_number:
            print_from_table('number')
            curr_number = True
    elif c == ' ':
        curr_number = False
    elif c == '.':
        print_from_table('decimal')
    print_from_table(c)

def print_braille(text):
    for c in text:
        print_char(c)
# ---

# ---
curr_number_2 = False
curr_capital_2 = False
curr_decimal_2 = False

def convert_to_english(text):
    global curr_capital_2
    global curr_decimal_2
    global curr_number_2
    global r_code_table
    

    if len(text) % 6 != 0:
        return None

    for c in text:
        if ((c != 'O') and (c != '.')):
            return None
        
    res = ''
    for i in range(0, len(text), 6):
        substr = text[i:i+6]
        print(substr, r_code_table[substr])
        if substr not in r_code_table:
            return None
        if curr_number_2 and substr not in r_code_table_num:
            return None
        if curr_capital_2 and not r_code_table[substr].isalpha():
            return None
        if curr_decimal_2 and not r_code_table[substr] != '.':
            return None
        if r_code_table[substr] == 'number':
            curr_number_2 = True
        elif r_code_table[substr] == 'capital':
            curr_capital_2 = True
        elif r_code_table[substr] == 'decimal':
            curr_decimal_2 = True
        elif r_code_table[substr] == '.':
            res += '.'
            curr_decimal_2 = False
        elif r_code_table[substr] == ' ':
            res += ' '
            curr_number_2 = False
        elif curr_number_2:
            res += r_code_table_num[substr]
        elif r_code_table[substr].isalpha():
            res += r_code_table[substr] if not curr_capital_2 else r_code_table[substr].upper()
            curr_capital_2 = False
        else: 
            res += r_code_table[substr]
    
    return res
# ---
        
        

text = ' '.join(sys.argv[1:])

english = convert_to_english(text)

if english == None:
    print_braille(text) 
else:
    print(english)