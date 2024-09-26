# Braille Translator

## Overview
This project is a **Braille-to-English** and **English-to-Braille** translator written in Python. It allows users to input either Braille code or English text, and it translates it into the corresponding form. The program supports:
- Translation of lowercase and uppercase letters.
- Support for numbers and basic punctuation.
- Recognition of Braille control characters like capitalization and number symbols.

## Features
- **Braille to English**: Translates a string of Braille code (represented with `O` for raised dots and `.` for unraised dots) into English.
- **English to Braille**: Translates a string of English text (letters, numbers, spaces) into Braille.
- **Supports Uppercase and Numbers**: The translator can handle capitalization and numerical values using appropriate Braille control characters.

## Usage
### Running the Translator
To run the translator, provide either Braille or English input as a command-line argument.

### 1. **Translate English to Braille**
Run the following command to translate an English sentence to Braille:

python braille_translator.py "Hello World"
Example output:
".....O.OO...O...........O..O.O"

### 2. ** Translate Braille to English **
To translate Braille to English, input the Braille characters (using O for raised dots and . for unraised dots):

python braille_translator.py "O..... O.O... OO...."
Example output: 
abc

## Supported Inputs
### 1. English Input: Any string of English letters (both lowercase and uppercase), numbers, and spaces.
### 2. Braille Input: Any string of Braille characters using O for raised dots and . for unraised dots. Each Braille character is represented by 6 characters (e.g., O.....).

## Error Handling
The program will return an error message in the following cases:

### 1. Invalid characters for either Braille or English input.
### 2. Incorrect Braille format.