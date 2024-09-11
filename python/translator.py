import sys

class translator:
    eng_to_braille_table = {
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
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "0": ".OOO..",
        " ": "......",
        "capital": ".....O",
        "number": ".O.OOO"
    }
    
    braille_to_eng_table_alpha = {
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",   
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q", 
        "O.OOO.": "r",   
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",  
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",     
        "......": " ",
        ".....O": "capital",
        ".O.OOO": "number"
    }
    
    braille_to_eng_table_number = {
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
    }
    
    def __init__(self):
        pass
    
    def is_braille(self, input):
        braille_flag = False

        for i in input:
            if braille_flag and i != "O" and i != ".":
                print("Invalid input.")
                exit(1)

            if i == ".":
                braille_flag = True
            
        return True if braille_flag else False
    
    def eng_to_braille(self, input):
        result = []
        
        number_flag = False
        
        for char in input:
            if char.isalpha():
                if number_flag:
                    result.append(self.eng_to_braille_table[" "])
                    number_flag = False
                    
                if char.isupper():
                    result.append(self.eng_to_braille_table["capital"])
                    
                char = char.lower()
                temp = self.eng_to_braille_table.get(char, "ERROR")
                if temp == "ERROR":
                    print("Invalid input.")
                    exit(1)
                else:
                    result.append(temp)
                
            elif char.isdigit():
                if not number_flag:
                    number_flag = True
                    result.append(self.eng_to_braille_table["number"])
                result.append(self.eng_to_braille_table[char])
                
            elif char == " ":
                result.append(self.eng_to_braille_table[" "])
                
        return "".join(result)
                
    def braille_to_eng(self, input):
        result = []
        
        number_flag = False
        capital_flag = False
        
        for i in range(0, len(input), 6):
            braille_chunk = input[i:i + 6]
            decoded_char = self.braille_to_eng_table_alpha.get(braille_chunk, "ERROR")

            if decoded_char == "ERROR":
                print("Invalid input.")
                exit(1)
            elif decoded_char == "capital":
                capital_flag = True
                continue
            elif decoded_char == "number":
                number_flag = True 
                continue  
            elif decoded_char == " " and number_flag:
                number_flag = False
                continue
            
            if number_flag:
                result.append(self.braille_to_eng_table_number[braille_chunk])           
            elif capital_flag:
                character = self.braille_to_eng_table_alpha[braille_chunk]
                result.append(character.upper())
                capital_flag = False
            else:
                result.append(decoded_char)
            
        return "".join(result)
        
    def solve(self, input):
        if self.is_braille(input):
            return self.braille_to_eng(input)
        else:
            return self.eng_to_braille(input)
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing arguments.")
        exit(1)
    
    input = " ".join(sys.argv[1:])
    print(translator().solve(input))