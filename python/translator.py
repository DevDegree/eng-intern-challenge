
import sys

class Translator():
    # enlgish to braille translation
    english_to_braille_chars = {
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
        ' ': '......'
    }
    english_to_braille_nums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'O': '.OOO..'
    }
    # braille to english translation
    braille_to_english_chars = {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f',
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z',
    }
    braille_to_english_nums = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0'
    }
    def convert_braille_to_english(braille):
        if (len(braille) % 6) != 0:
            raise ValueError('The length of the braille must be a mutliple of 6')

        res = ''
        i = 0
        is_capital = False
        is_number = False

        while i < len(braille):
            char = braille[i:i+6]
            
            if char == '.....O':
                is_capital = True
                i += 6
                continue
            if char == '.O.OOO':
                is_number = True
                i +=6
                continue

            if char == '......':
                res += ' '
                is_number = False
            elif is_number:
                res += Translator.braille_to_english_nums.get(char, '?')
            elif is_capital:
                res += Translator.braille_to_english_chars.get(char, '?').upper()
                is_capital = False
            else:
                res += Translator.braille_to_english_chars.get(char, '?')
            i +=6
        return res
    
    def convert_english_to_braille (english_text):
        res = []

        for word in english_text:
            word_res = ''
            is_number = False
            for char in word:
                if char.isnumeric():
                    if not is_number:
                        word_res += '.O.OOO'
                        is_number = True
                    
                    word_res += Translator.english_to_braille_nums.get(char,'......')
                elif char.isupper():
                    word_res += '.....O'
                    word_res += Translator.english_to_braille_chars.get(char.lower(),'......')
                else:
                    word_res += Translator.english_to_braille_chars.get(char,'......')
            res.append(word_res) 

        message = '......'.join(res)
        return(message)
    
    def is_braille(input_str):
        for char in input_str:
            if char == '.' or char == 'O':
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    translator = Translator

    if (len(sys.argv)) > 1:
        if (translator.is_braille(sys.argv[1])):
            print(translator.convert_braille_to_english(sys.argv[1]))
        else:
            print(translator.convert_english_to_braille(sys.argv[1:]))
    else:
        print('Usage: python translator.py { <braille_message> | <text> } ')
