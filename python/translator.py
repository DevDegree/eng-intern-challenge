#Ovia Kandiah
import sys #to use sys.argz
#make a dictionary containing letter, number and symbol representations in braile
braile_symbols = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "capital follows": ".....O",
    "decimal follows": ".O...O",
    "number follows": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
     " ": "......"  
}

#second dict for translations from braile to english
english_dict = {
    "O.....":"a", 
    "O.O...":"b",
    "OO....":"c", 
    "OO.O..":"d", 
    "O..O..":"e",
    "OOO...":"f", 
    "OOOO..":"g", 
    "O.OO..":"h", 
    ".OO...":"i", 
    ".OOO..":"j",
    "O...O.":"k", 
    "O.O.O.":"l", 
    "OO..O.":"m", 
    "OO.OO.":"n", 
    "O..OO.":"o",
    "OOO.O.":"p", 
    "OOOOO.":"q", 
    "O.OOO.":"r", 
    ".OO.O.":"s", 
    ".OOOO.":"t",
    "O...OO":"u", 
    "O.O.OO":"v", 
    ".OOO.O":"w", 
    "OO..OO":"x", 
    "OO.OOO":"y",
    "O..OOO":"z", 
    ".....O":"capital follows", 
    ".O.OOO":"number follows", 
    ".O...O" : "decimal follows",
    ".O...O":".",
    "......":  " ",
    ".O.OO.": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.":";" ,
    "....OO": "-",
    ".O..O.": "/" ,
    ".OO..O":"<" ,
    "O..OO.":">" ,
    "O.O..O": "(",
    ".O.OO.": ")",        
}

#third dict to seperate numbers as they share the same braile as some other characters
english_numbers = {

    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4", 
    "O..O..": "5",
    "OOO...": "6", 
    "OOOO..": "7", 
    "O.OO..": "8", 
    ".OO...": "9", 
    ".OOO..": "0",
    "......": " ",
}

def python_input_eng_or_braile(input):
#function to see whether the input is braile or english
    if len(input) >= 6: #can only be braille if the length is equal to or greater than 6
        for i in range(0,len(input)):
            if input[i] != "O" and input[i] != ".":
                return True #input is english
            else:
                return False #input is braile
    else:
        return True

def split_braile(input,length=6): 
#function to spilt input into 6 substrings
    substrings = [] #initialize an empty list for substrings
    for i in range(0, len(input), length):
        substring = input[i:i+length] #6 character substrings
        substrings.append(substring)
    return substrings
    pass

def python_translator(input):
    #main translator function
    if python_input_eng_or_braile(input) == True: #utilizing function above to check if input is braile or english

        braile = [] #empty list to append
        #print(input)
        for i in range(0,len(input)):
            #print("here")
            #print(i)
            if input[i].lower() in braile_symbols.keys(): #check if input is in dict
                if input[i].isnumeric():
                    if i != 0: #condition for number follows
                        if not input[i-1].isdigit():
                            braile.append(braile_symbols["number follows"])

                if i != 0:
                    if input[i]=="." and input[i-1].isnumeric(): #condition for decimal
                        braile.append(braile_symbols["decimal follows"])
       
                if input[i].isupper(): #condition for capitials
                    braile.append(braile_symbols["capital follows"])
            
                braile.append(braile_symbols[input[i].lower()])
     
            else:
                print("This character does correspond to any english to braile translations.") #error message for user if input character is not present

        return "".join(braile)
    
    else:
        braile_text = split_braile(input,6)
        english = []
        capital_follows = False
        number_follows = False
        decimal_follows = False
        is_number = False #keeps track of if i is a number
        for i in range(0,len(braile_text)):
            if braile_text[i] in english_dict.keys():
                if braile_text[i] != ".....O" and braile_text[i] != ".O.OOO" and braile_text != ".O...O":
                    if i != 0: #do not want to check i-1 if i=0
                        if braile_text[i-1] == ".....O": #capital check
                            capital_follows = True

                    if i != 0:
                        if braile_text[i-1] == ".O.OOO": #number check
                            number_follows = True
                            is_number = True

                    if braile_text[i] == "......":
                        is_number = False

                    if i != 0:        
                        if braile_text[i-1] == ".O...O": #decimal check
                            decimal_follows = True
                            
                    if capital_follows:
                        english.append(english_dict[braile_text[i]].upper()) #appends a capital letter if capital follows is present in i-1
                        capital_follows = False
                    elif number_follows or is_number == True:
                        english.append(english_numbers[braile_text[i]]) #appends a number if number follows is present for i-1
                        number_follows = False
                    elif decimal_follows:
                        english.append(english_numbers[braile_text[i]]) #appends a number if a decimal is detected
                        decimal_follows = False
                    elif is_number:
                        english.append(english_numbers[braile_text[i]])
                        is_number = False
                    else:
                        english.append(english_dict[braile_text[i]])
            else:
                print("This character does not correspond to any braile to english translations") #error message for user
        return "".join(english)

if __name__ == "__main__": #using sys.argv as input for unit test
    command = " ".join(sys.argv[1::])
    print(python_translator(command))
    

