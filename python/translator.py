from sys import argv

class Translator:
    def __init__(self):
        self.alphabet = {'A': 'O.....', 'B': 'O.O...', 'C': 'OO....',
                         'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...',
                         'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...',
                         'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.',
                         'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
                         'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.',
                         'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO',
                         'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO',
                         'Y': 'OO.OOO', 'Z': 'O..OOO', '1': 'O.....',
                         '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
                         '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
                         '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
                         '.': '..OO.O', ',': '..O...', '?': '..O.OO',
                         '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
                         '-': '....OO', '/': '.O..O.', '<': '.OO..O',
                         '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
                         ' ': '......'}

    def translate(self, text):
       pass

def main():
    if len(argv) > 1:
        translator = Translator()
        
    else:
        pass
    
if __name__ == '__main__':
    main()