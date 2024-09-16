

# Braille Translator
## Overview
The **Braille Translator** is a Python application that converts English text to Braille code and back. It automatically detects the type of input provided—whether it's English or Braille—and performs the appropriate translation. The program effectively handles letters, numbers, capitalization, spaces, and some punctuation marks.

This application is designed for ease of use and efficiency, utilizing mapping dictionaries for quick and accurate translations. It runs smoothly from the command line and maintains optimal performance even with long input strings.

## How it Works
### Input Detection
The translator begins by determining the input type:

- Braille Input: If the input string consists solely of the characters 'O', '.', and spaces, it is considered Braille code.
- English Input: If the input contains any other characters, it is treated as English text.
### English to Braille Conversion
When translating from English to Braille, the application processes each character in the input:

- Letters: Each letter is converted to its corresponding Braille pattern using a lookup dictionary.
  - Uppercase Letters: A Braille capitalization sign is added before the letter's Braille code.
- Numbers: When a digit is encountered:
  - A Braille number sign is inserted.
  - The digit is converted to a Braille pattern that represents numbers.
  - Spaces: Translated directly to the Braille space character.
  - Punctuation: Supported punctuation marks are converted to their Braille equivalents.

### Braille to English Conversion
For Braille to English translation, the application processes the Braille input as follows:

- Chunking: The input is divided into chunks of six characters, each representing a Braille cell.
- Special Signs:
    - Capitalization Sign: When encountered, the next letter is capitalized.
    - Number Sign: Activates number mode, affecting subsequent characters until the mode is turned off.
- Braille Cells: Each cell is mapped to its corresponding English character or digit using a reverse lookup dictionary.
- Spaces: Braille spaces are translated back to English spaces.
### Mode Handling
- Capital Mode: Triggered by a capitalization sign; affects only the next character.
- Number Mode: Triggered by a number sign; remains active until a non-number character or space is encountered.

## Usage
### Requirements
- Python 3.8+
- No additional libraries are required.

## Running the Application
- Navigate to the Project Directory:

Open your terminal and navigate to the directory containing translator.py.

- Run the Translator:

` 
  python3 translator.py "<input_text>"
`
- Replace <input_text> with the English text or Braille code you wish to translate.
- Enclose the input in quotes to handle spaces and special characters.
