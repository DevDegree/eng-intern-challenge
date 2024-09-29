import sys

# Dictionaries for English <--> Braille Translation

# Special markers for Braille translation
CAPITAL = '.....O' # Capital letter indicator
NUM_FOLLOWS = '.O.OOO' # Number indicator in Braille
SPACE = "......"   # Braille space character (whitespace)

# Alphabet and punctuation mapping from English to Braille
EtoB_ALPHA_PUNCT = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO', 
    'z': 'O..OOO',
      # punctuation begins here:
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"   # whitespace character
}

# Number mapping from English to Braille
EtoB_NUMBERS = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    '.': '.O...O'    # decimal_point
      # we assume that the convention is a decimal point, as indicated in Wikipedia article linked in the GitHub repo, under section Punctuation, table under cell "Decimal Point".
}

# Reverse dictionaries for Braille to English translation
BtoE_ALPHA_PUNCT = {v: k for k, v in EtoB_ALPHA_PUNCT.items()}
BtoE_NUMBERS = {v: k for k, v in EtoB_NUMBERS.items()}

def detect_language(input_str):
    """
    Detects whether the given string is Braille or English. Assumes that any string containing only 'O' and '.' and has a length that is a multiple of 6 is Braille.
    
    :param input_str: The input string to be checked
    :return: 'Braille' if the string is Braille, 'English' otherwise
    """
    
    if len(input_str) % 6 != 0: # If length is not a multiple of 6, it's English
        return "English"
    
    # Check if the string contains only 'O' and '.' characters
    for x in input_str:
        if x not in "O.":   # If any other character is found, it's English
            return "English"
    return "Braille"
    # If a single non-"O." character is reached, will end instead of going through entire string. Worst case O(n) linear time.


def is_number(word):
    """Check if a string represents a number, accounting for decimal points."""
    try:
        float(word)
        return True
    except ValueError:
        return False

def split(text,k):
    """Split a text into chunks of size `k`."""
    return [text[i:i+k] for i in range(0,len(text),k)] 
    # split text into chucks of size k, from index i to i+k, where i increments by k each step 

def translate_english_to_braille(input_str):
    """
    Translates English text into Braille, handles special cases for uppercase letters and numbers. Splits text by " " spaces, then, after inserting special characters, joins together with Braille space equivalent "......"
    
    :param input_str: The input English text as a string
    :return: Translated Braille string
    """

    text = input_str.split(" ")  # Split English text into words
    result = []  # Time complexity append() may be optimized with preset array size (preallocating memory, like in C, to avoid dynamic resizing of array)

    for word in text:
        if is_number(word):  # If the word is a number
            result.append(NUM_FOLLOWS)  # Add number indicator
            for i in word:
              result.append(EtoB_NUMBERS[i])  # Add Braille of each digit
        else:
            for i in word:            
                if i.isupper():    # Handle uppercase letters
                    result.append(CAPITAL)    # Add capital letter indicator in Braille
                    result.append(EtoB_ALPHA_PUNCT[i.lower()])   # Add lowercase equivalent
                else:   # Handle lowercase letters, or punctuation
                    result.append(EtoB_ALPHA_PUNCT[i])
        result.append((SPACE))   # Add Braille space at the end of a word
    
    # Join words and remove extra space at the end 
    return "".join(result).rstrip(SPACE)

def translate_braille_to_english(input_str):
    """
    Translates Braille text into English, handling special cases for capitalization and numbers.
    
    :param input_str: The input Braille text as a string
    :return: Translated English string
    """
    x = split(input_str, 6)  # Split Braille into chunks of 6 
    result = [] 

    capital_next = False
    number_next = False
    
    for i in x:
        if i == SPACE:
            result.append(" ")
            number_next = False   # Reset number status when word ends (i.e. space is encountered)

        elif i == NUM_FOLLOWS:   # Handle number indicator
            number_next = True  # next character uses NUM dict

        elif number_next:     # use EtoB_NUMBERS dictionary
            result.append(BtoE_NUMBERS[i])

        elif i == CAPITAL:  # Handle capital letter indicator
            capital_next = True  # next character uses upper() 
        
        elif i not in BtoE_ALPHA_PUNCT:  # Failsafe catch statement to break function and translate from English instead
            # Note that special characters like Capital_follows, and Number_follows, will still result in an empty string printed out
            translate_english_to_braille(input_str)
            return None

        else:   # detect the character in the general dictionary
            character = BtoE_ALPHA_PUNCT[i]
            if capital_next:   # Convert to uppercase if capital indicator was the previous character
                result.append(character.upper())  # use BtoE_ALPHA_PUNCT dict. with upper() command
                capital_next = False   # capitals persist for only one position, so turn it off after using it
            else:
                result.append(character)   # use as normal

    return "".join(result)


if __name__ == '__main__': 
    
    text = " ".join(sys.argv[1:])

    # First, detect input_str language
    input_str_lang = detect_language(text)

    # Perform translation
    if input_str_lang == "English":   # Chose for code legibility over a more efficient binary (e.g. 0/1, True/False, "E"/"B", etc.)
        result = translate_english_to_braille(text)
        print(result)
    elif input_str_lang == "Braille":
        result = translate_braille_to_english(text)
        print(result)
        
    # In case of errors, exit program
    else:
        sys.exit(1)
