import sys

BRAILLE_CHAR_LEN = 6


# Maps Braille characters to english/numbers
braille_to_english_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", ".....O": "capital", ".O.OOO": "number"  
}

# Seperate mapping for Braille numbers (To avoid duplicate keys for a-j & 0-9)
braille_to_numbers_map = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Map english to corresponding braille
english_to_braille_map = {}

# Add Braille letter mappings
for braille, letter in braille_to_english_map.items():
    english_to_braille_map[letter] = braille

# Add Braille number mappings
for braille, number in braille_to_numbers_map.items():
    english_to_braille_map[number] = braille

# Function to determines if input is braille or not (Only consists of O and or .)
def is_braille(text: str) -> bool:
    return set(text).issubset(set('O.')) and len(text) % BRAILLE_CHAR_LEN == 0
 
 # Function that takes braille input and returns its translated english representation   
def braille_to_english(text: str) -> str:
    english_translation = ""
    capital_mode = False
    number_mode = False

    for i in range(0, len(text), BRAILLE_CHAR_LEN):
        braille_char = text[i:i+BRAILLE_CHAR_LEN]

        if braille_char == english_to_braille_map["capital"]:
            capital_mode = True
            continue
        elif braille_char == english_to_braille_map["number"]:
            number_mode = True
            continue
        
        if number_mode:
            if braille_char == english_to_braille_map[" "]:
                number_mode = False
                english_translation += " "
            else:
                english_translation += braille_to_numbers_map[braille_char]
        else:
            if capital_mode:
                english_translation += braille_to_english_map[braille_char].upper()
                capital_mode = False
            else:
                english_translation += braille_to_english_map[braille_char]
        
    return english_translation

            
def english_to_braille(text: str) -> str:
    braille_translation = ""
    number_mode = False
    
    for char in text:
        if char.isnumeric():
            if not number_mode:
                braille_translation += english_to_braille_map["number"]
                number_mode = True
        elif char.isupper():
            braille_translation += english_to_braille_map["capital"]
        elif char == " ":
            number_mode = False
            
        braille_translation += english_to_braille_map[char.lower()]
    
    return braille_translation

def braille_translator(text: str) -> str:
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])  
        translated_text = braille_translator(input_text)
        print(translated_text)
    else:
        print("Please provide a string to translate.")