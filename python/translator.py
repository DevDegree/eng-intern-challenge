import sys 

# Note 1: Braille symbol "o" is the same as ">". There is no way to differentiate between the both of them when 
# translating from braille-to-english. Therefore, I have changed the braille symbol of ">" as all black :"000000"
# Note 2: not sure what decimal follows mean. 

# Braille-English mapping
braille_english = {
    "O....." : "a", 
    "O.O..." : "b", 
    "OO...." : "c", 
    "OO.O.." : "d", 
    "O..O.." : "e", 
    "OOO..." : "f", 
    "OOOO.." : "g",
    "O.OO.." : "h",
    ".OO..." : "i",
    ".OOO.." : "j", 
    "O...O." : "k",
    "O.O.O." : "l",
    "OO..O." : "m",
    "OO.OO." : "n",
    "O..OO." : "o",
    "OOO.O." : "p", 
    "OOOOO." : "q", 
    "O.OOO." : "r", 
    ".OO.O." : "s", 
    ".OOOO." : "t", 
    "O...OO" : "u", 
    "O.O.OO" : "v", 
    ".OOO.O" : "w", 
    "OO..OO" : "x", 
    "OO.OOO" : "y", 
    "O..OOO" : "z",
    ".....O" : "capital", 
    ".O...O" : "decimal", 
    ".O.OOO" : "number", 
    "..OO.O" : ".", 
    "..O..." : ",", 
    "..O.OO" : "?", 
    "..OOO." : "!", 
    "..OO.." : ":", 
    "..O.O." : ";", 
    "....OO" : "-", 
    ".O..O." : "/", 
    ".OO..O" : "<", 
    "OOOOOO" : ">", 
    "O.O..O" : "(", 
    ".O.OO." : ")",
    "......" : " ", 
    }

# English-Braille mapping
english_braille = { v: k for k, v in braille_english.items()}
english_braille.update({
    "A" : ".....OO.....", 
    "B" : ".....OO.O...", 
    "C" : ".....OOO....", 
    "D" : ".....OOO.O..", 
    "E" : ".....OOO.O..", 
    "F" : ".....OOOO...",
    "G" : ".....OOOOO..", 
    "H" : ".....OO.OO..",
    "I" : ".....O.OO...", 
    "J" : ".....O.OOO..", 
    "K" : ".....OO...O.", 
    "L" : ".....OO.O.O.", 
    "M" : ".....OOO..O.", 
    "N" : ".....OOO.OO.", 
    "O" : ".....OO..OO.", 
    "P" : ".....OOOO.O.", 
    "Q" : ".....OOOOOO.", 
    "R" : ".....OO.OOO.", 
    "S" : ".....O.OO.O.", 
    "T" : ".....O.OOOO.", 
    "U" : ".....OO...OO", 
    "V" : ".....OO.O.OO", 
    "W" : ".....O.OOO.O", 
    "X" : ".....OOO..OO", 
    "Y" : ".....OOO.OOO", 
    "Z" : ".....OO..OOO", 
    "1" : "O.....", 
    "2" : "O.O...", 
    "3" : "OO....", 
    "4" : "OO.O..", 
    "5" : "O..O..", 
    "6" : "OOO...", 
    "7" : "OOOO..", 
    "8" : "O.OO..", 
    "9" : ".OO...", 
    "0" : ".OOO..", 
})

#function to determine if input is braille 
def is_braille(input): 
    return all(x in "O." for x in input)

def braille_to_english(braille_input): 
    translated = [] 
    capitalize_next = False
    number_mode = False
    for x in range(0, len(braille_input), 6): 
        symbol = braille_input[x:x + 6] #length of braille input HAS to be multiple of 6 or else error
        if symbol in braille_english: 
            char = braille_english[symbol] #find key char from braille_to_english dict
            if char == "capital": 
                capitalize_next = True
            elif char == "number": 
                number_mode = True
            elif char == " ": 
                translated.append(" ")
                number_mode = False #exit from only numbers mode after space
            else: 
                if number_mode: 
                    number_translation = {
                        "a" : "1", "b" : "2", "c" : "3", "d" : "4", "e" : "5", 
                        "f" : "6", "g" : "7", "h" : "8", "i" : "9", "j" : "0"
                    }
                    char = number_translation.get(char,"ERROR")
                if capitalize_next: 
                    char = char.upper()
                    capitalize_next = False
                translated.append(char)
        else:
            translated.append("ERROR")
    return ''.join(translated)

def english_to_braille(english_input): #missing signs
    translated = []
    first_number = True
    for char in english_input: 
        if char.isupper(): 
            translated.append(english_braille["capital"])
            char = char.lower()
        if char.isdigit(): 
            if first_number: #enter number mode 
                translated.append(english_braille["number"])
                first_number = False
            translated.append(english_braille.get(char, "ERROR"))
        elif char == " ":
            first_number = True
            translated.append(english_braille[" "]) 
        else: 
            translated.append(english_braille.get(char, "ERROR"))
    return ''.join(translated)


def main(): 
    if len(sys.argv) < 2: 
        print("Usage: python3 translator.py <string>")
        return
    
    input_string = " ".join(sys.argv[1:]) #join all arguments into a single string
    if is_braille(input_string): 
        print(braille_to_english(input_string))
    else: 
       print(english_to_braille(input_string))

if __name__ == "__main__": 
    main()

            

