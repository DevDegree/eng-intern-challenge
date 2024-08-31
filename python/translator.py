import sys 


braille_to_english = {
    "0.....": "a", "0.0...": "b", "00....": "c", "00.0..": "d", "0..0..": "e",
    "000...": "f", "0000..": "g", "0.00..": "h", ".00...": "i", ".000..": "j",
    "0...0.": "k", "0.0.0.": "l", "00..0.": "m", "00.00.": "n", "0..00.": "o",
    "000.0.": "p", "00000.": "q", "0.000.": "r", ".00.0.": "s", ".0000.": "t",
    "0...00": "u", "0.0.00": "v", ".000.0": "w", "00..00": "x", "00.000": "y",
    "0..000": "z", "......": " "
}


braille_to_numbers = {
    "0.....": "1", "0.0...": "2", "00....": "3", "00.0..": "4", "0..0..": "5",
    "000...": "6", "0000..": "7", "0.00..": "8", ".00...": "9", ".000..": "0"
}

english_to_braille = {v: k for k, v in braille_to_english.items()}
numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}

capital_follows = ".....0"
number_follows = ".0.000"

def translator(input_str):
    # Braile to english
    if ('0.' in input_str):
        translated = ""
        i = 0
        while i < len(input_str):
            braille_char = input_str[i:i+6]
            if braille_char in braille_to_english:
                translated += braille_to_english[braille_char]
            elif braille_char in number_follows:
                while i < len(input_str):
                    i += 6
                    braille_char = input_str[i:i+6]
                    if braille_char in braille_to_numbers:
                        translated += braille_to_numbers[braille_char]
                        
            elif braille_char in capital_follows:
                i += 6 
                braille_char = input_str[i:i+6]
                translated += braille_to_english[braille_char].upper()
            else:
                translated += "?" 
            i += 6
    else:
        # English to braille
        translated = ""
        in_number_mode = False
        for char in input_str:
            if char == ' ':
                translated += "......"
                in_number_mode = False
            elif char.isupper():
                translated += capital_follows + english_to_braille.get(char.lower(), "......")
                in_number_mode = False
            elif char.isdigit():
                if not in_number_mode:
                    translated += number_follows
                    in_number_mode = True
                translated += numbers_to_braille.get(char, "......")
            else:
                translated += english_to_braille.get(char, "......")
                in_number_mode = False
    return translated           

if __name__ == "__main__":
    
    input_string = sys.argv[1]
    result = translator(input_string)
    print(result)
        
# For Input: 'Anandsagar 123'
# Output:  .....00.....00.00.0.....00.00.00.0...00.0.0.....0000..0.....0.000........0.0000.....0.0...00....
