import sys

#Create the String that will store the result
result = ""

#Get the text and remove the file name
args = sys.argv
args.pop(0)


#Store all of the braille alphabet apart from the special characters
braille = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", 
        "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", 
        ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"]

#Make sure that an input was provided
if len(args) == 0:
    print("No input was provided.")

#Check if more than one String was provided since it will only have one if it is in braille
elif len(args) > 1:

    #Combine all words into with spaces in between
    phrase = args[0]
    for index in range(1, len(args)):
        phrase += " " + args[index]
    
    #Create the variable to track if the "number follows" character is in effect
    currentlyNums = False

    #Loop through every character in the English text and add the braille equivalent to the result
    for letter in phrase:
         #Check if the current character is a space
        if letter == " ":
            #Add the space to the result text and reset the number checker to false
            result += "......"
            currentlyNums = False
                
        #Check if the current character is a number
        elif ord(letter) < 65:
            #Check if the "number follows" character has been added already
            if not currentlyNums:
                #Add the "number follows" character and set the checker to true
                currentlyNums = True
                result += ".O.OOO"

            #Check if the current number is a 0
            if letter == "0":
                    result += braille[9]
           
            else:
                #Add the current number to the result text
                result += braille[ord(letter) - 49]

        #Check if the current character is a captial letter   
        elif letter.isupper():
            #Add the "captial follows" character followed by the captial letter
            result += ".....O"
            result += braille[ord(letter) - 65]

        else:
            #Add the current lowercase letter to the result text
            result += braille[ord(letter) - 97]

#Check if it is a single word or braille using the assumption that if it is English it won't contain a '.'
elif "." in args[0]:

    #Split the long braille string into substrings of 6 characters each
    brailleLetters = []
    for i in range(0, len(args[0]), 6):
        brailleLetters.append(args[0][i : i+6])

    #Create variables to keep track of whether or not the "capital follows" or "number follows" characters are in effect
    currentlyNums = False
    currentlyCapital = False

    #Loop through every letter in the braille text
    for letter in brailleLetters:
       #Check if the current character is "captial follows"
        if letter == ".....O":
            currentlyCapital = True
        
        #Check if the current character is "number follows"
        elif letter == ".O.OOO":
            currentlyNums = True
        
        #Check if the "number follows" character is in effect
        elif currentlyNums:
            #Check if the current character is a space
            if letter == "......":
                #Add the space and reset the number checker to false
                currentlyNums = False
                result += " "
            
            #Check if the current character is a 0
            elif letter == ".OOO..":
                result += "0"

            else:
                #Add the appropriate number to the result text
                result += chr(braille.index(letter) + 49)
        
        #Check if the "captial follows" character is in effect
        elif currentlyCapital:
            #Check if the current character is a space
            if letter == "......":
                result += " "
            
            else:
                #Add the capital character to the result text and reset the capital checker to false
                currentlyCapital = False
                result += chr(braille.index(letter) + 65)
        
        else:
            #Check if the current character is a space
            if letter == "......":
                result += " "
            
            else:
                #Add the lowercase letter to the result text
                result += chr(braille.index(letter) + 97) 

else:
    #Create the variable to track if the "number follows" character is in effect
    currentlyNums = False

    #Loop through every character in the English text and add the braille equivalent to the result
    for letter in args[0]:
        #Check if the current character is a space
        if letter == " ":
            #Add the space to the result text and reset the number checker to false
            result += "......"
            currentlyNums = False
                
        #Check if the current character is a number
        elif ord(letter) < 65:
            #Check if the "number follows" character has been added already
            if not currentlyNums:
                #Add the "number follows" character and set the checker to true
                currentlyNums = True
                result += ".O.OOO"

            #Check if the current number is a 0
            if letter == "0":
                    result += braille[9]
           
            else:
                #Add the current number to the result text
                result += braille[ord(letter) - 49]

        #Check if the current character is a captial letter   
        elif letter.isupper():
            #Add the "captial follows" character followed by the captial letter
            result += ".....O"
            result += braille[ord(letter) - 65]

        else:
            #Add the current lowercase letter to the result text
            result += braille[ord(letter) - 97]
            
#Print the result
print(result)