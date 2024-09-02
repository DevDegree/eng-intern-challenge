import sys

def looks_like_braille(inp): 
    """
    Checks if input looks like braille
    input: str
    returns: bool
    output: None
    """
    for char in inp:
        if char != "." and char != "O": return False
    return True

def braille_to_english(braille_text): 
    """
    Braille to English Translator
    input: str
    returns: str
    output: None
    """
        
    alphabet = {
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z"
    }
    digits = {
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
        ".OOO..": "0"
    }
    indicators = {
            ".....O": "capital follows",
            ".O.OOO": "number follows"
        }
    space = "......"
    alphabet_or_digits = alphabet # keeps track of whether we are translating alphabet or digits
    english_tokens = []
    
    i = 0
    while i < len(braille_text):
        braille_token = braille_text[i:i+6]
        if alphabet_or_digits == alphabet:
            if braille_token in alphabet: english_tokens.append(alphabet[braille_token])
            elif braille_token in indicators: 
                if indicators[braille_token] == "capital follows": 
                    i += 6
                    braille_token = braille_text[i:i+6]
                    english_tokens.append(alphabet[braille_token].upper())
                elif indicators[braille_token] == "number follows": alphabet_or_digits = digits  
            elif braille_token == space: english_tokens.append(" ")
        else:
            if braille_token in digits: english_tokens.append(digits[braille_token])
            elif braille_token == space:
                alphabet_or_digits = alphabet
                english_tokens.append(" ")
        i += 6

    return "".join(english_tokens)

def english_to_braille(english_text):
    """
    English to Braille Translator
    input: str
    returns: str
    output: None
    """
    alphabet = {
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
        "z": "O..OOO"
    }
    digits = {
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
    indicators = {
            "capital follows": ".....O",
            "number follows": ".O.OOO",
        }
    space = "......"
    alphabet_or_digits = alphabet  # keeps track of whether we are translating alphabet or digits
    braille_tokens = []
    for char in english_text: 
        if char in alphabet: braille_tokens.append(alphabet[char])
        elif char.lower() in alphabet: braille_tokens.extend([indicators["capital follows"], alphabet[char.lower()]])
        elif char in digits:
            if alphabet_or_digits == alphabet: braille_tokens.append(indicators["number follows"])
            braille_tokens.append(digits[char])
            alphabet_or_digits = digits
        elif char == " ":
            braille_tokens.append(space)
            if alphabet_or_digits == digits: alphabet_or_digits = alphabet

    return "".join(braille_tokens)

def main():
    """
    main function
    input: None
    returns: None
    output: translated text
    """
    if len(sys.argv[1:])==1 and looks_like_braille(sys.argv[1]): out = braille_to_english(sys.argv[1])
    else: out = english_to_braille(" ".join(sys.argv[1:]))
    print(out)

if __name__ == "__main__": main()
