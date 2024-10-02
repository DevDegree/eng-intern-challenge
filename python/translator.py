import sys

class translator:
    def __init__(self):

        # Dictionary to map English characters to Braille representations
        self.braille_map = {
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
            ' ': '......',
            '.' : '.O...O'
        }

        # Mapping of alphabets to corresponding numbers (used in Braille conversion)
        self.alpha_to_num = {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '5',
            'f': '6',
            'g': '7',
            'h': '8',
            'i': '9',
            'j': '0',
        }

        # Special Braille characters to indicate capital letters and numbers
        self.capital_follows = '.....O'
        self.number_follows = '.O.OOO'
    
        # Reverse mapping from Braille to English
        self.english_map = {value: key for key, value in self.braille_map.items()}
    
        # Reverse mapping from English to Braille (alpha to num)
        self.num_to_alpha = {value: key for key, value in self.alpha_to_num.items()}
    '''
    Method to check if the input string is valid Braille.
    Braille strings must:
    - Contain only 'O' and '.' characters
    - Be a multiple of 6 in length, as each Braille character is represented by 6 dots
    '''
    def is_braille(self, user_input):
        if len(user_input) % 6 != 0:
            return False
        
        braille_char = {'.', 'O'}
        for char in user_input:
            if char not in braille_char:
                return False
        return True
    
    '''
    Method to convert a Braille string to English text.
    - Handles uppercase and number indicators
    - Looks up each 6-character Braille segment in the English map
    '''
    def braille_to_text(self, user_input):
        output = []
        status = 0  # Status indicator: 0 - lowercase, 1 - uppercase, 2 - number

        # Iterate through the Braille input in chunks of 6 characters
        for i in range(0, len(user_input), 6):
            char = user_input[i:i+6]

            # Check for special indicators (capital or number or space)
            if char == self.capital_follows:
                status = 1
                continue
            elif char == self.number_follows:
                status = 2
                continue
            elif char == self.braille_map[' ']:
                status = 0
            
            # Convert Braille to English using the mapping
            letter = self.english_map[char]

            # Apply transformations based on the status indicator
            if status == 1:
                letter = letter.upper()
                status = 0
            elif status == 2:
                letter = self.alpha_to_num[self.english_map[char]]
                
            output.append(letter)

        return ''.join(output)
        
    '''
    Method to convert English text to a Braille string.
    - Adds capital and number indicators as needed
    - Converts each letter or digit to its corresponding Braille representation
    '''
    def text_to_braille(self, user_input):
        output = []
        number_mode = False

        # Iterate through each character in the input text
        for char in user_input:
            # Handle uppercase and number indicators
            if char.isupper():
                output.append(self.capital_follows)
                char = char.lower()
            if char.isdigit():
                if not number_mode:
                    output.append(self.number_follows)
                    number_mode = True
                char = self.num_to_alpha[char]
            else:
                # Reset number mode if a space is encountered
                if char == ' ':
                    number_mode = False
                    
            output.append(self.braille_map.get(char))

        return ''.join(output)

# Main function to handle user input and call appropriate methods        
def main():
    user_input = ' '.join(sys.argv[1:])
    t = translator()

    # Determine whether the input is Braille or English and convert accordingly
    if (t.is_braille(user_input)):
        print(t.braille_to_text(user_input))
    else:
        print(t.text_to_braille(user_input))


if __name__=="__main__":
    main()