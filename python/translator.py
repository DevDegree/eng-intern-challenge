import sys

braille_dict = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", ".O.OOO": "number", "......": " "
}

english_dict = {v: k for k, v in braille_dict.items()}

char_to_number = {
    "a": '1', "b": '2', "c": '3', "d": '4', "e": '5',
    "f": '6', "g": '7', "h": '8', "i": '9', "j": '0'
}

number_to_char = {v: k for k, v in char_to_number.items()}

# Translate Braille to English
def braille_to_english(braille_str):
    translated_str = ""
    capitalize_next = False
    is_number = False

    for i in range(0, len(braille_str), 6): 
        braille_char = braille_str[i:i+6]
        if braille_char in braille_dict:
            curr_english_char = braille_dict[braille_char]
            if curr_english_char == "capital":
                capitalize_next = True
            elif curr_english_char == "number":
                is_number = True 
            else:
                if curr_english_char == " ":
                    is_number = False
                elif capitalize_next:
                    capitalize_next = False
                    curr_english_char = curr_english_char.upper()
                elif is_number:
                    curr_english_char = char_to_number[curr_english_char]

                translated_str += curr_english_char
        else:
            return "\nInvalid input:\nInvalid Braille character: " + braille_char

    return translated_str

# Translate English to Braille
def english_to_braille(english_str):
    translated_str = ""
    number_encountered = False

    for char in english_str:
        if char.lower() in english_dict:
            if char == " ":
                number_encountered = False # another number char needed for later numbers
            if char.isupper():
                translated_str += english_dict["capital"] # add capital char before every capital letter
                char = char.lower() # no capital char in the dictionary
            translated_str += english_dict[char]
        elif char in number_to_char:
            if not number_encountered: # if this is the first of a consecutive numbers
                translated_str += english_dict["number"]
                number_encountered = True 
            translated_str += english_dict[number_to_char[char]]
        else:
            return "\nInvalid input\nEnglish text can only include numbers, spaces, and English characters"

    return translated_str

# Translate Braille or English
def translate(input_str):
    if len(input_str) >= 6 and '.' in input_str[:6]: 
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

def main():
    args = sys.argv

    if len(args) < 2:
        print("\nNo input was given\nUse: python3 translator.py <input>")
    else:
        input_str = " ".join(args[1:]) 
        output_str = translate(input_str)
        print(output_str)

if __name__ == '__main__':
    main()