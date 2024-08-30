# 1. determine if string is in english or braille
#       -> iterate through each character
#       -> if character is not 'O' or '.' string is in braille
#       -> else string is in english

# 2. If string is in braille
#       -> create dict variable 'BRAILLE-ENGLISH-LETTER-MAP' that has the braille character letters as the keys, and english characters as the values
#       -> create dict variable 'BRAILLE-ENGLISH-NUMBER-MAP' that has the braille numbers as the keys, and english numbers as the values
#       -> create list variable 'braille-characters'
#       -> create string variable 'english-str'
#       -> create bool variable number = False
#       -> iterate through every sixth character
#       -> store characters in string from position i - 6 to position i as item in list
#       -> iterate through 'braille-characters'
    #       -> if item is 'capital follows'
    #           -> search for item in 'BRAILLE-ENGLISH-LETTER-MAP' keys
    #           -> add CAPITALIZED corresponding value to 'english-str'
    #       -> if number == True and item is 'space'
    #           -> set number = False
    #           -> add space to 'english-str'
    #       -> if item is 'number follows' or number == True
    #           -> set number = True
    #           -> search for item in 'BRAILLE-ENGLISH-NUMBER-MAP' keys
    #           -> add corresponding value to 'english-str'
#       -> return 'english-str'

# 3. If string is in english
#       -> create dict variable 'ENGLISH-BRAILLE-MAP' that has the english characters as the keys, and braille characters as the values
#           -> 
#       -> create string variable 'braille-str'
#       -> iterate through every character of string
#           -> if character is number, add 'number-follows'
#           -> if character is capital, add 'capital-follows'
        #   -> if previous character is number and current character is '.' add 'decimal follows' and continue to next iteration
    #       -> search for item in 'ENGLISH-BRAILLE-MAP' keys, add corresponding value to 'braille-str'
#       -> return 'braille-str'

