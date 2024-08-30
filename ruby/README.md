# Ruby Instructions

## Braille Translator

This project is a Braille translator written in Ruby. It provides a simple interface for converting English text to Braille and vice versa. The program supports uppercase letters, digits, and spaces, making it suitable for basic Braille translation tasks.

## Features

- **English to Braille Translation:** Converts English text, including uppercase letters and numbers, into Braille representation.
- **Braille to English Translation:** Converts Braille-encoded strings back into English text, recognizing uppercase letters and numbers.
- **Automatic Mode Detection:** Determines if the input is Braille or English and translates accordingly.

## Usage

### Command-Line Interface

To use the Braille translator from the command line, provide the text or Braille string as an argument:

```bash
ruby translator.rb "< braille/plain formatted text >"
```

Examples:

```bash
# Translate English text to Braille
ruby translator.rb "Hello 123"

# Translate Braille back to English
ruby translator.rb "O.....O.OO..O.O... .O.OOO .OO.....O"
```

### Output

The program will output the corresponding translation (either Braille or English text) directly to the console.

## Braille Mapping

### Alphabet Mapping

The translator supports the following Braille representations for lowercase English letters:

| Letter | Braille   |
|--------|-----------|
| a      | O.....    |
| b      | O.O...    |
| ...    | ...       |
| z      | O..OOO    |

Uppercase letters are prefixed with a special Braille character: `.....O`.

### Number Mapping

The translator supports the following Braille representations for numbers:

| Number | Braille   |
|--------|-----------|
| 1      | O.....    |
| 2      | O.O...    |
| ...    | ...       |
| 0      | .OOO..    |

Numbers are preceded by a special Braille character: `.O.OOO`.

## Requirements

- **Ruby**: Ensure you have Ruby installed on your machine. You can download Ruby from [ruby-lang.org](https://www.ruby-lang.org/en/downloads/).

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/braille-translator.git
```

2. Navigate to the project directory:

```bash
cd < project directory >
```

3. Run the translator with the following command:

```bash
ruby translator.rb "< braille/plain formatted text >"
```

## Testing

To test the functionality of the translator, you can use various text and Braille strings to ensure that both translations (English to Braille and Braille to English) work as expected.
