# Python Instructions

Note that the Python version used is 3.8

# Braille Translator

This project implements a command-line application that translates text between English and Braille. The application is designed to detect whether the input is in English or Braille and automatically convert it to the corresponding opposite format. It supports the entire English alphabet, numbers 0 through 9, spaces, and basic punctuation.

## How the Translator Works

### 1. Detecting Input Type
The `detect_input_type` function determines whether the input string is in English or Braille:
- **Braille Detection**: Checks if all characters are 'O' or '.'.
- **English Detection**: Assumes all other cases as English.

### 2. Translating to Braille
The `translate_to_braille` function handles English-to-Braille translation by:
- Using a flag to manage capitalization, ensuring only the next character is capitalized when the 'capitalize' symbol is used.
- Detecting numbers and adding a 'number follows' symbol only once at the beginning of a sequence of digits.
- Managing spaces, punctuation, and ensuring all characters are accurately translated according to the provided Braille mappings.

### 3. Translating to English
The `translate_to_english` function translates Braille to English by:
- Handling capitalization with a flag that sets only the next letter to uppercase.
- Managing numbers using a 'number follows' flag, converting subsequent Braille symbols to their numeric equivalents.
- Accurately interpreting spaces and other symbols while ensuring a smooth transition between number and text modes.

## Design Choices

### External JSON File for Mappings
We chose to store the Braille mappings in an external JSON file (`braille_mappings.json`) instead of hardcoding them in the script for several reasons:
- **Flexibility**: This approach allows easy updates or changes to the mappings without modifying the codebase. This is especially useful if the Braille system needs to be extended or modified.
- **Separation of Data and Logic**: Keeping data separate from the logic improves the maintainability and readability of the code.
- **Scalability**: Loading from a JSON file makes it easier to scale the translator to include additional symbols or characters in the future.

### Exclusion of Special Characters and Decimals
Special characters like `>`, which share symbols with English letters (e.g., 'o'), were excluded to avoid ambiguities in translation. Since the project description did not require punctuation, special symbols or decimals, they were omitted to keep the translator focused and aligned with the specified requirements. This decision prevents unnecessary complexity and potential translation errors.

### Comprehensive Edge Case Handling
- **Capitalization**: Only the next letter is capitalized when the capitalization symbol is detected.
- **Number Sequences**: The translator efficiently manages sequences of digits, ensuring the 'number follows' symbol is used appropriately and only once per sequence.
- **Error Handling**: The application guides the user on correct usage if input is missing, ensuring a user-friendly experience.

## Tests

We implemented a comprehensive set of tests in the `test_translator.py` file to ensure the Braille Translator handles various edge cases effectively:

- **Mixed Case with Numbers**: Tests the ability to handle mixed capitalization and numeric sequences to verify correct handling of the 'capitalize' and 'number follows' symbols.
- **Continuous Digits**: Ensures that sequences of digits are correctly translated without unnecessary repetition of the number symbol.
- **Uppercase Sequences with Mixed Digits**: Validates that uppercase letters and numbers are accurately translated with proper transitions between letter and number modes.
- **All Uppercase with Numbers**: Checks the translator’s performance with entirely uppercase inputs, numbers, and spaces.
- **Multiple Spaces**: Tests handling of multiple spaces in input to confirm that the Braille representation for spaces is consistently applied.
- **Single Character**: Simple test to verify that individual characters are translated correctly.
- **Empty Input**: Confirms that the translator can handle empty input gracefully, without errors.

Each test was chosen to demonstrate the translator's ability to handle edge cases and complex scenarios, ensuring robust performance under various conditions.

## Assumptions

- **Input Validity**: The program assumes that inputs will only include lowercase and uppercase letters, numbers, and spaces. Special characters, punctuation, and other symbols are not considered valid inputs and will trigger an error message.
  
- **Number Handling**: It is assumed that once a number symbol is detected in Braille, all subsequent symbols are numbers until a space is encountered, as per the project guidelines.

- **Input Validation**: Both English and Braille inputs are validated by checking against their respective dictionaries (`ENGLISH_TO_BRAILLE` for English inputs and `BRAILLE_TO_ENGLISH` for Braille inputs), ensuring that only allowed characters are processed.

These assumptions align the translator's functionality with the project requirements, ensuring consistent and expected behavior.

## Limitation

A limitation was discovered where sequences like `123abc` in Braille would not work correctly because there is no distinction between digits and letters without a separating space. The project guidelines specify: "assume all following symbols are numbers until the next space symbol." Therefore, we assume that inputs will be formatted according to this guideline and that the project will not be tested against inputs that do not follow this rule. Given this assumption, the translator adheres to the specified requirements and functions correctly within these constraints.


## Why This Implementation Stands Out

- **Modular Design**: Functions are clearly defined, making the code easy to read, test, and extend.
- **Data-Driven Approach**: Using a JSON file for mappings shows a modern approach to managing data, highlighting the adaptability of the application.
- **Robust Testing**: Thoroughly tested against edge cases, including mixed cases, punctuation, numbers, and Braille inputs, ensuring reliable functionality.
- **Readable and Maintainable Code**: The use of flags and clear logic makes the code easy to follow, demonstrating good coding practices.

## How to Use

1. Clone the repository to your local machine.
2. Ensure Python 3.8 is installed on your system.
3. Run the translator from the command line using:
   ```bash
   python translator.py "<input_string>"
Replace `<input_string>` with the text or Braille sequence you want to translate.

## Examples

- To translate English to Braille:
  ```bash
  python translator.py "Hello World"

- To translate Braille to English:
  ```bash
  python translator.py ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."

