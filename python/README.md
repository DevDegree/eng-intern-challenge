# Python Instructions

Note that the Python version used is 3.8

# Dev Degree
## Braille Converter
## Brandon Rose
### Steps for Project

1) Create a dictionary for english to braille 
   - The keys are english characters, and the values are braille equivalents
  
2) Take system argument as a terminal input 
3) Create a function that:
   - Parses through the string using Regular Expressions (ReGex)
   - Identify if the string reflects braille or standard english
   - Trigger a boolean that will tell if the string is braille or not
   - Use a conditional statement to trigger one of two functions, based on if braille = True for user input
4) Create two functions that are triggered by braille check function
   1) Function to convert English to Braille, if braille condition is False
      - ```newstring = ''```
      - Check each character in the user input sequentially
      - Conditional check for character types:
          - if character is uppercase, add ```brailledict['cf']``` to the string 
              - then add the braille equivalent of the ```character.lower()``` to the string
          - if the character is a digit, add ```brailledict['nf']``` to the string
              - then add the braille equivalent of the number to the string
          - if the character is a space, add ```brailledict[' ']``` to the string
          - else add the braille equivalent of the character to the string
      - When the function completes its iteration through the input string, return ```newstring```
   2) Function to convert Braille to English, if braille condition is True
      - ```newstring = ''```
      - Check batches of 6 characters in the user input, sequentially
      - Compare each batch of characters with the values in ```brailledict```
          - if the corresponding key is 'cf'
              - Make the next character added to ```newstring``` a capital
          - if the corresponding key is 'nf'
              - Any characters added to newstring are keys that pass an ```isdigit()``` check, end this condition when the next key added is ```' '```
          - else add the corresponding key from brailledict to ```newstring```
      - when the function completes its iteration through the input string, return ```newstring```
      
5) Encase these steps in an overarching function that will compile all results into a list, and compact the list elements into one seamless string.

6) Return resulting string to terminal output

### Research notes
In order to convert from braille back to english, we will need to swap the dictionary. 
The general rule of thumb for reversing dictionaries is to use python comprehension.

```dict_swap = {v: k for k, v in brailledict.items()}```

This will be more difficult than the english to braille function, as we will have instances of repeating keys during the key:value inversion. The best way to compensate for that would be to convert the singular dictionary into multiple, for both numerical braille and alphabetical braille respectively:

Python can check for data type in strings, so we would have to use ```is_alpha()``` and ```is_digit()``` in our new dictionary comprehensions:

```letters_to_braille = {k: v for k, v in brailledict.items() if k.isalpha()}
numbers_to_braille = {k: v for k, v in brailledict.items() if k.isdigit()}```

And vice versa. This allows for us to call the specifically required dictionary for the task at hand