import os
import sys

# Braille to English Dictionary with no numbers
bra_to_eng_no_num = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
    "OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".O.O..": 'i', ".OOO..": 'j',
    "O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
    "OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
    "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
    "O..OOO": 'z', "......": ' ', "O...O.": '.', "..O.OO": '?', "..OOO.": '!',
    "..OO..": ':', "..O.O.": ';', "....OO": '-', ".O..O.": '/', ".OO..O": '<',
    "O.O..O": '>', "O.O..O": '(', ".O.OO.": ')'
    }
# Braille to Numbers
bra_to_eng_with_num = {
     "O.....": '1', "O.O...": '2', "OO....": '3',
    "OO.O..": '4', "O..O..": '5', "OOO...": '6', "OOOO..": '7', "O.OO..": '8',
    ".OO...": '9', ".OOO..": '0'
}

# reversing the Dictionaries
eng_to_bra_no_num = {value: key for key, value in bra_to_eng_no_num.items()}
eng_to_bra_with_num = {value: key for key, value in bra_to_eng_with_num.items()}

# To check if its Braille
def isBraille(s) :
    return all(char in 'O.' for char in s)
 
def translate_bra_to_eng(s) : 
    ans = ""
    i = 0 
    num_follow = False
    while i < len(s) :
        
        if s[i:i+6] == ".....O" : #Capital follows
            i = i + 6
            ans = ans + bra_to_eng_no_num[s[i:i+6]].upper() 
             
        elif s[i:i+6] == "......" : #space encountered
            
            ans = ans + bra_to_eng_no_num[s[i:i+6]]
            num_follow = False  
            
        elif s[i:i+6] == ".O...O" : #decimal follows  
            
            ans += "."              
        
        elif s[i:i+6] == ".O.OOO" or num_follow: #Number follows
            
            if num_follow == False:
                i = i + 6
            num_follow = True
            ans = ans + bra_to_eng_with_num[s[i:i+6]]  
            
        else :
            
            ans = ans + bra_to_eng_no_num[s[i:i+6]]
        
        i+= 6
    return ans 

def translate_eng_to_bra(s) :
    ans = ""
    num_follow = False
    
    i = 0
    while i < len(s) :
        
        if s[i].isupper() : #Capital follows
            
            ans += ".....O"
            ans += eng_to_bra_no_num[s[i].lower()]
            
        elif s[i] == ' ' : #Space encountered
            
            num_follow = False
            ans += "......"
            
        elif s[i] == "." : #Decimal encountered
            
            ans+= ".O...O"
        
        elif s[i].isnumeric() or num_follow : #numbers
            
            if num_follow == False :
                ans += ".O.OOO"
            num_follow = True
            ans += eng_to_bra_with_num[s[i]]

        else :
            ans += eng_to_bra_no_num[s[i]]
            
        i+=1
    return ans

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please add a string that needs to be translated")
        sys.exit(1)
        
    user_input = " ".join(sys.argv[1:])
        
    if(isBraille(user_input)) :
        result = translate_bra_to_eng(user_input)
    else :
        result = translate_eng_to_bra(user_input)
    
    print(result)        
