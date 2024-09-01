from strategies.abstract_strategy import TranslationStrategy

class EnglishToBrailleStrategy(TranslationStrategy):
    # Time Complexity: O(n) where 'n' is the length of 'english_text'
    def __init__(self, translate_dict):
        self.translate_dict = translate_dict

    def translate(self, english_text):
        braille_list = [] # Using list to append characters and then join them at the end, because string concatentations have a time complexity of (O(n^2))
        number_flag = False
        last_char_was_space = False
        
        for char in english_text:
            if char == ' ':
                if last_char_was_space: continue  # Skip if the last character was also a space
                last_char_was_space = True
            else:
                last_char_was_space = False
                
            if char.lower() in self.translate_dict: # ignores all characters not in dictionary
                if char.isupper(): # if capital, add "C" before braille and lowercase the letter
                    braille_list.append(self.translate_dict['C']) 
                    char = char.lower()
                if char.isdigit() and not number_flag: # if number, add "N" before and assume numbers until space symbol is encountered
                    number_flag = True
                    braille_list.append(self.translate_dict['N'])
                if char == '.' and number_flag: # if dot, assume decimal if we're assuming numbers
                    braille_list.append(self.translate_dict['D'])
                if char == ' ': # if space, reset number flag
                    number_flag = False
                braille_list.append(self.translate_dict[char])
            else:
                print("Please ensure the input text is limited to letters, digits, and punctuation.")
                sys.exit(1)
        
        braille_text = ''.join(braille_list) 
        return braille_text
 