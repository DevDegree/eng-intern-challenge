# Python Instructions

# Braille Translator

This is a Python script that translates between English text and Braille. It supports translation of both plain English text (letters, numbers, and some special characters) to Braille and Braille back to English text.

## Features

- **Bidirectional Translation**: Convert English text to Braille and Braille to English.
- **Support for Special Symbols**: The script recognizes special symbols such as capital letters, numbers, and punctuation.
- **Error Handling**: The script logs errors for any formatting issues with the input.

## How It Works

The script defines mappings between plain text (letters, numbers, and some punctuation marks) and Braille representations. When a user inputs a string, the script detects whether it is Braille or plain English and translates it accordingly.

### Mappings

- **Plain Text to Braille**: Letters, numbers, and punctuation are mapped to corresponding Braille representations.
- **Braille to Plain Text**: Braille characters are mapped back to plain text, with support for capitalization and numbers.

### Special Symbols

The script recognizes certain Braille patterns as special symbols, such as:

- **Capitalization**: Indicated by a Braille pattern before a capital letter.
- **Numbers**: Indicated by a Braille pattern before a sequence of digits.
- **Punctuation**: Specific patterns are recognized for common punctuation marks.

## Usage

To run the script, use the following command in your terminal:

```bash
python translator.py <text to translate>
```
Note that the Python version used is 3.8

