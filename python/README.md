# Python Instructions

Note that the Python version used is 3.8

# Braille Translator
This repository has two Python scripts: `translator.py` for converting text between Braille and the English alphabet, and `translator.test.py` for testing these conversions.

# Files
translator.py:

Command-line tool to translate English text to Braille and vice versa. Currently only supports the entire English alphabet, space, and digits 0-9 `[A-Za-z0-9 ]`.

Usage:
```
python translator.py <input_string>
```
Translates English text to Braille or Braille to English text.

translator.test.py:

Contains unit tests to ensure accurate translation between Braille and English.

Usage:
```
python translator.test.py
```