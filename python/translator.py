#August 29, 2024
#Michael Karas 
#Shopify Submission for 2025 Winter Internships

#Import sys for testing pruposes
import sys

#other dependencies
import startup
import translator_functions
import unittest


#First check to see if string input is braille or English

#If Check says it is braille, create a new list/array where each element is of length 6, which keeps the info we need ex '[.0....],..'
#Length of new list/array will be equal to input/length of element (6)

#For braille, will need to code to handle cases where it is stating if the next element is a space, number, decimal or capital letter
#With those cases, theyll be sent to booleans and modifiy the outcome to the if statement properly

#If in English, create a new list/array and have each ellement within it seperated like "[A,b,c,1,...]"
#Sorta like with braille, create a boolean to handle cases when a capital letter is needed
#For cases with numbers, we will append the appropriate braille signifier to the first number of the string 

#The following is my dictionary that has 
dict_Eng_Bra = startup.setupDict()

# #English to Braille Translator


#Each braille term has 'O' present except for space, which has no "O's"
def translation_Setting(text):
    if (len(text) % 6 == 0 and ('O' in text or '......' in text)):
        #Braille
        output = translator_functions.bra_To_Eng(text,dict_Eng_Bra)
    else:
        #English
        output = translator_functions.eng_To_Bra(text, dict_Eng_Bra)

    print (output)

#Excecution of program
if __name__ == "__main__":

    text = ' '.join(sys.argv[1:]).strip()
    #text = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO"
    #text = " .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
    #text = "Abc 123 xYz"
    if (len(text) % 6 == 0 and ('O' in text or '......' in text)):
    #Braille
        output = translator_functions.bra_To_Eng(text,dict_Eng_Bra)
    else:
    #English
        output = translator_functions.eng_To_Bra(text, dict_Eng_Bra)

    print (output)