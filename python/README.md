# Braille - English Translator

This is a simple translator between English and Braille. It takes as input a text, detects whether it's in Braille or English and then prints out the translation. It contains some helper functions, especially for Braille to English to handle the special cases and then handle the conversion. Finally, a translate function takes as argument the input and returns the translation by calling on the other functions.

## Running the Program
Type in your argument through the command line.
```bash
python3 translator.py Hello world
```
## Assumptions

Braille is displayed as `O` and `.` where `O` represents a raised dot. The program is designed to handle the alphabet, numbers, and spaces. Additional characters would be invalid input.


