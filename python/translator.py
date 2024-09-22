import sys

# Mapping English letters to braille
alphabets_to_braille = {
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

symbols_to_braille = {
    # Numbers
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
    
    # Follows
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    "decimal follows": ".O...O",
    
    # Punctuation and symbols
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
    
    # space
    " ": "......" 
}

braille_to_alphabet = {v: k for k, v in alphabets_to_braille.items()}
braille_to_symbols = {v: k for k, v in symbols_to_braille.items()}

def translate_to_braille(text):
    result = ""
    number_follows = False

    # Loop through each character in the text
    for char in text:
        
        # If the character is a number, add the number follows symbol
        if char.isdigit():
            if not number_follows:
                result += symbols_to_braille["number follows"]
                number_follows = True
            result += symbols_to_braille[char]

        # If the character is a decimal, add the decimal follows symbol
        elif char == ".":
            if number_follows:
                result += symbols_to_braille["decimal follows"]
            result += symbols_to_braille[char]
        
        # If the character is uppercase, add the capital follows symbol
        elif char.isupper():
            result += symbols_to_braille["capital follows"]
            result += alphabets_to_braille[char.lower()]

        # Reset number follows if the character is a space
        elif char == " ":
            number_follows = False
            result += symbols_to_braille[char]

        elif char.isalpha():
            result += alphabets_to_braille[char.lower()]
            
        else:
            result += symbols_to_braille[char]

    return result

def translate_to_english(braille):
    result = ""
    caps_follows = False
    number_follows = False
    decimal_follows = False
    

    for i in range(0, len(braille), 6):
        char = braille[i:i+6]
        
        if char in braille_to_symbols:      
            if braille_to_symbols[char] == "capital follows":
                caps_follows = True   
                continue
            elif braille_to_symbols[char] == "number follows":
                number_follows = True
                continue
            elif braille_to_symbols[char] == "decimal follows":
                decimal_follows = True
                continue
            elif braille_to_symbols[char] == " ":
                number_follows = False
                result += " "
                continue
                
        if caps_follows:
            result += braille_to_alphabet[char].upper()
            caps_follows = False
        elif decimal_follows:
            result += braille_to_symbols[char]
            decimal_follows = False
        elif number_follows:
            result += braille_to_symbols[char]
        else:
            if char in braille_to_alphabet:
                result += braille_to_alphabet[char]
            else:
                result += braille_to_symbols[char]

    return result
    
def is_braille(text):
    for char in text:
        if char not in 'O.':
            return False
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        result = translate_to_english(input_text)
    else:
        result = translate_to_braille(input_text)

    print(result)

if __name__ == "__main__":
    main()