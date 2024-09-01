def eng_To_Bra(text, dict_Eng_Bra):
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


    return  translated_string


#Braille to English Translator
def bra_To_Eng(text, dict_Eng_Bra):
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


                #check to determine first number of a sequence of elements
                if brl_in_Str == ".O.OOO":
                    num_mode = True

                print(num_mode)
                if translation[0].isdigit() and num_mode:
                    print(translation)
                    translated_string +=  translation[0]


                    #This would be an expansion to switch back from numbers to letters, but for the scope of this assessment it is not required                    
                    if i+1< len(modified_text)and not translation[0].isdigit():
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
                else:
                    continue
                break



    return translated_string