# Braille Translator - Python

## Overview

The Braille Translator is a Python program that translates between English text and Braille. The program can automatically detect whether the input is a string of alphabetic characters or a string of Braille symbols, and it translates accordingly. The program supports both uppercase and lowercase letters, numbers, and spaces.

## Features

- **Automatic Detection:** The program determines whether the input is a string of letters or Braille symbols and translates in the appropriate direction.
- **Support for Uppercase and Numbers:** The program handles uppercase letters and numbers by using special Braille symbols.
- **Error Handling:** The program raises a `ValueError` if the input contains invalid characters or if the Braille input is incorrectly formatted.

## Assumptions

- The program assumes that no multiple consecutive spaces are used in the input. For example, `"hello‎ ‎ ‎ ‎ ‎ ‎ world"` will be treated as `"hello world"` with a single space.

## Usage

To run the program, use the following command:

```bash
python translator.py <input>
```

## Examples

### Case 1: Translating Text to Braille

Input: `Hello world`
Output: `.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..`

### Case 2: Translating Numbers to Braille

Input: `42`
Output: `.O.OOOOO.O..O.O...`

### Case 3: Translating Braille to Text

Input: `.....OO.....O.O...OO...........O.OOOO.....O.O...OO....`
Output: `Abc 123`
