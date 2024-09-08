import sys
# Eng-intern challenge by Keyshawn James

capital_follows = ".....O"
decimal_follows = ".O...O"
number_follows = ".O.OOO"

# Braille to English dictionary
braille_to_english = {
    #Letters
    "O....." : "a",
    "O.O..." : "b",
    "OO...." : "c",
    "OO.O.." : "d",
    "OOO..." : "f",
    "OOOO.." : "g",
    "O.OO.." : "h",
    ".OO..." : "i",
    ".OOO.." : "j",
    "O...O." : "k",
    "O.O.O." : "l",
    "OO..O." : "m",
    "OO.OO." : "n",
    "O..OO." : "o",
    "OOO.O." : "p",
    "OOOOO." : "q",
    "O.OOO." : "r",
    ".OO.O." : "s",
    ".OOOO." : "t",
    "O...OO" : "u",
    "O.O.OO" : "v",
    ".OOO.O" : "w",
    "OO..OO" : "x",
    "OO.OOO" : "y",
    "O..OOO" : "z",
    
    # Symbols
    "..OO.O" : ".",
    "..O..." : ",",
    "..O.OO" : "?",
    "..OOO." : "!",
    "..OO.." : ":",
    "..O.O." : ";",
    "....OO" : "-",
    ".O..O." : "/",
    ".OO..O" : "<",
    "O..OO." : ">",
    "O.O..O" : "(",
    ".O.OO." : ")",
    "......" : " "
}

# Braille to numbers dictionary
braille_to_numbers = {
    "O....." : "1",
    "O.O..." : "2",
    "OO...." : "3",
    "OO.O.." : "4",
    "O..O.." : "5",
    "OOO..." : "6",
    "OOOO.." : "7",
    "O.OO.." : "8",
    ".OO..." : "9",
    ".OOO.." : "0",
}

# English to braille dictionary
english_to_braille = {
    # Letters
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO", 
    
    # Symbols
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......"
}

# Numbers to braille dictionary
numbers_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

def detect_input_type(input):
    if set(input) <= {".", "O"}:
        return "braille"
    return "english"

def translate_to_english(braille_string):
    output = ""
    capital_next = False # Flag to indicate where the next character should be a capital letter
    number_next = False

    # Split the braille string into sections of 6 characters
    character_size = 6
    characters = [braille_string[i:i +character_size] for i in range(0, len(braille_string), character_size)]
    
    # Translation logic
    for char in characters:
        if char == capital_follows:
            # Flag condition has been met so the next character is capital
            capital_next = True
       
        elif char == number_follows:
            # Flag condition has been met so the next character is a number
            number_next = True

        else:
            if capital_next:
                # Capitalize if the flag is set
                if char in braille_to_english:
                    output += braille_to_english[char].upper()
                else:
                    output += "unknown"
                capital_next = False # Reset the flag

            elif number_next:
                # The character is a number 
                if char in braille_to_numbers:
                    output += braille_to_numbers[char]
                else:
                    output += "unknown"
                    number_next = False # Reset the flag

            else:
                number_next = False # Reset the flag
                if len(char) == character_size and char in braille_to_english:
                    output += braille_to_english[char]
                else:
                    output += "unknown"
    return output

def translate_to_braille(english_string):
    output = ""
    number_mode = False

    for char in english_string:
        if char.isupper():
            # If the letter is capitalized then add the capital then add the capital indicator before the braille letter
            output += capital_follows + english_to_braille[char.lower()]
        elif char.isdigit():
            if not number_mode: # This ensures that we use the number indicator once before the digits
                output += number_follows # Add the number follows indicator
                number_mode = True # Now in number mode
            # If the char is a number then the number indicator before the braille number
            output += numbers_to_braille[char]
        else:
            output += english_to_braille[char]
            number_mode = False # Exit number mode when a char that is not a number is encountered 
    return output

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please use this format: python translator.py <string to translate>")
        sys.exit(1)
    
    input_string = " ".join(sys.argv[1:])
    input_type = detect_input_type(input_string)

    if input_type == "braille":
        result = translate_to_english(input_string)
    else:
        result = translate_to_braille(input_string)
    
    print(result) 
