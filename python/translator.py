
import sys

b_to_e_special_chars = {'.....O':"cap", '......':" ", '.O.OOO':'num'}

braille_to_engl_dict = {'O.....':'a', 'O.O...':'b',
                        'OO....':'c', 'OO.O...':'d', 
                        'O..O..':'e', 'OOO...':'f', 
                        'OOOO..':'g', 'O.OO..':'h', 
                        '.OO...':'i', '.OOO..':'j',
                        'O...O.':'k', 'O.O.O.':'l',
                        'OO..O.':'m', 'OO.OO.':'n',
                        'O..OO.':'o', 'OOO.O.':'p',
                        'OOOOO.':'q', 'O.OOO.':'r',
                        '.OO.O.':'s', '.OOOO.':'t',
                        'O...OO':'u', 'O.O.OO':'v',
                        '.OOO.O':'w', 'OO..OO':'x',
                        'OO.OOO':'y', 'O..OOO':'z',
                        '..OO.O':'.', '..O...':',',
                        '..O.OO':'?', '..OOO.':'|',
                        '..OO..':':', '..O.O.':';',
                        '....OO':'-', '.O..O.':'/',
                        '.OO..O':'<', 'O..OO.':'>',
                        'O.O..O':'(', '.O.OO.':')'}

b_to_e_numbers = {'O.....':'1', 'O.O...':'2',
                'OO....':'3', 'OO.O...':'4', 
                'O..O..':'5', 'OOO...':'6', 
                'OOOO..':'7', 'O.OO..':'8', 
                '.OO...':'9', '.OOO..':'0'}


e_to_b_special_chars = {"cap":'.....O', "space":'......', 'num':'.O.OOO'}

engl_to_braille_dict = {'a': 'O.....', 'b': 'O.O...', 
                        'c': 'OO....', 'd': 'OO.O..', 
                        'e': 'O..O..', 'f': 'OOO...', 
                        'g': 'OOOO..', 'h': 'O.OO..', 
                        'i': '.OO...', 'j': '.OOO..', 
                        'k': 'O...O.', 'l': 'O.O.O.', 
                        'm': 'OO..O.', 'n': 'OO.OO.', 
                        'o': 'O..OO.', 'p': 'OOO.O.', 
                        'q': 'OOOOO.', 'r': 'O.OOO.', 
                        's': '.OO.O.', 't': '.OOOO.', 
                        'u': 'O...OO', 'v': 'O.O.OO', 
                        'w': '.OOO.O', 'x': 'OO..OO', 
                        'y': 'OO.OOO', 'z': 'O..OOO',
                        '.': '..OO.O', ',': '..O...',
                        '?': '..O.OO', '|': '..OOO.', 
                        ':': '..OO..', ';': '..O.O.', 
                        '-': '....OO', '/': '.O..O.', 
                        '<': '.OO..O', '>': 'O..OO.', 
                        '(': 'O.O..O', ')': '.O.OO.'}

e_to_b_numbers = {'1': 'O.....', '2': 'O.O...', 
                '3': 'OO....', '4': 'OO.O..', 
                '5': 'O..O..', '6': 'OOO...', 
                '7': 'OOOO..', '8': 'O.OO..', 
                '9': '.OO...', '0': '.OOO..'}

def check_for_braille(text):
    if all(i in '.O' for i in text): 
        return True
    return False

def translate_braille_to_engl(text):
    ans = [] # return value
    capital = False # equals True if next value should be capitalized
    num = False # is true until a space is seen in the string
    
    for i in range(0, len(text), 6):
        if num:
            if text[i:i+6] in b_to_e_special_chars: # spots a space after num is True, ending numbers segment
                num = False
                ans.append(b_to_e_special_chars[text[i:i+6]])
            else:
                ans.append(b_to_e_numbers[text[i:i+6]])
        else:
            if text[i:i+6] in b_to_e_special_chars:
                if b_to_e_special_chars[text[i:i+6]] == 'cap': # capitalizes the next letter
                    capital = True
                elif b_to_e_special_chars[text[i:i+6]] == 'num': # beings sequence of numbers
                    num = True
                else:
                    ans.append(b_to_e_special_chars[text[i:i+6]])
            elif text[i:i+6] in braille_to_engl_dict:
                if capital: # adds capital
                    ans.append(braille_to_engl_dict[text[i:i+6]].upper())
                    capital = False
                else:
                    ans.append(braille_to_engl_dict[text[i:i+6]])
                
    return ''.join(ans)
        
def translate_engl_to_braille(text):
    ans = []
    curr_nums = False # equals true if numbers are being dealt with

    for i in text:
        if i == " ":
            if curr_nums == True: # space has been seen after numbers, back to letters
                curr_nums = False
            ans.append(e_to_b_special_chars['space'])

        if i.lower() in engl_to_braille_dict:
            if i.isupper():
                ans.append(e_to_b_special_chars['cap'])
                ans.append(engl_to_braille_dict[i.lower()])
            else:
                ans.append(engl_to_braille_dict[i.lower()])
            continue

        if i.isdigit(): 
            if not curr_nums: # starts sequence of numbers if not already started
                curr_nums = True
                ans.append(e_to_b_special_chars['num'])
            ans.append(e_to_b_numbers[i])
            
    return ''.join(ans)

def main():
    if len(sys.argv[1:]) > 1:
        text = ' '.join(sys.argv[1:])
    if check_for_braille(text): 
        print(translate_braille_to_engl(text))
    else:
        print(translate_engl_to_braille(text))

if __name__ == "__main__":
    main()
