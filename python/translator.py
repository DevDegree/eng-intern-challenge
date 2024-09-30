import sys
import dictionary

def convert_to_braille(english_string):
    output_string = ""
    toggle_number = False
    for i in range(len(english_string)):
        char = english_string[i]
        if char.isupper():
            output_string += dictionary.english_to_braille["capital_indicator"]
            char = char.lower()
        elif char == '.' and i != len(english_string) - 1 and english_string[i + 1].isdigit():
            # A character is only a decimal point if a number comes after it, else, we can assume it's a period
            output_string += dictionary.english_to_braille["decimal"]
            continue # We don't want to include braille for period
        elif char.isdigit() and not toggle_number:
            output_string += dictionary.english_to_braille["number_indicator"]
            toggle_number = True
        
        if (char == ' '):
            toggle_number = False
        output_string += dictionary.english_to_braille[char]
    
    return output_string

def convert_to_english(braille_string):
    output_string = ""
    capitalize = False
    toggle_number = False
    for i in range(0, len(braille_string), 6):
        english_char_translation = dictionary.braille_to_english[braille_string[i:i+6]]
        if english_char_translation == "capital_indicator":
            capitalize = True
        elif english_char_translation == "decimal":
            output_string += '.'
        elif english_char_translation == "number_indicator":
            toggle_number = True
        else:
            if capitalize:
                english_char_translation = english_char_translation.upper()
                capitalize = False
            if english_char_translation == ' ':
                toggle_number = False
            if toggle_number:
                english_char_translation = str(ord(english_char_translation) - 96)[-1] # because letters a to j have the same mapping in braille as 0 to 9, by default, those braille characters will be converted to the letters but if it sees the number indicator like it has in this case, then we just convert each of the letters to their corresponding number using the ascii table
            output_string += english_char_translation
    return output_string

def main():
    original_string = ""
    for i in range(1, len(sys.argv)):
        original_string += sys.argv[i]
        if (i != len(sys.argv) - 1):
            original_string += " "

    # In order for the string to be braille, it should:
    # 1. Consecutive string of .'s and O's that's length is a multiple of 6
    # 2. Each substring of 6 should represent a valid character in english
    output_string = ""
    if len(original_string) % 6 == 0:
        for i in range(0, len(original_string), 6):
            if original_string[i:i+6] not in dictionary.braille_to_english.keys():
                # The original string is in english
                output_string = convert_to_braille(original_string)
                break
        else:
            # The original string is in braille
            output_string = convert_to_english(original_string)
    else:
        output_string = convert_to_braille(original_string)
    
    print(output_string)

if __name__ == "__main__":
    main()