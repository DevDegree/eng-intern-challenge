# Braille Translator

## Author

Emilio Andere

## Description

Command-line application for bidirectional translation between English and Braille.

## Features

- Auto-detects input type (English/Braille)
- Supports entire English alphabet, numbers 0-9, capitalization, and spaces
- Braille represented as 'O' (raised dot) and '.' (flat dot)

## Architecture

1. Input Processor: Determines input type
2. Translator: Performs bidirectional translation
3. Output Formatter: Formats translated text

## Flow

1. Parse args
2. Determine input type
3. Translate
4. Format output
5. Print result

## Usage

```
python translator.py <input_string>
```

## Example usage

```
python translator.py "Hello world"
python translator.py ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
```
