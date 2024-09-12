import sys

# Conversion dict of English to Braille 
brai_conv= {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO',

    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', ' ': '......','.' : '..OO.O',
    ',' : '..O...','?':'..O.OO','!' : '..OOO.',':':'..OO..','-':'....OO', '/': '.O..O.','<':
        '.OO..O','>':'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
}
#Conversion dict Braille to English
eng_conv_alp = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y',
    'O..OOO': 'Z' , '......': ' ', '..OO.O': '.',
    '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
}
eng_conv_num = {'.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9'}

#Detecting the input string language
def detect_lang(given_str):
    st = given_str.replace(' ', '')
    if all(c in 'O.' for c in st):
        return 'braille'
    else:
        return 'english'

def eng_to_brai(text):
    braille = []
    is_num = False
    for char in text:
        if char.isdigit():
            if not is_num:
                braille.append('.O.OOO')
                is_num = True
            braille.append(brai_conv[char])
        elif char == ' ':
            braille.append('......')
            is_num = False
        else:
            if is_num:
                is_num = False
            if char.isupper():
                braille.append('.....O')
                braille.append(brai_conv[char.upper()])
            else:
                braille.append(brai_conv.get(char.upper(), '......'))

    return ''.join(braille)

# Converting from Braille to English
def brai_to_eng(brai_text):
    english = []
    is_capital = False  #indicating if the next character should be capitalized
    is_num = False  #indicating if we are in "number mode"

    #As each char in Brai indicates 6 dots, we are processing them in chunks of 6
    for i in range(0, len(brai_text), 6):
        brai_char = brai_text[i:i + 6]

        if brai_char == '......':  # indicates space
            english.append(' ')
            is_num = False  # Reset number mode after space
        elif brai_char == '.....O':  #indicates captical letter
            is_capital = True  # Set flag to capitalize the next letter
        elif brai_char == '.O.OOO':  # Number followed by symbol
            is_num = True  # Set number mode until a space is encountered
        else:
            if is_num:  #we will map braille to digits if the input is in number mode
                english.append(eng_conv_num[brai_char])
            else:
                letter = eng_conv_alp[brai_char]  # Converting braille to letter
                if is_capital:  # Capitalizing the next letter if flag is set
                    letter = letter.upper()
                    is_capital = False  # Resets capitalization flag after one letter
                    english.append(letter)
                else:
                    letter = letter.lower()
                    english.append(letter)
    return ''.join(english)

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    given_str = ' '.join(sys.argv[1:])
    a = detect_lang(given_str)
    if a == 'english':
        print(eng_to_brai(given_str))
    else:
        print(brai_to_eng(given_str))
if __name__ == '__main__':
    main()