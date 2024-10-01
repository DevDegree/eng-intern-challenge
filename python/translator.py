import sys

braille = {
    #letters
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

    #indicators
    "capital_letter_ind": ".....O",
    "number_follows": ".O.OOO",    
    "decimal_follows": ".O...O",   
    " ": "......",
    
    #special characters and punctuations
    ".": "..OO.O",   
    ",": "..O...",  
    "?": "..O.OO",
    "!": "..OOO.",
    "-": "....OO",
    ":": "..00..", 
    ";": "..0.0.", 
    "(": "O.O..O",
    ")": ".O.OO.",
    "/": ".O..O.",  
    "<": ".OO..O",
    ">": "O..OO.",
}
reverse_braille = {v: k for k, v in braille.items()}

braille_numbers={
    #numbers
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO..",
}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

# using a for i loop as it will have more control
def translate_to_braille(word):
    translated = []
    for i in range(len(word)):
        #if character a space
        if word[i] == " ":
            translated.append(braille.get(" ","?"))
    
        #if character is number
        elif word[i].isdigit():
            #if starting character is a number
            if i == 0 and word[i].isdigit():
                translated.append(braille.get("number_follows", "?"))
                translated.append(braille_numbers.get(word[i], "?"))
            #if prev is not a number but number char is not at the start
            elif i > 0 and word[i-1].isnumeric() == False: 
                translated.append(braille.get("number_follows"))
                translated.append(braille_numbers.get(word[i],"?"))
            else:
                translated.append(braille_numbers.get(word[i],"?"))
                
        elif word[i] == ".":
            if word[i-1].isnumeric():
                translated.append(braille.get("decimal_follows","?"))
            else:
                translated.append(braille.get(word[i],"?"))
                
        #if character is a letter
        else:
            if word[i].isupper():
                translated.append(braille["capital_letter_ind"])
                translated.append(braille.get(word[i].lower(), "?"))
            else:
                translated.append(braille.get(word[i],"?")) 
                
        translated = [char if char is not None else " " for char in translated]
    return "".join(translated) # from list to a string

def translate_to_english(braille_text):
    translated = []
    i=0
    isNumber = False
    while i < len(braille_text):
        part = braille_text[i:i+6]
        
        # if part is space
        if part == "......":
            translated.append(reverse_braille.get(part,"?"))
            isNumber = False
        
        #if part is number follows
        elif part == ".O.OOO":
            isNumber = True
            i+=6
            continue
        
        #if part is decimal follows
        elif part == ".O...O":
            translated.append(reverse_braille.get("..OO.O","?"))
        
        elif isNumber:
            translated.append(reverse_braille_numbers.get(part,"?"))
            
        #if part is capital indicator
        elif part == ".....O":
            i+=6
            if i < len(braille_text):
                next_part = braille_text[i:i+6]
                translated.append(reverse_braille.get(next_part, "?").upper())
            isNumber = False
            
        else:
            isNumber = False
            translated.append(reverse_braille.get(part,"?"))
            
        i+=6
        translated = [char if char is not None else " " for char in translated]
    return "".join(translated)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_or_braille>")
        sys.exit(1)

    text_input = ' '.join(sys.argv[1:])

    # Check if the input is Braille or normal text
    if all(c in ".O" for c in text_input):  #check for Braille input
        print(translate_to_english(text_input))
    else:
        print(translate_to_braille(text_input))
        