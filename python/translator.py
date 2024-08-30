import sys

eng_to_b = {
    'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 'e':'O..O..', 'f':'OOO...', 'g':'OOOO..', 'h':'O.OO..',
    'i':'.OO...', 'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.', 'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 'p':'OOO.O.',
    'q':'OOOOO.', 'r':'O.OOO.', 's':'.OO.O.', 't':'.OOOO.', 'u':'O...OO', 'v':'O.O.OO', "w":'.OOO.O', 'x':'OO..OO',
    'y':'OO.OOO', 'z':'O..OOO', '1':'O.....', '2':'O.O...', '3':'OO....', '4':'OO.O..', '5':'O..O..', '6':'OOO...',
    '7':'OOOO..', '8':'O.OO..', '9':'.OO...', 'O':'.OOO..', 'cap':'.....O', 'dec':'.O...O', 'num':'.O.OOO', '.':'..OO.O',
    ',':'..O...', '?':'..O.OO', '!':'..OOO.', ':':'..OO..', ';':'..O.O.', '-':'....OO', '/':'.O..O.', '<':'.OO..O',
    '>':'.OO..O', '(':'O.O..O', ')':'.O.OO.', ' ':'......'
}

b_to_eng ={}
for key, value in eng_to_b.items():
    if value in b_to_eng:
        b_to_eng[value].append(key)
    else:
        b_to_eng[value] = [key]

def is_text_braille(text):
    for char in text:
        if char not in 'O.':
            return False
    return True

def english_to_braille(text):
    res = []
    is_number = False

    for char in text:
        if char.isalpha():
            is_number = False
            if char.isupper():
                res.append(eng_to_b['cap'])
                char = char.lower()
            res.append(eng_to_b[char])
        elif char.isdigit():
            if is_number == False:
                is_number = True
                res.append(eng_to_b['num'])
            res.append(eng_to_b[char])
        else:
            res.append(eng_to_b[char])

    return ''.join(res)

def braille_to_english(braille):
    res = []
    i = 0
    is_number = False

    while i < len(braille):
        brailleChar = braille[i:i+6]
        
        if brailleChar == eng_to_b['cap']:
            nextChar = braille[i+6:i+12]
            res.append(b_to_eng[nextChar][0].upper())
            i += 12
        elif brailleChar == eng_to_b['num']:
            is_number = True
            i += 6
        elif brailleChar == "......":
            res.append(' ')
            is_number = False
            i += 6
        else:
            nextChar = b_to_eng[brailleChar]
            if is_number:
                res.append(nextChar[1])
            else:
                is_number = False
                res.append(nextChar[0])
            i += 6
    
    return ''.join(res)


def main():
    inputString = " ".join(sys.argv[1:])

    if is_text_braille(inputString):
        print(braille_to_english(inputString))
    else:
        print(english_to_braille(inputString))

if __name__ == "__main__":
    main()

