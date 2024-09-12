# Python Instructions
## Overview

The Braille Translator is a Python script that translates text to Braille and Braille to text. The translation uses a configurable mapping, allowing customization for different Braille systems and special symbols. The script can handle standard text, numbers, and special symbols, with support for capital letters and decimal points.

## How to run
python3 translator.py "<input_string>"

## Features

- **Braille to Text Translation:** Converts Braille characters (represented as strings of 'O' and '.') into readable text.
- **Text to Braille Translation:** Converts readable text, including numbers and special symbols, into Braille representation.
- **Supports Capital Letters and Decimals:** Special handling for capitalization and decimal points.

## Requirements

- Python 3.x
- A configuration file in JSON format to define Braille mappings

## Configuration File

The script requires a JSON configuration file named `braille_config.json`. This file should include mappings for:
- **alphabet:** Braille representations for letters (a-z)
- **numbers:** Braille representations for digits (0-9)
- **special:** Braille representations for special symbols (e.g., space, number indicator, capital letter indicator, decimal indicator)

Here is an example configuration:

```json
{
  "alphabet": {
    "a": "O.....",
    "b": "O.O...",
    ...
  },
  "numbers": {
    "0": "O..O.O",
    "1": "O....O",
    ...
  },
  "special": {
    "space": "......",
    "number_indicator": "O..O..",
    "capital": "O...O.",
    "decimal_indicator": "O..O.O",
    ".": "......"
  }
}
Note that the Python version used is 3.8
