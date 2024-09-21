import sys

# English to Braile dictionaries
# Reminder: Braile should be read left to right, top down.
english_to_braille_letters = {
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
}

english_to_braille_numbers = {
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

english_to_braille_special = {
    "capital": ".....O",
    "number": ".O.OOO",
    "space": "......",
}

# Braile to English dictionaries
braille_to_english_letters = {value: key for key, value in english_to_braille_letters.items()}
braille_to_english_numbers = {value: key for key, value in english_to_braille_numbers.items()}
braille_to_english_special = {value: key for key, value in english_to_braille_special.items()}


def translate_to_braille(words):
    res = ""
    
    for word in words:
        # Reset number follows whenever a new word begins
        isNumber = False
        for char in word:
            if char.isalpha():
                if char.isupper():
                    res += english_to_braille_special["capital"]
                    res += english_to_braille_letters[char.lower()]
                else: #Lower case
                    res += english_to_braille_letters[char]
            elif char.isdigit():
                # Only set the number follows at the start of a number
                if isNumber == False:
                    res += english_to_braille_special["number"]
                    isNumber = True
                res += english_to_braille_numbers[char]
        res += english_to_braille_special["space"]
    # Get rid of the last space in the word
    res = res[:-6]
        
    print(res)

def translate_to_english(braille):
    isNumber = False
    isCapital = False
    res = ""
    
    for index in range(0, len(braille), 6):
        braille_char = braille[index:index+6]
        if braille_char in braille_to_english_special:
            if braille_to_english_special[braille_char] == "capital":
                isCapital = True
            elif braille_to_english_special[braille_char] == "number":
                isNumber = True
            elif braille_to_english_special[braille_char] == "space":  
                # No more numbers if space symbol is found
                if isNumber == True:
                    isNumber = False
                res += " "
        else:
            if isNumber == True:
                res += braille_to_english_numbers[braille_char]
            elif isCapital == True:
                res += braille_to_english_letters[braille_char].upper()
                # Only one symbol is capitalized
                isCapital = False
            else:
                res += braille_to_english_letters[braille_char]
            
    print(res)

def main(args):
    if len(args) > 1:
        # Braile cannot have more than one argument, so this is English,
        # which must be translated to Braile
        translate_to_braille(args)
    else:
        # Braile is always in sets of 6 chars
        if len(args[0]) % 6 == 0:
            for char in args[0]:
                #Check if all chars are . or O for Braile
                if char != "." or char != "O":
                    translate_to_english(args[0])
                    return
            translate_to_english(args[0])
            return
        translate_to_braille(args)
        
    return


if __name__ == "__main__":
    main(sys.argv[1:])
    
        