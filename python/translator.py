import sys 

#helper function to determine if input is braille or english: 
def is_braille(input_string):
    if all(char in 'O.' for char in input_string):
        return True
    
if __name__ == "__main__":
    # Dictionary for converting English chars to Braille     
    english_to_braille_letters = {
        'a' : 'O.....',  
        'b' : 'O.O...',  
        'c' : 'OO....',  
        'd' : 'OO.O..',  
        'e' : 'O..O..',  
        'f' : 'OOO...',  
        'g' : 'OOOO..',  
        'h' : 'O.OO..',  
        'i' : '.OO...',  
        'j' : '.OOO..',  
        'k' : 'O...O.',  
        'l' : 'O.O.O.',  
        'm' : 'OO..O.',  
        'n' : 'OO.OO.',  
        'o' : 'O..OO.',  
        'p' : 'OOO.O.',  
        'q' : 'OOOOO.',  
        'r' : 'O.OOO.',  
        's' : '.OO.O.',  
        't' : '.OOOO.',  
        'u' : 'O...OO',  
        'v' : 'O.O.OO',  
        'w' : '.OOO.O',  
        'x' : 'OO..OO',  
        'y' : 'OO.OOO',  
        'z' : 'O..OOO'
    }
    
    #dict for converting from english to braille (numbers only)
    english_to_braille_numbers = {
        '1' : 'O.....',  
        '2' : 'O.O...',  
        '3' : 'OO....',  
        '4' : 'OO.O..',  
        '5' : 'O..O..',  
        '6' : 'OOO...',  
        '7' : 'OOOO..',  
        '8' : 'O.OO..',  
        '9' : '.OO...',  
        '0' : '.OOO..',  
    }
    
    #dict for special symbols 
    special_symbols = {
        ' ' : '......',  
        'capital' : '.....O', 
        'number' : '.O.OOO' 
    }

    #creating directions in the opposite direction. 
    braille_to_english_letters = {v: k for k, v in english_to_braille_letters.items()} 
    braille_to_english_numbers = {v: k for k, v in english_to_braille_numbers.items()} 
    
    
    output = ""  #intializing the output string. 
    inarr = [] 
    

    #populating the input array: 
    for i, arg in enumerate(sys.argv[1:], start=1):
        inarr.append(arg) 
        
    #converting "english" to braille 
    if not is_braille(inarr[0]): 
        isnumber = False 
        outword = ""
        
        #joining the input words to a single string to make processing easier. 
        word = ' '.join(inarr)
        
        for char in word:
            #adding capital braille 
            if char.isupper():
                outword += special_symbols['capital']
                outword += english_to_braille_letters[char.lower()]
            #adding numbers 
            elif char.isdigit():
                if not isnumber:  
                    outword += special_symbols['number'] 
                    isnumber = True 
                outword += english_to_braille_numbers[char] 
            #dealing with spaces after number 
            elif char == ' ' and isnumber:
                isnumber = False
                outword += special_symbols[' ']
            #dealing with space 
            elif char == ' ':
                outword += special_symbols[' '] 
            #dealing with other characters. 
            else:
                isnumber = False 
                outword += english_to_braille_letters[char] 
        output += outword 
            
        #adding spaces in between words (making sure not at the end)
        if i < len(inarr) - 1:
            output += special_symbols[' '] 

    #converting braille to english 
    else: 
        outword = "" 
        braille_string = ' '.join(inarr) #generating a single string of braille. 
        
        #chunking the braille string into its pieces.  
        chunks = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]  
        
        #flag for dealing with numbers. 
        isnumber = False 
        
        #iterating over all the chunks 
        index = 0 
        while index < len(chunks):
            #handling capitals 
            if chunks[index] == special_symbols['capital']:
                index += 1
                if index < len(chunks):
                    outword += braille_to_english_letters[chunks[index]].upper()
            #handling spaces 
            elif chunks[index] == special_symbols[' '] and not isnumber:
                outword += " " 
            #handling spaces after numbers 
            elif chunks[index] == special_symbols[' '] and isnumber:
                outword += " "
                isnumber = False
            #handling number braille  
            elif chunks[index] == special_symbols['number']:
                isnumber = True
            #handing numbers 
            elif isnumber:
                outword += braille_to_english_numbers[chunks[index]]
            #handling other characters 
            else:
                outword += braille_to_english_letters[chunks[index]]
            index += 1
        
        output += outword
        
    print(output) 
            
