import sys

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

letter_to_braille = {
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
    " ": "......"
}

braille_to_letter = {v: k for k, v in letter_to_braille.items()}

number_to_braille = {
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

braille_to_number = {v: k for k, v in number_to_braille.items()}

def braille_to_english(braille):
    result = ""
    i = 0

    while i < len(braille):
        j = i + 6
        symbol = braille[i:j]
        
        if symbol == NUMBER_FOLLOWS:
            while j < len(braille):
                if braille[j:j+6] == SPACE:
                    break
                
                result += braille_to_number[braille[j:j+6]]
                i = j + 6
                j = i

        elif symbol == CAPITAL_FOLLOWS:
            capital_letter = braille[j:j+6]
            result += braille_to_letter[capital_letter].upper()
            i += 12

        else:
            result += braille_to_letter[symbol]
            i += 6

    return result

def english_to_braille(english):
    result = ""
    
    for i, c in enumerate(english):
        if c.isnumeric():
            if i == 0 or not english[i - 1].isnumeric():
                result += NUMBER_FOLLOWS + number_to_braille[c]

            else:
                result += number_to_braille[c]

        elif c.isupper():
            result += CAPITAL_FOLLOWS + letter_to_braille[c.lower()]
            
        else:
            result += letter_to_braille[c]

    return result

def is_braille(string):
    for c in string:
        if c != "O" and c != ".": 
            return False
    
    return True

def translate(string):
    if is_braille(string):
        return braille_to_english(string)

    return english_to_braille(string)

def main():
    input = " ".join(sys.argv[1:])
    print(translate(input))

if __name__ == '__main__':
    main()
