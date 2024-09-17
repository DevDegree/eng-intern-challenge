import sys

class DicoTranslator:
# 
# Each digit has the same first 4 Braille dots as its corresponding letter
# This pattern was used to map the 4 Braille dots combination to the correct letter and add the appropriate last 2 Braille dots using ASCII values, 
#   accounting for differences of 48, 58, or 68
# Example: a -> ASCII diff 48 -> 1 -> "O..." + ".." | b -> ASCII diff 48 -> 2 -> "O.O." + ".."  ... | i -> ASCII diff 48 -> 9 -> ".OO." + ".."
#          k -> ASCII diff 58 -> 1 -> "O..." + "O." | l -> ASCII diff 58 -> 2 -> "O.O." + "O."  ... | s -> ASCII diff 58-> 9 -> ".OO." + "O."
#           ...
# Note: Letters after 'w' do not follow this pattern because 'w' has no corresponding digit in Braille.
# Note: For the digit '0', 10 is added to the ASCII value so the first 4 Braille dots and 2 ending dots matches the correct letter.
#          ...
    ACTION = {".....O" : "MAJ", ".O.OOO" : "NUM"}
    ACTION_TO_BRAILLE = {"MAJ" : ".....O", "NUM" : ".O.OOO"}

    SPECIAL = {"......" : " ", ".OOO.O" : "w", "OO..OO" : "x",
                              "OO.OOO" : "y", "O..OOO" : "z" }
    SPECIAL_TO_BRAILLE = {" " : "......","w" : ".OOO.O", "x" : "OO..OO",
                                       "y" : "OO.OOO", "z" : "O..OOO" }
    
    DIGIT = {"O..." : "1", "O.O." : "2", "OO.." : "3", "OO.O" : "4",
                        "O..O" : "5", "OOO." : "6", "OOOO" : "7", "O.OO" : "8",
                          ".OO." : "9", ".OOO" : "0"}  
    DIGIT_TO_BRAILLE = {"1" : "O...", "2" : "O.O.", "3" : "OO..", "4" : "OO.O",
                        "5" : "O..O", "6" : "OOO.", "7" : "OOOO", "8" : "O.OO",
                          "9" : ".OO.", "0" : ".OOO"}
    
    ASCII_DECRYPTION = {".." : 48, "O." : 58, "OO" : 68}

    def isBraille(input : list):
        if len(input) <= 0: raise ValueError ("Invalid input")

#       Checks if the input is a single word, whose number of digits is a multiple of 6
        elif len(input) != 1 or len(input[0]) % 6 != 0:
            return False

#       Checks if there are digits that differs from "O" and "."
        for char in input[0]:
            if char != "." and char != "O":
                return False

        return True


    def toBraille(englishInput):
        brailleOutput = ""

#       Tracks whether the character is a numerical
        isNumber = False

        for word in englishInput:
            for char in word:
                if char.isdigit():
#                   Adds the Braille character indicating the following sequence is numeric
                    if not isNumber:
                        isNumber = True
                        brailleOutput += DicoTranslator.ACTION_TO_BRAILLE["NUM"]

#                   Completes the braille character, since the last two dots are common to all Braille digits
                    brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[char] + ".."
                
                else:
                
                    if not char.isalpha() and char != " ": raise ValueError("Character not handled")
                    
                    if char.isupper(): brailleOutput += DicoTranslator.ACTION_TO_BRAILLE["MAJ"]

                    if char.lower() in DicoTranslator.SPECIAL_TO_BRAILLE :

#                       It is not possible to combine letters and digits            
                        if char != " " and isNumber : raise ValueError("Invalid sequence")
                        
                        brailleOutput += DicoTranslator.SPECIAL_TO_BRAILLE[char.lower()]
                        isNumber = False

#                   Uses the ASCII value to determine the first 4 dots of the Braille character from the corresponding digit, 
#                       then appends the appropriate ending dots based on the ASCII value
                    else:
#                       It is not possible to combine letters and digits    
                        if isNumber : raise ValueError("Invalid sequence")

                        asciiValue = ord(char.lower())

                        if asciiValue >= 116: 
                            brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[chr(asciiValue - 68)] + "OO"

                        elif asciiValue >= 106: 
                            brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[chr(asciiValue - 58)] + "O."
              
                        else: 
                            brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[chr(asciiValue - 48)] + ".."

#           Adds a space between each word in the sentence
            brailleOutput += DicoTranslator.SPECIAL_TO_BRAILLE[" "]
            isNumber = False
        
        return brailleOutput[:-6]
    
    
    def toEnglish(brailleInput):

        englishOutput = ""
        sequenceState = ""

        for char in brailleInput:
            if sequenceState == "NUM":
#               The sequence is already numeric
                if char in DicoTranslator.ACTION and DicoTranslator.ACTION[char] == "NUM": raise ValueError("Invalid sequence")
                
                elif char in DicoTranslator.SPECIAL :
#                   It is not possible to combine letters and digits                    
                    if DicoTranslator.SPECIAL[char] != " " : raise ValueError("Invalid sequence")

                    englishOutput += DicoTranslator.SPECIAL[char]
#                   The sequence is no longer numeric
                    sequenceState = ""

                else:
#                    It is not possible to combine letters and digits    
                    if char[4:] != ".." : raise ValueError("Invalid sequence")

                    englishOutput += DicoTranslator.DIGIT[char[:4]]

            elif sequenceState == "MAJ":
#               The character is non-alphanumeric, which is invalid
                if char in DicoTranslator.ACTION: raise ValueError("Invalid sequence")
                
                elif char in DicoTranslator.SPECIAL:
                    charInEnglish = DicoTranslator.SPECIAL[char]

#                   The character is non-alphanumeric, which is invalid
                    if charInEnglish == " ": raise ValueError("Invalid sequence")
                    
                    englishOutput += DicoTranslator.SPECIAL[char]

                else:
#                   The character is not handled
                    if char[:4] not in DicoTranslator.DIGIT : raise ValueError("Invalid sequence")
                   
#                   The corresponding digit is 0, which is a special case; adds 10 to the ASCII value and converts it to uppercase
                    elif DicoTranslator.DIGIT[char[:4]] == "0":
                        englishOutput += chr( ord(DicoTranslator.DIGIT[char[:4]]) + DicoTranslator.ASCII_DECRYPTION[char[4:]] + 10 ).upper()

#                   Decrypts the character to get the first 4 dots, appends the corresponding ending dots, and converts to uppercase
                    else :  
                        englishOutput += chr( ord(DicoTranslator.DIGIT[char[:4]]) + DicoTranslator.ASCII_DECRYPTION[char[4:]] ).upper()

#               The sequence is no longer maj                    
                sequenceState = ""

            else:
                if char in DicoTranslator.ACTION:
                    sequenceState = DicoTranslator.ACTION[char]
                
                elif char in DicoTranslator.SPECIAL:
                    englishOutput += DicoTranslator.SPECIAL[char]
                
                else:
#                   The character is not handled
                    if char[:4] not in DicoTranslator.DIGIT : 
                        raise ValueError("Invalid sequence")

#                   The corresponding digit is 0, which is a special case; adds 10 to the ASCII
                    elif DicoTranslator.DIGIT[char[:4]] == "0":
                        englishOutput += chr(ord(DicoTranslator.DIGIT[char[:4]]) + DicoTranslator.ASCII_DECRYPTION[char[4:]] + 10)
            
#                   Decrypts the character to get the first 4 dots, appends the corresponding ending dots
                    else :  
                        englishOutput += chr(ord(DicoTranslator.DIGIT[char[:4]]) + DicoTranslator.ASCII_DECRYPTION[char[4:]] )
        return englishOutput


def translate(input):
    try:
        if DicoTranslator.isBraille(input):
            brailleInput = [input[0][i:6+i] for i in range(0, len(input[0]), 6)]
            try:
                return DicoTranslator.toEnglish(brailleInput)
            except ValueError:
                print("Invalid input, please follow the rules for Braille.")

        else:
            try:
                return DicoTranslator.toBraille(input)
            except ValueError:
                print("Invalid input, please follow the rules for Braille.")
            
    except ValueError:
        print("There is no input")


if __name__ == '__main__':
    translatedString = translate(sys.argv[1:])

    print(translatedString)
