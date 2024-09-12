import sys, re

braillea = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',
    'capital follows' : '.....O',
    'decimal follows' : '.O...O',
    'number follows' : '.O.OOO',
    '.' : '..OO.O',
    ',' : '..O...',
    '?' : '..O.OO',
    '!' : '..OOO.',
    ':' : '..OO..',
    ';' : '..O.O.',
    '-' : '....OO',
    '/' : '.O..O.',
    '<' : '.OO..O',
    '>' : 'O..OO.',
    '(' : 'O.O..O',
    ')' : '.O.OO.',
    ' ' : '......'
    }

brailled = {
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..'
    }

a = ' '.join(sys.argv[1:])

result = ''


digit = False
convertToBraille = False

if bool(re.fullmatch("[O.]*", a)) == True:
    convertToBraille = True

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if value is not found

if convertToBraille == False:
    for i in a:
        if i.isspace() == True:
            digit = False
            result += str(braillea.get(i))
        elif i.isdigit() == True and digit == False:
            result += braillea.get('number follows')
            result += str(brailled.get(i))
            digit = True
        elif i.isdigit() == True and digit == True:
            result += str(brailled.get(i))
        elif digit == True and i == '.':
            result += braillea.get('decimal follows')
        elif i.isupper() == True:
            result += braillea.get('capital follows')
            result += str(braillea.get(i.lower()))
        #elif i.islower() == True:
        else:
            result += str(braillea.get(i))
else:
    n = 6
    b = [a[i:i+n] for i in range(0, len(a), n)]
    capital = None
    for i in b:
        keya = get_key_by_value(braillea, i)
        keyd = get_key_by_value(brailled, i)
        if keya == ' ':
            digit = False
            result += str(keya)
        elif keya == 'number follows': #number follows
            digit = True
        elif digit == True:
            result += str(keyd) #getting number
        elif capital == True:
            result += str(keya).upper() #getting capital letter
            capital = None
        elif keya == 'capital follows':
            capital = True
        else:
            result += str(keya) #getting letter

 
print(result)