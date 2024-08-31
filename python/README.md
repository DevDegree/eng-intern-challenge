# Braille Translator

A Python-based Braille translator that converts between text and Braille. This application supports alphanumeric characters and basic punctuation, handling both text-to-Braille and Braille-to-text translations.

## Features

- Bidirectional translation: text to Braille and Braille to text
- Support for uppercase letters
- Support for numbers
- Command-line interface
- Input validation
- Error handling

## Requirements

- Python 3.6+

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/braille-translator.git

Copy Code
2. Navigate to the project directory:
cd braille-translator

Copy Code

## Usage

Run the script from the command line, providing the input string as an argument:
python braille_translator.py your_input


For Braille input, use 'O' for raised dots and '.' for flat dots. Each Braille character should be represented by 6 dots.

Examples:

1. Text to Braille:
python braille_translator.py Hello World


2. Braille to Text:
python braille_translator.py O.O.O.O.O....OO.O.O.OO



## How it Works

The translator uses a mapping between Braille patterns and alphanumeric characters. It handles  uppercase letters and numbers using specific Braille markers. The main components include:

- `BrailleSpecialChar`: Enum for special Braille characters
- `BrailleMapping`: Contains dictionaries for Braille-to-text mappings
- `BrailleChar` and `TextChar`: Classes to represent and convert individual characters
- `BrailleValidator` and `TextValidator`: Classes to validate input
- `Translator`: Main class that performs the translation

Note that there is not support for a string like "a1b2c3" since when a Braille number follows symbol is read, it is assumed all following symbols are numbers until the next space symbol. This means if we translate a1b2c3 to braille, and translate it back we would get a12233. 
Additionally, trailing spaces are trimmed and it is assumed that "AAA" is the same as "AAA ".


## Future Improvements

- Add support for additional punctuation marks
- Implement a graphical user interface (GUI)
- Extend support for different Braille standards
- Add unit tests for better code coverage
