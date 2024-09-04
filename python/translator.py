import sys

# Define Braille dictionary
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", 
    "d": "OO.O..", "e": "O..O..", "f": "OOO...", 
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", 
    "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", 
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", 
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", 
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", 
    "y": "OO.OOO", "z": "O..OOO", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", 
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", 
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
    "0": ".OOO..", "capital_next": ".....O", "number_next": ".O.OOO"
}

# Create English dictionary with arrays, but if there are duplicates, add it to an array so it has the format '0.....':['a','1']
english_dict = {}

for key, value in braille_dict.items():
    if value not in english_dict:
        english_dict[value] = [key]
    else:
        english_dict[value].append(key)
     

# Function to translate English to Braille
def translate_to_braille(english_text):
    braille_text = ""
    is_number_mode = False

    for char in english_text:
        if char.isdigit():
            if is_number_mode == False:  
                braille_text += braille_dict["number_next"]
                is_number_mode = True
            braille_text += braille_dict[char]

        elif char.isalpha():
            if is_number_mode:
                braille_text += braille_dict[" "]
                is_number_mode = False
            if char.isupper():
                braille_text += braille_dict["capital_next"]
                braille_text += braille_dict[char.lower()]
            else:
                braille_text += braille_dict[char]

        elif char == " ":
            braille_text += braille_dict[" "]
            is_number_mode = False

    return braille_text


def translate_to_english(braille_text):
    english_text = ""
    i = 0
    while i < len(braille_text):
        symbol = braille_text[i:i+6]
        if symbol == braille_dict["capital_next"]:
            next_symbol = braille_text[i+6:i+12]
            english_text += english_dict[next_symbol][0].upper()
            i += 12
        elif symbol == braille_dict["number_next"]:
            i += 6
            while i < len(braille_text) and braille_text[i:i+6] in english_dict:
                if symbol == "......":
                    i += 6
                    break
                english_text += english_dict[braille_text[i:i+6]][1]
                i += 6
        else:
            english_text += english_dict[symbol][0]
            i += 6
    return english_text

if __name__ == "__main__":
    # Combine all arguments into a single string
    input_text = " ".join(sys.argv[1:])

    # Determine if the input is Braille or English based on the content
    if all(c in "O." for c in input_text):
        # Braille to English
        output = translate_to_english(input_text)
    else:
        # English to Braille
        output = translate_to_braille(input_text)

    # Output the result for testing
    print(output.strip())