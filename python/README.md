# Python Instructions

Note that the Python version used is 3.8

# Braille Translator
# Description
This project implements a terminal/command-line application that can translate between Braille and English (and vice versa). The application automatically detects whether the input is in English or Braille and translates accordingly.

For Braille, raised dots are represented as O, and flat ones are represented as . in a 6-character cell, arranged left-to-right, top-to-bottom.

# The translator can handle:

Letters (a-z)
Numbers (0-9) with a "number follows" symbol
Capital letters with a "capital follows" symbol
Spaces
Usage

# How to Run the Application:
To translate between Braille and English, run the following command:

bash
Copy code
python3 translator.py <input_string>
The input string will be automatically detected as either Braille or English and translated accordingly.

# Example Usage:
English to Braille:
bash
Copy code
python3 translator.py "Hello World 123"
Output:

mathematica
Copy code
.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
Braille to English:
bash
Copy code
python3 translator.py ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
Output:

Copy code
Hello World 123

# Notes:
Capital Letters: The "capital follows" symbol (.....O) is used to denote that the next letter is capitalized.
Numbers: The "number follows" symbol (.O.OOO) is used before any number sequence to indicate digits.
Spaces: Spaces are represented as ...... in Braille.
Testing
A unit test is provided in the file translator.test.py to verify the functionality of the translator.

# How to Run the Test:
Run the following command to execute the test:

bash
Copy code
python3 -m unittest translator.test.py
The test compares the output of translating the string Abc 123 xYz to the expected Braille result.

# Files
translator.py: The main file containing the implementation of the translator.
translator.test.py: Unit test file for testing the translator.
Braille Representation
Letters: The letters a-z are represented in Braille using a 6-dot matrix.
Numbers: Numbers are preceded by a "number follows" symbol and then use the Braille letters a-j to represent digits 1-9 and 0.
Capital Letters: The "capital follows" symbol is used to indicate that the next letter is capitalized.

# License
This project is open-source and available for use and modification.
