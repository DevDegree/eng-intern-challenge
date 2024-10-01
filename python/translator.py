import sys
import re

# Store the given input from the command line (cast to string just in case)
#input = str(sys.argv[1])

input = "Hello world"

output = ""

isNum = False;

# If we are translating from Engish to Braille
if re.search('[a-zA-Z0-9]', input):

    # Go through every character
    for char in input:

        # If the character is a space
        if (char == ' '):

            # Set as 'space'
            output += "......"

            # If we have been dealing with numbers thus far
            if (isNum == True):

                # Set the flag back to False
                isNum == False
        
        # If the character is a period
        elif (char == '.'):

            # Check to see if we are dealing with numbers
            if (isNum):

                # Set as 'decimal follows'
                output += ".O...O"
            
            # Set as '.'
            output += "..OO.O"
        
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
        
        
        if (not isNum):

            # If the character we are on is capitalized
            if (char.isupper()):

                # Set as 'capital follows'
                output += ".....O"

            # Start Checking the letters
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
        
        else:

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


print(output)