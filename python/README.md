# Python Instructions

Note that the Python version used is 3.8

## Braille Translator
## Chen Xu
### Project implementation steps:

1. Create a dictionary that map English to Braille:
    - key - value pair many-to-one relation. Namely, different English symbol could map to the same Braille code

2. Based on the observation from previous step, 3 dictionaries map Braille to English are claimed:
    - Braille to number
    - Braille to letter
    - Braille to other marks or indicator: space, period (dot), capital indicator, number indicator

3. Implement a function that translate Braille to English:
    - Read very 6 characters as a pattern which is the Braille code that needs to be translated.
    - Use boolean isNum and isUpper to store the status of current iteration.
    - Check the category of the pattern: alphabet, number or other (space, capital indicator etc)
        a) Check non-numeric and non-alphabetical case: space, period, capital indicator, number indicator. And look up braiToOther for translation.
        b) If isNum is True, using braiToNum to translate the Braille code
        c) Otherwise, it is a alphabet. Using BraiToAlp for translation. Note that if isUpper is True, append upper case letter to the result and set isUpper back to False. 

4. Implement a function that translate English to Braille:
    - Use boolean isNum to determine whether we should put a number indicator into the result. If a number is detected:
        a) isNum == False, append the Braille code corresponding to "number follows" to the result and set isNum = True
        b) isNum == True, directely append the Braille code for that number.
        c) If a space (' ') is detected, that means it is the end of the number. Set isNum = False.
    - For alphabetic character, check it is upper case or not:
        a) It is upper case, append the Braille code corresponding to "capital follows" to the result.
        b) Otherwise, directly append the Braille code for that letter.
    - For the rest of the cases, append the Braille code for that character directly to the result.

5. Implement a function to check whether the input string is Braille or English:
    - First check the length of the string is a multiple of 6 or not. If not, return False
    - Split the string very 6 characters and check whether each one match with Braille code. If one pattern does not match with Braille code, it is not a Braille input.

6. Impelenmt a function to take the inputs from command line and do the translation:
    - Check the input type: English or Braille by calling the function from step 5.
    - If it is English, call the function created at step 4, add '......' between each input string
    - If it is Braille, call the function created at step 3, add ' ' between each input string


    
       
