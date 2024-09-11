import sys
braille_to_english = {
    "O.....": "CAPITAL",  # Capital sign
    "O.OO.O": "#",        # Number sign
    "O.....": "CAPITAL",  # Capital sign
    "O.....": "CAPITAL",
    "O.....": "CAPITAL",
    "O.....": "CAPITAL",
    "O.....": "CAPITAL",
    "O.....": "CAPITAL",
    "O.....": "CAPITAL",
    "O.....": "CAPITAL",
}

# English to Braille dictionary
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Function to detect if the input string is Braille
def is_braille(input_string):
    # Checks if the string contains only 'O' and '.'
    return set(input_string).issubset({'O', '.'})

# Function to translate Braille to English
def translate_braille_to_english(input_string):
    # Split the Braille input by spaces
    braille_chars = input_string.split()
    english_text = []
    is_number_mode = False  # To handle number translation

    for braille_char in braille_chars:
        if braille_char == "O.OO.O":  # Number sign
            is_number_mode = True
            continue
        elif braille_char == "O.....":  # Capital sign
            english_text.append(braille_to_english[braille_char].upper())
        else:
            # Get the English character from the dictionary
            english_char = braille_to_english.get(braille_char, "?")
            english_text.append(english_char)

    return "".join(english_text)

# Function to translate English to Braille
def translate_english_to_braille(input_string):
    braille_text = []
    is_number_mode = False

    for char in input_string:
        if char.isdigit():
            # Start number mode if digit is encountered
            if not is_number_mode:
                braille_text.append("O.OO.O")  # Number sign
                is_number_mode = True
            braille_text.append(english_to_braille[char])
        elif char.isalpha():
            # Handle capital letters
            if char.isupper():
                braille_text.append("O.....")  # Capital sign
            braille_text.append(english_to_braille[char.lower()])
            is_number_mode = False  # Exit number mode after letters
        elif char == " ":
            braille_text.append(" ")  # Preserve spaces

    return "".join(braille_text)


