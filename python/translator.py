import sys

# Braille to English
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "cap", ".....O.O": "num",
}

#Braille numbers to English numbers
num_to_english = {
    "0.....": "1", "0.0...": "2", "00....": "3", "00.0..": "4", "0..0..": "5",
    "000...": "6", "0000..": "7", "0.00..": "8", ".00...": "9", ".000..": "0",
}

# English to Braille
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......", "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO..",
}

def translate_to_english(braille):
    """
    Converts Braille string to English.
    Braille characters are 6 characters long.
    """
    results = []
    i = 0
    while i < len(braille):
        if i + 6 > len(braille):
            break
        symbol = braille[i:i+6]

        # handle capital and number indicators
        if symbol == ".....O":
            i += 6
            continue
        elif symbol == "....O.O":
            i += 6
            continue
        
        # translate Braille to English
        if symbol in braille_to_english:
            results.append(braille_to_english[symbol])
        elif symbol in num_to_english:
            results.append(num_to_english[symbol])
        else:
            results.append('?')  #  for unknown Braille symbols
        i += 6
    
    return ''.join(results)

def translate_to_braille(english):
    """
    Converts English string to Braille.
   
    """
    results = []
    is_number = False

    for char in english:
        char_lower = char.lower()
        
        # add capital indicator for uppercase letters
        if char.isupper():
            results.append(".....O")
        
        # add number indicator and Braille translation for digits
        if char.isdigit():
            if not is_number:
                results.append("....O.O")
                is_number = True
            results.append(english_to_braille.get(char, "??????"))
        else:
            is_number = False
            results.append(english_to_braille.get(char_lower, "??????"))

    return ''.join(results)

def main():
    """ 
    Main function to handle input and output.

    """
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return
    
    input_string = sys.argv[1]
    # check if its braille
    if 'O' in input_string or '.' in input_string:
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
