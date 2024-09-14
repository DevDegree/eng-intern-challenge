# Python Instructions

Note that the Python version used is 3.8

# Braille Translator

## Feature

- Covert English to Braille
- Convert Braille to English
- Support for letter, number, and punctuation
- Handle capital letters

## Usage

To run the Braille Translator, you need to run the following command:

```bash
python3 translator.py <english_or_braille_string>
```

Where `english_or_braille_string` is the string you want to translate.

## Example

### english to braille

```bash
python3 translator.py Hello World
```

Output:

```
Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```

### braille to english

```bash
python3 translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```

Output:

```
Output: Hello world
```
