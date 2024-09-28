# Python Instructions

Note that the Python version used is 3.8

# Notes & Assumptions for Reviewer

Interpret input as Braille if all of the following are met:

1. input string has no spaces, only `O` and `.`
2. input string has both `O` characters and `.` characters
3. input string has length a multiple of 6

Braille to alphabet character mapping:

- dynamically generated based on Braille design
- realistically retrieve as a resource

`decimal follows` character:

- Interpretation varies across Braille systems, interpreting as English system where this character means the decimal point `.`

`numbers follow` character:
While in "numbers" mode, only digits and decimal point are allowed. Anything else will cause the program to exit number mode and interpret the braille as possibly a letter or a symbol.

Input forms:

- Assuming Braille and English inputs characters will only be of the ones in [[braille.jpg]]

Other notes:

- Some symbols have the same braille as a letter. In this case the program always inteprets it as a letter as per the challenge description. Realistically, this program would be more context sensitive and decide whether to use a symbol or a letter depending on surrounding characters.

Files:

- `cutsom_test_cases` contains test cases used in `custom_tests`
- `custom_tests` is a custom test script
  - prints `yay` if test passed
- `translator.py` is main translation function
- `dictionary.py` stores the English/Braille dictionary
