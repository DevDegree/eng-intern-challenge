import sys

# Dictionary mapping letters, numbers, and punctuation to Braille patterns
brailleDict = {
    "A": "O.....", "B": "O.O...", "C": "OO....", "D": "OO.O..", "E": "O..O..", 
    "F": "OOO...", "G": "OOOO..", "H": "O.OO..", "I": ".OO...", "J": ".OOO..", 
    "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.", "O": "O..OO.", 
    "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.", 
    "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO", 
    "Z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
    "0": ".OOO..", ".": ".O...O", " ": "......",  # Space
    ",": "..O...", "?": "..O.OO", "!": "..OO.O", "'": "....O.", ":": "O..OOO", 
    ";": "O..OO.", "-": "....OO", "capital": ".....O", "number": ".O.OOO"  # Indicators
}

# Dictionary mapping numbers to Braille patterns
numMap = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", 
    ".": ".O...O"
}

def translate(text):
    """
    Translate between English text and Braille. Detects if the input is Braille or English
    and translates accordingly.
    """
    result = ""
    index = 0
    is_braille = all(char in {'O', '.'} for char in text)  # Check if input is Braille

    # Translate from English to Braille
    if not is_braille:
        while index < len(text):
            char = text[index]
            
            if char.isupper():  # Handle capital letters
                result += brailleDict["capital"] + brailleDict[char]
            elif char.isdigit():  # Handle digits
                if index == 0 or not text[index - 1].isdigit():
                    result += brailleDict["number"]
                result += brailleDict[char]
            elif char == " ":  # Handle space
                result += brailleDict[" "]
            elif char in brailleDict:  # Handle punctuation and letters
                result += brailleDict[char.upper()]
            index += 1

    # Translate from Braille to English
    else:
        while index < len(text):
            braille_char = text[index:index + 6]
            index += 6

            if braille_char == "......":  # Handle space
                result += ' '
            elif braille_char == ".....O":  # Capital letter indicator
                braille_char = text[index:index + 6]
                index += 6
                result += next((letter.upper() for letter, braille in brailleDict.items() if braille == braille_char), '')
            elif braille_char == ".O.OOO":  # Number indicator
                braille_char = text[index:index + 6]
                index += 6
                result += next((num for num, braille in numMap.items() if braille == braille_char), '')
            else:
                # Match regular Braille to English letter or number
                result += next((letter.lower() for letter, braille in brailleDict.items() if braille == braille_char), '')

    return result

if __name__ == "__main__":
    # Check if input is provided, else show a prompt
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    output_text = translate(input_text)
    print(output_text)

