import sys

# Dictionary containing all necessary key-value pairs for translating Braille to English and vice-versa
# The braille for the alphabet "o" and ">" is the same
braille_dictio={
    'a': "O.....",'b': "O.O...",'c': "OO....",'d': "OO.O..",'e': "O..O..", 'f': "OOO...",
    'g': "OOOO..",'h': "O.OO..",'i': ".OO...", 'j': ".OOO..",'k': "O...O.", 'l': "O.O.O.",
    'm': "OO..O.",'n': "OO.OO.",'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
    's': ".OO.O.",'t': ".OOOO.",'u': "O...OO",'v': "O.O.OO",'w': ".OOO.O", 'x': "OO..OO",
    'y': "OO.OOO",'z': "O..OOO",'1' : "O.....",  '2' : "O.O...",   '3' : "OO....",  '4' : "OO.O..",  
    '5' : "O..O..",  '6' : "OOO...",  '7' : "OOOO..",  '8' : "O.OO..",  '9' : ".OO...",  '0' : ".OOO..",
    '.': "..OO.O",',': "..O...",'?': "..O.OO",'!': "..OOO.",':': "..OO..",';': "..O.O.",'-': "..O.O.",
    '/': ".O..O.",'>': ".OO..O",  '<': "O..OO.", '(': "O.O..O",')': ".O.OO.",'capital': ".....O",
    'number': ".O.OOO",'decimal': ".O.O..",  'space': "......"
}
# Translate Braille to English
def translate_toBraille(word):
    """
    Translates an English word or number to Braille using the braille_dictio.
    - Capital letters are prefixed by the capital indicator.
    - Numbers are prefixed by the number indicator.
    - Floats are handled with the decimal indicator.
    
    Args:
    word (str or int or float): The word or number to translate into Braille.
    
    Returns:
    str: The translated Braille string.
    """
    braille = ""
    # Add number prefix if the input is a number
    if type(word) is int or type(word) is float:
          braille+= braille_dictio.get('number')
    wordStr = str(word)
    # Loop through the word and add the respective Braille symbols 
    for letter in wordStr:
        if(letter.isupper()): # Add capital letter prefix and corresponding Braille
            braille+= braille_dictio.get('capital') + braille_dictio.get(letter.lower())
        # Special condition to ensure decimals/floats are properly processed
        elif type(word) is float and letter=='.':
                braille+= braille_dictio.get('decimal')
        # General case, fetch Braille character from dictionary
        else:
            braille += braille_dictio.get(letter)
    return braille

# Translate English to Braille
def translate_toEnglish(word):
    """
    Translates a Braille string back to English using the braille_dictio.
    - Capital letters are recognized and returned in uppercase.
    - Numbers are recognized after the number indicator.
    
    Args:
    braille_word (str): The Braille string to translate back to English.
    
    Returns:
    str: The translated English string.
    """
    english = ""
    disectedWord = splitString(word) # Split Braille into 6-dot segments
    num= False # Track if number indicator was encountered
    capital = False # Track if capital indicator was encountered
    for braille in disectedWord:
        if(get_key(braille)=='space'): # Handle space
            english+= " "
            num = False # Reset number mode after space
            continue
        if(get_key(braille)=='decimal'): # Handle decimal point
            english+="."
            continue
        if(num): # If in number mode, add digits
            english += get_integer(braille)
            continue
        if(capital):  # If in capital mode, add uppercase letter
            english += get_key(braille).upper()
            capital = False
            continue
        if(get_key(braille)=='number'): # Enter number mode
            num = True
            continue
        if(get_key(braille)=='capital'): # Enter capital mode
            capital = True
            continue
        # # Add regular letter
        english+= get_key(braille)
        
    return english

def splitString(s):
    """
    Splits a string into segments of 6 characters (each representing one Braille character).
    
    Args:
    s (str): The Braille string to split.
    
    Returns:
    list: A list of 6-character segments.
    """
    return [s[i:i+6] for i in range(0,len(s),6)]

# Searching for the key given a particular value
def get_key(val):
    """
    Finds the corresponding English character or symbol for a Braille value.
    
    Args:
    val (str): The Braille string to search for.
    
    Returns:
    str: The corresponding English character, or None if not found.
    """    
    # Here it is assumed all inputs correspond to a given key-value pair
    for key, value in braille_dictio.items():
        if val == value:
            return key
        
# Searching for an integer value instead of the corresponding alphabet in Braille       
def get_integer(val):
    """
    Finds the corresponding number for a Braille value.
    
    Args:
    val (str): The Braille string to search for.
    
    Returns:
    str: The corresponding number, or None if not found.
    """
    for key, value in braille_dictio.items():
        if val == value and key.isdigit():
            return key

def isBraille(arg):
    """
    Determines whether a given string is a valid Braille string.
    
    Args:
    arg (str): The string to check.
    
    Returns:
    bool: True if the string could be Braille, False otherwise.
    """
    # Check if the string length is a multiple of 6 and contains Braille-like characters(Assuming only 1 decimal point/period per float/string)
    arg= str(arg)
    if(len(arg)%6==0 and arg.count('.')>1):
        return True
    return False
        
def main():
    """
    Main function to handle command-line input, determine if input is Braille or English, and translate accordingly.
    """
    translated = ""
    n = len(sys.argv)
    numSpaces = n - 2 # Calculate spaces to be added between words
    # If only one argument is passed and it's Braille, translate to English
    if n == 2 and isBraille(sys.argv[1]):
        translated += translate_toEnglish(sys.argv[1])
    else:
        # Loop through all arguments to translate to Braille
        for i in range(1, n):
            arg = sys.argv[i]
            if arg.replace('.', '', 1).isdigit(): # Check if argument is a number (int or float)
                if '.' in arg:
                    arg = float(arg)
                else:
                    arg = int(arg)
            translated += translate_toBraille(arg)
            if numSpaces > 0: # Add spaces between words if needed
                translated += braille_dictio.get('space') 
                numSpaces -= 1
    print(translated)

if __name__ == "__main__":
    main()
