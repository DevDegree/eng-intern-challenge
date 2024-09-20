# Braille Converter

### Overview

This project provides a bidirectional translator between English and Braille. You can convert standard English text to Braille or decode Braille back into readable English. The tool handles letters, numbers, and various punctuation marks, while automatically adjusting for capitalization and numeric modes.

## Installation

Make sure you have Ruby installed on your machine. If not, you can download it [here](https://www.ruby-lang.org/en/downloads/).

## Running the code

To run the code, open a terminal and go to the directory containing the file.

```
cd ruby
```

## Converting the English to Braille code

Run the following command:

```
ruby translator.rb <input>
```

Replace `<input>` with the string you want to convert.

```
ruby translator.rb hello
```

This will output the translation of the input string

```
O.OO..O..O..O.O.O.O.O.O.O..OO.
```

## Converting the Braille Code to English

Run the following command:

```
ruby translator.rb <input>
```

Replace `<input>` with the braille code you want to convert.

```
ruby translator.rb O.OO..O..O..O.O.O.O.O.O.O..OO.
```

This will output the translation of the input string

```
hello
```

### Contact info

- Email: aman.shah@uwaterloo.ca
- Phone: 2266669400
- LinkedIn: https://www.linkedin.com/in/askaman/
