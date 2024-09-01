# Python Instructions

Note that the Python version used is 3.8

Hi, Shopify! 👋🏾

This is my submission for the Eng Intern Challenge Fall - Winter 2025. 

# Braille Translator

## Overview
The Braille Translator is a Python script that allows you to convert English text to Braille and vice versa. It supports the translation of alphabetic characters, numbers, and spaces, with special handling for uppercase letters and numbers.

## Features
- **English to Braille Translation:** Converts English alphabetic characters, numbers, and spaces to Braille.
- **Braille to English Translation:** Converts Braille patterns back into readable English text.
- **Special Handling:** The script uses format markers for uppercase letters and numbers, ensuring accurate translations.

## Usage
You can run the script directly from the command line, providing the text you wish to translate as an argument. The script will automatically detect whether the input is in English or Braille and translate it accordingly.

### Examples:
```bash
# Translate English to Braille
$ python3 translator.py "Hello 123"

# Translate Braille to English
$ python3 translator.py ".....O.OO.OO.O..OO.O.OO..OOO.."
