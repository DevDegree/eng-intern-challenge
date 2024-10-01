import sys

trans_to_Letters = {
    'O.....':'a', 'O.O...':'b', 'OO....':'c', 'OO.O..':'d', 'O..O..':'e', 'OOO...':'f',
    'OOOO..':'g', 'O.OO..':'h', '.OO...':'i', '.OOO..':'j', 'O...O.':'k', 'O.O.O.':'l',
    'OO..O.':'m', 'OO.OO.':'n', 'O..OO.':'o', 'OOO.O.':'p', 'OOOOO.':'q', 'O.OOO.':'r',
    '.OO.O.':'s', '.OO.O.':'s', '.OOOO.':'t', 'O...OO':'u', 'O.O.OO':'v', '.OOO.O':'w',
    'OO..OO':'x', 'OO.OOO':'y', 'O..OOO':'z', '......':' ', '.....O':'cap', '.O...O':'deci',
    '.O.OOO':'num'
}
trans_to_Numbers = {
    'O.....':'1', 'O.O...':'2', 'OO....':'3', 'OO.O..':'4', 'O..O..':'5', 'OOO...':'6',
    'OOOO..':'7', 'O.OO..':'8', '.OO...':'9', '.OOO..':'0'
}

letters_to_braille = {i:j for j, i in trans_to_Letters.items()}
nums_to_braille = {i:j for j, i in trans_to_Numbers.items()}

def isBraille(input):
    brailles = {'0','.'}
    for c in input:
        if c not in brailles:
            return False
    return True

def translate_to_english(input):
    brailles = [input[i:i+6] for i in range(0, len(input), 6)]
    english = []
    isCap = isNum = False
    for c in brailles:
        translated = trans_to_Letters[c]
        if isCap:
            translated = translated.upper()
            isCap = False
        elif isNum:
            translated = trans_to_Numbers[c]
            
        if translated == ' ':
            isNum = False
        elif translated == 'cap':
            isCap = True
        elif translated == 'num':
            isNum = True
            continue
        english.append(translated)
    return "".join(english)

def translate_to_braille(input):
    brailles = []
    isNum = False
    for c in input:
        if c == ' ':
            isNum = False
        if c.isupper():
            brailles.append(letters_to_braille['cap'])
            c = c.lower()
        
        if not isNum and c.isdigit():
            brailles.append(letters_to_braille['num'])
            brailles.append(nums_to_braille[c])
            isNum = True
        elif isNum and c.isdigit():
            brailles.append(nums_to_braille[c])
        else:
            brailles.append(letters_to_braille[c])
    return "".join(brailles)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You must provide an input")
    
    user_input = ' '.join(sys.argv[1:])
    
    if isBraille(user_input):
        print(translate_to_english(user_input))
    else:
        print(translate_to_braille(user_input))
