import sys

# dictionary mapping english characters to braille
braille_map = {
    'a' : 'O.....','b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..', 'e' : 'O..O..','f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..', 'i' : '.OO...', 'j' : '.OOO..',
    'k' : 'O...O.', 'l' : 'O.O.O.', 'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.','p' : 'OOO.O.', 'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
    'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO', 'y' : 'OO.OOO', 'z' : 'O..OOO', 'capital' : '.....O', 'number' : '.O.OOO', ' ' : '......'
}

# dictionary mapping braille to english characters
english_map = {val: key for key, val in braille_map.items()}


# dictionary mapping english characters (a-j) to numbers (0-9)
number_map = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

# dictionary mapping numbers (0-9) to english characters (a-j)
alpha_map  = {val: key for key, val in number_map.items()}

# function to translate english to braille
def english_to_braille(english_text):
    result = []
    number_mode = False # flag to see if the char is a number

    for char in english_text: 
        if char.isdigit(): 
            if not number_mode: # check if it is the first number
                number_mode = True
                result.append(braille_map['number'])  
            result.append(braille_map[alpha_map[char]])  
        elif char.isalpha():
            if number_mode: 
                number_mode = False 
            if char.isupper():
                result.append(braille_map['capital']) 
            result.append(braille_map[char.lower()]) 
        elif char == ' ':
            result.append(braille_map[' ']) 
        else:
            result.append(braille_map[char])

    return ''.join(result)

# function to translate braille to english

def braille_to_english(braille_text):
    result = [] 
    number_mode = False 
    i = 0 # starting index of the first braille symbol
    while i < len(braille_text):
        symbol = braille_text[i:i+6] # retrieve the current braille symbol
        i += 6 # shift to the next braille symbol
        if symbol == braille_map['number']: 
            number_mode = True

        elif symbol == braille_map['capital']: 
            result.append(english_map[braille_text[i:i+6]].upper()) # capialize english letter
            i += 6 
        else:
            char = english_map[symbol]
            if number_mode and char in number_map: 
                result.append(number_map[char]) 
            else:
                result.append(char) 
                number_mode = False 
    return ''.join(result)

# function to translate braille to english and vice versa
def translate(text):
    return braille_to_english(text) if all(char in 'O.' for char in text) else english_to_braille(text) # check if text contains only 'O.' to see if it is braille or english

if __name__ == "__main__":
    if all(char in 'O.'for arg in sys.argv[1:] for char in arg): # check if text contains only 'O.' to see if we need to append ' ' or '......' between the args
        translated_text =  ' '.join([translate(arg) for arg in sys.argv[1:]])
    else:
        translated_text =  '......'.join([translate(arg) for arg in sys.argv[1:]])

    print(translated_text)