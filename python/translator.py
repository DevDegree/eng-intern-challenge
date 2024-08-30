# O is a raised dot
# Keep in mind the "Capital follows"


#check if capital than convert to lowercase to lookup
import sys

letters = { 
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    "." : "..OO.O",
    "," : "..O...",
    "?" : "..O.OO",
    "!" : "..OOO.",
    ":" : "..OO..",
    ";" : "..O.O.",
    "-" : "....OO",
    "/" : ".O..O.",
    "<" : ".OO..O",
    ">" : "O..OO.",
    "(" : "O.O..O",
    ")" : ".O.OO.",
    " " : "......",
}

numbers = {
    "1" : "O.....",
    "2" : "O.O...",
    "3" : "OO....",
    "4" : "OO.O..",
    "5" : "O..O..",
    "6" : "OOO...",
    "7" : "OOOO..",
    "8" : "O.OO..",
    "9" : ".OO...",
    "1O" : ".OOO..",
    " " : "......",
}


commands = {
    "capital" : ".....O",
    "decimal" : ".O...O",
    "number" : ".O.OOO",
}


def check(inputs):
    braille_comps = {"O", "."}

    for i, input in enumerate(inputs):
        if all(char in braille_comps for char in input):
            #Then input is braille therefore will translate to English
            toEnglish(input)
        else:
            #Then input has other characters besides . and O then it is braille and must be translated to English
            final = (i == len(inputs) -1)
            toBraille(input, final)
            
        

def toEnglish (s):
    reverse_letters = {v: k for k, v in letters.items()}
    reverse_numbers = {v: k for k, v in numbers.items()}
    reverse_commands = {v: k for k, v in commands.items()}

    i = 0
    char = ""
    word = ""
    command = None
    for i in range(len(s)):    
        char += s[i]
        if (i+1) % 6 == 0:
            if char in reverse_commands:
                command = reverse_commands[char]
            else:              
                if command == "capital":
                    if char in reverse_letters:
                        l = reverse_letters[char]
                        word += l.upper()
                        command = None

                elif command == "number":
                    if char in reverse_numbers:
                        word += reverse_numbers[char]
                       
                
                else:
                    if command == "decimal":
                        word += reverse_letters[char]
                        command = "number"
                        
                    elif char in reverse_letters:
                        word += reverse_letters[char]
                        
                
                if char == "......":
                    command = None
                    
            char = ""  
 
    print(word, end="")



def toBraille(input, final):

    braille = ""
    numberFlag = False
    for char in input:
    
        if char.isdigit():
            if not numberFlag:
                braille += commands["number"]
            numberFlag = True
            
        
        else:
            
            if char.isupper():
                braille += commands["capital"]
            if char == "." and numberFlag:
                braille += commands["decimal"]
                numberFlag = True
            braille += letters[char.lower()]
            if char == "......":
                numberFlag = False
            if numberFlag:
                continue
        if numberFlag:
            braille += numbers[char]
    

    print(braille, end="")
    if not final:
        print("......", end="")
        

if __name__ == "__main__":
    inputs = sys.argv[1:]
    check(inputs)
  
