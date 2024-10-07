import sys
import re

alpha_to_braille = {
    # Alphabet
    'a': "O.....", 'b': "O.O...",  
    'c': "OO....", 'd': "OO.O..", 
    'e': "O..O..", 'f': "OOO...", 
    'g': "OOOO..", 'h': "O.OO..", 
    'i': ".OO...", 'j': ".OOO..", 
    'k': "O...O.", 'l': "O.O.O.", 
    'm': "OO..O.", 'n': "OO.OO.", 
    'o': "O..OO.", 'p': "OOO.O.", 
    'q': "OOOOO.", 'r': "O.OOO.", 
    's': ".OO.O.", 't': ".OOOO.", 
    'u': "O...OO", 'v': "O.O.OO", 
    'w': ".OOO.O", 'x': "OO..OO", 
    'y': "OO.OOO", 'z': "O..OOO",
    # Space
    ' ': "......"
}

braille_to_alpha = {value: key 
                        for key, value in alpha_to_braille.items()}


def alpha_to_num(letter: str) -> str:
    """
    Converts a letter from 'a' to 'j' into its corresponding Braille numeric value.
    
    letter: A single letter between 'a' and 'j'.
    
    Returns: The numeric representation as a string.
             'a' returns '1', 'j' returns '0'.
    """
    first_ten_letters = ['a', 'b', 'c', 'd', 'e', 
                         'f', 'g', 'h', 'i', 'j']
    converted_num = first_ten_letters.index(letter)+1 if letter != 'j' else 0
    return str(converted_num)

def num_to_alpha(numeric: int) -> str:
    """
    Converts a numeric value (0-9) into its corresponding letter in Braille.
    
    numeric: A number between 0 and 9.
    
    Returns: The letter corresponding to the given number.
             '1' returns 'a', '0' returns 'j'.
    """
    braille_number_order = ['j', 'a', 'b', 'c', 'd', 
                            'e', 'f', 'g', 'h', 'i']
    alpha = braille_number_order[int(numeric)]
    return alpha


def braille_to_english(braille: str) -> str:
    """
    Translates a string of Braille characters into readable English text.
    
    braille: A sequence of Braille characters made up of 'O' and '.'.
    
    Returns: The equivalent English text as a string.
             Handles spaces, numbers, and capital letters.
    """
    SPACE           = "......"
    CAPITAL_FOLLOWS = ".....O"  
    NUMBER_FOLLOWS  = ".O.OOO"
    
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    translation = []
    i = 0
    while i < len(braille_chars):
        if braille_chars[i] == CAPITAL_FOLLOWS:
            i+=1
            translation.append(braille_to_alpha[braille_chars[i]].upper())  
       
        elif braille_chars[i] == NUMBER_FOLLOWS:
            i+=1
            while i < len(braille_chars) and braille_chars[i] != SPACE:
                char = braille_to_alpha[braille_chars[i]]
                if char in "abcdefghij":
                    translation.append(alpha_to_num(char))
                i+=1        
        else:
            translation.append(braille_to_alpha[braille_chars[i]])
        i+=1
    
    return ''.join(translation)    

def english_to_braille(english: str) -> str:
    """
    Converts English text into its Braille representation.
    
    english: A string of English text, including letters and numbers.
    
    Returns: The corresponding string of Braille characters.
             Capital letters and numbers are converted using special Braille prefixes.
    """
    CAPITAL_FOLLOWS = ".....O" 
    NUMBER_FOLLOWS  = ".O.OOO"

    english_chars = list(english)
    translation = []
    for index, i in enumerate(english_chars)
    	
        if i.isnumeric():
            if index == 0 or not english_chars[index-1].isnumeric():
                translation.append(NUMBER_FOLLOWS) 
            braille = alpha_to_braille[num_to_alpha(i)]
            translation.append(braille)
       
        elif i.isupper():
            translation.append(CAPITAL_FOLLOWS)
            braille = alpha_to_braille[i.lower()]
            translation.append(braille)
        
        else:
            braille = alpha_to_braille[i]
            translation.append(braille)
    
    return ''.join(translation)

def translate_input(input: str):
    """
    Determines if the input is Braille or English and translates accordingly.
    
    input: A string, either Braille ('O' and '.') or English (letters/numbers).
    
    Returns: The translated result printed to the console.
             Braille input will be translated to English, and vice versa.
    """
    english = re.compile(r"[A-Za-z0-9\s]+")
    braille = re.compile(r"^(?:[O.]{6})+$")

    if braille.match(input):
        print(braille_to_english(input))
    elif english.match(input):
        print(english_to_braille(input))
    else:
        print(f"Error! => Input: {input}")  


def main():
    """
    Main function to handle command-line input.
    """
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        translate_input(input_text)



if __name__ == "__main__":
    main()

