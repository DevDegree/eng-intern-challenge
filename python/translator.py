import sys

# The braille alphabet
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO." : "o", 
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", ".O...O": "decimal",".O.OOO": "number",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", 
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(", 
    ".O.OO.": ")", "......": " "
}

# Numbers for braille
numbers_to_braille = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OOO.."
}

# Swap keys and values in numbers_to_braille to create braille_to_numbers
def build_braille_to_numbers():
    braille_to_numbers = {}
    
    for digit, braille_pattern in numbers_to_braille.items():
        braille_to_numbers[braille_pattern] = digit

    return braille_to_numbers

braille_to_numbers = build_braille_to_numbers()

# Swap keys and values in braille_to_english to create english_to_braille
def build_english_to_braille():
    english_to_braille = {"o" : "O..OO.", "O" : ".....OO..OO."}

    for key, value in braille_to_english.items():
        if value.isalpha() and value.islower() and value != "o":
            english_to_braille[value] = key

    for key, value in braille_to_english.items():
        if value.isalpha() and value.islower() and value != "o":
            english_to_braille[value.upper()] = ".....O" + key

    for key, value in braille_to_english.items():
        if value in ".,?!:;-/()< ":
            english_to_braille[value] = key

    for number, braille in numbers_to_braille.items():
        english_to_braille[number] = ".O.OOO" + braille

    return english_to_braille

english_to_braille = build_english_to_braille()

# Is input in Braille
def is_braille(text):
    valid_braille_chars = "O. "

    for char in text:
        if char not in valid_braille_chars:
            return False

    return True

# Translate braille to english
def translate_braille_to_english(braille_text):
    words = braille_text.split(" ")
    english_output = []
    capital_mode = False
    number_mode = False
    
    for word in words:
        for i in range(0, len(word), 6):
            braille_char = word[i:i+6]
            
            if braille_char == ".....O":
                capital_mode = True
            elif braille_char == ".O.OOO":
                number_mode = True
            elif braille_char == "......":
                english_output.append(" ")
                number_mode = False
            else:
                if number_mode and braille_char in braille_to_numbers:
                    if braille_char == "O..OO.":
                        english_output.append(">")
                    else:
                        english_output.append(braille_to_numbers[braille_char])
                elif braille_char in braille_to_english:
                    letter = braille_to_english[braille_char]
                    if capital_mode:
                        letter = letter.upper()
                        capital_mode = False
                    english_output.append(letter)

        english_output.append(" ")
    
    return "".join(english_output).strip()


# Translate english to braille
def translate_english_to_braille(english_text):
    braille_output = []
    number_mode = False
    
    for char in english_text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(".O.OOO")
                number_mode = True
            braille_output.append(numbers_to_braille[char])
        else:
            if number_mode:
                number_mode = False
            if char == ">":
                braille_output.append("O..OO.")
            else:
                braille_output.append(english_to_braille[char])

    return "".join(braille_output)


# CLA handling
def main():
    if len(sys.argv) < 2:
        return

    input_text = " ".join(sys.argv[1:])
    
    if is_braille(input_text):
        # Convert braille to english
        result = translate_braille_to_english(input_text)
    else:
        # Convert english to braille
        result = translate_english_to_braille(input_text)
    
    print(result)

if __name__ == "__main__":
    main()