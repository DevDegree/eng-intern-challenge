# Python Instructions

Note that the Python version used is 3.8

# Braille to English and English to Braille Translator

## Overview

This script is a command-line application that translates text between Braille and English. It is capable of automatically detecting whether the input text is in Braille or English and converting it to the appropriate opposite. The application is designed to handle the entire English alphabet, numbers, spaces, capitalization, and a wide range of punctuation marks.

## Features

### 1. Automatic Language Detection
- The script determines whether the input text is in Braille or English based on its format.
- If the input consists of `O` and `.` characters and the length is a multiple of 6, it is treated as Braille.
- If the input does not meet the criteria for Braille, it is treated as English text.

### 2. Translation Between Braille and English
- **Braille to English**: Converts a valid Braille input (represented by `O` for raised dots and `.` for flat dots) to its English equivalent.
- **English to Braille**: Converts English text into its corresponding Braille representation.

### 3. Support for Capitalization and Numbers
- **Capitalization**: The translator correctly handles capitalized letters by using a special Braille symbol to indicate that the following letter should be capitalized.
- **Numbers**: The translator uses a special Braille symbol to indicate that the following characters should be interpreted as numbers until a space is encountered.

### 4. Comprehensive Punctuation Handling
- The translator has been extended to handle a wide range of punctuation marks, including `. , ? ! : ; - / < > ( )`.
- This enhancement goes beyond the basic requirements of the challenge, ensuring that texts with punctuation can be accurately translated between English and Braille.

## Instructions Fulfillment

The script meets the requirements of the challenge as follows:

1. **Input Handling**: The script can accept input from the command line and automatically detect whether it is in Braille or English.
2. **English to Braille Conversion**: The script converts the entire English alphabet, numbers, spaces, and capitalization into Braille.
3. **Braille to English Conversion**: The script converts valid Braille inputs back into their English equivalents, including handling of capitalization and numbers.
4. **Error Handling**: If the input is invalid Braille (e.g., not divisible by 6), the script treats the input as English, preventing errors.

## Additional Features

### Punctuation Handling
The script goes beyond the original challenge requirements by adding support for punctuation marks in both English to Braille and Braille to English conversions. This makes the translator more versatile and capable of handling real-world text inputs that include punctuation.

### Edge Case Handling
The script is robust against edge cases such as incomplete Braille inputs. If the input does not meet the criteria for valid Braille, it defaults to treating the input as English text. This ensures that the script can handle a wide range of inputs without crashing or producing incorrect results.

## Usage

### Command-Line Execution

To use the translator, run the following command in your terminal:

```bash
python3 translator.py "Your text here"
