import argparse

# Parse command line argument
parser = argparse.ArgumentParser()
input_arg = parser.add_argument("input_string", nargs="*")
args = parser.parse_args()

string_to_translate = "".join(args.input_string)

braille_alphabet = {"O.....": ["a", "1"], "O.O...": ["b", "2"], "OO....": ["c", "3"], "OO.O..": ["d", "4"],
                    "O..O..": ["e", "5"], "OOO...": ["f", "6"], "OOOO..": ["g", "7"], "O.OO..": ["h", "8"],
                    ".OO...": ["i", "9"], ".OOO..": ["j", "0"], "O...O.": "k", "O.O.O.": "l","OO..O.": "m",
                    "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s",
                    ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
                    ".....O": "cf",".O.OOO": "nf", "......": " "}

# English alphabet mapping is reverse of Braille mapping
english_alphabet = {}
for braille_char, english_char in braille_alphabet.items():
    if isinstance(english_char, list):
        english_alphabet[english_char[0]] = braille_char
        english_alphabet[english_char[1]] = braille_char
    else:
        english_alphabet[english_char] = braille_char

# Determine if input string is English or Braille
is_english = True
input_chars = set(string_to_translate)
input_length = len(string_to_translate)

if "." in input_chars:
    is_english = False

# Check if input string is a valid English or Braille string
if is_english:
    if not string_to_translate.isalnum():
        raise argparse.ArgumentError(input_arg, "Enter a valid English or Braille string")
else:
    if len(args.input_string) > 1 or input_length % 6 != 0:
        raise argparse.ArgumentError(input_arg, "Enter a valid English or Braille string")
    else:
        num_chars = input_length // 6
        for i in range(num_chars):
            j = i * 6
            if string_to_translate[j: j + 6] not in braille_alphabet:
                raise argparse.ArgumentError(input_arg, "Enter a valid English or Braille string")
            
# Translate Braille to English
def translate_to_english(text):
    translated_text = []
    english_length = len(text) // 6
    capital_follows = False
    number_follows = False
    for i in range(english_length):
        j = i * 6
        braille_char = text[j: j + 6]
        english_char = braille_alphabet[braille_char]
        if english_char == "cf":
            capital_follows = True
            continue

        if english_char == "nf":
            number_follows = True
            continue

        if capital_follows:
            if isinstance(english_char, list):
                english_char = english_char[0]
            translated_text.append(english_char.upper())
            capital_follows = False
        
        elif number_follows:
            if isinstance(english_char, list):
                english_char = english_char[1]

            if english_char == " ":
                number_follows = False

            translated_text.append(english_char)
        
        elif isinstance(english_char, list):
            translated_text.append(english_char[0])
        
        else:
            translated_text.append(english_char)
    
    return "".join(translated_text)

# Translate English to Braille
def translate_to_braille(text):
    translated_text = []
    for word in text:
        is_number = False
        for english_char in word:
            if english_char.isupper():
                translated_text.append(english_alphabet["cf"])
                translated_text.append(english_alphabet[english_char.lower()])
            elif english_char.isnumeric():
                if not is_number:
                    is_number = True
                    translated_text.append(english_alphabet["nf"])
                translated_text.append(english_alphabet[english_char])
            else:
                translated_text.append(english_alphabet[english_char])
        translated_text.append(english_alphabet[" "])
        is_number = False
                
    if translated_text:
        translated_text.pop()
    return "".join(translated_text)

if is_english:
    print(translate_to_braille(args.input_string))
else:
    print(translate_to_english(string_to_translate))