# Python Instructions

Note that the Python version used is 3.8


## Status Overview

- Satisfied all the instruction requirements
- passed the translator.test.py
- passed the unit tests created personally (not included in the branch)
- passed the examples given in the instruction

## Code Structure

### `translator.py`

This file contains the main logic for the translator, including:
- `is_braille()`: Determines if the input is Braille based on the characters.
- `braille_to_text()`: Converts Braille input to English text.
- `text_to_braille()`: Converts English text to Braille.
- `main()`: Handles input processing and calls the appropriate translation function.


## Features

- **English to Braille**: Converts regular English text (including capital letters, numbers, and spaces) into Braille.
- **Braille to English**: Converts Braille symbols (using `O` for raised dots and `.` for flat dots) into regular English text.
- **Automatic Input Detection**: Automatically determines if the input is in English or Braille and converts it accordingly.
- **Support for Numbers and Capitalization**: Special Braille symbols are used to indicate numbers (`.O.OOO`) and capital letters (`.....O`).

## Usage

### Running the Program

To run the Braille Translator, open your terminal and navigate to the directory where the `translator.py` file is located. Then run the following command:

```bash
python3 translator.py <text here>
```

### Input Examples

#### Example 1: English to Braille

```bash
python3 translator.py "Hello world 123 xYz"
```

**Expected Output (Braille):**

```
.....OO.OO..O..O..O.O.O.O.O.O.O..OO.......O.OOOO.O..O.O.....OO.O..OOO.OOOO..OOO
```

#### Example 2: Braille to English

```bash
python3 translator.py ".....OO.OO..O..O..O.O.O.O.O.O.O..OO.......O.OOOO.O..O.O.....OO.O..OOO.OOOO..OOO"
```

**Expected Output (English):**

```
Hello world 123 xYz
```

### Handling Special Symbols

1. **Numbers**: Braille uses a special symbol `.O.OOO` to denote that the following characters are numbers. This symbol is inserted only once before the numbers in a sequence.
   
2. **Capital Letters**: A capital letter in Braille is preceded by the symbol `.....O`. This is used once per capital letter.

3. **Spaces**: Braille uses `......` to represent a space between words, which the program also supports.


