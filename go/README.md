# Go Instructions

Here's a concise `README.md` for your project:

---

# Braille Translator

A simple command-line tool for translating between English text and Braille representations.

## Features

- **English to Braille Translation:**
  - Converts English characters (including numbers and capitalization) into Braille.
  - Handles special sequences for capitalization and numbers.

- **Braille to English Translation:**
  - Converts Braille representations back to English text.
  - Supports capitalization and numbers.

## Usage

### Translating English to Braille

```sh
go run translator.go "Hello World 123"
```

**Output:**
```
.....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.........O.OOOO.....O.O...OO....
```

### Translating Braille to English

```sh
go run translator.go ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.........O.OOOO.....O.O...OO...."
```

**Output:**
```
Hello World 123
```

## Installation

Clone this repository and run the `translator.go` file using Go.

```sh
go run translator.go "Your text here"
```

## Test

You can run the included test by running
```sh
go test
```

## Note

- This tool uses correct Braille representations for numbers based on standard mappings. If your use case involves specific test cases or different mappings, you may need to adjust the `numberToBraille` map.

