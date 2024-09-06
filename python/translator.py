# translator.py

# Define Braille alphabet mappings for letters, numbers, and special control characters
braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", " ": "......",
    "capital": ".....O", "number": ".O.OOO",
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO..."
}

def english_to_braille(text, braille_alphabet):
    output = ""
    in_number_mode = False
    for char in text:
        if char.isupper():
            output += braille_alphabet["capital"]
            output += braille_alphabet[char.lower()]
            in_number_mode = False
        elif char.isdigit():
            if not in_number_mode:
                output += braille_alphabet["number"]
                in_number_mode = True
            output += braille_alphabet[char]
        else:
            in_number_mode = False if char == " " else in_number_mode
            output += braille_alphabet.get(char, '')
    return output

def braille_to_english(braille, braille_alphabet):
    reversed_alphabet = {v: k for k, v in braille_alphabet.items()}
    english = ""
    i = 0
    capitalize_next = False
    in_number_mode = False

    while i < len(braille):
        current_symbol = braille[i:i+6]

        if current_symbol == braille_alphabet["capital"]:
            capitalize_next = True
            i += 6
            continue
        elif current_symbol == braille_alphabet["number"]:
            in_number_mode = True
            i += 6
            continue
        elif current_symbol == braille_alphabet[" "]:
            english += " "
            in_number_mode = False
            i += 6
            continue
        else:
            char = reversed_alphabet.get(current_symbol, '')
            if in_number_mode and char.isalpha():
                char = str(ord(char) - ord('a'))
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            english += char
        i += 6
    return english

if __name__ == "__main__":
    import sys
    input_text = sys.argv[1]
    
    # Determine if input is Braille or English and translate accordingly
    if all(c in 'O.' for c in input_text):
        print(braille_to_english(input_text, braille_alphabet))
    else:
        print(english_to_braille(input_text, braille_alphabet))
