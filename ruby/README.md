# Braille Converter

### Overview

This Ruby application translates English text to Braille and vice versa. The application uses predefined mappings for English characters, Braille characters, and control codes (for capitalization, numbers, and punctuation).

### Command Line Execution

To run the application from the command line:

```shell
ruby braille_converter.rb "Your input text here"
```
### Examples

- **English to Braille**:

```shell
>> ruby braille_converter.rb "Hello world"
>> .....O.O.....O.O..OOO..O..O....O..O......O...O..OO...O..O......
```

- **Braille to English**:

```shell
>> ruby braille_converter.rb ".....O.O.....O.O..OOO..O..O....O..O......O...O..OO...O..O......"
>> Hello, World!

```

### Run tests

- Run tests by running

``` shell
>> rspec translator.test.rb 
```
### Code Structure

- `ENGLISH_TO_BRAILLE_MAP`: Maps English letters, numbers, and punctuation to their Braille equivalents.
- `BRAILLE_TO_ENGLISH_MAP`: Inverts the Braille map for reverse conversion.

### Functions:

- **`english_to_braille(string)`**: Converts an English string into its Braille equivalent.
- **`braille_to_english(string)`**: Converts a Braille string back into English text.
- **`check_if_input_english(user_input)`**: Determines if the input is in English or Braille based on pattern matching.
- **`main`**: The main function that integrates input detection and conversion.

### Contact info

- Email: khush.patel@uwaterloo.ca
- Phone: 4319988848
- LinkedIn: https://www.linkedin.com/in/khush-patel-uw/