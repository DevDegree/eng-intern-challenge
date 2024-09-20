import sys

# Braille Translator 
def translator(s: str) -> str:
    """
    Translate Braille to English and vice-versa

    Input: Hello world
    Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

    Args:
        s (string): string to be translated (English to Braille/ Braille to English)
    
    Returns:
        str: translated string
    """

    def is_braille(s: str) -> bool:
        """
        Checks is string is braille

        Input: '.....O'
        Output: True

        Args:
            s (string): string to be checked
        
        Returns: 
            boolean value
        """
        valid_char = set('O.')
        return len(s) % 6 == 0 and all(char in valid_char for char in s)
    
    braille_pattern = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
        'w': '.OOO.O', ' ': '......', '^': '.....O', 'num':'.O.OOO'
    }

    # Generate braille number mapping
    number_mapping = {
    '1': braille_pattern['a'],
    '2': braille_pattern['b'],
    '3': braille_pattern['c'],
    '4': braille_pattern['d'],
    '5': braille_pattern['e'],
    '6': braille_pattern['f'],
    '7': braille_pattern['g'],
    '8': braille_pattern['h'],
    '9': braille_pattern['i'],
    '0': braille_pattern['j']
}

    # Check if Braille or English
    is_braille_str = is_braille(s)
    output = []

    if is_braille_str:
        # Braille to English translation
        braille_cells = [s[i:i+6] for i in range(0, len(s), 6)]  # Split by Braille cells
        capital_follows = False
        number_follows = False
        
        for cell in braille_cells:
            if cell == braille_pattern['^']:  # Capital follows
                capital_follows = True
                continue
            if cell == braille_pattern['num']:  # Number follows
                number_follows = True
                continue
            if number_follows:
                # Handle numbers from the mapping
                number = next((k for k, v in number_mapping.items() if v == cell), None)
                if number is not None:
                    output.append(number)
                else:
                    output.append('error')
                continue
            else:
                # Handle letters
                letter = next((k for k, v in braille_pattern.items() if v == cell), None)
                if letter:
                    output.append(letter.upper() if capital_follows else letter)
                    capital_follows = False
                else:
                    output.append('error')  # Unknown cell
    else:
        # English to Braille translation
        number_follows = False
        for char in s:
            if char.isupper():
                output.append(braille_pattern['^'])  # Capital indicator
                char = char.lower()
            if char.isdigit():
                if not number_follows:
                    output.append(braille_pattern['num'])  # Number indicator
                    number_follows = True
                output.append(number_mapping.get(char, '......'))  # Map number to Braille
            else:
                number_follows = False  # Reset number follow for letters
                output.append(braille_pattern.get(char, '......'))  # Default to space for unknown characters
    
    return ''.join(output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translator(input_text))
    else:
        print("Please provide input text.")