# Python Instructions

Note that the Python version used is 3.8 

This Python script provides a tool for translating between English text and Braille. The translated text will be printed to the console.
The script will automatically detect the input format (Braille or English) and translate accordingly. 
Detection is done through initial assumption of input string as Braille and translate into English. 
If the translation is not possible then the script assumes it is English to be translated into Braille.

## Installation
There are no external dependencies to install.

## Usage
Translate from Braille to English:
python3 translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO...O..............O.OOO.OO..OO.O.OOO.O.O.O.OO.O....OOO.
Translate from English to Braille:
python3 translator.py Hello, World!


## Assumptions
<p align='center'>
  <img src='./braille.jpg' alt='Braille Alphabet' />
</p>
1. Only above characters are supported in translation
2. Alphabet "o" and symbol ">" have the same Braille translation; typically readers gauge based on context. For this script, symbol ">" has been included only preceded by a "number follows" Braille. 
3. Multiple arguments are assumed to be English input. Each input are assumed to be seperated by " " (Space symbol). 

