import sys

# Braille mapping for letters and numbers
braille_map = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
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
    " ": "......",  # Space
    ".": "..OO.O", # decimal
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OO.O",
    "'": "....O.",
    ":": "O..OOO",
    ";": "O..OO.",
    "-": "....OO",
    "capital": ".....O",  # Capital follows indicator
    "number": ".O.OOO",   # Number follows indicator
}

braille_map_num = {
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
    ".": ".O...O",
}

def translator(string):
    result = ""
    i = 0
    is_braille = True
    number_mode = False

    # check if braille or english
    for char in string:
        if char not in {'O', '.'}:
            is_braille = False

     # english -> braille
    if not is_braille:
        while i < len(string):
            char = string[i]

            if char.isupper():
                result += ".....O" + braille_map[char]    
            elif string[i].isdigit():
                if i > 0 and string[i-1].isdigit():
                    result += braille_map[char]
                else:
                    result += ".O.OOO" + braille_map[char]  
            elif char == ".":
                result += ".O...O"
            else:
                result += braille_map[char.upper()]
            i += 1      

    # braille -> english
    while i < len(string):
        braille_char = string[i:i+6]
        i += 6

        if braille_char == "......" and number_mode:
            number_mode = False
            result += ' '    

        elif braille_char == ".....O":  # capital indicator
            braille_char = string[i:i+6]  
            i += 6
            for letter, braille in braille_map.items():
                if braille == braille_char:
                    result += letter.upper()
                    number_mode = False
                    break
        elif braille_char == ".O.OOO":  # number indicator
            number_mode = True 
            braille_char = string[i:i+6]  # extract the next Braille character
            i += 6
            for number, braille in braille_map_num.items():
                if braille == braille_char:
                    result += number
                    break
        else:
            if number_mode:
                for number, braille in braille_map_num.items():
                    if braille == braille_char:
                        result += number
                        break
            else:
                for letter, braille in braille_map.items():
                    if braille == braille_char:
                        if number_mode:
                            result += letter  
                        else:
                            result += letter.lower()
                        break

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)
    
    input_string = " ".join(sys.argv[1:])
    
    output = translator(input_string)
    print(output)
