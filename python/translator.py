import argparse

#Mapping Braille to characters
braille_letter_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

#Mapping Braille to numbers
braille_number_map = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

#Mapping Braille to symbols and punctuation
braille_symbol_map = {
    "......": " ", "..OO.O": ".", "..O...": ",", "..OOO.": "!", "..O.OO": "?",
    "....OO": "-", "..OO..": ":", "..O.O.": ";", ".O..O.": "/", ".OO..O": "<",
    "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")"
}

#Inverse mappings for converting text to Braille
letter_to_braille = {v: k for k, v in braille_letter_map.items()}
number_to_braille = {v: k for k, v in braille_number_map.items()}
symbol_to_braille = {v: k for k, v in braille_symbol_map.items()}

#Special Braille markers for numbers,symbols, decimals and capital letters
capital_indicator = ".....O"
number_indicator = ".O.OOO"
braille_empty_space = "......"
decimal_point_braille = ".O...O"

#parsing the input
def parse_arguments():
    parser = argparse.ArgumentParser(description="Braille<->EnglishTranslator")
    parser.add_argument("input_data", nargs='+', help="EntertextorBraillecodetotranslate.")
    return parser.parse_args()

#checking if input is Braille based on pattern
def is_braille_pattern(text):
    return all(c in "O." for c in text)

#function to translate from text to Braille
def text_to_braille_conversion(text):
    output = []
    num_mode = False

    #looping through each character in the text
    for ch in text:
        #handling uppercase letters
        if ch.isupper():
            output.append(capital_indicator)
            ch = ch.lower()

        #handling whitespace
        if ch == " ":
            output.append(braille_empty_space)
            num_mode = False
        #handling numbers
        elif ch.isdigit():
            if not num_mode:
                output.append(number_indicator)
                num_mode = True
            output.append(number_to_braille[ch])
        #handling decimal points in numbers
        elif ch == "." and num_mode:
            output.append(decimal_point_braille)
        #handling regular letters
        elif ch in letter_to_braille:
            num_mode = False
            output.append(letter_to_braille[ch])
        #handling punctuation and symbols
        elif ch in symbol_to_braille:
            num_mode = False
            output.append(symbol_to_braille[ch])
        #handling unrecognized characters
        else:
            raise ValueError(f"Unsupported character '{ch}' found in input.")

    return ''.join(output)

#function to translate from Braille to text
def braille_to_text_conversion(braille_text):
    output = []
    num_mode = False
    idx = 0

    #looping through Braille input
    while idx < len(braille_text):
        symbol = braille_text[idx:idx + 6]

        #handling capital letters
        if symbol == capital_indicator:
            idx += 6
            symbol = braille_text[idx:idx + 6]
            output.append(braille_letter_map[symbol].upper())
        #handling whitespace
        elif symbol == braille_empty_space:
            output.append(" ")
        #handling number mode
        elif symbol == number_indicator:
            num_mode = True
            idx += 6
            continue
        #handling decimal points in number mode
        elif num_mode and symbol == decimal_point_braille:
            output.append(".")
        #handling numbers in Braille
        elif num_mode and symbol in braille_number_map:
            output.append(braille_number_map[symbol])
        #handling letters in Braille
        elif symbol in braille_letter_map:
            num_mode = False
            output.append(braille_letter_map[symbol])
        #handling symbols and punctuation
        elif symbol in braille_symbol_map:
            output.append(braille_symbol_map[symbol])
        #handling unrecognized Braille symbols
        else:
            raise ValueError(f"Unrecognized Braille symbol:'{symbol}'.")

        idx += 6

    return ''.join(output)

#main function to handle the translation process
if __name__ == "__main__":
    args = parse_arguments()
    input_data = " ".join(args.input_data)

    #checkifinputisBrailleorplaintext
    if is_braille_pattern(input_data):
        print(braille_to_text_conversion(input_data))
    else:
        print(text_to_braille_conversion(input_data))
