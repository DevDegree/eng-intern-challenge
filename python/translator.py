import sys

class Translator:
    def __init__(self, input_string) -> None:
        self.alpha_braille_dictionary = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 
            ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
            '/': '.O..O.', '<': '.OO...O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
            'Capital': '.....O', 'Decimal': '.O...O', 'Number': '.O.OOO',
        }
        self.digit_braille_dictionary = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        }
        self.input_string = input_string

    def is_braille(self):
        # if the string only consists of 0 and . then it must be a braille string
        return all(char in '.O' for char in self.input_string)
    
    def translate_braille_to_en(self):
        # this function will take in a braille sentence and convert them into an english sentence for each block of six braille characters
        braille_sentence = self.input_string
        reverse_alpha_braille_dict = {v: k for k, v in self.alpha_braille_dictionary.items()}
        reverse_digit_braille_dict = {v: k for k, v in self.digit_braille_dictionary.items()}
        english_sentence = []
        i = 0
        while i < len(braille_sentence):
            current_string = braille_sentence[i:i+6]
            current_braille_en = reverse_alpha_braille_dict[current_string]
            if current_braille_en == 'Capital':
                i+=6
                next_braille_string = braille_sentence[i:i+6]
                next_braille_en = reverse_alpha_braille_dict[next_braille_string].upper()
                english_sentence.append(next_braille_en)
            elif current_braille_en == 'Number':
                i += 6
                while i < len(braille_sentence) and braille_sentence[i:i+6] in reverse_digit_braille_dict:
                    next_braille_string = braille_sentence[i:i+6]
                    next_braille_en = reverse_digit_braille_dict[next_braille_string]
                    english_sentence.append(next_braille_en)
                    i+=6
                    if(next_braille_en == ' '): # keep adding numbers until encountering a space
                        break
            else: # we encounter a normal character
                next_braille_string = braille_sentence[i:i+6]
                next_braille_en = reverse_alpha_braille_dict[next_braille_string]
                english_sentence.append(next_braille_en)
            i+=6
        return ''.join(english_sentence)

    def translate_english_to_braille(self):
        # this function translate english to braille
        braille_sentence = []
        is_number = False
        english_sentence = self.input_string
        for braille_character in english_sentence:
            english_character = ''
            # this character is a digit number
            if braille_character.isdigit():
                if not is_number: # set is_number to true to know that 'Number' is already added
                    is_number = True
                    braille_string_number = self.alpha_braille_dictionary['Number']
                    braille_sentence.append(braille_string_number)
                english_character = self.digit_braille_dictionary[braille_character]
            else: # current character is no longer a digit number, set to False so that in the future we can reset it
                is_number = False
                
                # current number is uppercase
                if braille_character.isupper():
                    braille_capital_string = self.alpha_braille_dictionary["Capital"]
                    braille_sentence.append(braille_capital_string)
                    # change the current char to lowercase
                    english_character = self.alpha_braille_dictionary[braille_character.lower()]
                else: # if the character is just a normal character
                    english_character = self.alpha_braille_dictionary[braille_character]

            # append the current character into the answer
            braille_sentence.append(english_character)

        return ''.join(braille_sentence)
    
    def translate(self):
        if(self.is_braille()):
            return self.translate_braille_to_en()
        else:
            return self.translate_english_to_braille()
        
def main():
    input_string = ' '.join(sys.argv[1:])
    my_translator = Translator(input_string=input_string)
    print(my_translator.translate())

if __name__ == "__main__":
    main()