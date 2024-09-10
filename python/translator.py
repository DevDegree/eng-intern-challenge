import sys

# Braille dictionary for English letters, numbers and characters
braille_alpha_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
}
braille_digit_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
braille_follow_dict = {
    'capital': '.....O', 'decimal':'.O...O', 'number':'.O.OOO'
}
braille_special_dict = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', 
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', 
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

# Braille to English translation
eng_alpha_dict = {v: k for k, v in braille_alpha_dict.items()}
eng_digit_dict = {v: k for k, v in braille_digit_dict.items()}
eng_follow_dict = {v: k for k, v in braille_follow_dict.items()}
eng_special_dict = {v: k for k, v in braille_special_dict.items()}

# Function to convert text to braille
def text_to_braille(text: str):
    output = ''
    isDigit = False
    
    for char in text:
        # Check if it is a space
        if char == ' ':
            isDigit = False
            output += braille_special_dict.get(' ')

        # Check if it is a digit
        elif char.isdigit():
            # If we already appended the number follows character
            if isDigit:
                output += (braille_digit_dict.get(char))
            else:
                output += (braille_follow_dict.get('number'))
                output += (braille_digit_dict.get(char))
                isDigit = True;
        
        #Check if it is character
        elif char.isalpha():
            #If it is upper
            if char.isupper():
                output += braille_follow_dict.get('capital')
                output += braille_alpha_dict.get(char.lower())
            else:
                output += braille_alpha_dict.get(char)
        
        #Check if it is a decimal or full stop
        elif char == '.':
            if isDigit:
                output += braille_follow_dict.get('decimal')
            else:
                output += braille_special_dict.get(char)
        
        else:
            output += braille_special_dict.get(char)

    return output

# Function to convert braille to text
def braille_to_text(braille: str):
    output = ''
    isDigit = False
    isCapital = False
    
    for i in range(0, len(braille), 6):
        #Get 6 characters of braille
        curr_chunk = braille[i:i+6]

        #If the character is representing a follows
        if curr_chunk in eng_follow_dict.keys():
            #If capital
            if eng_follow_dict[curr_chunk] == 'capital':
                #Insert the next chunk as capital
                isCapital = True
            # If indicating number
            elif eng_follow_dict[curr_chunk] == 'number':
                isDigit = True
            # It is decimal 
            else:
                output += '.'
                
        # If the character is one of special characters
        elif curr_chunk in eng_special_dict.keys():
            if eng_special_dict[curr_chunk] == ' ':
                isDigit = False
                
            output += eng_special_dict[curr_chunk]

        #If it is a digit    
        elif isDigit:
            output += eng_digit_dict[curr_chunk]

        #If it is an alphabet
        elif isCapital:
            output += eng_alpha_dict[curr_chunk].upper()
            isCapital = False
        
        #If it is lower case character
        else:
            output += eng_alpha_dict[curr_chunk]
            
    return output

def main():
    # Handle case when no input is passed
    if len(sys.argv) < 2:
        print("Pass in a english or braille string while running the program.")
        sys.exit(1)

    # Get the input text
    input = ""
    for arg in sys.argv[1:]:
        input += arg + " "
    
    # Remove the trailing space
    input = input.strip()
    
    #check if it is braille
    if all(c in 'O.' for c in input):
        print(braille_to_text(input))
    else:
        print(text_to_braille(input))

if __name__ == "__main__":
    main()

