import sys
englishToBraille = {
    'capital': '.....O',
    'space': '......',
    'decimal': '.O...O',
    'number': '.O.OOO',
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    '.': '..OO.O',
}

brailleToEnglish = {v: k for k, v in englishToBraille.items()}

def is_braille(text):
    return all(c in 'O.' for c in text)

def toEnglish(braille):
    result = []
    braille_chars = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    is_capital = False
    is_number = False

    for braille_char in braille_chars:
        if braille_char == '.....O':
            is_capital = True
            continue
        if braille_char == '.O.OOO':
            is_number = True
            continue
        if braille_char == '.O...O':
            result.append('.')
            continue
        else:
            character = brailleToEnglish[braille_char]
            if character == " ":
                is_number = False
            elif is_number:
                 character = str(ord(character) - ord('a') + 1) if character != 'j' else '0'
                
            elif is_capital:
                character = character.upper()
                is_capital = False
            result.append(character)
    return "".join(result)

def to_braille(text):
    result = []
    is_number = False
    for i, char in enumerate(text):
        if char.isupper():
            result.append(englishToBraille['capital'])
            result.append(englishToBraille[char.lower()])
            is_number = False
        elif char.isdigit():
            if not is_number:
                result.append('.O.OOO')
                is_number = True
            mapped_char = chr(ord('a') + int(char) - 1) if char != '0' else 'j'
            result.append(englishToBraille[mapped_char])
        elif char == '.':
            if is_number and i > 0 and text[i - 1].isdigit():
                result.append(englishToBraille['decimal'])
            else:
                result.append(englishToBraille['.'])
        elif char == " ":
            result.append(englishToBraille[' '])
            is_number = False
            
        elif char in englishToBraille:
            result.append(englishToBraille[char])

    return "".join(result)

            
        
def main():
    input_text = input_text = " ".join(sys.argv[1:])

    if is_braille(input_text):
        print(toEnglish(input_text))
    else:
        print(to_braille(input_text))

        
if __name__ == "__main__":
    main()       



    