# Braille Translator

## Overview

This project is a coding challenge for the Shopify internship technical test. The challenge involves creating a command-line application that can translate between Braille and English. The application can handle both translation directions and supports the entire English alphabet, numbers 0 through 9, and spaces.

## Project Structure

- `translator.js`: The main script for translating between Braille and English.
- `translator.test.js`: The test file to ensure the correctness of the translation.
- `package.json`: Contains metadata about the project and dependencies.
- `README.md`: This file.

## Usage

### Running the Translator

To use the translator, run the `translator.js` script from the command line. You can pass either an English string or a Braille string as an argument. The script will automatically detect the input type and convert it to the opposite.

**Example:**

```bash
node translator.js "Hello world"
```

### Running Tests

To ensure everything is working correctly, you can run the tests using Jest. Run the following command:

```bash
npm test
```

## Code Explanation

**Braille Translation:** The translator.js script uses a mapping of Braille symbols to English characters and vice versa. It handles both translations and detects whether the input is in Braille or English.

**Testing:** The translator.test.js file uses Jest to test the functionality of the translator. It ensures that the correct output is produced for given inputs.