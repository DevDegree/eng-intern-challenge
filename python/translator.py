import sys

 #Creating English to Braille mapping 
englishToBraille = {
        # Letters
        "a": ["O", ".", 
                ".", ".", 
                ".", "."],

        "b": ["O", ".", 
                "O", ".", 
                ".", "."],

        "c": ["O", "O", 
                ".", ".", 
                ".", "."],

        "d": ["O", "O", 
                ".", "O", 
                ".", "."],

        "e": ["O", ".", 
                ".", "O", 
                ".", "."],

        "f": ["O", "O", 
                "O", ".", 
                ".", "."],

        "g": ["O", "O", 
                "O", "O", 
                ".", "."],

        "h": ["O", ".", 
                "O", "O", 
                ".", "."],

        "i": [".", "O", 
                "O", ".", 
                ".", "."],

        "j": [".", "O", 
                "O", "O", 
                ".", "."],

        "k": ["O", ".", 
                ".", ".", 
                "O", "."],

        "l": ["O", ".", 
                "O", ".", 
                "O", "."],

        "m": ["O", "O", 
                ".", ".", 
                "O", "."],

        "n": ["O", "O", 
                ".", "O", 
                "O", "."],

        "o": ["O", ".", 
                ".", "O", 
                "O", "."],

        "p": ["O", "O", 
                "O", ".", 
                "O", "."],

        "q": ["O", "O", 
                "O", "O", 
                "O", "."],

        "r": ["O", ".", 
                "O", "O", 
                "O", "."],

        "s": [".", "O", 
                "O", ".", 
                "O", "."],

        "t": [".", "O", 
                "O", "O", 
                "O", "."],

        "u": ["O", ".", 
                ".", ".", 
                "O", "O"],

        "v": ["O", ".", 
                "O", ".", 
                "O", "O"],

        "w": [".", "O", 
                "O", "O", 
                ".", "O"],

        "x": ["O", "O", 
                ".", ".", 
                "O", "O"],

        "y": ["O", "O", 
                ".", "O", 
                "O", "O"],

        "z": ["O", ".", 
                ".", "O", 
                "O", "O"],

        # Numbers
        "0": [".", "O", 
                "O", "O", 
                ".", "."],

        "1": ["O", ".", 
                ".", ".", 
                ".", "."],

        "2": ["O", ".", 
                "O", ".", 
                ".", "."],

        "3": ["O", "O", 
                ".", ".", 
                ".", "."],

        "4": ["O", "O", 
                ".", "O", 
                ".", "."],

        "5": ["O", ".", 
                ".", "O", 
                ".", "."],

        "6": ["O", "O", 
                "O", ".", 
                ".", "."],

        "7": ["O", "O", 
                "O", "O", 
                ".", "."],

        "8": ["O", ".", 
                "O", "O", 
                ".", "."],

        "9": [".", "O", 
                "O", "O", 
                ".", "."],

        #Commands (e.g. Capital Follows)
        "capital": [".", ".", 
                    ".", ".", 
                    ".", "O"],

        "decimal": [".", "O", 
                    ".", ".", 
                    ".", "O"],

        "number": [".", "O", 
                    ".", "O", 
                    "O", "O"],

        #Symbols
        ".": [".", ".", 
              "O", "O", 
              ".", "O"],

        ",": [".", ".", 
              "O", ".", 
              "", "."],

        "?": [".", ".", 
              "O", ".", 
              "O", "O"],   

        "!": [".", ".", 
              "O", "O", 
              "O", "."],           

        ":": [".", ".", 
              "O", "O", 
              ".", "."],           

        ";": [".", ".", 
              "O", ".", 
              "O", "."],           

        "-": [".", ".", 
              ".", ".", 
              "O", "O"],

        "/": [".", "O", 
              ".", ".", 
              "O", "."],                      

        "<": [".", "O", 
              "O", ".", 
              ".", "O"],

        ">": ["O", ".", 
              ".", "O", 
              "O", "."],                      

        "(": ["O", ".", 
              "O", ".", 
              ".", "O"],           

        ")": [".", "O", 
              ".", "O", 
              "O", "."],           

        #space
        " ": [".", ".", 
              ".", ".", 
              ".", "."],           
   }

    #This allows us to correctly convert Braille -> numbers (i.e. '1' instead of 'a')

# Mapping from letters (a to j) to (1 to 9)
letterToNumber = { 
        #Numbers
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "0",
   }

def input_in_english(word):
    """
     Helper method to determine if input arg is in English
    """
     #Step 1: Determine if input is braille or english 
    for character in word: 
        #Checking if input has anything other than "." or "O"
        if ord(character) != 79 and ord(character) != 46:
            return True
    return False
    

def translator(word):
    """
    Function to translate between English and Braille.
    Returns translated string based on input. 
    """
    #Flag to determine if value is capital 
    isCapital = False
    #Flag to determine if value is number
    isNumber = False 
    #Variable that stores translation
    translation = []

    #Step 1: Determine if input is in English
    isEnglish = input_in_english(word)

    #Step 2: Translating input based on language
    if isEnglish:
        #Translate to Braille
        for letter in range(0, len(word)): 
            #Case 1: Number follows
            if 49 <= ord(word[letter]) <= 57: 
                # Checking if previous value was a number   
                if not isNumber:
                        translation.append(englishToBraille["number"])
                        isNumber=True
                translation.append(englishToBraille[word[letter]])

            #Case 2: Decimal follows
            elif word[letter - 1].isdigit() and word[letter + 1].isdigit():
                translation.append(englishToBraille["decimal"])
                translation.append(englishToBraille[word[letter]])
            
            #Case 3: Character is letter and uppercase follows
            elif 65 <= ord(word[letter]) <= 90 and (word[letter] == word[letter].upper()):
                translation.append(englishToBraille["capital"])
                translation.append(englishToBraille[word[letter].lower()])
                isNumber=False

            #Base case: Regular letter or symbol 
            else:
                translation.append(englishToBraille[word[letter]])
                isNumber=False

    else:
        #Translate to English
        for symbol in range(0, len(word), 6): 
            #Storing chunk of 6 symbols
            braille_symbol = list(word[symbol:symbol+6])

            #Special Case 1: braille_symbol is capital
            if braille_symbol == englishToBraille["capital"]:
                isCapital = True
                isNumber = False 
                continue

            #Special Case 2: braille_symbol is number
            if braille_symbol == englishToBraille["number"]:
                isNumber = True
                continue

            #Special Case 1: braille_symbol is decimal
            if braille_symbol == englishToBraille["decimal"]:
                translation += "."
                isNumber = False
                continue

            #Finding key associated to this value
            for key, value in englishToBraille.items():
                if value == braille_symbol:
                    #Symbol is number
                    if isNumber:
                        translation += letterToNumber[key]
                    #Symbol is capitalized
                    elif isCapital:
                        translation += key.upper()
                        isCapital = False
                    #Regular case
                    else:
                        translation+=key
                    break
                    

    # Format translation as string 
    formattedTranslation = ''.join(["".join(symbol) for symbol in translation])
    return formattedTranslation
    

# Command line functionnality
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # List to store the results
        results = []
        #Loop through each input argument
        for word in sys.argv[1:]:  
            # Store the translation in the list
            results.append(translator(word))
            # Store input language
            inEnglish = input_in_english(word)
        
        #Join all the results together based on language
        if inEnglish:
                print("......".join(results))
        else:
            print(" ".join(results))

    else:
        print("Please input words.")

