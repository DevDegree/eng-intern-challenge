import sys

BRAILLE_DICT = {
    
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "......": " ",

    ".....OO.....": "A", ".....OO.O...": "B", ".....OOO....": "C", ".....OOO.O..": "D", ".....O..O..": "E", ".....OOOO...": "F", ".....OOOOO..": "G",
    ".....O.OO..": "H", ".....O.OO...": "I", ".....O.OOO..": "J", ".....O...O.": "K", ".....O.O.O.": "L", ".....OO..O.": "M", ".....OO.OO.": "N",
    ".....O..OO.": "O", ".....OOO.O.": "P", ".....OOOOO.": "Q", ".....O.OOO.": "R", ".....O.OO.O.": "S", ".....O.OOOO.": "T", ".....O...OO": "U",
    ".....O.O.OO": "V", ".....O.OOO.O": "W", ".....OO..OO": "X", ".....OO.OOO": "Y", ".....O..OOO": "Z"
}

NUMBER_DICT = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", "OOO.O.": "9", "OOO.OO": "0"
}


CHAR_DICT = {
    "..OO.O": ".",  
    "..O...": ",",  
    "..O.OO": "?",  
    "..OOO.": "!",  
    "..OO..": ":",  
    "..O.O.": ";", 
    "....OO": "-",  
    ".O..O.": "/", 
    ".OO..O": "<",  
    "O..OO.": ">",
    "O.O..O": "(",  
    ".O.OO.": ")",  
    "......": " "   
}


FULL_DICT = {**BRAILLE_DICT, **NUMBER_DICT, **CHAR_DICT}

def is_braille(text):
    return all(c in "O." for c in text)

def translate_braille_to_english(braille_text):
    translated_text = ""
    i = 0
    number_lock = False  
    decimal_lock = False  
    capitalize_next = False  

    while i < len(braille_text):
        braille_char = braille_text[i:i+6]

       
        if braille_char == ".O.OOO":  #number lock 
            number_lock = True  
            i += 6  
            continue

       
        if braille_char == ".O...O":  #decimals lock
            decimal_lock = True  
            i += 6  
            continue

        
        if braille_char == ".....O":  #caps lock
            capitalize_next = True  
            i += 6  
            continue

      
        if number_lock:
            
            translated_text += NUMBER_DICT.get(braille_char, "?")
        else:
            
            letter = BRAILLE_DICT.get(braille_char, "?")
            if capitalize_next:
                translated_text += letter.upper()  
                capitalize_next = False 
            else:
                translated_text += letter  

        i += 6  

      
        if braille_char == "......":  #space
            number_lock = False
            decimal_lock = False

    return translated_text


def translate_english_to_braille(english_text):
    braille_text = ""
    number_lock = False  

    for char in english_text:
        if char.isdigit():  
            if not number_lock:  
                braille_text += ".O.OOO"  # Number lock
                number_lock = True  
            for key, value in NUMBER_DICT.items():
                if value == char:
                    braille_text += key
                    break

        elif char.isupper():  
            braille_text += ".....O"  # caps lock 
            lower_char = char.lower()  
            
            for key, value in BRAILLE_DICT.items():
                if value == lower_char:
                    braille_text += key
                    break

        elif char == " ":  
            braille_text += "......" #space
            number_lock = False  

        else:  
            number_lock = False 
            for key, value in BRAILLE_DICT.items():
                if value == char:
                    braille_text += key
                    break
    return braille_text



def main():

    input_text = " ".join(sys.argv[1:])

    if is_braille(input_text):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))

if __name__ == "__main__":
    main()
