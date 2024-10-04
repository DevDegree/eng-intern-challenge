import sys

braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "CAP", ".O...O": "DEC", ".O.OOO": "NUM", "......": " ",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
    "O.O..O": "(", ".O.OO.": ")", "......": " "
}


english_to_braille = {
    "a": "O.....", "b": "O.O..", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "CAP": ".....O", "DEC": ".O...O", "NUM": ".O.OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", 
    "(": "O.O..O", ")": ".O.OO.", " ": "......"
}



# Check if input is Braille or English
def is_braille(input_str):
    return all(char in "O." for char in input_str)

# Braille to English
def braille_to_english_translate(braille):
    result = []
    capital = False
    number_mode = False
    
    # empty list to store 6-character chunks
    chars = []
    
    # Get 6-character chunks
    for i in range(0, len(braille), 6):
        chars.append(braille[i:i+6])

    # Process the 'chars' list
    for char in chars:
        if char == ".....O":  # If current character is capital prefix
            capital = True
        elif char == ".O.OOO":  # If current character is number prefix
            number_mode = True
        elif char == "......":  # If current character is a space
            result.append(" ")
            number_mode = False  # reset number_mode
        else:
            letter = braille_to_english.get(char, "")
            if capital:
                letter = letter.upper()
                capital = False
            if number_mode:
                letter = str(ord(letter) - ord('a') + 1)  # Convert to unicode
            result.append(letter)

    return "".join(result)

# English to Braille
def english_to_braille_translate(eng):
    result = []
    for char in eng:
        if char.isdigit():  # Handle digits
            result.append(".O.OOO")  # If current character is number prefix
            corresponding_letter = chr(ord('a') + int(char))  # Convert digit to letter
            result.append(english_to_braille[corresponding_letter])  # Get Braille for that letter
        elif char.isalpha():  # Handle letters
            if char.isupper():  # If current cjaracter is a capital letter
                result.append(".....O")  # Capital letter prefix
                result.append(english_to_braille[char.lower()])  # Convert to lowercase Braille
            else:
                result.append(english_to_braille[char])  # Current character is lowercase letters
        elif char == " ":and
            result.append("......")
    return "".join(result)




def main():
    # Read input from command line
    input_str = " ".join(sys.argv[1:])

    if is_braille(input_str):
        print(braille_to_english_translate(input_str))
    else:
        print(english_to_braille_translate(input_str))

if __name__ == "__main__":
    main()
    
