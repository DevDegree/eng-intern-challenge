# Braille Translator

## Overview

The Braille Translator script converts between English text and Braille representations. It supports both Braille and English input and can handle letters, numbers, and common punctuation marks.

## Requirements

- Python 3.8

## Usage

To use the script, run the following command from your terminal:

```bash
python3 translator.py <input_string>
```

## Example

### English to Braille

```bash
python3 translator.py "Hello world 123
```

Output:

```bash
......O.O..O..O...O.O..O..OO..O....O...O.O.O..OO...O...O..OOO
```

### Braille to English

```bash
python3 translator.py ......O.O..O..O...O.O..O..OO..O....O...O.O.O..OO...O...O..OOO
```

Output:

```bash
Hello world 123
```

## Functions

- detect_input_type(input_string):
  Detects whether the input string is in Braille or English.

  - Parameters:

    - input_string (str): The input string to be detected.

  - Returns:

    - "Braille" if the input contains only Braille characters (O and .).
    - "English" if the input contains other characters.

- braille_to_english(braille_string):
  Converts a Braille string into English text.

  - Parameters:

    - braille_string (str): The Braille string to be converted.

  - Returns:

  - The English text corresponding to the provided Braille string.

- english_to_braille(input_string):
  Converts English text into Braille.

  - Parameters:

    - input_string (str): The English text to be converted.

  - Returns:

    - The Braille string corresponding to the provided English text.
