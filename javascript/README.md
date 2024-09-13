# Braille Translator

A simple Braille translator that converts English text to Braille and vice versa. The translator supports handling uppercase letters, numbers, and basic punctuation, providing a clear and efficient way to translate Braille to English and English to Braille using predefined mappings.

## Features

- **Translate English to Braille**: Converts English text to its Braille representation.
- **Translate Braille to English**: Converts Braille input back into readable English text.
- **Handles Uppercase Letters**: Automatically adds capitalization indicators in Braille.
- **Supports Numbers**: Includes number mode for translating numbers.
- **Basic Error Handling**: Validates Braille input for correct formatting.

## Getting Started

### Prerequisites

- Node.js installed on your system.
- A code editor such as VSCode for editing files.

### Installation

1. **Clone the repository**:

2. **Install dependencies** (if there are any; update this step if you add dependencies):
   ```bash
   npm install
   ```

### Usage

1. **Run the translator**:

   You can use the command line to translate text between English and Braille.

   ```bash
   node translator.js "Your text here"
   ```

   - **For English to Braille**: Input English text, e.g., `node translator.js "Hello World"`
   - **For Braille to English**: Input Braille text using `O` and `.` notation, e.g., `node translator.js "O.....O.O..."`

2. **Example Commands**:

   - Translate English to Braille:

     ```bash
     node translator.js "Abc 234"
     ```

     Output: `.....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..`

   - Translate Braille to English:
     ```bash
     node translator.js ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
     ```
     Output: `Hello world`

### Notes on Testing

- **Numbers Test Error**: During testing, it was observed that there was an inconsistency in the handling of numbers according to the test requirements. The implementation was adjusted to align with the visual representation provided in the picture, ensuring consistency in number handling between English and Braille translations. This issue has now been resolved.

### Project Structure

- `translator.js`: Main file containing the logic for translating between English and Braille.
- `brailleDictionary.js`: Contains mappings for letters, numbers, and special Braille characters.
- `validation.js`: Contains functions for validating Braille input.
- `utils.js`: Utility functions for common tasks, such as checking character types and finding keys in objects.

### Code Overview

- **`detectInputType(input)`**: Determines if the input is Braille or English based on the characters used.
- **`translateToBraille(text)`**: Converts English text to Braille.
- **`translateToEnglish(braille)`**: Converts Braille text to English.
- **`validateBrailleInput(braille)`**: Validates that the Braille input is properly formatted.
- **`splitIntoBrailleCells(braille)`**: Splits a Braille string into cells for processing.
- **Helper functions**: `isDigit`, `isUppercase`, and `findCharacterInMap` are used for checking character types and finding Braille mappings.

### Future Enhancements

- **Extend punctuation support**: Add more Braille mappings for special symbols.
- **GUI version**: Develop a graphical user interface to make the translator more user-friendly.
- **Audio output**: Provide audio feedback for Braille translations.
