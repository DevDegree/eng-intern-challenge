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

#Braille to english character map
braille_char_map = {value: key for key, value in eng_char_map.items()}

#Braille to english number map
braille_num_map = {value: key for key, value in eng_num_map.items()}

#Braille follows alphabet
capf = ".....O"
decf = ".O...O"
numf = ".O.OOO"

#Function to change Braille to English
def braille_to_eng(to_trans):
    

    return


#Function to change English to Braille
def eng_to_braille(to_trans):

    brailled = []
    number = False

    trans_str_eng = list(to_trans)
    
    for i  in range(len(trans_str_eng)):

        if trans_str_eng[i].isupper(): #Adds upper Alpha follows is letter is capital then lowers the case
            brailled.append(capf)
            trans_str_eng[i] = trans_str_eng[i].lower()

        elif trans_str_eng[i].isnumeric() and number == False: #Adds number Alpha if char is a number only adds it once
            brailled.append(numf)
            number = True

        elif trans_str_eng[i] == "." and trans_str_eng[i-1].isnumeric(): #Adds decimal alpha if the 
            brailled.append(decf)
            continue

        elif trans_str_eng[i] == " ": #Turns the numberic boolen off at the first space as specified 
            number = False


        if trans_str_eng[i] in eng_char_map:
            brailled.append(eng_char_map[trans_str_eng[i]])
       
        elif trans_str_eng[i] in eng_num_map:
            brailled.append(eng_num_map[trans_str_eng[i]]) 

        else:
            raise ValueError("Character not in Dictionarys")

    
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
                translated.append(eng_char_map[" "])

    result = ''.join(translated) #takes all the results and put it in one string

    print(result)

    return

if __name__ == "__main__":
    main()