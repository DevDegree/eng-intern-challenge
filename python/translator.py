import sys
# writing out the English to Braille alphabet 
braille_alphabet = {'a': "O.....", 'b':'O.O...', 'c':"OO....", 'd':"OO.O..", 'e':"O..O..",
            'f':'OOO...', 'g':'OOOO..', "h":"O.OO..", "i":".OO...",
            'j':'.OOO..', 'k':'O...O.', "l":"O.O.O.", "m":"OO..O.",
            "n":"OO.OO.", "o":"O..OO.", "p":"OOO.O.", 'q':"OOOOO.", 
            "r":"O.OOO.", "s":".OO.O.", "t":".OOOO.", "u":"O...OO",
            "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", 
            "z":"O..OOO"}

braille_numbers = { '1':"O.....", '2':"O.O...", '3':"OO....",
            '4':"OO.O..", '5':"O..O..", '6':"OOO...", '7':"OOOO..", 
            '8':"O.OO..", '9':".OO...", '0':".OOO.."}

braille_symbols = { " ":"......", "capital":".....O", "number":".O.OOO"}

# now reversing the dictionary to get the English to Braille alphabet 
english_alphabet = {value: key for key, value in braille_alphabet.items()}

english_numbers = {value: key for key, value in braille_numbers.items()}

english_symbols = {value: key for key, value in braille_symbols.items()}

# writing a function that converts English to Braille
# convert English to Braille 
def convert_english_to_braille(s):
    braille = ""
    for index, c in enumerate(s): 
        if c.isupper(): # upper case letters
            braille += braille_symbols["capital"]
            c = c.lower()
            braille += braille_alphabet[c]
        elif c in braille_alphabet:
            braille += braille_alphabet[c]
        elif c.isdigit():
            # if digit is the first thing in the string
            if index == 0: 
                braille += braille_symbols["number"] 
                braille += braille_numbers[c]
            elif s[index-1].isdigit():
                braille += braille_numbers[c]
            else: 
                braille += braille_symbols["number"]
                braille += braille_numbers[c]
        elif c in braille_symbols:
            braille += braille_symbols[c]
    return braille

# writing a function to split the braille characters by 6 
# to be able to convert every braille character individually into English
def split_string_by_six(s):
    return [s[i:i + 6] for i in range(0, len(s), 6)]

# writing a function to convert Braille to English 
def convert_braille_to_english(s):
    list_braille = split_string_by_six(s) # first splitting into individual braille characters
    english = ""
    skip_next = False
    is_digit = False 
    for index, char in enumerate(list_braille):
        if skip_next: # if it is a digit will be taken care of next
            skip_next = False
            continue
        elif char in english_symbols:
            if english_symbols[char] == "capital":
                english += english_alphabet[list_braille[index+1]].upper()
                skip_next = True
            elif english_symbols[char] == "number":
                is_digit = True
            elif english_symbols[char] == " ":
                is_digit = False
                english += english_symbols[char]
        elif is_digit:
            english += english_numbers[char]
        else: 
            english += english_alphabet[char]
    return english 

# creating a function that takes in a string and converts it
# to Braille/English depending on the input 
def translate(s):
    flag = 0 
    for char in s: 
        if char == '.': # if it has a . sympbol then it is braille 
            flag = 1
    if flag == 1:
        return convert_braille_to_english(s)
    else: 
        return convert_english_to_braille(s)

# Main function to handle command-line input
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])  # Join all arguments into a single string
        print(translate(input_string))
    
    
    



  

