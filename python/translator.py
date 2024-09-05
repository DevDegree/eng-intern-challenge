import sys

# Define the alphabet and corresponding Braille representations
alphabet = "abcdefghijklmnopqrstuvwxyz"
braille = [
    "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..",
    "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.",
    "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"
]
numbers = "1234567890"

# Mapping alphabet and numbers to Braille and vice versa
alphabet_to_braille = {ch: br for ch, br in zip(alphabet, braille)}
braille_to_alphabet = {br: ch for ch, br in zip(alphabet, braille)}
numbers_to_braille = {num: br for num, br in zip(numbers, braille[:10])}
braille_to_numbers = {br: num for num, br in zip(numbers, braille[:10])}

# Modes for special cases in Braille (e.g., capitalization or numerics)
modes = {
    ".....O": "capitalize",
    ".O.OOO": "numerize"
}

# Check if the input string is a valid Braille representation
def is_braille(input_str):
    """
    Verifies if the input string is a valid Braille sequence.
    - Must be a multiple of 6 characters (Braille cell length).
    - Can only contain 'O' and '.' characters.
    """
    return len(input_str) % 6 == 0 and all(ch in "O." for ch in input_str)

# Convert alphabetic characters to Braille
def convert_to_braille(input_str):
    """
    Converts alphabetic characters to their corresponding Braille representation.
    Non-alphabetic characters are ignored.
    """
    return "".join(alphabet_to_braille.get(ch, "") for ch in input_str.lower() if ch in alphabet_to_braille)

# Convert Braille back to alphabetic characters
def convert_to_alphanumerics(input_str):
    """
    Converts Braille sequences back into their corresponding alphabetic characters.
    If the sequence is invalid or not found, returns an empty string.
    """
    result = []
    for i in range(0, len(input_str), 6):
        braille_char = input_str[i:i+6]
        result.append(braille_to_alphabet.get(braille_char, ""))
    return "".join(result)

# Test functionality and output results
if __name__ == "__main__":
    # Testing Braille conversion
    print(f"Braille for 'a' and 'b': {alphabet_to_braille['a']} {alphabet_to_braille['b']}")
    
    # Display the number of Braille characters mapped
    print(f"There are {len(braille)} Braille characters in the dictionary.")
    
    # Test if input is valid Braille
    test_cases = ["Hello", "O.....", "O......"]
    for test in test_cases:
        print(f"Is '{test}' Braille? {is_braille(test)}")

