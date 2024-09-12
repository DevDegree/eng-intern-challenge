---

# Braille Translator CLI

Application Email: m4mehra@uwaterloo.ca

## Overview

The Braille Translator is a command-line tool that translates between English and Braille. It automatically detects the input language and provides the corresponding translation. This tool was developed as part of the Shopify Eng Intern Challenge and supports both English to Braille and Braille to English conversions.

## Features

- **Automatic Language Detection**: Input can be either Braille or English, and the tool will automatically identify and translate it.
- **Full Support for Basic Braille**: Handles letters (A-Z), digits (0-9), and special Braille characters (Capital and Number indicators).
- **Debug Mode**: Enable detailed logging to troubleshoot and understand the translation process. 

## Usage
Run the tool directly using the Python interpreter:
    ```sh
    python translator.py Text to translate
    ```

### Basic Usage

To translate text, pass the text as an argument:
```sh
python translator.py Hello World
```
This will output the Braille translation of "Hello World".

### Translating Braille to English

To translate Braille to English:
```sh
python translator.py .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
```
This will output the English translation.

### Enabling Debug Mode

For more detailed output and debugging information, use the `--debug` or `-d` flag:
```sh
python translator.py -d Hello World
```

### Command Line Options

- `input_text_to_translate` - The text you want to translate (required).
- `-d` or `--debug` - Enables debug logging for detailed output.

## Error Handling

The tool will raise a `TranslationError` if the input text contains unsupported characters or if there is an error in the Braille format.

# Future Improvements:
- Break project down into seperate modules/classes and add testing for each component ie Logger, Translator, Languages etc
- Create a script to take csvs or images like braille.jpg of langauge symbols to braille mappings and convert them into dictionaries to simplify support of new languages/chars

:)

Made Email Public on github.
---