# Braille Translator

A simple command-line application that translates text between English and Braille.

## Installation

1. Clone the repository or download the `translator.py` file.
2. Ensure you have Python installed on your system (Python 3.x is recommended).

## Usage

To use this app, run the following command:

```bash
python translator.py <text>
```

Replace `<text>` with the text you want to translate. The app will automatically detect if the input is in Braille or English and perform the appropriate translation.

## Examples

### English to Braille

**Input:**
```bash
python translator.py Hello world
```
**Output:**
```bash
.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```

### Braille to English

**Input:**
```bash
python translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```
**Output:**
```bash
Hello world
```

## Translation Rules

<p align='center'>
  <img src='../braille.jpg' alt='Braille Alphabet' />
</p>
<p align='center'>
  <em style='font-size:xx-small;'>Black dots represent raised areas</em>
</p>

- **Braille Representation:** Braille characters are represented using six-dot patterns where 'O' indicates a raised dot and '.' represents a flat dot.
  - Braille symbols are a 6 character string read left to right, line by line, starting at the top left.  
- **Special Characters:**
  - Capital letters are prefixed with the Braille capital symbol: `.....O.`
  - Numbers are prefixed with the Braille number symbol: `.O.OOO.`
    - A sequence of numbers will be followed by a space symbol: `......`

## Supported Characters

- English Letters (A-Z, a-z)
- Numbers (0-9)
- Space between words or numbers
