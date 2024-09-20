# Evan Smedley - Shopify Engineering Intern Challenge

import yaml, string, sys

class Braille_Translator():

    def __init__(self):
        # Import braille from yaml file
        with open("braille.yml", 'r') as file:
            braille = yaml.safe_load(file)["braille"]

        # Extract Braille special chars
        self._capital_follows = braille["special_chars"]["capital_follows"]
        self._number_follows = braille["special_chars"]["number_follows"]
        self._space = braille["special_chars"][' ']

        # Define English-Braille alphabet and digit maps
        self._eng_to_braille_alphabet_map = { k: braille["alphabet"][k] for k in string.ascii_lowercase }
        self._eng_to_braille_digit_map = { k: braille["digits"][k] for k in string.digits }
        
        # Define Braille-English maps by flipping
        self._braille_to_eng_alphabet_map = { v: k for k, v in self._eng_to_braille_alphabet_map.items() }
        self._braille_to_eng_digit_map = { v: k for k, v in self._eng_to_braille_digit_map.items() }



    def is_braille(self, input: str) -> bool:
        """
        A Braille character is a sequence of only characters 'O' and '.', a set is used to find unique characters.
        """
        return set(input) == set(['O', '.'])
    


    def eng_to_braille(self, english: str) -> str:
        """
        When converting english to braille, there will be more braille charaters due to state indicators such as capital follows.

        As a result an iterator is used to allow nested loops to continue looping through the same string.

        I wish it was indented less but I hope it is ok :).
        """
        braille_output = ""
        english_iterator = iter(english)

        # Use try/except to catch StopIteration when iterator is exhausted
        try:
            while c := next(english_iterator):
                
                # Check for capitals
                if c.isupper():
                    braille_output += self._capital_follows
                    braille_output += self._eng_to_braille_alphabet_map[c.lower()]

                # Check for digits
                elif c in string.digits:
                    braille_output += self._number_follows
                    braille_output += self._eng_to_braille_digit_map[c]

                    # Continue looping through digits until a space is found
                    while True:
                        c = next(english_iterator)
                        if c == ' ':
                            braille_output += self._space
                            break
                        braille_output += self._eng_to_braille_digit_map[c]

                # Check for space
                elif c == ' ':
                    braille_output += self._space

                # Otherwise, output a lowercase character
                else:
                    braille_output += self._eng_to_braille_alphabet_map[c]

        except StopIteration:
            pass

        return braille_output



    def braille_to_eng(self, braille: str) -> str:
        """
        Method for converting braille to english.
        
        number of braille chars >= number of english chars
        
        Flags are used to keep track of state imposed on current chars by previous braille special characters.
        """
        output = ""
        capital_follows_flag = False
        number_follows_flag = False

        # Split into list of braille characters
        groups_of_six = [braille[i:i+6] for i in range(0, len(braille), 6)]

        braille_chars_iter = iter(groups_of_six)
        
        # Iterate through braille characters until StopIteration is thrown.
    
        # Capital follows and number follows flags keep track of state that can affect the next char(s).
        try:
            while (braille_char := next(braille_chars_iter)):

                if braille_char == self._capital_follows:
                    capital_follows_flag = True

                elif braille_char == self._number_follows:
                    number_follows_flag = True

                elif braille_char == self._space:
                    capital_follows_flag, number_follows_flag = False, False
                    output += ' '

                elif capital_follows_flag:
                    output += self._braille_to_eng_alphabet_map[braille_char].upper()
                    capital_follows_flag = False

                elif number_follows_flag:
                    output += self._braille_to_eng_digit_map[braille_char]
                
                else:
                    output += self._braille_to_eng_alphabet_map[braille_char]

        except StopIteration:
            pass

        return output



    def translate(self, input: str) -> str:
        """
        Detect if Braille or English is inputted and translate accordingly.
        """
        return self.braille_to_eng(input) if self.is_braille(input) else self.eng_to_braille(input)
    
    

if __name__ == "__main__":
    braille_translator = Braille_Translator()
    
    # Translate contents of command line argument
    translated_input = braille_translator.translate(sys.argv[1])
    
    print(translated_input)