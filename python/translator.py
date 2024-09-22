# Create a dicitonary for english to braille
englishToBrailleDictionary = {
    # Letters
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..", "f" : "OOO...", 
    "g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...", "j" : ".OOO..", "k" : "O...O.", "l" : "O.O.O.", 
    "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.", "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.", 
    "s" : ".OO.O.", "t" : ".OOOO.", "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
    "y" : "OO.OOO", "z" : "O..OOO",
    # Special characters
    "." : "..OO.O", "," : "..O...", "?" : "..O.OO", "!" : "..OOO.", ":" : "..OO..", ";" : "..O.O.",
    "-" : "....OO", "/" : ".O..O.", "<" : ".OO..O", ">" : "O..OO.", "(" : "O.O..O", ")" : ".O.OO.",
    " " : "......",
    # Speical meaning
    "capital follows" : ".....O", 
    "decimal follows" : ".O...O", 
    "number follows" : ".O.OOO"
}




# Create a dictionary for numbers to braille 
numbersToBrailleDictionary = {
    # Numbers
    "1" : englishToBrailleDictionary["a"], "2" : englishToBrailleDictionary["b"], "3" : englishToBrailleDictionary["c"], "4" : englishToBrailleDictionary["d"], "5" : englishToBrailleDictionary["e"],
    "6" : englishToBrailleDictionary["f"], "7" : englishToBrailleDictionary["g"], "8" : englishToBrailleDictionary["h"], "9" : englishToBrailleDictionary["i"], "0" : englishToBrailleDictionary["j"]
}




# Create a dictionary for braille to english
brailleToEnglishDictionary = {val: key for key, val in englishToBrailleDictionary.items()}




# Create a dictionary for braille to numbers
brailleToNumbersDictionary = {val: key for key, val in numbersToBrailleDictionary.items()}




# Function that determines if the given string should be translated to English or Braille
def englishOrBraille(inputString) :
    return all(characters in ".O" for characters in inputString)




# Function to translate from Braille -> English
def brailleToEnglish(inputString):
    # Define variables
    output = []
    isCapital = False
    isNumber = False

    # Iterate through the inputString and add to the output as needed
    for i in range(0, len(inputString), 6):
        brailleChar = inputString[i:i+6]

        # Check for capital follows
        if brailleChar == englishToBrailleDictionary["capital follows"]:
            isCapital = True
            continue
        # Check for number follows
        elif brailleChar == englishToBrailleDictionary["number follows"]:
            isNumber = True
            continue
        # Check for spaces
        elif brailleChar == englishToBrailleDictionary[" "]:
            output.append(brailleToEnglishDictionary.get(brailleChar, ""))
            isCapital = False
            isNumber = False
            continue

        # Handles Braille -> Number
        if isNumber:
            # Use brailleToNumbersDictionary
            output.append(brailleToNumbersDictionary.get(brailleChar,""))
        # Handles Braille -> English
        else:
            # Use BrailleToEnglishDictionary
            englishChar = brailleToEnglishDictionary.get(brailleChar, "")

            # Handles capital follows
            if isCapital:
                englishChar = englishChar.upper()
                isCapital = False
            
            # Base case
            output.append(englishChar)
        
    # Returns a string of the output
    return ''.join(output)
            



# Function to translate from English -> Braille
def englishToBraille(inputString):
    # Define variables
    output = []
    isNumber = False
    
    # Iterate through the inputString and add to the output as needed
    for i in range (0, len(inputString), 1):
        englishChar = inputString[i]

        # Handles capital follows
        if englishChar.isupper():
            output.append(englishToBrailleDictionary["capital follows"])
            englishChar = englishChar.lower()
            output.append(englishToBrailleDictionary.get(englishChar))
        # Handles number follows
        elif englishChar.isdigit():
            if not isNumber:
                output.append(englishToBrailleDictionary["number follows"])
                isNumber = True
            output.append(numbersToBrailleDictionary[englishChar])
        # Handles spaces
        elif englishChar == " ":
            output.append(englishToBrailleDictionary[" "])
            isNumber = False
        # Handles base case
        else:
            output.append(englishToBrailleDictionary.get(englishChar, ""))
            isNumber = False

    # Returns a string of the output
    return ''.join(output)




# Translation implementation
def translation(inputString):
    # Convert Brailled -> English
    if englishOrBraille(inputString):
        return brailleToEnglish(inputString)
    # Convert English -> Braille
    else:
        return englishToBraille(inputString)
    



# Main
def main():
    import sys
    cmd_line_args = sys.argv[1:]

    inputString = ' '.join(cmd_line_args)

    result = translation(inputString)

    print(result)


if __name__ == "__main__":
    main()