# Author: Oluchukwu Obi-Njoku

import character #python file that contains all character mappings. Braille to English, and vice versa
import sys


def check_is_braille(value: str) -> bool:

    #check_is_braille accepts a string, checks if it is braille, returns true if so, and false if not
    
    if (len(value) < 6) or (len(value) % 6 != 0):
        return False
    else:
        for v in value:
            if v not in {'O','.'}:
                return False
    return True

def translate_statement_to_english(value:str) -> str:

    #translate_statement_to_english converts a braille string to English
    
    is_capital = False
    is_number = False
    char_store = ""
    translated_statement = ""
    
    for i in range(len(value)):
        
        char_store += value[i]
        
        if len(char_store) == 6:
            
            if char_store == character.braille_blank_space and is_number == True:
               is_number = False

            if char_store != character.braille_capital_symbol and char_store != character.braille_number_follows:
                translated_statement += translate_char_to_english(char_store,is_capital, is_number)
                is_capital = False
            elif char_store == character.braille_capital_symbol:
                is_capital = True
            elif char_store == character.braille_number_follows:
                is_number = True
            
               
            char_store = ""
        
    return translated_statement
            
            
def translate_char_to_english(braille_letter: str, is_capital: bool, is_number: bool) -> str:

    #translate_char_to_english converts a braille character to its English equivalent
    
    if is_capital != True and is_number != True:
        return character.braille_letters[braille_letter] if braille_letter in character.braille_letters else character.braille_symbols[braille_letter]
    elif is_capital == True:
        return character.braille_letters[character.braille_capital_symbol + braille_letter]
    elif is_number == True:
        return character.braille_numbers[braille_letter]
        

def translate_char_to_braille(eng_letter: str,is_number: bool) -> str:

    #translate_char_to_braille converts an English character to its braille equivalent

    if is_number == False:
        return character.braille_letters.inverse[eng_letter] if eng_letter.isalpha() else character.braille_symbols.inverse[eng_letter]
    else:
        return character.braille_numbers.inverse[eng_letter] if is_number > 1 else character.braille_number_follows + character.braille_numbers.inverse[eng_letter]

        

def translate_statement_to_braille(value:str) -> str:

    #translate_statement_to_braille converts an English string to its braille equivalent
    
    translated_statement = ""
    is_number = 0
    try:
        for i in range(len(value)):
            is_number = is_number + 1 if value[i].isdigit() else 0
            translated_statement += translate_char_to_braille(value[i],is_number)
            
        return translated_statement
    except TypeError as e:
        print(f"Error handling: {e}")
    except KeyError as e:
        print(f"Error handling: {e}")
    except:
        print(f"Error")

def main():
   
    if len(sys.argv) > 1:
        translated_parts = []
        is_braille = False

        try:
            for i in range(1,len(sys.argv)):
                statement = sys.argv[i]
                is_braille = check_is_braille(statement)
                if is_braille == True:
                    translated_parts.append(translate_statement_to_english(statement))
                else:
                    translated_parts.append(translate_statement_to_braille(statement))
            if is_braille:
                print(" ".join(translated_parts))
            else:
                print((character.braille_blank_space).join(translated_parts))
        except:
            print("There was an exception. Sorry about that! I'll get to fixing it.")
    else:
        print("Please provide a statement to translate.")
    
    
if __name__ == "__main__":
    main()
    