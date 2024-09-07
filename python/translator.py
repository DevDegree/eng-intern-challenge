import sys 
import re 

class BrailleEnglishTranslator: 
    def __init__(this): 
        this.text = sys.argv[1:]  # get text to translate  
        this.language_is_braille = this.is_braille()
        this.braille_to_english_dict, this.english_to_braille_dict = BrailleEnglishTranslator.get_dictionary() 

    def is_braille(this):
        # Check if the following conditions are met for braille:
        # 1. checks if only one argument needs to be translated.
        # 2. checks if the argument has a length of a multiple of 6.
        # 3. checks if the argument contains only characters '.' and 'O'.
        return len(this.text) == 1 and len(this.text[0]) % 6 == 0 and bool(re.fullmatch(r'[.O]*', this.text[0]))
    
    def is_english(this):
        return not this.is_braille() 
    
    def get_dictionary():
        braille_to_english_dict = {
            # alpha
            'O.....': 'a', 
            'O.O...': 'b',
            'OO....': 'c', 
            'OO.O..': 'd',  
            'O..O..': 'e',
            'OOO...': 'f', 
            'OOOO..': 'g', 
            'O.OO..': 'h',
            '.O.O..': 'i', 
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

            # space 
            '......': ' ', 

            # capital and number follows 
            '.....O': 'capital follows', 
            '.O.OOO': 'number follows', 
        }

        english_to_brail_dict = { v:k for k, v in braille_to_english_dict.items() }
        return braille_to_english_dict, english_to_brail_dict
    
    def translate_braille(this): 
        english_letters = []
                
        # possible states: 'alpha', 'capital', 'number'
        state = 'alpha'
        for ind in range(0, len(this.text[0]), 6): 
            token = this.text[0][ind:ind+6]
            translated_token = this.braille_to_english_dict[token]

            if state == 'alpha': 
                if translated_token == 'capital follows': 
                    state = 'capital'
                elif translated_token == 'number follows': 
                    state = 'number'
                else: 
                    english_letters.append(translated_token)

            elif state == 'capital': 
                english_letters.append(translated_token.capitalize())
                state = 'alpha'

            elif state == 'number': 
                if translated_token == ' ': 
                    state = 'alpha'
                    english_letters.append(' ')
                    continue 

                def letter_to_number(letter): 
                    letter = letter.lower() 
                    if letter == 'j': 
                        return '0' 
                    return str(ord(letter) - ord('a') + 1)

                english_letters.append(letter_to_number(translated_token)) 
 
        return ''.join(english_letters)

    def translate_english(this): 

        braille_tokens = []
        input_text = ' '.join(this.text)
        
        # possible states: 'alpha' 'number'
        state = 'alpha'
        for ind in range(0, len(input_text), 1): 
            token = input_text[ind]
            token_is_upper = token.isupper() 
            token_is_digit = token.isdigit() 
            def number_to_letter(token):
                if not token.isdigit(): 
                    return token 

                if token == '0': 
                    return 'j'
                return chr(ord('a') + int(token) - 1) 
            token = number_to_letter(token)           

            translated_token = this.english_to_braille_dict[token.lower()]

            # handle state switching 
            if state == 'alpha' and token_is_digit: 
                braille_tokens.append(this.english_to_braille_dict['number follows'])
                state = 'number'
            elif state == 'number' and token == ' ': 
                state = 'alpha'
            
            if state == 'alpha': 
                if token_is_upper:
                    braille_tokens.append(this.english_to_braille_dict['capital follows']) 
                braille_tokens.append(translated_token)
            elif state == 'number': 
                braille_tokens.append(translated_token) 

        return ''.join(braille_tokens)

    def translate(this): 
        if this.language_is_braille: 
            translated_text = this.translate_braille() 
        else:  # language is english 
            translated_text = this.translate_english()
        
        print(translated_text, end='')

if __name__ == '__main__': 
    translator = BrailleEnglishTranslator() 
    translator.translate()  
