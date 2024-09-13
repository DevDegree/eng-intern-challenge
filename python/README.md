## Python Instructions

Note that the Python version used is 3.8

## Braille Translator

### Overview

The Braille Translator is a command-line application that allows bidirectional translation between English text and Braille. The program detects whether the input string is in English or Braille and performs the appropriate translation. It supports the entire English alphabet, numbers (0-9), capitalization, and spaces.

Braille in this application is represented using O (uppercase letter O) for raised dots and . (period) for flat dots.

### Project Structure

- `translator.py`: Main script handling command-line arguments and coordinating translation.
- `braille_translator.py`: Contains the `BrailleTranslator` class with methods for translation.
- `translator.test.py`: Unit tests to verify the functionality.

### How it works

#### Braille Representation

- Braille Cell: Each Braille character is a combination of 6 dots arranged in a 3x2 matrix.
- Dot Representation:
  - O: Raised dot.
  - .: Flat dot.
- Reading Order: The dots are read in order from top to bottom, left to right.

#### Translation Logic

- Language detection

  - The program analyzes the input string: If it contains only O and ., it's treated as Braille. Otherwise, it's treated as English.

- English to Braille:

      - Letters: Each letter is mapped to its Braille equivalent.
      - Capitalization: A special CAPITAL Braille sign (.....O) is inserted before capital letters.
      - Numbers: A NUMBER Braille sign (.O.OOO) is inserted before digits. Subsequent characters are treated as numbers until a space is encountered.
      - Spaces: Spaces in English are translated to Braille spaces (......).

- Braille to English:

- Processing Chunks: The input Braille text is processed in chunks of 6 characters.
- Special Signs:
  - Capital Sign: Indicates the next letter is capitalized.
  - Number Sign: Indicates that subsequent characters are numbers.
- Modes:
  - Capital Mode: Activated by the CAPITAL sign; capitalizes the next letter.
  - Number Mode: Activated by the NUMBER sign; remains active until a space is encountered.

### Author

Emilio Andere
