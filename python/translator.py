#August 29, 2024
#Michael Karas 
#Shopify Submission for 2025 Winter Internships

#Import sys for testing pruposes
import sys
#text = sys.argv
#text = "Hello world"
#text = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO."
#text = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
text = "trans.py"
text= ".OOOO.O.OOO.O.....OO.OO..OO.O...OO.OOOO.O.OO.OOO"
print (f"Input was {text}")

#other dependencies
import startup
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

#English to Braille Translator
def eng_To_Bra(text):
    text_Translate= text
    translated_string = ""
    first_num = False

    for i, char_in_Str in enumerate(text_Translate):
        for translation in dict_Eng_Bra:

            if char_in_Str.lower() == translation[0].lower():
                #Check if value is an uppercase letter 
                if char_in_Str.isupper():
                    translated_string += ".....O" + translation[1]

                #Check if value is a number
                elif char_in_Str.isdigit():
                        #Check if value is the first number or not
                        if not first_num:
                            translated_string += ".O.OOO" + translation[1]
                            first_num = True

                        #Values that are not the first number in the string
                        else:
                            translated_string +=  translation[1]

                        #Check if the next value is a number or not
                        if i+1< len(text_Translate) and not text_Translate[i+1].isdigit():
                            
                            first_num = False
                else:
                     translated_string +=  translation[1]
                break

                #translated_string += capitalized + dict_Eng_Bra[j][1]

    return  translated_string


#Braille to English Translator
def bra_To_Eng(text):
    text_to_be_modified = text
    modified_text = []
    capital = False
    num_mode = False
   
   #This for loop modifies the input and breaks up the braille into 6 characters per element
    for i in range(0, len(text_to_be_modified),6):
        modified_text.append(text_to_be_modified[i:i+6])

    translated_string = ""
    for i, brl_in_Str in enumerate(modified_text):
        for translation in dict_Eng_Bra:
            if brl_in_Str == translation[1]:
                #If statement for when the followoing value is a capital letter
                #Sets a variable for that the next letter in the sequence to have a capial
                print(num_mode)
              
                #check to determine first number of a sequence of elements
                if brl_in_Str == ".O.OOO":
                    num_mode = True
                    continue
                    
                if num_mode:
                    if translation[0].isdigit():
                        translated_string += translation[0]
                    else:
                        num_mode = False

                elif not num_mode and not translation[0].isdigit():
                    if capital == True:
                        #Making a capital letter
                        translated_string += translation[0].upper() 
                        capital = False
                    elif i+1< len (modified_text) and brl_in_Str == ".....O" :
                        capital = True
                    else:
                        #Normal letter in the string
                        translated_string += translation[0]



    return translated_string


class eng_brl_cnvrtr(unittest.TestCase)
#Each braille term has 'O' present except for space, which has no "O's"
if (len(text) % 6 == 0 and ('O' in text or '......' in text)):
    #Braille
    output = bra_To_Eng(text)
else:
    #English
    output = eng_To_Bra(text)

print (output)