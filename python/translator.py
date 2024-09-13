from typing import List
import sys

braille_to_english: dict[str, str] = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
    "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
    "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
    "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "......": " ",
}

braille_to_numbers: dict[str, str] = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7",
    "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

capitalization_prefix: str = ".....O"  # Braille symbol for capital letters
number_prefix: str = ".O.OOO"  # Braille "number follows" operator

# Create a reverse dictionaries for english/numbers to braille
english_to_braille: dict[str, str] = {v: k for k, v in braille_to_english.items()}
number_to_braille: dict[str, str] = {v: k for k, v in braille_to_numbers.items()}

# Convert English to Braille
def english_to_braille_translation(text: str) -> str:
    braille_translation: List[str] = []
    is_number: bool = False
    for char in text:
        if char.isdigit():
            if not is_number:
                braille_translation.append(number_prefix)  # Prefix for numbers
                is_number = True
            braille_translation.append(number_to_braille[char])
        elif char.isupper():
            # Append capitalization prefix for uppercase letters
            braille_translation.append(capitalization_prefix)
            braille_translation.append(english_to_braille[char.lower()])
            is_number = False
        else:
            if char in english_to_braille:
                braille_translation.append(english_to_braille[char])
            is_number = False
    return "".join(braille_translation)

# Convert Braille to English
def braille_to_english_translation(braille_text: str) -> str:
    english_translation: List[str] = []
    i: int = 0
    capitalize_next: bool = False
    number_next: bool = False
    while i < len(braille_text):
        current_braille: str = braille_text[i:i + 6]
        if current_braille == "......": # Space detected, reset number_next
            number_next = False
            english_translation.append(" ")
        elif current_braille == capitalization_prefix:
            # Handle capitalization
            capitalize_next = True
        elif current_braille == number_prefix:
            # Handle numbers
            number_next = True
        else:
            if number_next:
                english_translation.append(braille_to_numbers[current_braille])
            elif capitalize_next:
                english_translation.append(braille_to_english.get(current_braille, "").upper())
                capitalize_next = False
            else:
                english_translation.append(braille_to_english.get(current_braille, ""))
        i += 6
    return "".join(english_translation)

# Function to detect if the input is Braille or English
def brailleInput(input_text: str) -> str:
    # Input is Braille if it contains only "O" and ".", otherwise English
    return all(c in "O." for c in input_text)

# Main function to handle the translation
def translate(input_text: str) -> bool:
    if brailleInput(input_text):
        return braille_to_english_translation(input_text)
    else:
        return english_to_braille_translation(input_text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Join space separated input arguments
        input_text = " ".join(sys.argv[1:])
        print(translate(input_text))
    else:
        print("No text input detected.")