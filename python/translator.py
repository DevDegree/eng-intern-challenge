import sys

English_To_Braille_alph = { 'a': "O.....", 
                      'b' : "O.O...", 
                      'c': "OO....", 
                      'd': "OO.O..", 
                      'e': "O..O..", 
                      'f': "OOO...", 
                      'g': "OOOO..", 
                      'h': "O.OO.." , 
                      'i': ".OO...",
                      'j': ".OOO..",
                      'k': "O...O.",
                      'l': "O.O.O.",
                      'm': "OO..O.",
                      'n': "OO.OO.",
                      'o': "O..OO.",
                      'p': "OOO.O.",
                      'q': "OOOOO.",
                      'r': "O.OOO.",
                      's': ".OO.O.",
                      't': ".0000.",
                      'u':"O...OO",
                      'v': "O.O.OO",
                      'w': ".OOO.O",
                      'x': "OO..OO",
                      'y': "OO.OOO",
                      'z': "O..OOO",
                        '1': "O.....",
                      '2': "O.O...",
                      '3': "OO....",
                      '4': "OO.O..",
                      '5': "O..O..",
                      '6': "OOO...",
                      '7': "OOOO..",
                      '8': "O.OO.." ,
                      '9': ".OO...",
                      '0 ': ".OOO..",
                       '.':"..OO.O" ,
                       ',': "..O...",
                       '?': "..O.OO",
                       '!': "..O.OO",
                       ':': "..OO..",
                       ';': "..O.O.",
                       '-': "....OO",
                       '/': ".O..O.",
                       '<': ".OO..O",
                       '>': "O..OO.",
                       '(': "O.O..O",
                       ')': ".0.00.",
                      ' ' : "......"}

Braille_To_English_alph= { 'O.....': "a", 
                      'O.O...' : "b", 
                      'OO....' : "c", 
                      'OO.O..' : "d", 
                      'O..O..': "e", 
                      'OOO...': "f", 
                      'OOOO..': "g", 
                      'O.OO..': "h" , 
                      '.OO...': "i",
                      '.OOO..': "j",
                      'O...O.': "k",
                      'O.O.O.': "l",
                      'OO..O.': "m",
                      'OO.OO.': "n",
                      'O..OO.': "o",
                      'OOO.O.': "p",
                      'OOOOO.': "q",
                      'O.OOO.': "r",
                      '.OO.O.': "s",
                      '.0000.': "t",
                      'O...OO': "u",
                      'O.O.OO': "v",
                      '.OOO.O': "w",
                      'OO..OO': "x",
                      'OO.OOO': "y",
                      'O..OOO': "z",
                       '..OO.O': "." ,
                       '..O...': ",",
                       '..O.OO': "?",
                       '..O.OO': "!",
                       '..OO..': ":",
                       '..O.O.': ";",
                       '....OO': "-",
                       '.O..O.': "/",
                       '.OO..O': "<",
                       'O..OO.': ">",
                       'O.O..O': "(",
                       '.0.00.': ")",
                       '......': " "
                      }


Braille_To_English_numb= { 'O.....': "1",
                      'O.O...': "2",
                      'OO....': "3",
                      'OO.O..': "4",
                      'O..O..': "5",
                      'OOO...': "6",
                      'OOOO..': "7",
                      'O.OO..': "8" ,
                      '.OO...': "9",
                      '.OOO..': "0",
                      '......': " "}

Braille_number_follows= ".O.OOO"

Braille_capital_follows=".....O"

Braille_Decimal_follows=".O...O"

def translate_to_braille(text):
    braille_output =[]
    number_mode = False


    for char in text:

        if char.isupper():
            braille_output.append(Braille_capital_follows)
            braille_output.append(English_To_Braille_alph[char.lower()])

        elif char.isdigit():
                if not number_mode :
                   braille_output.append(Braille_number_follows)
                if  Braille_number_follows in braille_output:
                   number_mode=True
                   braille_output.append(English_To_Braille_alph[char])

        else:
            if number_mode and not char.isdigit(): 
       
                number_mode = False
                braille_output.append("......")
            braille_output.append(English_To_Braille_alph[char])  

    return ''.join(braille_output)




def translate_to_english(braille):
     number_mode = False 
     capital_mode = False
     result = []

     for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]

        if braille_char == Braille_number_follows:
            number_mode = True
            continue
          
        if braille_char == Braille_capital_follows:
            capital_mode = True
            continue  


        if number_mode: 
            if braille_char == "......":
                 number_mode = False
            else:
             result.append(Braille_To_English_numb.get(braille_char, ''))

        else:
            translated_char = Braille_To_English_alph.get(braille_char, '')
            if capital_mode: 
                translated_char = translated_char.upper()
                capital_mode = False  
            result.append(translated_char)

     return ''.join(result)



if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        braille_text = translate_to_braille(text)
        print(braille_text)

# !!!! when entering " python3 translator.py Abc 123 xYz" through the command,
#  the output has extra space symbols after the number because o the space between Abc 123 and xYz 
# since it also reads the space in between each block of characters  !!!!





#TEST
#english_text = "(12c78"
#braille_text = translate_to_braille(english_text)
#print(braille_text) 

#translated_back = translate_to_english(braille_text)
#print(translated_back) 
