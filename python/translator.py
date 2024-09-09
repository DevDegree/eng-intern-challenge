class BrailEngTranslator:
    def __init__(self): 

        # Braille letters for a-z, where each string represents the 6-dot Braille pattern    
        self.brailleLetters = [
            "O.....", "O.O...", "OO....", "OO.O..", "O..O..", 
            "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", 
            "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", 
            "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", 
            "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", 
            "O..OOO"
        ]

        # Braille pattern indicates a capital follows
        self.capitalFollows = ".....O"

        # Braille pattern indicates numbers follow
        self.numberFollows = ".O.OOO"

    # Creates a dictionary that maps each english letter (a-z)
    # and each number (0-9) to its corresponding Braille pattern.
    def dictionaryBraille(self):

        # Map letters a-z to Braille patterns
        englishLetters = {}
        for i in range(26):
            englishLetters[chr(97+i)] = self.brailleLetters[i]

        # Map numbers 0-9 to Braille patterns
        numbers = {str(i): self.brailleLetters[i-1] for i in range(1,10)}
        numbers ["0"] = self.brailleLetters[9]

        return englishLetters, numbers
    
    # Similar to function above except it maps Braille patterns
    # to english letters and numbers
    def dictionaryEnglish(self):

        brailleLetters = {}
        for i in range(26):
            brailleLetters[self.brailleLetters[i]] = chr(97+i)

        brailleNumbers = {self.brailleLetters[i-1]: str(i) for i in range(1,10)}
        brailleNumbers[".OOO.."] = "0"

        return brailleLetters, brailleNumbers

    # Translates a string of Brailles in english letters and numbers
    def brail_to_eng(self, input):

        # Split the input in groups of 6 characters
        brailleChars = [input[i:i+6] for i in range(0, len(input), 6) ]
        englishBraille, numbersBraille = self.dictionaryEnglish()
        engResult = ""
        capitalize = False
        is_numbers = False

        # Convert each Braille character into a letter or a number.
        for brailleChar in brailleChars:
            if brailleChar == self.numberFollows: # Detects if the Braille that indicates  
                is_numbers = True                 # numbers is present.
                continue

            elif brailleChar == self.capitalFollows:
                capitalize = True
                continue

            elif brailleChar == "......": # Detects if there's a space.
                engResult += " "          # If there is, number mode is off.
                is_numbers = False

            elif is_numbers:
                engResult += numbersBraille[brailleChar]

            else:
                char = englishBraille[brailleChar]
                if capitalize:
                    engResult += char.upper() # Capitalizes the letter if capitalize
                    capitalize = False        # is true.
                else:
                    engResult += char

        return engResult            

    # Translates a string of english letters and numbers into Braille.
    def eng_to_brail(self, input):

        # Split the string into individual characters including whitespace
        englishChars = [char for char in input]
        brailleResult = ""
        englishBraille, numbersBraille = self.dictionaryBraille()
        is_numbers = False

        # Convert each character into Braille character
        for char in englishChars:
            if char.isnumeric(): # If the character is a number
               if is_numbers:    # If it's already in number mode, only add the Braille for the number
                   brailleResult += numbersBraille[char]
               else:             # Else, add the Braille that indicates numbers follow
                   brailleResult += self.numberFollows + numbersBraille[char]
                   is_numbers = True
               
            elif char == " ":
               brailleResult += "......"
               is_numbers = False

            elif char.isupper():
                brailleResult += self.capitalFollows + englishBraille[char.lower()]
            else:
               brailleResult += englishBraille[char]
        
        return brailleResult

    # Detects if the given string should be translated to english or braille
    def input_type(self, input):
        if "O" in input and "." in input:
            return "braille"
        else:
            return "english"
        
if __name__ == "__main__":
    import sys
    input_text = " ". join(sys.argv[1:])
    translator = BrailEngTranslator()
    if translator.input_type(input_text) == "braille":
        result = str(translator.brail_to_eng(input_text))
        print(result)
    else:
        result = str(translator.eng_to_brail(input_text))
        print(result)

