import sys

class Translator():
    "A class to translate between Braille and English."

    braille_to_english = {
        'letters': {
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
            'O..OOO': 'z'
        },
        'numbers': {
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
        },
        'characters': {
            '.....O': 'cf',
            '.O.OOO': 'nf',
            '......': ' '
        }
    }

    english_to_braille = {
        'letters': {
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
            'z': 'O..OOO'
        },
        'numbers': {
            '1': 'O.....',  
            '2': 'O.O...',
            '3': 'OO....',
            '4': 'OO.O..',
            '5': 'O..O..',
            '6': 'OOO...',
            '7': 'OOOO..',
            '8': 'O.OO..',
            '9': '.OO...',
            '0': '.OOO..'
        },
        'characters': {
            'cf': '.....O',
            'nf': '.O.OOO',
            ' ': '......'
        }
    }


    def braille_translator(self, input_str: str) -> str:
        "Translates a braille string into its english counterpart."

        i = 0
        num_follows = False 
        translated_str = ''

        while i < len(input_str):
            braille = input_str[i:i+6]

            assert(
                braille in self.braille_to_english['letters'] or 
                braille in self.braille_to_english['numbers'] or 
                braille in self.braille_to_english['characters']
            ), f"Braille '{braille}' is not supported."

            if not num_follows: 
                if braille in self.braille_to_english['characters']:
                    if self.braille_to_english['characters'][braille] == 'nf': 
                        num_follows = True
                        
                    elif self.braille_to_english['characters'][braille] == 'cf': 
                        i += 6
                        braille = input_str[i:i+6]
                        if braille in self.braille_to_english['letters']:
                            translated_str += self.braille_to_english['letters'][braille].upper()

                    elif self.braille_to_english['characters'][braille] == ' ':
                        translated_str += ' '
                        num_follows = False

                elif braille in self.braille_to_english['letters']:
                    translated_str += self.braille_to_english['letters'][braille]

            else: 
                if braille in self.braille_to_english['numbers']:
                    translated_str += self.braille_to_english['numbers'][braille]

                elif braille in self.braille_to_english['characters'] and self.braille_to_english['characters'][braille] == ' ':
                    translated_str += ' '
                    num_follows = False
            
            i += 6

        return translated_str

    def english_translator(self, input_str: str) -> str:
        "Translates and english string into its braille counterpart."

        i = 0
        firstNum = True
        translated_str = ''

        while i < len(input_str):
            character = input_str[i]

            assert(
                character.lower() in self.english_to_braille['letters'] or
                character in self.english_to_braille['numbers'] or 
                character in self.english_to_braille['characters']
            ), f"Character '{character}' is not supported."

            if character.lower() in self.english_to_braille['letters']:
                if character.isupper():
                    translated_str += '.....O'
                translated_str += self.english_to_braille['letters'][character.lower()]
                
            elif character in self.english_to_braille['numbers']:
                if firstNum:
                    translated_str += '.O.OOO'
                    firstNum = False               
                translated_str += self.english_to_braille['numbers'][character]

            elif character in self.english_to_braille['characters']:
                if character == ' ':
                    translated_str += self.english_to_braille['characters'][character]
                    firstNum = True

                else:
                    translated_str += self.english_to_braille['characters'][character]
            i += 1

        return translated_str
    

    def translate(self, s: str) -> str:
        "Determines if the string is in Braille or in English, and translates the input string to the other format."

        if len(s) < 6:
            return self.english_translator(s)

        is_braille = all(character in ('O', '.') for character in s) and len(s) % 6 == 0

        contains_O = all(character in ('O') for character in s)

        if contains_O:
            return self.english_translator(s)


        if is_braille:
            return self.braille_translator(s)
        else:
            return self.english_translator(s)
    


def main():
    input_strings = sys.argv[1:]  
    translator = Translator()
    finalStr = ''

    for i in range(len(input_strings)):
        translated = translator.translate(input_strings[i])    
        finalStr += translated 

        if i < (len(input_strings) - 1):
            finalStr += '......'

    print(finalStr)

if __name__ == '__main__':
    main()



