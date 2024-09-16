import sys

braille_map = {
        'a': '0.....', 'b':'0.0...', 'c':'00....', 'd':'00.0..', 'e': '0..0..',
        'f': '000...', 'g': '0000..', 'h': '0.00..', 'i': '.00...', 'j': '.000..',
        'k': '0...0.', 'l': '0.0.0.', 'm': '00..0.', 'n': '00.00.', 'o': '0..00.',
        'p': '000.0.', 'q': '00000.', 'r': '0.000.', 's': '.00.0.', 't': '.0000.',
        'u': '0...00', 'v': '0.0.00', 'w': '.000.0', 'x': '00..00', 'y': '00.000', 'z': '0..000',
        ' ': '......',
        'cap': '.....0',
        'num': '.0.000'
}

english_map = { v: k for k,v in braille_map.items()}

for i, letter in enumerate('abcdefghij'):
    braille_map[str(i)] = braille_map[letter]
    english_map[braille_map[letter]] = str(i)

def is_braille(input_string):
    return all(char in '0.' for char in input_string)

def english_to_braille(text):
    braille = []
    for char in text:
        if char.isupper():
            braille.append(braille_map['cap'])
            braille.append(braille_map[char.lower()])
        elif char.isdigit():
            braille.append(braille_map['num'])
            braille.append(braille_map[char])
        elif char in braille_map:
            braille.append(braille_map[char])
        else:
            raise ValueError(f"Unsupported Character: {char}")
    return ''.join(braille)

def braille_to_english(braille):
    english = []
    i = 0
    capitalize_next = False
    number_mode = False

    number_map = {
        '.000..':'0','0.....': 'a', '0.0...': 'b', '00....': 'c', '00.0..': 'd', '0..0..': '5',
        '000...': '6', '0000..': '7', '0.00..': '8', '.00...': '9' 
    }

    while i < len(braille):
        chunk = braille[i:i+6]

        if chunk == braille_map['cap']:
            capitalize_next = True
            i+=6
            continue
        elif chunk == braille_map['num']:
            number_mode = True
            i+=6
            continue

        if chunk in english_map:
            char = english_map[chunk]
            if number_mode:
               if chunk in number_map:
                   char = number_map[chunk]
               else:
                    number_mode = False
                    char = english_map[chunk]
            else:
                number_mode = False

            if capitalize_next:
                char = char.upper()
                capitalize_next=False
            
            english.append(char)
        else:
            raise ValueError(f"Unsupported Braille chunk: {chunk}")
        i+=6
    return ''.join(english)

def main():
    if len(sys.argv) != 2:
        print("Usage: python braille_translator.py <text>")
        return
    
    input_string = sys.argv[1]

    if is_braille(input_string):
        translated = braille_to_english(input_string)
    else:
        translated = english_to_braille(input_string)

    print(translated)

if __name__ == "__main__":
    main()