import sys

def main():
    '''
    Main functions to validate command line input and check whether to 
    translate from Braille to English or English to Braille
    '''
    
    # Get the argument from the command line
    if len(sys.argv) != 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)
        
    # Get input strings and join strings on spaces to handle strings with spaces
    input_string = ' '.join(sys.argv[1:])
    
    
    # Check if input is Braille or English
    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))
    
    
    
def is_braille(string):
    '''
    Checks if the input string is Braille containing only '0' and '.'
    Input: String
    Output: Boolean: True if the input is Braille, else, returns False
    '''
    
    return all(char in '0.' for char in string)


def translate_english_to_braille(english_string):
    '''
    Translate English to Braille
    Input: String in English
    Output: Braille translation of the input string
    '''
    return


def translate_braille_to_english(braille_string):
    '''
    Translate Braille to English
    Input: String in Braille
    Output: English translation of the input string
    '''
    return