# Braille Translator
The Braille Translator is a Python program designed to translate text between English and Braille. It provides functionality to convert English text into Braille and vice versa. This can be particularly useful for visually impaired individuals or anyone interested in Braille translation.

## Features
- **English to Braille**: Converts English characters, numbers, and punctuation into their Braille representation.
- **Braille to English**: Converts Braille patterns back into readable English text.
- **Handles Capitalization and Punctuation**: Supports translation of capital letters and various punctuation marks.

## Usage
To use the Braille Translator, you need to provide an input text via the command line. The program will determine whether the input is in English or Braille and perform the appropriate translation.

### Command Line Usage
1. Save the code to a file named `braille_translator.py`.
2. Run the script from the command line, passing the text you want to translate as an argument.
   ```bash
   python braille_translator.py "Your text here"

## Functions
### english_to_braille(text)
**Converts English text to Braille.**
Parameters: text (str) - The English text to be converted.
Returns: Braille representation of the text.

### braille_to_english(text)
**Converts Braille text to English.**
Parameters: text (str) - The Braille text to be converted.
Returns: English representation of the Braille text.

### translate(text)
**Determines if the input is in Braille or English and performs the appropriate translation.**
Parameters: text (str) - The text to be translated.
Returns: Translated text in the opposite format.

## Deployment
Deployed Web Application on Hugging Face Spaces
`https://huggingface.co/spaces/nooshinbah/Braille_Translator/blob/main/app.py`
Google Colab Notebook
`https://colab.research.google.com/drive/1W0CYFKUmurPZXcaNftj7qMP0zjvaQpsB?authuser=0#scrollTo=rzCg4XTTntuZ`

## Requirements
Python3
No external libraries are required.

## Author
Created by **Nooshin Bahador**. For any questions or issues, please contact `nooshin.bah@gmail.com`.