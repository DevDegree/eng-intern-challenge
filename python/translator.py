
"""
Main module for translating between Braille and English.

This file serves as the entry point for a terminal-based application that translates text between Braille and English.
It utilizes `argparse` to take user input directly from the command line,
determining whether the input is Braille or English and translating accordingly.
"""
import argparse

from translator_helper import translate_braille_to_english, translate_english_to_braille
from utils import is_braille


def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Braille and English translator")

    # Add a positional argument to capture the entire input string
    parser.add_argument('input_string', nargs='+', help='Input string to process')

    # Parse the arguments
    args = parser.parse_args()

    # Join the list of words into a single string (because nargs='+' gives a list)
    input_string = " ".join(args.input_string)
    if is_braille(input_string):
        return translate_braille_to_english(input_string)
    return translate_english_to_braille(input_string)


if __name__ == "__main__":
    print(main())
