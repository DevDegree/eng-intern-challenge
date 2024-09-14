import sys

# Braille dictionary for English letters (lowercase)
braille_alpha = [
    "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",
    "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",
    "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"
]

# Braille dictionary for numbers (0-9)
braille_num = [
    ".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."
]

# Braille capital follow symbol
braille_cap = ".....O"

# Braille number follow symbol
braille_num_f = ".O.OOO"

# Braille space
braille_space = "......"

def braille_translator(input_string):
    # Check if the input is Braille or English
    is_braille = all(s in ['O', '.', ' '] for s in input_string)
    
    if not is_braille:
        # Translate English to Braille
        result = ""
        num = False
        for char in input_string:
            if char == ' ':
                result += braille_space  # Handle spaces correctly
                num = False # Reset the flag for numbers
            elif char.isdigit():
                # Number follow symbol and corresponding Braille number
                if not num:
                    result += braille_num_f + braille_num[int(char)]
                else:
                    result += braille_num[int(char)]
                num = True # Set the flag to handle multiple digits
            elif char.isupper():
                # Capital follow symbol and lowercase Braille
                result += braille_cap + braille_alpha[ord(char.lower()) - ord('a')]
            elif char.islower():
                # Lowercase letter Braille
                result += braille_alpha[ord(char) - ord('a')]
        return result
    else:
        # Translate Braille to English
        i = 0
        capital = False
        numbers = False
        result = ""
        
        while i < len(input_string):
            if input_string[i:i+6] == braille_space:
                result += " "
                i += 6
                numbers = False # Reset the flag for numbers
                continue  # Skip to the next iteration
            
            if input_string[i:i+6] == braille_cap:
                capital = True
                i += 6
                continue  # Skip to the next iteration
            
            if input_string[i:i+6] == braille_num_f:
                numbers = True
                i += 6
                continue  # Skip to the next iteration
            
            # Translate Braille characters
            if numbers:
                for j in range(10):
                    if input_string[i:i+6] == braille_num[j]:
                        result += str(j)
                        i += 6
                        break
                # Continue to handle the next character without resetting the `numbers` flag
            else:
                for j in range(26):
                    if input_string[i:i+6] == braille_alpha[j]:
                        if capital:
                            result += chr(ord('A') + j)
                            capital = False
                        else:
                            result += chr(ord('a') + j)
                        i += 6
                        break
                # Continue to handle the next character without resetting the `capital` flag
        return result

# Main function to handle command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string to translate>")
        sys.exit(1)
    
    # Join all command-line arguments into a single string
    input_string = ' '.join(sys.argv[1:])
    
    # Perform translation and print the result
    print(braille_translator(input_string))