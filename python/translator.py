# Dict that translates letters to braille
braille_dict_mutex = {
    'CAPFLW': '.....O', 'DECFLW': '.O...O', 
    'NUMFLW': '.O.OOO', 'SPC': '......'
}

braille_dict_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O....OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', '.': '..O.O.',
    ',': '.O....', '?': '.O.O.O', '!': '..OO..', '-': '....O.'
}

braille_dict_numbers= {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..',
}

def isBraille(input_string):
    # Split the braille_sequence into chunks of 6 characters each
    n = 6
    segment = [(input_string[i:i+n]) for i in range(0, len(input_string), n)]

    #Characters that make a Braille symbol
    brailChar = {'O','.'}

    # Check each segment to ensure it matches the Braille pattern
    for x in segment:
        if any(char not in brailChar for char in x) or len(x)!=6:
            return False  # Not Braille if any segment doesn't match
    
    return True if x else False  
    
def text_to_braille(text):
    braille_text_simple = ""
    usingNumbers = False  
    uppercaseIndicator= ".....O"
    numberIndicator= ".O.OOO" 
    
    for char in text:
        # Check if we need to switch to number mode for digits
        if char.isdigit():
            if not usingNumbers:
              # Add number indicator before the Braille character
                braille_text_simple += numberIndicator 
                usingNumbers = True
        else:
            if usingNumbers:
                usingNumbers = False  # Switch back to letter mode after numbers

        # Determine if the character is uppercase
        if char.isupper():
            # Add uppercase indicator before the Braille character
            braille_text_simple += uppercaseIndicator

        # Normalize the character to lowercase for dictionary lookup
        normalized_char = char.lower()

        # Choose the correct dictionary based on the current mode
        current_dict = braille_dict_numbers if usingNumbers else braille_dict_letters
        
        # Get the braille representation for the current character
        if normalized_char in current_dict:
            braille_char = current_dict[normalized_char]
        else:
            braille_char = "......"  # Default to unknown pattern for chars not in the dictionary
        
        braille_text_simple += braille_char

    return braille_text_simple

def braille_to_text(braille_sequence):
    nextIsUpper=False
    usingNumbers=False
    # Initialize the output text
    text_output = ""
    
    # Split the braille_sequence into chunks of 6 characters each
    n=6
    segments = [braille_sequence[i:i+n] for i in range(0, len(braille_sequence), n)]
    
    # Iterate over each segment and find corresponding text character
    for segment in segments:
        if segment == braille_dict_mutex["CAPFLW"]:
                   nextIsUpper = True
                   continue
        elif segment == braille_dict_mutex["NUMFLW"]:
                   usingNumbers = True
                   continue
       
       # Choose the correct dictionary based on the current mode
        current_dict = braille_dict_numbers if usingNumbers else braille_dict_letters

        for key, value in current_dict.items():
              if value == segment:
                     if nextIsUpper:
                          text_output += key.upper()
                          nextIsUpper = False
                     else:
                          text_output += key
                     break
            
    return text_output

val = input()

if isBraille(val):
    print(braille_to_text(val))
else:
    print(text_to_braille(val))





