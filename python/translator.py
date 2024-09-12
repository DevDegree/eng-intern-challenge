import sys

# Braille dictionary for letters, capitalization, number mode, decimal, and space
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", " ": "......",
    "cap": ".....O", "num": ".O.OOO", "dec": ".O...O", ".": "..OO.O"
}

# Separate Braille number dictionary (used in number mode)
braille_num_dict = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", 
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse dictionaries for Braille to English conversions
letter_dict = {v: k for k, v in braille_dict.items() if k not in ["num", "cap", " "]}
num_dict = {v: k for k, v in braille_num_dict.items()}

# Determine if the input is Braille (O and . characters only, divisible by 6)
def is_braille(input_string):
    return all(c in "O." for c in input_string) and len(input_string) % 6 == 0

# Convert Braille to English
def braille_to_english(braille):
    english_text = []
    i = 0
    number_mode = False

    while i < len(braille):
        char_braille = braille[i:i+6]

        if char_braille == braille_dict["cap"]:
            next_char_braille = braille[i+6:i+12]
            if next_char_braille in letter_dict:
                english_text.append(letter_dict[next_char_braille].upper())
            i += 12  # Skip 6 for cap, 6 for the next letter
        elif char_braille == braille_dict["num"]:
            number_mode = True
            i += 6
        elif char_braille == braille_dict[" "]:
            english_text.append(" ")
            number_mode = False
            i += 6
        elif number_mode:
            if char_braille == braille_dict["dec"]:
                english_text.append(".")
                i += 12  # Skip both "dec" and "."
            elif char_braille in num_dict:
                english_text.append(num_dict[char_braille])
                i += 6
            else:
                english_text.append("?")
                i += 6
        else:
            if char_braille in letter_dict:
                english_text.append(letter_dict[char_braille])
            i += 6

    return ''.join(english_text)

# Convert English to Braille
def english_to_braille(text):
    braille_text = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_text.append(braille_dict["num"])
                number_mode = True
            braille_text.append(braille_num_dict[char])
        elif char.isalpha():
            if char.isupper():
                braille_text.append(braille_dict["cap"])
                char = char.lower()
            braille_text.append(braille_dict[char])
            number_mode = False
        elif char == " ":
            braille_text.append(braille_dict[" "])
            number_mode = False
        elif char == ".":
            braille_text.append(braille_dict["dec"])
            braille_text.append(braille_dict["."])
            number_mode = True
        else:
            braille_text.append("?")  # Handle unknown characters

    return ''.join(braille_text)

# Main function to handle input/output
def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()

