import sys

# Mapping of Braille patterns to English characters
braille_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i",
    ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "......": " ",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
    "O.O..O": "(", ".O.OO.": ")", ".....O": "Capital follows", ".O.OOO": "Number follows"
}

# Reverse mapping from English characters to Braille
text_to_braille = {v: k for k, v in braille_map.items()}

# Numbers in Braille (assume number prefix .O.OOO)
digit_map = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

def braille_to_text(braille_input):
    """ Convert Braille patterns to English text """
    output = []
    index = 0
    while index < len(braille_input):
        braille_chunk = braille_input[index:index+6]
        
        if braille_chunk == ".....O":
            # Capital follows
            index += 6
            next_chunk = braille_input[index:index+6]
            output.append(braille_map.get(next_chunk, "?").upper())
        
        elif braille_chunk == ".O.OOO":
            # Number follows
            index += 6
            while index < len(braille_input):
                digit_chunk = braille_input[index:index+6]
                if digit_chunk == "......":
                    break
                digit_char = [num for num, pattern in digit_map.items() if pattern == digit_chunk]
                if digit_char:
                    output.append(digit_char[0])
                else:
                    output.append("?")
                index += 6
            continue  # Move to the next segment
        
        else:
            output.append(braille_map.get(braille_chunk, "?"))
        
        index += 6
    
    return ''.join(output)

def text_to_braille_conversion(text_input):
    """ Convert English text to Braille patterns """
    braille_output = []
    number_flag = False
    for char in text_input:
        if char.isdigit():
            if not number_flag:
                braille_output.append(".O.OOO")  # Number follows
                number_flag = True
            braille_output.append(digit_map[char])
        
        elif char.isalpha():
            if number_flag:
                braille_output.append("......")  # Space to exit number mode
                number_flag = False
            if char.isupper():
                braille_output.append(".....O")  # Capital follows
            braille_output.append(text_to_braille[char.lower()])
        
        else:
            # Handle punctuation or spaces
            if number_flag:
                number_flag = False  # Reset number mode when a non-digit is found
            braille_output.append(text_to_braille.get(char, ""))
    
    return ''.join(braille_output)

def start_translation():
    # Combine all arguments passed as input text
    input_str = ' '.join(sys.argv[1:])
    
    # Check if the input is Braille or plain text
    if all(c in 'O.' for c in input_str):
        print(braille_to_text(input_str))
    else:
        print(text_to_braille_conversion(input_str))

if __name__ == "__main__":
    start_translation()
