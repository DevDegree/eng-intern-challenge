import sys

#dictionaries used to translate from english to braille and vice-versa
english_to_braille_dictionary= {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
    #"Capital follows": ".....O" , "Number follows": ".O.OOO" ,    
    ".": "..OO.O", ",": "..O...", "?": "...OOO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..O", "(": "O.O..O", ")": ".O.OO.", " ": "......"
    # ">": "O..OO." has the same pattern as "o":"O..OO."
}
english_to_braille_dictionary_numbers= {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO.."
}
braille_to_english_dictionary= {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", 
    "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h", 
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", 
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", 
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", 
    "OO.OOO": "y", "O..OOO": "z",
    ".....O": "Capital follows", ".O.OOO": "Number follows", ".O...O": "Decimal follows",   
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", 
    ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", "......": " "
    # ">": "O..OO." has the same pattern as "o":"O..OO."
}
braille_to_english_dictionary_numbers= {
    "O.....":"1", "O.O...":"2", "OO....":"3", "OO.O..":"4",
    "O..O..":"5", "OOO...":"6", "OOOO..":"7", "O.OO..":"8",
    ".OO...":"9", ".OOO..":"0"
}




#returns true if input_text is in braille and false if it's in english.
def determine_braille_or_english(input_text):

    #checks for multiple args 
    #an input in braille is comprised of only 1 argument (1 long string) 
    #whereas English can be comprised of 1 or more args
    if len(input_text) > 1: 
        return False        
    
    #checks if arg length is a multiple of 6
    # if the input isn't a multiple of 6, then it cant be in braille
    elif len(input_text[0])%6 != 0: 
        return False
    
    #if all the char in the string are "O" or "." then the text is considered in braille
    else :
        for char in input_text[0]:
            if char != "O" and char != ".":
                return False
    #if the input_text fails every previous conditions,then it is in braille.
    return True

#translates the input_text from braille to english
def translate_to_english(input_txt):
    output_txt = ""             #text translated to english that will be printed 
    is_number_flag = False      #if true then the sequence is considered a number instead of a letter
    capital_flag = False        #If true then the following character is a capital letter

    input_txt= input_txt[0]     #the text in braille is passed as one argument into the command line

    #Take 6 character in braille to translate one at a time.
    #Every 6 character sequence in braille represents one character in english.
    for i in range(0,len(input_txt)-5,6):
        char = input_txt[i:i+6]
        
        #verifies that the 6 character sequence is a valid one and stops the program if its not valid
        try:
            braille_to_english_dictionary[char]
        except:
            print("not a valid 6 character sequence")
            sys.exit(1) 

        
        # Checks if the 6 character sequence is the one to indicate 
        # that the following 6 character sequences are numbers
        # and changes the flag to true 
        if(char == ".O.OOO"):
            is_number_flag=True

        # Checks if the 6 character sequence is the one to indicate 
        # that the following 6 character sequence is a capital letter
        # and changes the flag to true 
        elif(char == ".....O"):
            capital_flag= True

        # Checks if the 6 character sequence is the one for a space " "
        # and adds it to the output_text.
        # Also sets the is_number_flag to false
        elif(char == "......"):
            output_txt += braille_to_english_dictionary[char]
            is_number_flag= False

        else:

            # If the is_number_flag is true then we use the english_to_braille_dictionary_numbers to 
            # add the corresponding number to the output_txt 
            if(is_number_flag):
                output_txt += braille_to_english_dictionary_numbers[char] 

            # If the is_number_flag is false then we use the english_to_braille_dictionary 
            else:

                # If the capital_flag is true then the letter added will be capitalized in the output_txt 
                if(capital_flag):
                    output_txt += braille_to_english_dictionary[char].upper()
                    capital_flag= False

                # the character sequence is translated using the english_to_braille_dictionary and added to the output_txt 
                else:  
                    output_txt += braille_to_english_dictionary[char]

    #prints the translated message in english.
    print(output_txt)
        
#translates the text from english to braille
def translate_to_braille(input_txt):
    output_txt = ""                 #text that will be printed 
    is_first_number_flag = True     #if true then the sequence is considered a number instead of a letter

    for word in range (len(input_txt)):

        # adds the space " " in braille to the output text in between every args (word) passed in the command line
        # and returns the is_first_number_flag to true after adding a space
        if(word!=0): 
            output_txt += "......"
            is_first_number_flag = True 
        for char in input_txt[word]:

            
            # checks if the character is a digit, if its the first number in the word 
            # and adds the corresponding braille sequnce to the output_txt.
            # if it is the first number in the word, is_first_number_flag is set to false. 
            if(char.isdigit()):
                if(is_first_number_flag):
                    output_txt += ".O.OOO"
                    is_first_number_flag= False
                output_txt +=  english_to_braille_dictionary_numbers[char]
            else:

                # verifies that the character has a corresponding 6 character sequence in braille 
                # and stops the program if its not valid
                try:
                    english_to_braille_dictionary[char.lower()]
                except:
                    print(char)
                    print("Character doesn't have a 6 character sequence in braille")
                    sys.exit(1)

                # If the character is capatolized then it will add the "capital follows" sequence in braille
                # before adding the corresponding 6 character sequence in braille to the output_txt
                if(char.isupper()):

                    output_txt += ".....O" + english_to_braille_dictionary[char.lower()]

                # adds the corresponding 6 character sequence in braille to the output_txt    
                else:
                    output_txt +=  english_to_braille_dictionary[char]

    #prints the translated message in braille.
    print (output_txt)


def main():
    input =sys.argv[1:]
    input_in_braille = determine_braille_or_english(input)
    

    
    if(input_in_braille):
        translate_to_english(input)
    else:
        translate_to_braille(input)




if __name__ == "__main__":
    main()