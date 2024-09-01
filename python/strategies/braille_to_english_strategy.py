from strategies.abstract_strategy import TranslationStrategy

class BrailleToEnglishStrategy(TranslationStrategy):
    # Total Time Complexity: O(n) because 2 for loops: 1 for reverse dict and 1 for braille_text, but not nested
    def __init__(self, translate_dict):
        self.reverse_dict = {}
        for key, value in translate_dict.items():
            if value not in self.reverse_dict:
                self.reverse_dict[value] = []
            self.reverse_dict[value].append(key)

    def translate(self, braille_text):
        # Using list to append characters and then join them at the end, because string concatentations have a time complexity of (O(n^2))
        english_list = []
        number_flag = False
        capital_flag = False
        
        # Process the Braille text in chunks of 6 characters
        for i in range(0, len(braille_text), 6):
            braille_char = braille_text[i:i+6]
            if len(braille_char) < 6:
                print("Please ensure the braille text is complete with 6 digits for each character.")
                sys.exit(1)
            
            keys = self.reverse_dict[braille_char]
            
            if not keys: # Empty list means the braille character is not in the dictionary
                print("Please ensure the braille text translates correctly to an English character.")
                sys.exit(1)
            
            char = keys[0] # Get the first key from the list of keys
            if char == 'D': continue # if decimal, it wouldn't affect the output so skip to next iteration
            if char == 'C': 
                capital_flag = True
                continue # skip to next iteration
            if char == 'N':
                number_flag = True
                continue # skip to next iteration
            if char == ' ' and number_flag: number_flag = False
            char = keys[1] if (len(keys) > 1 and number_flag) else keys[0]
                
            if capital_flag:
                char = char.upper()
                capital_flag = False
            
            english_list.append(char)
            
        english_text = ''.join(english_list)
        return english_text
