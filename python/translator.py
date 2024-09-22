import sys

def isBraille(input):
    '''
    Check if inputs is in Braille format
    - As all characters in braille symbols are 6 character strings long, then the length of the whole input must be a multiple of 6 
    - All braille symbols are made of either '.' or '0' and of the regex form ^[\.0]{6}
    '''
    # Check if the input length is a multiple of 6
    if (len(input) % 6 != 0):
        return False

    # Check if all symbols are either '.' or '0'
    for i in input:
        if (i not in {'.', '0'}):
            return False
    return True

def run():
    '''
    Check and convert into input that is valid for translation
    '''
    # Check if an argument or input is given for translation
    if (len(sys.argv) == 1):
        return
    
    # Add spaces for english words if required (braille input will have a single input)
    inputs =  ' '.join(sys.argv[1:])

    if (isBraille(inputs)):
        BrailleTranslator(inputs) # translate to English
    else:
        EnglishTranslator(inputs) # translate to Braille

if __name__ == "__main__":
    run()