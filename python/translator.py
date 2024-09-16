import sys
# We assume that special characters and decimals are not considered, 
# as they are not mentioned in the technical requirements.

class DicoTranslator:
#   ...
#   ...
#   ...
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
#       Checks if the input is a single word, whose number of digits is a multiple of 6.
        elif len(input) != 1 or len(input[0]) % 6 != 0:
            return False
#       Checks if there are digits that differs from O and .
        for char in input[0]:
            if char != "." and char != "O":
                return False

        return True


    def toBraille(englishInput):
        brailleOutput = ""
#       ...
        isNumber = False

        for word in englishInput:
            for char in word:
                if char.isdigit():
#                   ...
                    if not isNumber:
                        isNumber = True

                        brailleOutput += DicoTranslator.ACTION_TO_BRAILLE["NUM"]
#                   ...
                    brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[char] + ".."
                
                else:
                    isNumber = False

                    if not char.isalpha() and char != " ": ValueError("Character not handled")

                    if char.isupper():
                        brailleOutput += DicoTranslator.ACTION_TO_BRAILLE["MAJ"]

                    if char.lower() in DicoTranslator.SPECIAL_TO_BRAILLE:
                        brailleOutput += DicoTranslator.SPECIAL_TO_BRAILLE[char.lower()]
#
                    else:
                        asciiValue = ord(char.lower())
#                       ...
                        if asciiValue >= 116: brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[chr(asciiValue- 68)] + "OO"
#                       ...                      
                        elif asciiValue >= 106: brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[chr(asciiValue - 58)] + "O."
#                       ...                      
                        else: brailleOutput += DicoTranslator.DIGIT_TO_BRAILLE[chr(asciiValue - 48)] + ".."

#           ...
            brailleOutput += DicoTranslator.SPECIAL_TO_BRAILLE[" "]
            isNumber = False
        
        return brailleOutput
    
    
    def toEnglish(brailleInput):

        englishOutput = ""
        sequenceState = ""

        for char in brailleInput:
            if sequenceState == "NUM":
#               ...
                if char in DicoTranslator.ACTION: raise ValueError("Invalid sequence")
                
                elif char in DicoTranslator.SPECIAL:
                    charInEnglish = DicoTranslator.SPECIAL[char]
#                   ...
                    if charInEnglish != " ": raise ValueError("Invalid sequence")

                    else:
                        englishOutput += charInEnglish
#                   ...
                    sequenceState = ""

                else:
                    englishOutput += DicoTranslator.DIGIT[char[:4]]

            elif sequenceState == "MAJ":
#               ...
                if char in DicoTranslator.ACTION: raise ValueError("Invalid sequence")
                
                elif char in DicoTranslator.SPECIAL:
                    charInEnglish = DicoTranslator.SPECIAL[char]
#                   ...
                    if charInEnglish == " ": raise ValueError("Invalid sequence")
                    
                    englishOutput += DicoTranslator.SPECIAL[char]

                else:
#                   ...
                    if char[:4] not in DicoTranslator.DIGIT : raise ValueError("Invalid sequence")
#                   ...
                    elif DicoTranslator.DIGIT[char[:4]] == "0":
                        englishOutput += chr( ord(DicoTranslator.DIGIT[char[:4]]) + DicoTranslator.ASCII_DECRYPTION[char[4:]] + 10 ).upper()
                    
                    else :  
                        englishOutput += chr( ord(DicoTranslator.DIGIT[char[:4]]) + DicoTranslator.ASCII_DECRYPTION[char[4:]] ).upper()
#               ...                    
                sequenceState = ""

            else:
                if char in DicoTranslator.ACTION:
                    sequenceState = DicoTranslator.ACTION[char]
                
                elif char in DicoTranslator.SPECIAL:
                    englishOutput += DicoTranslator.SPECIAL[char]
                
                else:
#                   ...
                    if char[:4] not in DicoTranslator.DIGIT : 
                        raise ValueError("Invalid sequence")
#                   ...
                    elif DicoTranslator.DIGIT[char[:4]] == "0":
                        englishOutput += chr(ord(DicoTranslator.DIGIT[char[:4]]) + DicoTranslator.ASCII_DECRYPTION[char[4:]] + 10)
                    
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
            return DicoTranslator.toBraille(input)
        
    except ValueError:
        print("There is no input")


if __name__ == '__main__':
    translatedString = translate(sys.argv[1:])

    print(translatedString)

#test not passed: mehdi le roi du MonDe 783Mer HEheHEhe Iulk34 34