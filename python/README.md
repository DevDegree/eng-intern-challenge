### README

---

### Omer Adeel (oadeel@uwaterloo.ca) - Submission for Shopify 2025 Engineering Intern Challenge

---

## Overview

This Python script converts English text to Braille and vice versa. It handles both capital letters and numbers by using appropriate Braille indicators. The script can automatically determine whether the input is in English or Braille and perform the correct conversion.

## Features

- **English to Braille Conversion:**
  - Converts lowercase and uppercase letters to Braille.
  - Handles numbers by converting them to corresponding Braille patterns with a number indicator.
  - Supports spaces between words.
  
- **Braille to English Conversion:**
  - Converts Braille patterns back to English text.
  - Handles capitalization and numbers by interpreting the appropriate Braille indicators.
  - Supports spaces between words.

## Usage

To run the script, use the following command in your terminal:

```bash
python3 translator.py [input_text]
```

- **`[input_text]`**: The text you want to translate. It can be either English text or a Braille string consisting of 'O' (dots) and '.' (spaces).

### Examples

1. **Convert English to Braille:**

    ```bash
    python3 translator.py "Hello World"
    ```

    Output:

    ```
    .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
    ```

2. **Convert Braille to English:**

    ```bash
    python3 translator.py ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
    ```

    Output:

    ```
    Hello World
    ```

## Code Explanation

### 1. **Dictionaries:**

- **`ALPHA_TO_BRAILLE`:**
  - Maps each letter, digit, and special indicator (capitalization, number) to its corresponding Braille pattern.

- **`BRAILLE_TO_ALPHA`:**
  - Reverse mapping of `ALPHA_TO_BRAILLE`, converting Braille patterns back to letters and digits.

- **`ALPHA_TO_NUM` and `NUM_TO_ALPHA`:**
  - These mappings help convert between alphabetic letters and digits for the Braille translation of numbers.

### 2. **Functions:**

- **`english_to_braille(text)`:**
  - Converts English text to Braille. Handles capitalization and numbers by adding appropriate indicators before translating the characters.

- **`braille_to_english(braille)`:**
  - Converts Braille patterns back to English text. Handles capital letters and numbers by interpreting the Braille indicators and converting them accordingly.

- **`determine_mode(input_text)`:**
  - Determines whether the input is in English or Braille by checking the content and length of the string.

### 3. **Main Execution:**

- The script reads input from the command line, determines the mode (English or Braille), and then prints the converted result.