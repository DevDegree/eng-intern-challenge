import sys
import re

# Store the given input from the command line (cast to string just in case)
input = ""
for string in sys.argv[1:]:
    input += str(string) + " "
input = input.strip()

# Output variable to hold our final translation
output = ""

# If we are translating from Engish to Braille
if re.search('(?![oO])[a-zA-Z0-9]', input):

    isNum = False;

    # Go through every character
    for char in input:

        # If the character is a space
        if (char == ' '):

            # Set as 'space'
            output += "......"

            # If we have been dealing with numbers thus far
            if (isNum):

                # Set the flag back to False
                isNum = False
        
        # If the character is a period
        elif (char == '.'):

            # Check to see if we are dealing with numbers
            if (isNum):

                # Set as 'decimal follows'
                output += ".O...O"
            
            # Set as '.'
            output += "..OO.O"
        
        # Check other special characters
        elif (char == ','):

            output += "..O..."

        elif (char == '?'):

            output += "..O.OO"

        elif (char == '!'):

            output += "..OOO."

        elif (char == ':'):

            output += "..OO.."

        elif (char == ';'):

            output += "..O.O."

        elif (char == '-'):

            output += "....OO"

        elif (char == '/'):

            output += ".O..O."

        elif (char == '<'):

            output += ".OO..O"

        elif (char == '>'):

            output += "O..OO."

        elif (char == '('):

            output += "O.O..O"

        elif (char == ')'):

            output += ".O.OO."

        # Otherwise, check if the character is a number and this is the first number in a row
        elif (char.isdigit() and isNum == False):

            # Set as 'number follows'
            output += ".O.OOO"

            # Set flag as True
            isNum = True;
        
        # If we are working with letters
        if (not isNum):

            # If the character we are on is capitalized
            if (char.isupper()):

                # Set as 'capital follows'
                output += ".....O"

            # Start checking the letters
            if (char.lower() == 'a'):

                output += "O....."

            elif (char.lower() == 'b'):

                output += "O.O..."

            elif (char.lower() == 'c'):

                output += "OO...."

            elif (char.lower() == 'd'):

                output += "OO.O.."

            elif (char.lower() == 'e'):

                output += "O..O.."

            elif (char.lower() == 'f'):

                output += "OOO..."

            elif (char.lower() == 'g'):

                output += "OOOO.."

            elif (char.lower() == 'h'):

                output += "O.OO.."

            elif (char.lower() == 'i'):

                output += ".OO..."

            elif (char.lower() == 'j'):

                output += ".OOO.."

            elif (char.lower() == 'k'):
                
                output += "O...O."

            elif (char.lower() == 'l'):

                output += "O.O.O."

            elif (char.lower() == 'm'):

                output += "OO..O."

            elif (char.lower() == 'n'):

                output += "OO.OO."

            elif (char.lower() == 'o'):

                output += "O..OO."

            elif (char.lower() == 'p'):

                output += "OOO.O."
                
            elif (char.lower() == 'q'):

                output += "OOOOO."

            elif (char.lower() == 'r'):

                output += "O.OOO."

            elif (char.lower() == 's'):

                output += ".OO.O."

            elif (char.lower() == 't'):

                output += ".OOOO."

            elif (char.lower() == 'u'):

                output += "O...OO"

            elif (char.lower() == 'v'):

                output += "O.O.OO"

            elif (char.lower() == 'w'):

                output += '.OOO.O'

            elif (char.lower() == 'x'):

                output += 'OO..OO'

            elif (char.lower() == 'y'):

                output += "OO.OOO"

            elif (char.lower() == 'z'):

                output += "O..OOO"
        
        # If we are working with numbers
        else:

            # Start checking the letters
            if (char == '1'):
                
                output += "O....."

            elif (char == '2'):

                output += "O.O..."

            elif (char == '3'):
                
                output += "OO...."

            elif (char == '4'):

                output += "OO.O.."

            elif (char == '5'):

                output += "O..O.."

            elif (char == '6'):

                output += "OOO..."

            elif (char == '7'):

                output += "OOOO.."

            elif (char == '8'):
                
                output += "O.OO.."

            elif (char == '9'):

                output += ".OO..."

            elif (char == '0'):

                output += ".OOO.."

# If we're translating from Braille to English
else:
    
    isCaptial = False
    isNum = False

    currentCharNum = 0
    
    for i in range(int(len(input) / 2)):

        substring = input[currentCharNum:currentCharNum+6]

        # If we reach 'number follows'
        if (substring == ".O.OOO"):

            # Set that flag to True
            isNum = True
        
        # If we reach the 'capital follows'
        elif (substring == ".....O"):

            # Set that flag to True
            isCaptial = True
        
        # If we have a space
        elif (substring == "......"):

            # If we've been dealing with numbers
            if (isNum):

                # Set the flag back to False
                isNum = False

            # Add a space
            output += " "
        
        # If we have a period/decimal
        elif (substring == '.O...O'):
            
            # Add a period/decimal
            output += "."
                
        # If we are working with letters
        if (not isNum):
            
            # Start checking the letters
            if (substring == "O....."):
                
                if isCaptial:

                    output += "A"
                    isCaptial = False
                
                else:

                    output += "a"

            elif (substring == "O.O..."):

                if isCaptial:

                    output += "B"
                    isCaptial = False

                else:
                    
                    output += "b"
            
            elif (substring == "OO...."):

                if isCaptial:

                    output += "C"
                    isCaptial = False
                
                else:
                    
                    output += "c"

            elif (substring == "OO.O.."):

                if isCaptial:

                    output += "D"
                    isCaptial = False

                else:
                    
                    output += "d"

            elif (substring == "O..O.."):

                if isCaptial:

                    output += "E"
                    isCaptial = False

                else:
                    
                    output += "e"

            elif (substring == "OOO..."):

                if isCaptial:

                    output += "F"
                    isCaptial = False

                else:
                    
                    output += "f"

            elif (substring == "OOOO.."):

                if isCaptial:

                    output += "G"
                    isCaptial = False

                else:
                    
                    output += "g"

            elif (substring == "O.OO.."):

                if isCaptial:

                    output += "H"
                    isCaptial = False

                else:
                    
                    output += "h"

            elif (substring == ".OO..."):

                if isCaptial:

                    output += "I"
                    isCaptial = False

                else:
                    
                    output += "i"

            elif (substring == ".OOO.."):

                if isCaptial:

                    output += "J"
                    isCaptial = False

                else:
                    
                    output += "j"

            elif (substring == "O...O."):

                if isCaptial:

                    output += "K"
                    isCaptial = False

                else:
                    
                    output += "k"

            elif (substring == "O.O.O."):

                if isCaptial:

                    output += "L"
                    isCaptial = False

                else:
                    
                    output += "l"

            elif (substring == "OO..O."):

                if isCaptial:

                    output += "M"
                    isCaptial = False

                else:
                    
                    output += "m"

            elif (substring == "OO.OO."):

                if isCaptial:

                    output += "N"
                    isCaptial = False

                else:
                    
                    output += "n"

            elif (substring == "O..OO."):

                if isCaptial:

                    output += "O"
                    isCaptial = False

                else:
                    
                    output += "o"

            elif (substring == "OOO.O."):

                if isCaptial:

                    output += "P"
                    isCaptial = False

                else:
                    
                    output += "p"

            elif (substring == "OOOOO."):

                if isCaptial:

                    output += "Q"
                    isCaptial = False

                else:
                    
                    output += "q"

            elif (substring == "O.OOO."):

                if isCaptial:

                    output += "R"
                    isCaptial = False

                else:
                    
                    output += "r"

            elif (substring == ".OO.O."):

                if isCaptial:

                    output += "S"
                    isCaptial = False

                else:
                    
                    output += "s"

            elif (substring == ".OOOO."):

                if isCaptial:

                    output += "T"
                    isCaptial = False

                else:
                    
                    output += "t"

            elif (substring == "O...OO"):

                if isCaptial:

                    output += "U"
                    isCaptial = False

                else:
                    
                    output += "u"

            elif (substring == "O.O.OO"):

                if isCaptial:

                    output += "V"
                    isCaptial = False

                else:
                    
                    output += "v"

            elif (substring == ".OOO.O"):

                if isCaptial:

                    output += "W"
                    isCaptial = False

                else:
                    
                    output += "w"

            elif (substring == "OO..OO"):

                if isCaptial:

                    output += "X"
                    isCaptial = False

                else:
                    
                    output += "x"

            elif (substring == "OO.OOO"):

                if isCaptial:

                    output += "Y"
                    isCaptial = False

                else:
                    
                    output += "y"

            elif (substring == "O..OOO"):

                if isCaptial:

                    output += "Z"
                    isCaptial = False

                else:
                    
                    output += "z"
            

            # If we have a comma
            elif (substring == "..O..."):

                output += ","
            
            # If we have a question mark
            elif (substring == "..O.OO"):

                output += "?"

            # If we have an exclamation mark
            elif (substring == "..OOO."):

                output += "!"

            # If we have a colon
            elif (substring == "..OO.."):

                output += ":"

            # If we have a semicolon
            elif (substring == "..O.O."):

                output += ";"

            # If we have a dash
            elif (substring == "....OO"):

                output += "-"
            
            # If we have a forward slash
            elif (substring == ".O..O."):

                output += "/"

            # If we have a greater than/less than
            elif (substring == ".OO..O"):

                output += "<"

            elif (substring == "O..OO."):

                output += ">"

            # If we have a round bracket
            elif (substring == "O.O..O"):

                output += "("

            elif (substring == ".O.OO."):

                output += ")"

        # If we are working with numbers
        else:

            if (substring == "O....."):
            
                output += "1"

            elif (substring == "O.O..."):
                    
                output += "2"
            
            elif (substring == "OO...."):
                    
                output += "3"

            elif (substring == "OO.O.."):
                    
                output += "4"

            elif (substring == "O..O.."):
                    
                output += "5"

            elif (substring == "OOO..."):
                    
                output += "6"

            elif (substring == "OOOO.."):
                    
                output += "7"

            elif (substring == "O.OO.."):
                    
                output += "8"

            elif (substring == ".OO..."):
                    
                output += "9"

            elif (substring == ".OOO.."):
                    
                output += "0"
            

        currentCharNum += 6


print(output)