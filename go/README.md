# Go Instructions

This is a simple Braille translator written in Go. It can convert text to Braille and Braille to text.

## How to Use

1. Make sure you have Go installed on your system.


3. Run the translator using one of these commands:

   - To translate text to Braille:
     ```
     go run translator.go Hello world
     ``` 
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

