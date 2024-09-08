import sys

#  brail dictionary
toBrail = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', ',': '..OO.O', '.': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', 
    ' ': '......',
}

#shows a special char comes next
brailSpecial = {
    '.....O': 'CAPITAL',
    '.O.OOO': 'NUMBER',
}

#shows a special char comes next
engSpecial = {
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO',
}

toEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '..OO.O': ',', '..O...': '.', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';',
    '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')', '......': ' ', '.O...O': '.',
}

engNums = {
    '.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '......': ' ',
}

def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

#trans from braille to english
def braille_to_english(braille):
    result = []
    is_capital = False
    is_number = False
    
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        
        if symbol in brailSpecial:
            if brailSpecial[symbol] == 'CAPITAL':
                is_capital = True
            elif brailSpecial[symbol] == 'NUMBER':
                is_number = True
            continue
        
        if is_number:
            char = engNums.get(symbol, ' ')
            if char == ' ':
                is_number = False
        else:
            char = toEnglish.get(symbol, ' ')
        
        if is_capital:
            char = char.upper()
            is_capital = False
        
        result.append(char)
    
    return ''.join(result)

#trans from english to braille
def english_to_braille(text):
    result = []
    is_number = False
    
    for char in text:
        if char.isupper():
            result.append(engSpecial['CAPITAL'])
            char = char.lower()
        
        if char.isdigit():
            if not is_number:
                result.append(engSpecial['NUMBER'])
                is_number = True
        elif is_number:
            is_number = False
        
        if char in toBrail:
            result.append(toBrail[char])
        else:
            result.append(toBrail[' '])
    
    return ''.join(result)

def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_to_translate>")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))