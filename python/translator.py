import sys

braille_dict = {
    'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 
    'e':'O..O..', 'f':'OOO...', 'g':'OOOO..', 
    'h':'O.OO..', 'i':'.OO...', 'j':'.OOO..', 'k':'O...O.',
    'l':'O.O.O.', 'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 
    'p':'OO.O.', 'q':'OOOOO.', 'r':'O.OOO.', 's':'.OO.O.',
    't':'.OOOO.', 'u':'O...OO', 'v':'O.O.OO', 'w':'.OOO.O', 
    'x':'OO..OO', 'y':'OO.OOO', 'z':'O..OOO', 
}

num_to_bra = {
    '1':'O.....', '2':'O.O...', '3':'OO....', '4':'OO.O..', 
    '5':'O..O..', '6':'OOO...', '7':'OOOO..', '8':'O.OO..', 
    '9':'.OO...', '0':'.OOO..'
}
braille_to_english = {v: k for k, v in braille_dict.items()}
braille_to_english['......'] = ' '
braille_to_num = {v: k for k, v in num_to_bra.items()}
def eng_braille(text):
        translation = []
        nums = False
        for char in text:
            if char == ' ':
                translation.append('......')
                nums = False
            elif nums:
                translation.append(num_to_bra.get(char))
            elif char.isupper():
                    translation.append('.....O')
                    char = char.lower()
                    translation.append(braille_dict.get(char))
            elif char.isdigit():
                translation.append('.O.OOO')
                nums = True
                translation.append(num_to_bra.get(char))
            else:
                braille = braille_dict.get(char)
                if braille:
                    translation.append(braille)
        return ''.join(translation)
                
def braille_eng(braille_text):
    braille_text = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    eng_translation = []
    nums =False
    caps = False
    for char in braille_text:
        if char == '......':
            eng_translation.append(' ')
            nums = False
        elif nums:
            eng_translation.append(braille_to_num.get(char))
        elif caps:
            capital = braille_to_english.get(char)
            capital = capital.upper()
            eng_translation.append(capital)
            caps = False
        elif char == '.....O':
            caps = True
        elif char == '.O.OOO':
            nums = True
        else:
            braille = braille_to_english.get(char)
            if braille:
                eng_translation.append(braille)
    return ''.join(eng_translation)
eng =False
def detect_lang(text):
    global eng
    for char in text:
        if char == 'O' or char == ".":
            pass
        else:
            eng = True
args = (sys.argv[1:])

input = ''
for arg in args:
    input += " " +arg
input = input[1:]
detect_lang(input)

if eng:
    output = (eng_braille(input))
    print(output)
else:
    output = (braille_eng(input))
    print(output)