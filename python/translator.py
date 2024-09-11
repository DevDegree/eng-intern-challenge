import argparse

# Function to convert English text to Braille
def english_to_braille(english_text):
    braille_dict = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
        "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
        "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
        "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO", " ": "......", 
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
        "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
        "9": ".OO...", "0": ".OOO.."
    }

    braille_text = ''.join([braille_dict.get(char.lower(), "") for char in english_text])
    return braille_text

# Function to convert Braille text to English
def braille_to_english(braille_text):
    english_dict = {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
        "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
        ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
        "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
        "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
        "OO.OOO": "y", "O..OOO": "z", "......": " ", 
        "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", 
        "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", 
        ".OO...": "9", ".OOO..": "0"
    }

    english_text = ''.join([english_dict.get(braille_text[i:i+6], "") for i in range(0, len(braille_text), 6)])
    return english_text

# Main function to run the translator
def main():
    parser = argparse.ArgumentParser(description='Translate between English and Braille.')
    parser.add_argument('texts', nargs='+', help='Text(s) to translate')
    args = parser.parse_args()

    results = []
    for input_text in args.texts:
        # Check if the input is English (letters and numbers)
        if any(char.isalnum() for char in input_text):
            translated = english_to_braille(input_text)
        else:
            # Otherwise, assume it's Braille
            translated = braille_to_english(input_text)

        results.append(translated)

    # Join results into a single string and print without additional newlines
    print(''.join(results))

if __name__ == "__main__":
    main()

