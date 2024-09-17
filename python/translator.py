import sys

class Transalate:
    
    def __init__(self):
        self.braille_alphabets = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
            'z': 'O..OOO',
            ' ': '......',
            }  
        self.number_prefix = '.O.OOO' 
        self.braille_capital = '.....O'
        self.braille_numbers = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
            '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
            }
        self.english_alphabets = {v: k for k, v in self.braille_alphabets.items()}
        self.english_numbers = {v: k for k, v in self.braille_numbers.items()}
        
    def braille_to_english(self,input_text):
        output_text = []
        is_number = False   
        i, j = 0, 6
        while j <= len(input_text):
            # space
            # print(input_text[i:j],)
            if input_text[i:j] == '......':
                output_text.append(' ')
                is_number = False
            # numbers
            elif input_text[i:j] == '.O.OOO':
                i += 6
                j += 6
                output_text.append(self.english_numbers[input_text[i:j]])
                is_number = True
            # capital
            elif is_number and input_text[i:j]:
                output_text.append(self.english_numbers[input_text[i:j]])
            elif input_text[i:j] == '.....O':
                i += 6
                j += 6
                output_text.append(self.english_alphabets[input_text[i:j]].upper())
            # alphabets
            else:
                output_text.append(self.english_alphabets[input_text[i:j]])
            # print(output_text)
            i += 6
            j += 6
            # print(output_text)
        return ''.join(output_text)
                
    def english_to_braille(self,input_text):
        output_text = []
        is_number = False
        for w in input_text:
            for char in w:
                if char.isupper():
                    output_text.append(self.braille_capital)
                    output_text.append(self.braille_alphabets[char.lower()])
                elif is_number:
                    output_text.append(self.braille_numbers[char])
                elif char.isdigit():
                    output_text.append(self.number_prefix)
                    output_text.append(self.braille_numbers[char])
                    is_number = True
                else:
                    output_text.append(self.braille_alphabets[char])
            if w != input_text[-1]:
                output_text.append(self.braille_alphabets[' '])
                is_number = False
        return ''.join(output_text).strip()
    
def is_braille(input_string):
    """Check if the input is in Braille format."""
    return all(c in 'O. ' for c in input_string) & (len(input_string) % 6 == 0)

def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Please provide the input text")
        input_text = sys.argv[1:]
        translator = Transalate()
        if is_braille(input_text[0]):
            print(translator.braille_to_english(input_text[0]))
            
        else:
            print(translator.english_to_braille(input_text)) 
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()
    
        