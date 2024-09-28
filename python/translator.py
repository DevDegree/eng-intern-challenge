import argparse

class English_to_Braille:
    # Braille mapping
    braille_dict = {
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
        ' ': '......',  # Space
        # Capital prefix
        '^': '.....O',  # Use this before any capitalized letter
        # Numbers prefix (for digits)
        '#': '.O.OOO',
        '0': '.OOO..',  # Same as "j"
        '1': 'O.....',  # Same as "a"
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
    }

    def __init__(self, input_text) -> None:
        self.input_text = input_text

    def preprocess(self):
        preprocessed_text = ""
        hashtag_inserted = False
        for i in range(len(self.input_text)):
            if not hashtag_inserted and self.input_text[i].isdigit():
                preprocessed_text += "#"
                hashtag_inserted = True
            elif self.input_text[i] == ' ':
                hashtag_inserted = False
            if self.input_text[i].isupper():
                preprocessed_text += "^"
            preprocessed_text += self.input_text[i].lower()
        return preprocessed_text

    def process(self, preprocessed_text):
        output = ""
        for i in range(len(preprocessed_text)):
            if preprocessed_text[i] in self.braille_dict:
                output += self.braille_dict[preprocessed_text[i]]
        return output
    
    def translate(self):
        return self.process(self.preprocess())
    
class Braille_to_English():
    inverse_braille_dict = {
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
        '......': ' ',  # Space
        '.....O': '^',  # Capital prefix
        '.O.OOO': '#',  # Numbers prefix not needed for reverse
    }
    alpha_numeric = {
        'j': '0', 
        'a': '1',
        'b': '2', 
        'c': '3',
        'd': '4', 
        'e': '5',
        'f': '6',
        'g': '7', 
        'h': '8',
        'i': '9',
    }
    
    def __init__(self, input_text) -> None:
        self.input_text = input_text
    
    def process(self):
        output = ""
        for i in range(0, len(self.input_text), 6):
            if self.input_text[i:i+6] in self.inverse_braille_dict:
                output += self.inverse_braille_dict[self.input_text[i:i+6]]
        return output
    
    def postprocess(self, output_text):
        post_output = ""
        is_capital = False
        is_numbers = False
        for i in range(len(output_text)):
            if(output_text[i] == '^'):
                is_capital = True
            elif(is_capital):
                post_output += output_text[i].upper()
                is_capital = False
            elif(output_text[i] == '#'):
                is_numbers = True
            elif(output_text[i] == ' '):
                post_output += ' '
                is_numbers = False
            elif(is_numbers):
                post_output += self.alpha_numeric[output_text[i]]
            else:
                post_output += output_text[i]
        return post_output
    
    def translate(self):
        return self.postprocess(self.process())
            
class Translator():
    def __init__(self, input_text) -> None:
        self.input_text = input_text
    
    def is_braille(self):
        return all(char in 'O. ' for char in self.input_text)
    
    def translate(self):
        if self.is_braille():
            return Braille_to_English(self.input_text).translate()
        else:
            return English_to_Braille(self.input_text).translate()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_text', nargs=argparse.REMAINDER, type=str)

    args = parser.parse_args()

    input_text = ' '.join(args.input_text)

    translator = Translator(input_text)
    result = translator.translate()
    print(result)

if __name__ == '__main__':
    main()




