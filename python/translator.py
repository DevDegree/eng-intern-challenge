
#August 29, 2024
#Michael Karas 
#Shopify Submission for 2025 Winter Internships

#Import sys for testing pruposes
import sys

#other dependencies
import startup
import translator_functions

#The following set of comments are my thoughts when first encountering the problem

# #First check to see if string input is braille or English

# #If Check says it is braille, create a new list/array where each element is of length 6, which keeps the info we need ex '[.0....],..'
# #Length of new list/array will be equal to input/length of element (6)

# #For braille, will need to code to handle cases where it is stating if the next element is a space, number, decimal or capital letter
# #With those cases, theyll be sent to booleans and modifiy the outcome to the if statement properly

# #If in English, create a new list/array and have each ellement within it seperated like "[A,b,c,1,...]"
# #Sorta like with braille, create a boolean to handle cases when a capital letter is needed
# #For cases with numbers, we will append the appropriate braille signifier to the first number of the string 


def translation_Setting(text):
    dict_english_braille = startup.setup_dictionary()
    if (len(text) % 6 == 0 and ('O' in text or '......' in text)):
        #Braille
        output = translator_functions.braille_to_eng(text,dict_english_braille)
    else:
        #English
        output = translator_functions.eng_to_braille(text, dict_english_braille)

    print (output)
def main():
    translation_Setting(text = ' '.join(sys.argv[1:]).strip())
    
#Excecution of program
if __name__ == "__main__":
    main()