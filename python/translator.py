import sys

#dicts for mapping text/braille
normal_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

inverse_normal_braille_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 
    'O..OOO': 'z',
    '......': ' ', '.....O': 'capital', '.O.OOO': 'number'
}

num_braille_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
}

inverse_num_braille_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    '......': ' '
}


#converts braille to text output
def braille2text(braille_str):
    text = ""
    capital = False
    number = False

    for pos in range(0, len(braille_str), 6):
        bchar = braille_str[pos:pos+6]
        if not number:
            conv = inverse_normal_braille_dict[bchar]
            if conv == 'number':
                number = True
            elif conv == 'capital':
                capital = True
            else:
                if capital:
                    text += conv.upper()
                    capital = False
                else:
                    text += conv
        else:
            conv = inverse_num_braille_dict[bchar]
            if conv == ' ':
                number = False
            text += conv

    print(text) 


#converts text to braille output
def text2braille(text):
    braille = ""
    number = False
    for char in text:
        if char.isupper():
            braille += normal_braille_dict['capital']
            braille += normal_braille_dict[char.lower()]
        elif char.isnumeric():
            if number:
                braille += num_braille_dict[char]
            else:
                number = True
                braille += normal_braille_dict['number']
                braille += num_braille_dict[char]
        elif char == ' ':
            number = False
            braille += normal_braille_dict[char]
        else:
            braille += normal_braille_dict[char]
    print(braille)

def main():
    if len(sys.argv) > 2:
        text2braille(" ".join(sys.argv[1:]))
    elif len(sys.argv[1]) % 6 == 0 and sys.argv[1].count(".") + sys.argv[1].count("O") == len(sys.argv[1]):
        braille2text(sys.argv[1])
    else: 
        text2braille(" ".join(sys.argv[1:]))

if __name__ == '__main__':
    main()