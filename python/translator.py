import sys

# Map to translate english letters to braille representation
english_to_braille = {
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
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    " ": "......",
}

# Map to translate numbers to braille representation
number_to_braille = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

# maps that will be used to convert braille into letters / numbers
braille_To_English = {v: k for k, v in english_to_braille.items()}
braille_To_Number = {v: k for k, v in number_to_braille.items()}

# Method to translate Braille --> English
def translate_to_english(input):
    result = ""
    capital_follows = number_follows = False
    
    for section in [input[i:i+6] for i in range(0, len(input), 6)]:
        if braille_To_English[section] == "number follows":
            number_follows = True
        elif braille_To_English[section] == "capital follows":
            capital_follows = True  
        elif braille_To_English[section] == " ":
            result += " "
            number_follows = capital_follows = False
        else:
            if number_follows:
                result += braille_To_Number[section]
            elif capital_follows:
                result += braille_To_English[section].upper()
                capital_follows = False
            else:
                result += braille_To_English[section]
    return result

# Method to translate English --> Braille   
def translate_to_braille(input):
    result = ""
    number_follows = False
    
    for character in input:
        if character.isdigit():
            if not number_follows:
                result += (english_to_braille["number follows"])
                number_follows = True
            result += (number_to_braille[character])
        else:
            if character == " ":
                result += (english_to_braille[" "])
                number_follows = False
            else:               
                if character.isupper():
                    result += (english_to_braille["capital follows"])
                result += (english_to_braille[character.lower()])                        
    return result

def main(args):
    if all(char in ['O', '.'] for char in "".join(args)):
        result = translate_to_english("".join(args))
    else:
        result = translate_to_braille(" ".join(args))
    
    return result
    
if __name__ == "__main__":
    args = sys.argv[1:]
    result = main(args) if args else "" 
    print(result)