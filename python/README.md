# Braille Translator

This project implements a bidirectional Braille translator that can convert text to Braille and vice versa. It's designed to be efficient, extensible, and easy to use.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Descriptions](#file-descriptions)

## Project Structure

The project consists of the following Python files:

- `translator.py`: The main script that handles the translation process.
- `braille_state.py`: Implements the `BrailleState` class for Braille to text conversion.
- `text_state.py`: Implements the `TextState` class for text to Braille conversion.
- `braille_mappings.py`: Contains the mappings between Braille and English characters.
- `config.py`: Stores configuration variables.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/shruthigudimalla/eng-intern-challenge.git
   cd eng-intern-challenge/python
   ```

2. Ensure you have Python 3.8 or later installed.

3. No additional dependencies are required for basic functionality.

## Usage

You can use the translator via command line:

```
python translator.py [INPUT]
```

For example:
```
python translator.py Hello world
```

This will output the Braille representation of "Hello world".

To translate from Braille to text, simply input the Braille characters:

```
python translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```

This will output the text representation of the Braille input.

For verbose output, use the `-v` or `--verbose` flag:

```
python translator.py -v "Hello world"
```

## File Descriptions

### translator.py

This is the main script that orchestrates the translation process. It includes functions for both text-to-Braille and Braille-to-text translation, as well as a command-line interface.

### braille_state.py

This file contains the `BrailleState` class, which manages the state for Braille to text conversion. It handles the processing of Braille characters, including managing capitalization and number mode.

### text_state.py

This file contains the `TextState` class, which manages the state for text to Braille conversion. It processes text characters and converts them to their Braille representations, handling capitalization and number mode.

### braille_mappings.py

This file contains the mappings between Braille and English characters, as well as number mappings. These mappings are used by both the `BrailleState` and `TextState` classes.

### config.py

This file contains configuration variables, such as the set of valid Braille characters.
