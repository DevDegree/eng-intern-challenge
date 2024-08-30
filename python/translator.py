import sys

braille_to_english = {
    '100000': 'a', '101000': 'b', '110000': 'c', '110100': 'd', '100100': 'e',
    '111000': 'f', '111100': 'g', '101100': 'h', '011000': 'i', '011100': 'j',
    '100010': 'k', '101010': 'l', '110010': 'm', '110110': 'n', '100110': 'o',
    '111010': 'p', '111110': 'q', '101110': 'r', '011010': 's', '011110': 't',
    '100011': 'u', '101011': 'v', '011101': 'w', '110011': 'x', '110111': 'y',
    '100111': 'z', '001000': ' ', '000001': '0', '001001': '1', '001010': '2',
    '001011': '3', '001100': '4', '001101': '5', '001110': '6', '001111': '7',
    '000111': '8', '000110': '9'
}

english_to_braille = {
    'a': '100000', 'b': '101000', 'c': '110000', 'd': '110100', 'e': '100100',
    'f': '111000', 'g': '111100', 'h': '101100', 'i': '011000', 'j': '011100',
    'k': '100010', 'l': '101010', 'm': '110010', 'n': '110110', 'o': '100110',
    'p': '111010', 'q': '111110', 'r': '101110', 's': '011010', 't': '011110',
    'u': '100011', 'v': '101011', 'w': '011101', 'x': '110011', 'y': '110111',
    'z': '100111', ' ': '001000', '0': '000001', '1': '001001', '2': '001010',
    '3': '001011', '4': '001100', '5': '001101', '6': '001110', '7': '001111',
    '8': '000111', '9': '000110'
}

def english_to_braille_func(text):
    braille = []
    for char in text.lower():
        if char in english_to_braille:
            braille.append(english_to_braille[char])
        else:
            braille.append('000000')  
    return ' '.join(braille)

def braille_to_english(text):
    english = []
    braille_chars = text.split(' ')
    for braille_char in braille_chars:
        if braille_char in braille_to_english:
            english.append(braille_to_english[braille_char])
        else:
            english.append('?') 
    return ''.join(english)

def is_braille(text):
    return all(c in 'O.' for c in text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string>")
        return

    input_text = sys.argv[1]

    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille_func(input_text))

if __name__ == "__main__":
    main()
