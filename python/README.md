# Eng Intern Challenge Fall - Winter 2025 - Python

Author: Suren Kulasegaram<br>
Email: surenkula24@gmail.com
## Thought Process
- I use a hashmap to map a Braille character code to it's equivalent English character and a second map with vice versa mapping
    - I do the same thing with numbers as well, because the numbers Braille character codes overlaps the character code for some of the English characters as well
- Using maps helps us efficiently find Braille <--> English mapping because of the O(1) look up time for a character

## Notes
- There's some minimal error handling but input must be alphanumeric and total length of braille input must be divisible by 3 (6 symbols per character)

## Instructions
- Open Terminal or any Command Line Interface
- Enter:
    - `python3 translator.py <input>`
    - Where \<input> is your desired input
- Program will assess input as Braille or English and output the translation of the opposite
