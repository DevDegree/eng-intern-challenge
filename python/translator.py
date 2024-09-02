import sys

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"

ALPHANUM_BRAILE = {
    "a": "O.....", "b": "O.O...", "c": "OO....",
    "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...",
    "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO"
}

ALPHANUM_BRAILE.update( { letter.upper(): CAPITAL_FOLLOWS+braille  
                     for letter, braille in ALPHANUM_BRAILE.items() })

ALPHANUM_BRAILE.update({
    "1": "O.....", "2": "O.O...", "3": "OO....", 
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
    "0": ".OOO..",
})

PUNCTUATION_BRAILE = {
    ".": "OO..O.", ",": "OO.OOO", "?": "OO.O..",
    "!": "OO...O", ":": "OO..OO", ";": "OO.O.O",
    "-": "OOOO..", "/": "O.OO.O", "<": "O..OO.",
    ">": ".OO..O", "(": ".O.OO.", ")": "O.O..O",
    " ": "......"   
}

BRAILLE_ALPHA = dict(reversed(item) for item in ALPHANUM_BRAILE.items() if item[0].isalpha())
BRAILLE_NUM = dict(reversed(item) for item in ALPHANUM_BRAILE.items() if item[0].isdigit())
BRAILE_PUNCTUATION = dict(reversed(item) for item in PUNCTUATION_BRAILE.items())


def english_to_braille(english_input: str) -> str:  
    
    # Convert the input to a list for easier manipulation  
    english_input = list(english_input)
    
    # Replace punctuation characters with their Braille representations
    english_input = [PUNCTUATION_BRAILE.get(char, char) for char in english_input]
    
    # Insert the Braille representation for number follows where necessary
    i = 0
    while i < len(english_input):
        if english_input[i].isnumeric():
            if i == 0 or not english_input[i-1].isnumeric():
                english_input.insert(i, NUMBER_FOLLOWS)
                i += 1
        i += 1
          
    # Replace alphanumeric characters wiht their Braille representations   
    braille_output = "".join([ALPHANUM_BRAILE.get(char, char) for char in english_input])
    
    return braille_output

def braille_to_english(braille_input: str) -> str:
    
    # Split the Braille input into individual Braille characters
    braille_input = [braille_input[i : i + 6] for i in range(0, len(braille_input), 6)]
    
    # Initialize an empty list to store the English output
    english_output = []
    
    # Initialize flags to track whether the previous character was a number or uppercase
    number = False
    upper = False
    
    # Iterate over each Braille character
    for i, braille_char in enumerate(braille_input):
       
        # If the Braille character represents a number follows, set the number flag
        if braille_char == NUMBER_FOLLOWS:
            number = True
            continue
        
        # If the number flag is true and the current braille is a number append it
        elif number and braille_char in BRAILLE_NUM:
            english_output.append(BRAILLE_NUM[braille_char])
        
        # If the Braille character represents a space, reset the number flag
        elif braille_char == "......":
            number = False
            english_output.append(" ")
        
        # If the Braille character represents an uppercase letter, 
        # set the upper flag to true
        elif braille_char.startswith(CAPITAL_FOLLOWS):
            upper = True
        
        # If the previous character was CAPITAL_FOLLOWS, 
        # convert the Braille character to uppercase
        elif upper:
            english_output.append(BRAILLE_ALPHA.get(braille_char, braille_char).upper())
            upper = False
        
        # Otherwise, convert the Braille character to its corresponding English character
        elif not upper:
            english_output.append(BRAILLE_ALPHA.get(braille_char, braille_char))
        
        # If the Braille character represents a punctuation mark, convert it to its corresponding English punctuation
        elif braille_char in BRAILE_PUNCTUATION:
            english_output.append(BRAILE_PUNCTUATION[braille_char])
    
    # Join the English output into a single string
    return ''.join(english_output)


def main() -> None:
    inputStr = " ".join(sys.argv[1:])
    if all(len(inputStr[i:i+6]) == 6 and inputStr[i:i+6] in BRAILLE_ALPHA.values() for i in range(0, len(inputStr), 6)):
        outputStr = braille_to_english(inputStr)
    else:
        outputStr = english_to_braille(inputStr)
    sys.stdout.write(outputStr)

main()