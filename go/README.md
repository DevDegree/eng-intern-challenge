# Go Instructions

This is a simple Braille translator written in Go. It can convert text to Braille and Braille to text.

## How to Use

1. Make sure you have Go installed on your system.


3. Run the translator using one of these commands:

   - To translate text to Braille:
     ```
     go run translator.go Hello world
     ``` 
    

  

   - To translate Braille to text:
     ```
     go run translator.go .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
     ```

4. The translated output will be printed to the console.

Note: When using special characters (like `!`, `@`, `#`), enclose your input in single quotes:

```
go run translator.go '!@#$%^&*()'
```

That's it! You can now use this tool to translate between text and Braille.

## How It Works

The Braille translator operates based on the following principles:

1. **Braille Representation**: Each Braille character is represented by a 6-character string of 'O' and '.'. For example, 'a' is "O.....".

2. **Character Mapping**: The program uses two maps to store the Braille representations of letters and numbers.

3. **Text to Braille**:
   - The program iterates through each character in the input text.
   - For capital letters, it adds the capital symbol (".....O") before the letter's Braille representation.
   - For numbers, it adds the number symbol (".O.OOO") before the first number in a sequence.
   - It then adds the Braille representation of each character to the output.

4. **Braille to Text**:
   - The program reads the input Braille string in 6-character chunks.
   - It identifies special symbols for capitals and numbers.
   - It then matches each 6-character Braille representation to its corresponding letter or number.
   - The program handles capitalization and number sequences based on the special symbols it encounters.

5. **Input Detection**: The program automatically detects whether the input is text or Braille based on whether it consists only of 'O' and '.' characters and has a length divisible by 6.

This design allows the translator to handle both directions of translation (text to Braille and Braille to text) in a single program, making it versatile and easy to use.

