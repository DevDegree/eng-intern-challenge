english_to_braille={
'a': '0.....',
'b': '0.0...',
'c': '00....',
'd': '00.0..',
'e': '0..0..',
'f': '000...',
'g': '0000..',
'h': '0.00..',
'i': '.00...',
'j': '.000..',
'k': '0...0.',
'l': '0.0.0.',
'm': '00..0.',
'n': '00.00.',
'o': '0..00.',
'p': '000.0.',
'q': '00000.',
'r': '0.000.',
's': '.00.0.',
't': '.0000.',
'u': '0...00',
'v': '0.0.00',
'w': '.000.0',
'x': '00..00',
'y': '00.000',
'z': '0..000',
'1': '0.....',
'2': '0.0...',
'3': '00....',
'4': '00.0..',
'5': '0..0..',
'6': '000...',
'7': '0000..',
'8': '0.00..',
'9': '.00...',
'0': '.000..',
'capital_follows': '.....0',
'decimal_follows': '.0...0',
'number_follows':  '.0.000',
'.': '..00.0',
',': '..0...',
'?': '..0.00',
'!': '..0.00',
':': '..000.',
';': '..0.0.',
'-': '....00',
'/': '.0..0.',
'<': '.00..0',
'>': '0..00.',
'(': '0.0..0',
')': '.0.00.',
' ': '......',
}

def translate_english_to_braille(string_input):
    braille_output = ''
    processing_numbers = False
    
    for char in string_input:
        if char.isdigit(): 
            if not processing_numbers:
                braille_output += english_to_braille['number_follows']
                processing_numbers = True
            braille_output += english_to_braille[char]

        elif char.isalpha(): 
            if char.isupper(): 
                braille_output += english_to_braille['capital_follows']
            braille_output += english_to_braille[char.lower()]
            processing_numbers = False

        elif char == '.':
            braille_output += english_to_braille['decimal_follows']
            processing_numbers = False

        else: 
            braille_output += english_to_braille.get(char, '......')
            processing_numbers = False

    return braille_output

if __name__ == "__main__":
    string_input = "Hello, World! 012345!"
    braille_representation = translate_english_to_braille(string_input)
    print(braille_representation)
  
import argparse

def main():
    parser = argparse.ArgumentParser(description="Translate the text between braille and english")
    parser.add_argument("string_input", type=str, help=" string to translate")
    args = parser.parse_args()

    input_string = args.string_input
    input_type = detect_input_type(input_string)
    
    if input_type == 'english':
        output = translate_english_to_braille(input_string)

    elif input_type == 'braille':
        output = translate_braille_to_english(input_string)

    print(output)

if __name__ == "__main__":
    main()



 
