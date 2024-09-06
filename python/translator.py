import sys
import re

def check_if_braille(input_text):
   # If input string is not a multiple of six characters, then it cannot be braille
   if len(input_text) % 6 != 0:
       return False

   # If the input string only contains the characters 'O' and '.', then it is considered to be braille
   return bool(re.match('^[O.]+$', input_text))

def translate_to_braille(english_input):
    return ''

def translate_from_braille(braille_input):
    return ''

def main():
    # Parse input from command line
    if len(sys.argv) <= 1:
        print('')
        return
    
    input_text = ' '.join(sys.argv[1:])

    # Check if command line input is braille or not
    is_braille = check_if_braille(input_text)

    # Perform translation
    output = ''
    if is_braille:
        output = translate_from_braille(input_text)
    else:
        output = translate_to_braille(input_text)

    # Output result
    print(output)

if __name__ == "__main__":
    main()