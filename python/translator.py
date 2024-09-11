import sys

# Braille to English dictionary
braille_to_english = {
'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

# English to Braille dictionary
english_to_braille = {value: key for key, value in braille_to_english.items()}

# Braille to Number dictionary
braille_to_number = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8",
    ".OO...": "9", "O..OO.": "0"
}

# Number to Braille dictionary
number_to_braille = {value: key for key, value in braille_to_number.items()}


# Here I'm assuming that Alphabet and Numbers are always separated by a space
# depending on this technical requirment given

# When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.

# Function to translate English to Braille
def translate_english_to_braille(english):
    braille_text = ""
    numberOn = False # Flag to check if a number is on

    for char in english:
        if char.isalpha():
            if char.isupper(): # Check if the character is uppercase
                braille_text += ".....O" # Add the capital letter symbol
                char = char.lower()
            braille_text += english_to_braille[char]
        elif char.isdigit(): # Check if the character is a number
            if not numberOn:
                braille_text += ".O.OOO" # Add the number symbol if it is the start of a number
                numberOn = True
            braille_text += number_to_braille[char]
        
        # If the character is a space, turn off the number flag
        elif char == " ": 
            numberOn = False
            braille_text += english_to_braille[char]
    return braille_text


# Function to translate Braille to English
def translate_braille_to_english(braille):
    english = ""
    numberOn = False
    capitalOn = False

    # Loop through the Braille text in steps of 6
    for i in range(0, len(braille), 6): 
        char = braille[i:i+6]
        if char == ".....O": # Turn on the capital flag
            capitalOn = True
        elif char == '.O.OOO': # Turn on the number flag
            numberOn = True
        elif char == '......': # Turn off the number flag
            english += " "
            numberOn = False
        else:
            if numberOn: # If number flag is on, using braille_to_number dictionary
                english += braille_to_number[char]
            elif capitalOn: # If capital flag is on, convert the character to uppercase
                english += braille_to_english[char].upper()
                capitalOn = False
            else:
                english += braille_to_english[char]
    return english
    


def main():
    # Check if the user has entered a language to translate to
    if (len(sys.argv) < 2):
        print("Usage: python translator.py <English or Braille>")
        sys.exit()

    # Get the language to translate to
    result = ''
    text = ' '.join(sys.argv[1:])

    # Check if the text is Enlgish or Braille
    braille = [".", "O"]
    if all(char in braille for char in text):
        result = translate_braille_to_english(text)
    else:
        result = translate_english_to_braille(text)
    print(result)
    
if __name__ == "__main__":
    main()