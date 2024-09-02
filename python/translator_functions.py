#this file holds the code that does the translation from English to Braille or Braille to English
#Bulk of the code is here

UPPER_CASE_BRAILLE = ".....O"
NUMBER_BRAILLE = ".O.OOO"

def change_case(bool):
    return not bool

def text_modification(text_to_be_modified):

    return [text_to_be_modified[i:i+6] for i in range(0, len(text_to_be_modified), 6)]

def eng_to_braille(text, dict_english_braille):
    text_Translate= text
    translated_string = ""
    first_num = False

    for i, char_in_string in enumerate(text_Translate):
        for translation in dict_english_braille:

            if char_in_string.lower() == translation[0].lower():
                #Check if value is an uppercase letter 
                if char_in_string.isupper():
                    translated_string += UPPER_CASE_BRAILLE  + translation[1]

                #Check if value is a number
                elif char_in_string.isdigit():
                        #Check if value is the first number or not
                        if not first_num:
                            translated_string += NUMBER_BRAILLE + translation[1]
                            first_num = change_case(first_num)

                        #Values that are not the first number in the string
                        else:
                            translated_string +=  translation[1]

                        #Check if the next value is a number or not
                        if i+1< len(text_Translate) and not text_Translate[i+1].isdigit():
                            
                            first_num = change_case(first_num)
                else:
                     translated_string +=  translation[1]
                break


    return  translated_string


#Braille to English Translator
def braille_to_eng(text, dict_english_braille):
    modified_text = text_modification(text)
    capital = False
    num_mode = False
    translated_string = ""
    
    for i, braille_in_string in enumerate(modified_text):
        for translation in dict_english_braille:

            if braille_in_string == translation[1]:


                #check to determine first number of a sequence of elements
                if braille_in_string == NUMBER_BRAILLE:
                    num_mode = change_case(num_mode)

                if translation[0].isdigit() and num_mode:
                    translated_string +=  translation[0]

                    #This would be an expansion to switch back from numbers to letters, but for the scope of this assessment it is not required                    
                    # if i+1< len(modified_text)and not translation[0].isdigit():
                    #     num_mode = change_case(num_mode)

                elif not num_mode and not translation[0].isdigit():
                    if capital == True:
                        #Making a capital letter
                        translated_string += translation[0].upper() 
                        capital = change_case(capital)
                    elif i+1< len (modified_text) and braille_in_string == UPPER_CASE_BRAILLE:
                        capital = change_case(capital)
                    else:
                        #Normal letter in the string
                        translated_string += translation[0]
                else:
                    continue
                break



    return translated_string