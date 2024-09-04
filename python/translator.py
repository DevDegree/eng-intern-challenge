import sys
e_t_b ={ #english to braille mapping
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..','f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..','k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.','p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.','u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO','z': 'O..OOO', ' ': '......', '0': '.OOO..', '1': 'O.....', '2': 'O.O...', 
    '3': 'OO....', '4': 'OO.O..','5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...','capital': '.....O', 'number': '.O.OOO','.': '..OO.O', ',': '..O...', '?':
    '..O.OO', '!': '..OOO.', ':': '..OO..',';': '..O.O.', '-': '..O..O', '/': '.O..O.','<':'.OO.O',
    '>':'O.OO.O','(': 'O.O.OO', ')': '.O.OO.'
}
b_t_e={} #braile to english mapping
for i in e_t_b: 
    b_t_e[e_t_b[i]]=i
def is_b(inputStr):
    if (len(inputStr)<6):
        return 
    for i in inputStr:
        if i not in ['O', '.', ' ']:
            return False
    return True
def translate_to_braille(inputStr):
    ans = ""
    isNumber = False
    for i in inputStr:
        if i.isupper():
            ans += e_t_b['capital']
            ans += e_t_b[i.lower()]
        elif i.isdigit():
            if not isNumber:  
                ans += e_t_b['number']
                isNumber = True
            ans += e_t_b[i]
        else:
            if isNumber: 
                isNumber = False
            ans += e_t_b[i]
    
    return ans


def translate_to_english(inputStr):
    words =inputStr.split(' ')
    ans= ""
    isCaps = False 
    isNumber = False

    for i in words:
        j= 0
        while j < len(i):
            braille_char = i[j:j+6]
            if braille_char==e_t_b['capital']:
                isCaps = True
            elif braille_char==e_t_b['number']:
                isNumber = True
            else:
                letter = b_t_e.get(braille_char, '')
                if isNumber and letter.isdigit():
                    ans+=letter
                elif isCaps:
                    ans+=letter.upper()
                    isCaps=False
                else:
                    ans+=letter
            j+= 6
        ans+= ' '

    return ans.strip()

def main():
    if len(sys.argv) <2:
        sys.exit(1)
    input_text = " ".join(sys.argv[1:])
    if is_b(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))
if __name__ == "__main__":
    main()
