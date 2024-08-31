# Braille Translator
A Ruby-based Braille translator that converts English text to Braille and vice versa. It supports uppercase letters, digits, and spaces, making it suitable for basic Braille translation tasks.

## Features
English to Braille Translation: Converts English text, including uppercase letters and numbers, into Braille.
Braille to English Translation: Converts Braille-encoded strings back into English text, recognizing uppercase letters and numbers.
Automatic Mode Detection: Automatically determines if the input is Braille or English and translates accordingly.
Usage
Command-Line Interface
To use the Braille translator from the command line, provide the text or Braille string as an argument:

ruby translator.rb "<braille/plain formatted text>"

## Examples:

### Translate English text to Braille
ruby translator.rb "Hello 123"

### Translate Braille back to English
ruby translator.rb "O.....O.OO..O.O... .O.OOO .OO.....O"

### Output
The program outputs the corresponding translation (either Braille or English text) directly to the console.

Braille Mapping
Alphabet Mapping
The translator supports the following Braille representations for lowercase English letters:

| Letter | Braille   |
|--------|-----------|
| a      | O.....    |
| b      | O.O...    |
| ...    | ...       |
| z      | O..OOO    |

Uppercase letters are prefixed with a special Braille character: .....O.

Number Mapping
The translator supports the following Braille representations for numbers:

| Number | Braille   |
|--------|-----------|
| 1      | O.....    |
| 2      | O.O...    |
| ...    | ...       |
| 0      | .OOO..    |

Numbers are preceded by a special Braille character: .O.OOO.

## Requirements
Ruby: Ensure Ruby is installed on your machine. Download Ruby from ruby-lang.org.
Installation
Clone the repository:
git clone https://github.com/DevDegree/eng-intern-challenge.git

Navigate to the project directory:
cd braille-translator

Run the translator:
ruby translator.rb "<braille/plain formatted text>"

Testing
Test the translator’s functionality using various text and Braille strings to ensure both translations (English to Braille and Braille to English) work as expected.