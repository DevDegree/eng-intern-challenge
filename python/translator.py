import sys

# Dictionary mapping Braille patterns to their corresponding English letters.
char_key = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y',
    'O..OOO': 'Z'
}

# Function to convert English text to Braille notation.
def english_to_braille(s):
    is_alphabet = True  # Flag to determine if we are processing letters or numbers.
    result = ""  # String to store the Braille translation.

    # Iterate through each character in the input string.
    for i in range(len(s)):
        # Handle lowercase letters.
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            result += list(char_key.keys())[ord(s[i]) - 97]
        
        # Handle uppercase letters.
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            result += '.....O' + list(char_key.keys())[ord(s[i]) - 65]
        
        # Handle digits.
        elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
            if is_alphabet:
                result += '.O.OOO'  # Prefix to indicate the following characters are numbers.
            is_alphabet = False
            if ord(s[i]) == 48:  # Special case for digit '0'.
                result += '.OOO..'
                continue
            result += list(char_key.keys())[ord(s[i]) - 49]
        
        # Handle spaces or other non-alphanumeric characters.
        else:
            is_alphabet = True
            result += '......'  # Braille for space.
    
    return result

# Function to convert Braille notation back to English text.
def braille_to_english(s):
    char_stack = []  # Stack to hold Braille characters in reverse order.
    result = ""  # String to store the English translation.

    # Process the Braille string in reverse order, extracting 6-character Braille cells.
    for i in range(len(s) - 1, -1, -6):
        char_stack.append(s[i-5:i+1])

    is_alphabet = True  # Flag to determine if we are processing letters or numbers.

    # Process each Braille character from the stack.
    while len(char_stack) > 0:
        curr = char_stack.pop()
        
        # Handle capitalization.
        if curr == '.....O':
            curr = char_stack.pop()
            result += char_key[curr]
        
        # Handle transition from letters to numbers.
        elif curr == '.O.OOO':
            is_alphabet = False
            continue
        
        # Handle space.
        elif curr == '......':
            is_alphabet = True
            result += ' '
        
        # Handle regular letters or numbers.
        else:
            if is_alphabet:
                result += char_key[curr].lower()  # Convert to lowercase if it's a letter.
            else:
                if curr == '.OOO..':  # Special case for digit '0'.
                    result += '0'
                    continue
                result += chr(ord(char_key[curr]) - 16)  # Convert Braille number to digit.
    
    return result

# Main program execution starts here.
user_input = sys.argv  # Capture the command-line arguments.
output = ""  # Variable to store the final translation.
curr_input = ""  # String to accumulate the full input for translation.
is_english = False  # Flag to determine if the input is English or Braille.

# Check if the input is in English by looking for non-Braille characters.
for j in range(len(user_input[1])):
    if user_input[1][j] != '.' and user_input[1][j] != 'O':
        is_english = True
        break

# Combine all arguments into a single string, adding appropriate separators.
for i in range(1, len(user_input)):
    curr_input += user_input[i]
    if i == len(user_input) - 1:
        break
    if is_english:
        curr_input += ' '
    else:
        curr_input += '......'

# Translate the input based on its type.
if is_english:
    output += english_to_braille(curr_input)
else:
    output += braille_to_english(curr_input)

# Print the final translation.
print(output)
