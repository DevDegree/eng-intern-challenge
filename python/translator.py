import sys

#Dictionary for english letters and numbers mapping to braille.
BRAILLE_ALPHABET = {
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

    '0': '.OOO..', 
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',

    ' ': '......'    
}

#Reverse the dictionary key-value pairs. This is helpful when converting from braille to english.
BRAILLE_TO_ENGLISH = {braille:english for english, braille in BRAILLE_ALPHABET.items()}


CAPITAL_PREFIX = '.....O'

NUMBER_PREFIX = '.O.OOO'



#Check if the entire string is O and . and nothing else.
def is_braille(input_text):
    """Function to check if the input is braille or not by checking if the entire input consists of O and . and nothing else."""
    store_bool = [char in ('O','.') for char in input_text]
    return all(store_bool)




def braille_to_english(braille_text):
    """Function to convert from braille to english by splitting the text into an array of symbols each with 6 characters."""

    english_output = []

    number_mode = False

    symbols = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    i = 0

    while i< len(symbols):
        symbol = symbols[i]
        
        if symbol == NUMBER_PREFIX:
            number_mode = True
            i+=1
            continue
        
        #Condition for capital letters. The important thing here is to make sure the symbol for 0 is accounted.
        #for and set to be j since a number cant be a capital so its assumed the next symbol is j.
        
        if symbol == CAPITAL_PREFIX:
            if i+1 < len(symbols):
                next_symbol = symbols[i+1]
                character = BRAILLE_TO_ENGLISH.get(next_symbol, ' ')
                if symbol == '.OOO..':
                    character = 'j'
                
                #Making sure the conversion of ascii of the numbers to the corresponding letters is in the alphabet.
                elif chr(ord(character) + 48) in BRAILLE_ALPHABET:
                
                
                    character = chr(ord(character) + 48)
                english_output.append(character.upper())
                i+=2
                continue
        
        if not number_mode:
            character = BRAILLE_TO_ENGLISH.get(symbol, ' ')
            if symbol == '.OOO..':
                    character = 'j'
        
            elif chr(ord(character) + 48) in BRAILLE_ALPHABET:
                
                
                character = chr(ord(character) + 48)
            english_output.append(character)
            i+=1 
            continue

        else:
            character = BRAILLE_TO_ENGLISH.get(symbol, ' ')
            if character == ' ':
                number_mode = False

            english_output.append(character)
            i+=1
            continue
    
    return ''.join(english_output)









def english_to_braille(words):

    """Function to convert from english to braille. This is an easy implementation since the dictionary has all the letters and symbols we need."""

    braille_output = []
    number_mode = False

    for idx, word in enumerate(words):
        word_braille = []
        i=0
        while i< len(word):
            char = word[i]

            if char.isupper():
                word_braille.append(CAPITAL_PREFIX)
                char = char.lower()
            
            if char.isdigit():
                if not number_mode:
                    number_mode = True
                    word_braille.append(NUMBER_PREFIX)
                
                word_braille.append(BRAILLE_ALPHABET.get(char, '......'))

            else:
                if number_mode:
                    number_mode = False
                
                
                word_braille.append(BRAILLE_ALPHABET.get(char, '......'))

            i+=1
        
        braille_output.append(''.join(word_braille))

        if idx < len(word) - 1:
            braille_output.append(BRAILLE_ALPHABET.get(' ', '......'))
    
    return ''.join(braille_output)
                





def main():

    args = sys.argv[1:]

    #validate input
    if not args:
        print("No input detected")
        sys.exit()

    


    input_text = " ".join(args)
    if is_braille(input_text.replace(" ","")):
        braille_input = input_text.replace(" ", "")
        

        english_output = braille_to_english(braille_input)
        print(english_output)
    
    else:
        braille_output = english_to_braille(args)

        print(braille_output)
    
    

if __name__ == "__main__":
    main()