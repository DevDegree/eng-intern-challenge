import sys

# Defining Braille to English dictionary
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'capital', '..OOO.': 'number', '......': ' ', '.....O.O...': '.'
}

# Defining English to Braille dictionary
english_to_braille = {x: y for y, x in braille_to_english.items() if x not in ['capital', 'number']}
english_to_braille.update({
    'A': '.....O' + 'O.....', 'B': '.....O' + 'O.O...', 'C': '.....O' + 'OO....',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', '.': '.....O.O...'
})

# Function to translate Braille to English
def braille_to_text(braille_input):
    text_output = ""
    i = 0
    number_mode = False

    while i < len(braille_input):
        br_char = braille_input[i:i+6]

        if br_char == '.....O':  # Capital symbol
            i += 6
            br_char = braille_input[i:i+6]
            text_output += braille_to_english.get(br_char, '?').upper()
        elif br_char == '..OOO.':  # Number symbol
            number_mode = True
        elif br_char == '......':  # Space
            number_mode = False
            text_output += ' '
        elif br_char == '.....O.O...':  # Period
            text_output += '.'
        else:
            if number_mode:
                # Numbers mapping (correct mapping for digits)
                numbers_mapping = {
                    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
                    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
                }
                text_output += numbers_mapping.get(br_char, '?')
                number_mode = False  # End number mode after processing
            else:
                text_output += braille_to_english.get(br_char, '?')
        
        i += 6
        
    return text_output

# Function to translate English to Braille
def text_to_braille(text_input):
    br_output = ""
    number_mode = False

    for char in text_input:
        if char.isupper():
            br_output += '.....O'  # Capital
            char = char.lower()
        elif char.isdigit():
            if not number_mode:
                br_output += '..OOO.'  # Number symbol
                number_mode = True
            br_output += english_to_braille.get(char, '......')
        elif char == '.':
            br_output += english_to_braille['.']
        else:
            number_mode = False
            br_output += english_to_braille.get(char, '......')
            
    return br_output

# Main
def main():
    if len(sys.argv) < 3:
        print("Usage: python translator.py <mode> <string>")
        return
    
    mode = sys.argv[1]
    input_text = " ".join(sys.argv[2:])
    
    if mode == "text-to-braille":
        output = text_to_braille(input_text)
    elif mode == "braille-to-text":
        output = braille_to_text(input_text)
    else:
        print("Invalid mode! Use 'text-to-braille' or 'braille-to-text'")
        return
    
    print(output)

if __name__ == "__main__":
    main()
