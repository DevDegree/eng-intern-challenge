
import sys

# Braille mapping 
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'cap': '.....O', 'num': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse dictionary for English lookup
english_dict = {v: k for k, v in braille_dict.items()}

def braille_english(braille_text):
    words = braille_text.split(' ')
    translated = []
    is_number = False
    for word in words:
        chars = [word[i:i+6] for i in range(0, len(word), 6)]
        translated_word = []
        for ch in chars:
            if ch == '.....O':  # Capitalization
                continue  # Handle in next iteration
            elif ch == '.O.OOO':  # Number indicator
                is_number = True
                continue
            else:
                if ch in english_dict:
                    translated_char = english_dict[ch]
                    if is_number and translated_char.isdigit():
                        is_number = False
                    translated_word.append(translated_char.upper() if '.....O' in chars else translated_char)
                else:
                    translated_word.append('?')  # Unknown character
        translated.append(''.join(translated_word))
    return ' '.join(translated)

def english_braille(english_text):
    translated = []
    for ch in english_text:
        if ch.isdigit():
            translated.append(braille_dict['num'] + braille_dict[ch])
        elif ch.isalpha() and ch.isupper():
            translated.append(braille_dict['cap'] + braille_dict[ch.lower()])
        else:
            translated.append(braille_dict[ch.lower()])
    return ' '.join(translated)

def check_translate(input_text):
    if set(input_text) <= {'O', '.', ' '}:
        return braille_english(input_text)
    else:
        return english_braille(input_text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translator.py '<input_text>'")
        sys.exit(1)
    
    input_text = sys.argv[1]
    print(check_translate(input_text))
