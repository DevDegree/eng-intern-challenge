brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'capital',
    # Punctuation and symbols
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':',
    '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', #'O..OO.': '>',
    'O.O..O': '(', '.O.OO.': ')', '......': ' ', '.O...O': 'decimal', '.O.OOO': 'number'
}

btoeNums = {    # Numbers
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', 
    '.OO...': '9', '.OOO..': '0',
}

etobNums = {v: k for k, v in btoeNums.items()}

englishToBraille = {v: k for k, v in brailleToEnglish.items()}

def english_to_braille(text):
    braille = ""
    is_number_mode = False

    for i in range(len(text)):
        char = text[i]

        # Handle uppercase letters
        if char.isupper():
            braille += englishToBraille['capital']
            char = char.lower()
            braille += englishToBraille.get(char, "......")

        # Handle numbers
        elif char.isnumeric():
            if not is_number_mode:
                braille += englishToBraille['number']
                is_number_mode = True
            braille += etobNums.get(char, "......")
        
        # Exit number mode on non-numeric characters
        else:
            is_number_mode = False
            # Distinguish between a period and a decimal
            if char == '.':
                if i > 0 and i < len(text) - 1 and text[i-1].isnumeric() and text[i+1].isnumeric():
                    braille += englishToBraille['decimal'] + englishToBraille['.']
                else:
                    braille += englishToBraille.get(char, "......")
            else:
                braille += englishToBraille.get(char, "......")

    return braille

def braille_to_english(text):
    english = ""
    i = 0
    is_number_mode = False

    while i < len(text):
        charB = text[i:i+6]
        
        # Handle capital letters
        if charB == ".....O":
            i += 6
            if i + 6 <= len(text):
                charB = text[i:i+6]
                english += brailleToEnglish.get(charB, "").upper()  
            i += 6
        
        # Handle numbers
        elif charB == ".O.OOO":
            is_number_mode = True
            i += 6
        
        # Handle regular characters or numbers
        else:
            if is_number_mode:
                english += btoeNums.get(charB, "")
            else:
                english += brailleToEnglish.get(charB, "")
            i += 6
            
        # Reset number mode after space
        if charB == "......":
            is_number_mode = False
            english += " "

    return english