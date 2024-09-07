#Program to translate Braille to English and vice versa
import argparse

#Braille to English alphabets dictionary
braille_letters = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

#Braille to numbers dictionary
braille_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

#Braille to symbols dictionary
braille_symbols = {
    "......": " ",        # Space
    "..OO.O": ".",        # Dot
    "..O...": ",",        # Comma
    "..OOO.": "!",        # Exclamation mark
    "..O.OO": "?",        # Question mark
    "....OO": "-",        # Hyphen
    "..OO..": ":",        # Colon
    "..O.O.": ";",        # Semicolon
    ".O..O.": "/",        # backslash
    ".OO..O": "<",        # Less than symbol
    "O..OO.": ">",        # Greater than symbol
    "O.O..O": "(",        # Open parenthesis
    ".O.OO.": ")"         # Close parenthesis
}


#Reversing the dictionaries for English to Braille
english_to_braille_letters = {v: k for k, v in braille_letters.items()}
english_to_braille_numbers = {v: k for k, v in braille_numbers.items()}
english_to_braille_symbols = {v: k for k, v in braille_symbols.items() if v not in ["capital", "number", " "]}

#Variables for Braille special characteristcs
capital_symbol = ".....O"
number_symbol = ".O.OOO"
space_symbol = "......"
decimal_symbol = ".O...O"


#Function to parse the arguments passed during running the program
def parse_arguments():
    #Parsing multiple arguments for input string
    parser = argparse.ArgumentParser(description="Braille to English and vice versa translator.")
    parser.add_argument("input_strings", nargs='+', help="The strings to translate.")
    return parser.parse_args()

#Function to check whether the given string is of Braille or not
def is_braille(input_string):
    # Check if the input consists of only Braille characters (O and .)
    return all(char in "O." for char in input_string)

#Function to translate English to Braille
def translate_english_to_braille(input_string):
    output = []
    number_mode = False
    for char in input_string:
        if char.isupper():
            output.append(capital_symbol)  #Adding capital symbol for uppercase letters
            char = char.lower()
        if char == " ":
            output.append(space_symbol)  #Adding space symbol for spaces
        elif char.isdigit():
            if not number_mode:
                output.append(number_symbol)  #Adding number symbol for digit sequences
                number_mode = True
            output.append(english_to_braille_numbers[char])
        elif char == "." and number_mode:
            output.append(decimal_symbol)  #Handling decimal point in number mode
        elif char in english_to_braille_letters:
            number_mode = False  #Exiting number mode if letter is found
            output.append(english_to_braille_letters[char])
        elif char in english_to_braille_symbols:
            number_mode = False  #Exiting number mode if symbol is found
            output.append(english_to_braille_symbols[char])
        else:
            raise KeyError(f"Character '{char}' not found in Braille dictionary.")
    return ''.join(output)

#Function to translate braille to English
def translate_braille_to_english(input_string):
    # Translate from Braille to English
    output = []
    i = 0
    number_mode = False
    while i < len(input_string):
        symbol = input_string[i:i+6]
        if symbol == capital_symbol:
            i += 6
            symbol = input_string[i:i+6]
            output.append(braille_letters[symbol].upper())  #Capital letters handling
        elif symbol == space_symbol:
            output.append(" ")  #Handling spaces
        elif symbol == number_symbol:
            number_mode = True
            i += 6
        elif symbol == decimal_symbol and number_mode:
            output.append(".")  #Handling decimals
        elif number_mode and symbol in braille_numbers:
            output.append(braille_numbers[symbol])  #Handling numbers
        elif symbol in braille_letters:
            number_mode = False
            output.append(braille_letters[symbol])  #Handling letters
        elif symbol in braille_symbols:
            number_mode = False
            output.append(braille_symbols[symbol])  #Handling symbols
        else:
            raise KeyError(f"Braille symbol '{symbol}' not found in the dictionary.")
        i += 6
    return ''.join(output)

#Starting point of the program
if __name__ == "__main__":
    #Parsing the argument
    args = parse_arguments()
    input_string = " ".join(args.input_strings)  # Join input arguments with spaces

    #Validating whether the given string is Braille or English
    if is_braille(input_string):
        translated_text = translate_braille_to_english(input_string)
    else:
        translated_text = translate_english_to_braille(input_string)

    #Printing the output
    print(translated_text)



