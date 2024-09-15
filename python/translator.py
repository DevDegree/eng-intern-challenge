import sys

braille_to_english_dict = {
    'O.....': 'a', '.....OO.....': 'A',
    'O.O...': 'b', '.....OO.O...': 'B',
    'OO....': 'c', '.....OOO....': 'C',
    'OO.O..': 'd', '.....OOO.O..': 'D',
    'O..O..': 'e', '.....OO..O..': 'E',
    'OOO...': 'f', '.....OOOO...': 'F',
    'OOOO..': 'g', '.....OOOOO..': 'G',
    'O.OO..': 'h', '.....OO.OO..': 'H',
    '.OO...': 'i', '.....O.OO...': 'I',
    '.OOO..': 'j', '.....O.OOO..': 'J',
    'O...O.': 'k', '.....OO...O.': 'K',
    'O.O.O.': 'l', '.....OO.O.O.': 'L',
    'OO..O.': 'm', '.....OOO..O.': 'M',
    'OO.OO.': 'n', '.....OOO.OO.': 'N',
    'O..OO.': 'o', '.....OO..OO.': 'O',
    'OOO.O.': 'p', '.....OOOO.O.': 'P',
    'OOOOO.': 'q', '.....OOOOOO.': 'Q', 
    'O.OOO.': 'r', '.....OO.OOO.': 'R',
    '.OO.O.': 's', '.....O.OO.O.': 'S',
    '.OOOO.': 't', '.....O.OOOO.': 'T',
    'O...OO': 'u', '.....OO...OO': 'U',
    'O.O.OO': 'v', '.....OO.O.OO': 'V',
    '.OOO.O': 'w', '.....O.OOO.O': 'W',
    'OO..OO': 'x', '.....OOO..OO': 'X',
    'OO.OOO': 'y', '.....OOO.OOO': 'Y',
    'O..OOO': 'z', '.....OO..OOO': 'Z',
    '.O...O': '.',    
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    # 'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' ',
    
    '.O.OOO': '#' # number sign, # is used as a special character 
                  # to indicate that the following characters are numbers
}
braille_to_number_dict = {
    '......': ' ',
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
}

def braille_to_english(braille_text):
    '''
    Idea:
    try to convert the braille text to english with 6 braile characters
    if it fails, try with 6 extra characters, along with the first 6; totaling 12
    '''
    english = ""
    i = 0
    numberMode = False
    while(i < len(braille_text)):
        if numberMode:
            # When a Braille number follows symbol is read, assume all following 
            # symbols are numbers until the next space symbol.
            character = braille_to_number_dict.get(braille_text[i:i+6], '')
            if character == ' ':
                numberMode = False
            
            english += character
        
        else:
            character = braille_to_english_dict.get(braille_text[i:i+6], '')
            if character == '':
                english += braille_to_english_dict.get(braille_text[i:i+12], '')
                i += 6
            elif character == '#':
                numberMode = True
                i += 6
                continue
            else:
                english += character
            
        i += 6
                
    return english
    
def english_to_braille(english_text):    
    english_to_braille_dict = {value: key for key, value in braille_to_english_dict.items()}
    number_to_braille_dict = {value: key for key, value in braille_to_number_dict.items()}

    braille_text = ""
    prevCharNum = False
    for char in english_text:
        if char.isdigit():
            if not prevCharNum:
                braille_text += english_to_braille_dict['#']
                prevCharNum = True
            braille_text += number_to_braille_dict[char]
        else:
            prevCharNum = False
            braille_text += english_to_braille_dict.get(char, '')
    
    return braille_text

def is_brail(text):
    for char in text:
        if (char != '.' and char != 'O'):
            return False
    return True


text = ' '.join(sys.argv[1:])
if is_brail(text):
    print(braille_to_english(text))
else:
    print(english_to_braille(text))
