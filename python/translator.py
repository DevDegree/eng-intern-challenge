import sys

# Dictionary mapping each English character (lowercase, numbers, space) to its Braille equivalent.
# Each Braille character is represented as a string of 6 characters, where 'O' is a raised dot and '.' is an absence of a dot.
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......' 
}

# Capital letter symbol in Braille is a special symbol preceding an uppercase letter
capital_braille = '.....O'

# Number prefix symbol in Braille, used to denote that the following characters are numbers
number_braille = '.O.OOO'

# Reverse dictionary to map Braille back to English for easy lookup
reverse_braille_map = {v: k for k, v in braille_map.items()}

def to_braille(text):
    """
    Converts a given English text into Braille notation.
    
    Time Complexity: O(n), where n is the length of the input text. We traverse each character once.
    
    Algorithm:
    - For each character in the input, check if it is a number or a letter.
    - If it is a number, append the number Braille prefix if necessary.
    - If it is a capital letter, append the capital prefix and convert the letter to lowercase.
    - Handle spaces and other supported characters by appending their respective Braille patterns.
    - Return the Braille string concatenated from all the characters.
    """
    braille_output = []  
    is_number = False  

    for char in text:
        # Handling numbers
        if char.isdigit():
            if not is_number:  
                braille_output.append(number_braille)
                is_number = True  
            braille_output.append(braille_map[char])

        elif char.isalpha():
            if is_number: 
                is_number = False
            if char.isupper(): 
                braille_output.append(capital_braille)
                char = char.lower()  
            braille_output.append(braille_map[char])
        
        elif char in braille_map:  
            braille_output.append(braille_map[char])
            is_number = False  
        else:
            braille_output.append('......')  

    return ''.join(braille_output)  

def to_english(braille):
    """
    Converts a given Braille string into English text.
    
    Time Complexity: O(n), where n is the length of the input Braille string. Each Braille character is 6 dots, and we process them in chunks of 6.
    
    Algorithm:
    - For every 6-character chunk (representing a Braille character), check if it is a special prefix for numbers or capitals.
    - If a capital prefix is encountered, capitalize the next character.
    - If a number prefix is encountered, treat subsequent characters as numbers.
    - Append each translated character to the result string.
    - Return the full English text.
    """
    english_output = [] 
    i = 0  
    is_number = False  

    while i < len(braille):

        current_symbol = braille[i:i+6]  
        if current_symbol == capital_braille:
            i += 6
            current_symbol = braille[i:i+6]
            english_output.append(reverse_braille_map[current_symbol].upper())
       
        elif current_symbol == number_braille:
            is_number = True  
        else:
            
            english_output.append(reverse_braille_map.get(current_symbol, '?'))
            is_number = False  

        i += 6  

    return ''.join(english_output)

def detect_and_translate(input_string):
    """
    Detects if the input string is Braille or English and performs the appropriate translation.
    
    Time Complexity: O(n), where n is the length of the input string. We need to check each character to determine if it’s Braille (O or .) or English.
    
    - If the input consists entirely of Braille characters (O, .), it will call `to_english()`.
    - Otherwise, it will assume the input is in English and call `to_braille()`.
    """
   
    if all(c in 'O.' for c in input_string):
        return to_english(input_string)
    else:
        return to_braille(input_string)

if __name__ == "__main__":
   
    input_text = ' '.join(sys.argv[1:])
    print(detect_and_translate(input_text))