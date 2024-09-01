import sys
# Create a dictionary to map braille to english 
braille_english_map = {
    "non-numerical": {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
        "O..OOO": "z", "......": " ", ".....O": "capital follows", ".O.OOO": "number follows",
        ".O...O":"decimal follows", "..OO.O":".", "..O...": ",", "..O.OO": "?", "..OOO." : "!",
        "..OO.." : ":", "..O.O." : ";", "....OO" : "-", ".O..O.":"/", "O.O..O": "(", ".O.OO." : ")"
    },
    "numbers": {
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
        "..OO.O":".", "....OO" : "-", ".O..O.": "/", ".OO..O" : "<", "O..OO.": ">",
        "O.O..O": "(", ".O.OO." : ")", "......": " ",
    }
}

#Also generate a reverse mapping for english to braille
english_braille_map = {v: k for k, v in braille_english_map["non-numerical"].items()}
english_braille_map.update({v: k for k, v in braille_english_map["numbers"].items()})

def split_string(input_string:str) -> list:
    '''Splits a string into groups of 6 chars'''
    return [input_string[i:i+6] for i in range(0, len(input_string), 6)]

def is_braille(input_string:str) -> bool:
    ''' checks if a string is braille'''
    #split the string into chars of 6 
    char_list = split_string(input_string)
   # If all chunks are in the keys of the braille_english_map, letters or numbers, then this will return True i.e it is Braille
    return all(char in braille_english_map["non-numerical"] or char in braille_english_map["numbers"] for char in char_list)

def translate_braille(input_string: str) -> str:
    '''Translates a Braille string to English'''
    translated_string = ''
    char_list = split_string(input_string)
    capitalize = False
    numericize = False

    for char in char_list:
        if char in braille_english_map["non-numerical"]:
            braille_char = braille_english_map["non-numerical"][char]

            # Handle the special Braille instructions
            if braille_char == "capital follows":
                capitalize = True
                continue
            elif braille_char == "number follows":
                numericize = True
                continue
            elif braille_char == "decimal follows":
                translated_string += "."

            elif braille_char == " ":
                translated_string += ' '
                numericize = False  # Reset numericize after a space
                continue
            
        # Process the character based on the instruction flags
        if numericize:
            if char in braille_english_map["numbers"]:
                braille_char = braille_english_map["numbers"][char]
                translated_string += braille_char
                if braille_char == ' ':
                    numericize = False
        else:
            if capitalize:
                translated_string += braille_char.upper()
                capitalize = False  # Reset capitalize after one character
            else:
                translated_string += braille_char

    return translated_string

def translate_english(input_string: str) -> str:
    '''Translates an English string to Braille.'''
    translated_string = ''
    for char in input_string:
        if char.isupper():
            translated_string += english_braille_map["capital follows"]
            char = char.lower()
            #check if we added the char too

        if char.isdigit():
            if not translated_string.endswith(english_braille_map["number follows"]):
                translated_string += english_braille_map["number follows"]
            translated_string += english_braille_map[char]
        elif char in english_braille_map:
            translated_string += english_braille_map[char]

    return translated_string


def main():
    # Get the input string from the command line arguments
    arguments = sys.argv[1:]
    input_string = "".join(arguments)

    # Determine if string is English or braille
    if is_braille(input_string):
        #If the string is braille translate to braille
        translation = translate_braille(input_string)
    else:
        translation = translate_english(input_string)
    print(translation)


if __name__ == "__main__":
    main()