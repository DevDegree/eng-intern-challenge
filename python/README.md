# Eng Intern Challenge Fall - Winter 2025 - Python

Author: Suren Kulasegaram<br>
Email: surenkula24@gmail.com

## Personal Thought Process 
- I use a hashmap to map a Braille character code to it's equivalent English character and a second map with vice versa mapping
    - I do the same thing with numbers as well, because the numbers Braille character codes overlaps the character code for some of the English characters as well
- Using maps helps us efficiently find Braille <--> English mapping because of the O(1) look up time for a character
- To handle capitals and numbers follow code, I used flags to signal that we need to need to treat the current character or the following character with more care
- sys module was imported so that we can handle sub arguments when starting the program


## Notes
- Note that the Python version used is 3.8
- There's some minimal error handling but input must be alphanumeric and total length of braille input must be divisible by 3 (6 symbols per character)

## Overview
This program translates text between English and Braille. It supports both alphabetic characters and numbers, allowing for seamless conversion in either direction.

## Features
- Converts English text to Braille.
- Converts Braille to English text.
- Supports uppercase letters and numeric representation.
- Uses a simple text-based representation for Braille.

## Installation
- Ensure you have Python 3.x installed.
- Download or clone this repository.
- Navigate to the project directory in your terminal.

## Instructions
- Open Terminal or any Command Line Interface
- Enter:
    - `python3 translator.py <input>`
    - Where \<input> is your desired input
- Program will assess input as Braille or English and output the translation of the opposite

## Examples
- To translate English to Braille:
    - input: `python3 translator.py Hello world`
    - output: `.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..`
- To tranlsate Braille to English:
    - input: `python3 translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..`
    - output: `Hello world`

