import sys
from collections import defaultdict

# Braille dictionary for letters, numbers, capitalization, and spaces
eng_to_braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "cap": ".....O", "num": ".O.OOO", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Create a reverse dictionary dynamically
braille_to_eng_map = defaultdict(list)
for key, value in eng_to_braille_map.items():
    braille_to_eng_map[value].append(key)

def is_braille(text):
    # Simple check to determine if input is Braille or English
    return all(char in "O." for char in text) and len(text) % 6 == 0

def translate_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(eng_to_braille_map["num"])
                number_mode = True
            result.append(eng_to_braille_map[char])
        else:
            if char == " ":
                number_mode = False  # Reset number mode after a space
            if char.isupper():
                result.append(eng_to_braille_map["cap"])
                char = char.lower()
            result.append(eng_to_braille_map[char])
    
    return "".join(result)

def translate_to_english(text):
    result = []
    capital_flag = False
    number_flag = False
    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]
        candidates = braille_to_eng_map.get(braille_char, [])
        
        if braille_char == eng_to_braille_map["cap"]:
            capital_flag = True
        elif braille_char == eng_to_braille_map["num"]:
            number_flag = True
        elif braille_char == eng_to_braille_map[" "]:
            number_flag = False  # Reset number flag after a space
            result.append(" ")
        else:
            if number_flag:
                # If number flag is true, find the digit candidate
                digit = next((c for c in candidates if c.isdigit()), "")
                result.append(digit)
            else:
                # Otherwise, find the letter candidate
                letter = next((c for c in candidates if c.isalpha()), "")
                if capital_flag:
                    letter = letter.upper()
                    capital_flag = False
                result.append(letter)
    return "".join(result)

def main():
    if len(sys.argv) < 2:
        print("Please provide input text.")
        return
    
    input_text = " ".join(sys.argv[1:])
    
    if is_braille(input_text):
        output = translate_to_english(input_text)
    else:
        output = translate_to_braille(input_text)
    
    print(output)

if __name__ == "__main__":
    main()
