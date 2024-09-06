import sys

#English to braille character map
eng_char_map = {
        "a":"O.....",
        "b":"O.O...",
        "c":"OO....",
        "d":"OO.O..",
        "e":"O..O..",
        "f":"OOO...",
        "g":"OOOO..",
        "h":"O.OO..",
        "i":".OO...",
        "j":".OOO..",
        "k":"O...O.",
        "l":"O.O.O.",
        "m":"OO..O.",
        "n":"OO.OO.",
        "o":"O..OO.",
        "p":"OOO.O.",
        "q":"OOOOO.",
        "r":"O.OOO.",
        "s":".OO.O.",
        "t":".OOOO.",
        "u":"O...OO",
        "v":"O.O.OO",
        "w":".OOO.O",
        "x":"OO..OO",
        "y":"OO.OOO",
        "z":"O..OOO",
    }

#English to braille number map
eng_num_map = {
        "1":"O.....",
        "2":"O.O...",
        "3":"OO....",
        "4":"OO.O..",
        "5":"O..O..",
        "6":"OOO...",
        "7":"OOOO..",
        "8":"O.OO..",
        "9":".OO...",
        "0":".OOO.."
    }

#English to braille special chars map
eng_spc_map = {
        ".":"..OO.O",
        ",":"..O...",
        "?":"..O.OO",
        "!":"..OOO.",
        ":":"..OO..",
        ";":"..O.O.",
        "-":"....OO",
        "/":".O..O.",
        "<":".OO..O",
        ">":"O..OO.",
        "(":"O.O..O",
        ")":".O.OO.",
        " ":"......"
}

#Braille to english character map
braille_char_map = {value: key for key, value in eng_char_map.items()}

#Braille to english number map
braille_num_map = {value: key for key, value in eng_num_map.items()}

braille_spc_map = {value: key for key, value in eng_spc_map.items()}

#Braille follows alphabet
capf = ".....O"
decf = ".O...O"
numf = ".O.OOO"

#Function to change Braille to English
def braille_to_eng(to_trans):
    
    englished = []
    number = False
    capital = False

    jumps = 6
    braille_groups = [to_trans[i:i+jumps] for i in range(0, len(to_trans), jumps)]

    for i in range(len(braille_groups)):

        if braille_groups[i] == capf: #Sets to true when the capf braile is detected used for logic later
            capital = True
            continue

        elif braille_groups[i] == numf: #Sets to true when the numf braile is detected used for logic later
            number = True
            continue

        elif braille_groups[i] == decf: #Add a decimal point
            englished.append(".")
            continue

        elif braille_groups[i] == "......": #Turns the numberic boolen off at the first space as specified 
            number = False

        if braille_groups[i] == "O..OO." and number == True and (braille_num_map[braille_groups[i-1]]).isnumeric() and (braille_num_map[braille_groups[i+1]]).isnumeric: #Since > is a dupe value of o in the chars i decide to only use it when there is a number before and after to show greater than
            englished.append(braille_spc_map[braille_groups[i]])
            continue

        if number == True and  braille_groups[i] in braille_num_map: #Only allows the selection of numbers when the bool is active as there should only be numbers till the next space
            englished.append(braille_num_map[braille_groups[i]])
        
        elif braille_groups[i] in braille_char_map: #Only selects chars or spc chars when number isnt True

            if capital == True: #If the capital braile is detected it only capitalizes the next character then turns off
                englished.append(braille_char_map[braille_groups[i]])
                englished[-1] = englished[-1].upper()
                capital = False
            else:
                englished.append(braille_char_map[braille_groups[i]])

        elif braille_groups[i] in braille_spc_map: #Only selects chars or spc chars when number isnt True
            englished.append(braille_spc_map[braille_groups[i]])

        else:
            raise ValueError("Character not in Dictionarys") #If the character doesnt exist in both dictionaries it throws an error

    braille_result = ''.join(englished) #takes all the results and put it in one string

    return braille_result


#Function to change English to Braille
def eng_to_braille(to_trans):

    brailled = []
    number = False
    trans_str_eng = list(to_trans)
    
    for i in range(len(trans_str_eng)):

        if trans_str_eng[i].isupper(): #Adds upper Alpha follows is letter is capital then lowers the case
            brailled.append(capf)
            trans_str_eng[i] = trans_str_eng[i].lower()

        elif trans_str_eng[i].isnumeric() and number == False: #Adds number Alpha if char is a number only adds it once
            brailled.append(numf)
            number = True

        elif number == True and trans_str_eng[i] == "." and trans_str_eng[i+1].isnumeric(): #Adds decimal alpha if there is a number before the dot
            brailled.append(decf)
            continue

        elif trans_str_eng[i] == "." and trans_str_eng[i+1].isnumeric(): #Correctly places the right braille groups before decimals without a number before it
            brailled.append(numf)
            brailled.append(eng_spc_map["."])
            number = True
            continue


        


        elif trans_str_eng[i] == " ": #Turns the numberic boolen off at the first space as specified 
            number = False


        if trans_str_eng[i] in eng_char_map: #Checks the dictionary to see if there a char that matches
            brailled.append(eng_char_map[trans_str_eng[i]])
       
        elif trans_str_eng[i] in eng_num_map: #Checks the dictionary to see if there a number that matches
            brailled.append(eng_num_map[trans_str_eng[i]]) 

        elif trans_str_eng[i] in eng_spc_map: #Checks the dictionary to see if there a special char that matches
            brailled.append(eng_spc_map[trans_str_eng[i]])

        else:
            raise ValueError("Character not in Dictionarys") #If the character doesnt exist in both dictionaries it throws an error

    
    eng_result = ''.join(brailled) #takes all the results and put it in one string

    return eng_result



#Main function
def main():
    
    translated = []

    for arg in sys.argv[1:]:
        if all(c in {'.', 'O'} for c in arg): #check if its braille or english
           translated.append(braille_to_eng(arg))
        else:
            translated.append(eng_to_braille(arg))
            
            if arg != sys.argv[-1]:
                translated.append(eng_spc_map[" "])

    result = ''.join(translated) #takes all the results and put it in one string

    print(result)

    return

if __name__ == "__main__":
    main()