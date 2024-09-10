import sys

dic_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'O.OO.O': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.O.O': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'O.OOOO': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'CAPS', '.O.OOO': 'NUM', '......': 'SPACE'
}

letters_to_num = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                   'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10'
}

# we are able to make bi-directional mappings using the following
# technique because (English - braille) and (letters to numbers) are one to one transformations
dic_to_braille = {value: key for key, value in dic_to_english.items()}
num_to_letters = {value: key for key, value in letters_to_num.items()}

# determines whether to do a braille - English translation or vice versa
# returns 1 if input is braille, 0 if English
def check_input(s):
    if len(s) % 6 != 0:
        return 0
    for char in s:
        if char not in 'O.':
            return 0
    return 1

def braille_to_english(s):
    if not s: 
        return ''
    
    output = ''
    i = 0
    caps = False
    num = False

    while i < len(s):
        seq = s[i:i+6] # single braille character
        translate = dic_to_english[seq]

        if translate == 'CAPS':
            caps = True
        elif translate == 'NUM':
            num = True
        else:
            if caps:
                translate = translate.upper()
                caps = False
            if translate == 'SPACE':
                translate = ' '
                num = False
            if num:
                translate = letters_to_num[translate]
            
                
            output += translate
        i = i + 6
    return output


def english_to_braille(s):
    if not s:
        return ''
    
    output = ''
    num = False

    for char in s:
        # look at capital, number and space special characters
        if char.isupper():
            output += dic_to_braille['CAPS']
            char = char.lower()
            output += dic_to_braille.get(char, '').upper()
        elif char in '0123456789':
            if not num:
                output += dic_to_braille['NUM']
                num = True
            letter = num_to_letters[char]
            output += dic_to_braille[letter]
        elif char == ' ':
            output += dic_to_braille['SPACE']
            num = False 
        else:
            # add to string builder
            output += dic_to_braille.get(char, '')
            num_mode = False

    return output


def main():
    if len(sys.argv) < 2:
        print("Requires arguments")
        return
    
    input = ' '.join(sys.argv[1:])
    # print(input)

    if check_input(input) == 0:
        # English to braille
        s = english_to_braille(input)
    else:
        # braille to English
        s = braille_to_english(input)
    print(s)

if __name__ == "__main__":
    main()
