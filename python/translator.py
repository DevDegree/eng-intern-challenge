import re, sys
english_symbols = {
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..",
    "e" : "O..O..", "f" : "OOO...", "g" : "OOOO..", "h" : "O.OO..",    
    "i" : ".OO...", 'j' : ".OOO..", "k" : "O...O.", "l" : "O.O.O.",
    "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.", "p" : "OOO.O.",
    "q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.",
    "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
    "y" : "OO.OOO", "z" : "O..OOO", "." : "..OO.O", "," : "..O...",
    "?" : "..O.OO", "!" : "..O.OO", ":" : "..OO..", ";" : "..O.O.",
    "-" : "....OO", "/" : ".0..0.", "<" : ".OO..O", 
    "(" : "O.O..O", ")" : ".O.OO.", " " : "......"
    
}
english_numbers = {
    "1" : "O.....", "2" : "O.O...", "3" : "OO....", "4" : "OO.O..",
    "5" : "O..O..", "6" : "OOO...", "7" : "OOOO..", "8" : "O.OO..",
    "9" : ".OO...", "0" : ".OOO.."
}
#Reverse symbols to get the dictionary for braille-en
braille_symbols = {braille : en for en, braille in english_symbols.items()}
braille_numbers = {braille : en for en, braille in english_numbers.items()}

capital_follows_braille = ".....O"
number_follows_braille = ".O.OOO"

def capital_follows(char):
    return char == capital_follows_braille
 
def number_follows(char):
    return char == number_follows_braille

def is_space(char):
    return char == "......"

def translate_Braille_char_to_En(char, is_number):
    braille = braille_symbols
    if is_number: 
        braille = braille_numbers      
    en_char = braille[char]
    return en_char

#Translate braille input to english      
def braille_to_en(string):
    translated_string = ""
    is_number = False #for digit mode
    is_capital = False
    for i in range(0, len(string), 6):
        symbol_to_translate = string[i:i+6] 
        #Check if next braille char is a number
        if number_follows(symbol_to_translate):
            is_number = True
            continue
        
        #Stay in digit mode until we have have space's braille char
        if is_number and is_space(symbol_to_translate):
            is_number = False  
                      
        #Check if next braille char is a capital letter
        if capital_follows(symbol_to_translate):
            is_capital = True
            continue
        en_char = translate_Braille_char_to_En(symbol_to_translate, is_number)
        if is_capital:
            en_char = en_char.upper()
            is_capital = False
        translated_string +=en_char
    return translated_string
             
def translate_En_char_to_Braille(char, is_number):
    braille = english_symbols
    if is_number: 
        braille = english_numbers      
    braille_char = braille[char]
    return braille_char

#Translate braille input to english  
def en_to_braille(string):
    translated_string = ""
    is_number = False
    not_digit_mode = True #To avoid having to check numbers that follow when we are in digit mode
    
    for symbol_to_translate in string :    
        #Check if en char is a capital letter
        if symbol_to_translate.isupper():
            #Convert english symbol to lowercase so we can check corresponding braille in dic
            symbol_to_translate = symbol_to_translate.lower()
            
            #Add 'capital follows' braille to translated string before adding symbol's braille
            translated_string += capital_follows_braille

        #Check if we are in digit mode so that we won't need to check again if the next char is a digit
        if not_digit_mode:
            #Add 'number follows' braille to translated string before continuing to add symbols braille
            if symbol_to_translate.isdigit():
                is_number = True
                translated_string += number_follows_braille
                not_digit_mode = False  
            
        #Stay in digit mode until we have have space's char
        if is_number and is_space(symbol_to_translate):
            is_number = False  
            not_digit_mode = True

        braille_char = translate_En_char_to_Braille(symbol_to_translate, is_number)
        translated_string += braille_char
        
    return translated_string

#Check if given argument is Braille or English   
def is_braille(string):
    return bool(re.fullmatch(r"[O.]*", string)) and len(string)%6==0
  
def translate(string):
    if is_braille(string):
        return braille_to_en(string)
    else:
        return en_to_braille(string)
    
def main(input):
    translated_string = translate(input)
    print(translated_string)
    
if __name__ == "__main__":
    main(' '.join(sys.argv[1:]))
