# Braille to english
braille_translations = {
    "0.....": 'a', "0.0...": 'b', "00....": 'c', "00.0..": 'd', "0..0..": 'e', 
    "000...": 'f', "0000..": 'g', "0.00..": 'h', ".00...": 'i', ".000..": 'j', 
    "0...0.": 'k', "0.0.0.": 'l', "00..0.": 'm', "00.00.": 'n', "0..00.": 'o', 
    "000.0.": 'p', "00000.": 'q', "0.000.": 'r', ".00.0.": 's', ".0000.": 't', 
    "0...00": 'u', "0.0.00": 'v', ".000.0": 'w', "00..00": 'x', "00.000": 'y', 
    "0..000": 'z', "......": ' '
}
# English to braille
english_translations = {
    'a': "0.....", 'b': "0.0...", 'c': "00....", 'd': "00.0..", 'e': "0..0..",
    'f': "000...", 'g': "0000..", 'h': "0.00..", 'i': ".00...", 'j': ".000..",
    'k': "0...0.", 'l': "0.0.0.", 'm': "00..0.", 'n': "00.00.", 'o': "0..00.",
    'p': "000.0.", 'q': "00000.", 'r': "0.000.", 's': ".00.0.", 't': ".0000.",
    'u': "0...00", 'v': "0.0.00", 'w': ".000.0", 'x': "00..00", 'y': "00.000",
    'z': "0..000", ' ': "......"
}
# numbers to braille
digit_to_braille = {
    '1': "0.....", '2': "0.0...", '3': "00....", '4': "00.0..", '5': "0..0..",
    '6': "000...", '7': "0000..", '8': "0.00..", '9': ".00...", '0': ".000.."
}
# braille to numbers
braille_to_digits = {
    "0.....": '1', "0.0...": '2', "00....": '3', "00.0..": '4', "0..0..": '5',
    "000...": '6', "0000..": '7', "0.00..": '8', ".00...": '9', ".000..": '0'
}

# capital and number constant
capital_braille = ".....0"
number_braille = ".0.000"

# Checks if input is valid and braille
def is_braille(input_string):
    for char in input_string:
        if char not in ['0', '.', ' ']:
            return False
    return True

# convert English to Braille
def english_to_braille(input_string):
    output = ""
    is_number = False
    
    for char in input_string:
        if char.isalpha():
            if char.isupper():
                output += capital_braille
                char = char.lower()
            output += english_translations[char]
            is_number = False
        elif char.isdigit():
            if not is_number:
                output += number_braille
                is_number = True
            output += digit_to_braille[char]
        elif char == ' ':
            output += english_translations[' ']
            is_number = False
    
    return output

# convert Braille to English
def braille_to_english(input_string):
    output = ""
    if len(input_string) % 6 != 0:
        print("Invalid number of characters. Should be multiples of 6.")
        return ""
    
    capital_next = False
    is_number = False
    
    for i in range(0, len(input_string), 6):
        braille_char = input_string[i:i+6]
        
        if braille_char == capital_braille:
            capital_next = True
        elif braille_char == number_braille:
            is_number = True
        elif is_number and braille_char in braille_to_digits:
            output += braille_to_digits[braille_char]
            is_number = False
        elif braille_char in braille_translations:
            translated_char = braille_translations[braille_char]
            if capital_next:
                translated_char = translated_char.upper()
                capital_next = False
            output += translated_char
        else:
            print(f"Unknown Braille Character {braille_char}")
            return ""
    
    return output

# Handles input and output
def main():
    #Directly take input for conversion
    text = input("Enter text (English or Braille): ").strip()
    
    if all(char in ['0', '.', ' '] for char in text):
        # If input is Braille
        if len(text) % 6 == 0:
            result = braille_to_english(text)
            print(result)
        else:
            print("Invalid Braille input. Must be multiples of 6 characters.")
    else:
        # If input is English
        result = english_to_braille(text)
        print(result)

if __name__ == "__main__":
    main()

