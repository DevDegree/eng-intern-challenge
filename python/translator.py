#Tolu Lawal
#Aug 31 2024
#SHOP ENG CHALLENGE

import sys

#Creating a braille to english dictonary, assuming there are special rule for the other 
# special charcters hence they are not included in this. Only Numbers letters and periods 
braille_lang= {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO..O', 'q': 'OOOO..', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO', 
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
    'capital': '.....O', 'num': '.O.OOO', 'decimal': '.O...O'
}


#reseving that dictonary for easy english to braille translation
reverse_braille_lang = {v: k for k, v in braille_lang.items()}
reverse_braille_lang[braille_lang['capital']] = 'CAPITAL'
reverse_braille_lang[braille_lang['num']] = 'NUM'
reverse_braille_lang[braille_lang['decimal']] = 'DECIMAL'
reverse_braille_lang.update({'O.....': 'a', 'O.O...': 'b','OO....': 'c', 'OO.O..': 'd',
                             'O..O..': 'e', 'OOO...': 'f','OOOO..': 'g', 'O.OO..': 'h',
                             '.OO...': 'i', '.OOO..': 'j'})



#creating a flag to see if braille is present 
def is_braille(inp):
    return all(c in 'O.' for c in inp)

#Creating a function 
def translate():
    inp = ' '.join(sys.argv[1:])
    if is_braille(inp):
        translated = []
        i = 0
        num_mode = False

        while i < len(inp):
            #reset revese braille lang to letters only
            reverse_braille_lang.update({'O.....': 'a', 'O.O...': 'b','OO....': 'c', 'OO.O..': 'd',
                             'O..O..': 'e', 'OOO...': 'f','OOOO..': 'g', 'O.OO..': 'h',
                             '.OO...': 'i', '.OOO..': 'j'})
            braille_char = inp[i:i+6]
            if braille_char == braille_lang['capital'] :
                # if  6 matching for capitilization, next will be capital or 
                i += 6
                braille_char = inp[i:i+6]

                #marking undefined english char with $
                
                translated.append(reverse_braille_lang.get(braille_char, '$').upper())
            elif braille_char == braille_lang['num']:
                # Enable number mode
                num_mode = True
            elif braille_char == braille_lang['decimal']:
                # Next character is a decimal point period
                i += 6
                translated.append('.')
                # #Turn number on because decimals only exist in numbers
                # num_mode = True
            elif braille_char == '......':  # Space resets number mode
                translated.append(' ')
                num_mode = False
            else:
                if num_mode: 
                    # Convert to number
                    reverse_braille_lang.update({'O.....': '1', 'O.O...': '2','OO....': '3', 'OO.O..': '4',
                             'O..O..': '5', 'OOO...': '6','OOOO..': '7', 'O.OO..': '8',
                             '.OO...': '9', '.OOO..': '0'})
                    num_char = reverse_braille_lang.get(braille_char, '$')
                    if num_char.isdigit():
                        translated.append(num_char)
                    else:
                        translated.append('$')
                else:
                    translated.append(reverse_braille_lang.get(braille_char, '$'))
            i += 6
        return ''.join(translated)
    
    else:
        # Translating in reverse from english to brialle, unknown chars respresented by $ 
        translated = []
        num_mode = False
        for eng_char in inp:
            if eng_char.isupper():
                translated.append(braille_lang['capital'])
                translated.append(braille_lang.get(eng_char.lower(), '$'))
            elif eng_char.isdigit():
                if not num_mode:
                    translated.append(braille_lang['num'])
                    num_mode = True
                translated.append(braille_lang.get(eng_char, '$'))
            elif eng_char == '.':
                translated.append(braille_lang['decimal'])
            else:
                translated.append(braille_lang.get(eng_char.lower(), '$'))
        return ''.join(translated)

if __name__ == "__main__":
        print(translate())