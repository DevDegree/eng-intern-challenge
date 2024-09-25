import sys

english_to_braille_map = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OO.OO",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    '0': '.OOO..',
    '1': 'O.....', 
    '2': 'O.O...',
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...',
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    ' ': '......',
    'number': '.O.OOO', 
    'capital': '.....O', 
}

braille_to_english = {v: k for k, v in english_to_braille_map.items()}

def translate_to_braille(text):
    b_text = []
    is_num = False

    for char in text:
        if char.isdigit():
            b_text.append(english_to_braille_map['number'])
            is_num = True
        elif not char.isdigit():
            is_num = False

        if char.isupper():
            b_text.append(english_to_braille_map['capital'])

        b_text.append(english_to_braille_map[char.lower()])

    return ''.join(b_text)

def translate_to_english(b_word):
    b_cells = [b_word[i:i + 6] for i in range(0, len(b_word), 6)]
    text = []
    is_num = False
    is_caps = False

    for cell in b_cells:
        if cell == english_to_braille_map['number']:
            is_num = True
            continue
        elif cell == english_to_braille_map['capital']:
            is_caps = True
            continue

        if is_num and cell in english_to_braille_map:
            text.append(english_to_braille_map[cell]) 
        elif cell in english_to_braille_map:
            letter = english_to_braille_map[cell].upper() if is_caps else english_to_braille_map[cell]
            text.append(letter)

        if cell == english_to_braille_map[' ']:
            is_num = False

        is_caps = False

    return ''.join(text)

def detect_input_type(input_string):
    
    if all(char in '.O' for char in input_string) and len(input_string) % 6 == 0:
        return "braille" 
    else:
        return "english"
    
def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate. The command is: python3 translator.py <string>")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == "braille":
        result = translate_to_english(input_string)
    elif input_type == "english":
        result = translate_to_braille(input_string)

    print(result)

if __name__ == "__main__":
    main()