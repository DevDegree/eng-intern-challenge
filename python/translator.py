from dictionary import make_dictionary
from strategies.BrailleToEnglishStrategy import BrailleToEnglishStrategy
from strategies.EnglishToBrailleStrategy import EnglishToBrailleStrategy
import sys

def main():
    """
    The main entry point for the translator program.

    This function initializes the Braille-to-English dictionary, processes
    command-line arguments to determine whether the input is English or Braille,
    and applies the appropriate translation strategy. The result of the
    translation is printed to the standard output.

    Usage:
        python3 translator.py <text_to_translate>

    Exits with a status code of 1 if no input is provided or if invalid
    characters are found in the user input.
    """
    # Define the valid elements for Braille input
    elements = ["O", "."]
    braille_to_english_dict = make_dictionary(elements)

    # Take in user input
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_to_translate>")
        sys.exit(1)

    # Combine all command-line arguments into a single string
    user_input = ' '.join(sys.argv[1:])
    
    # Check if the input is valid Braille or English
    is_not_braille = any(char not in elements for char in user_input)
    
    # Apply the strategy pattern for translation
    if is_not_braille:
        strategy = EnglishToBrailleStrategy(user_input, braille_to_english_dict)
    else:
        strategy = BrailleToEnglishStrategy(user_input, braille_to_english_dict)
        
    # Translate and output the result
    result = strategy.translate()
    print(result)

if __name__ == "__main__":
    main()