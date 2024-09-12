# Python Instructions

Note that the Python version used is 3.8


## Algorithm
1. Braille checking: If a string is correct Braille syntax, it must have the following:
  - len(str) % 6 == 0 as all braille symbols are at least 6 characters long
  - braille sequence must have only 'O' (capital o) or '.'
  - `OOOOOO` is not valid braille 
2. Translating English to Braille
  - **Handling Digits**: Detects digits and inserts a Braille number indicator (`NUM` token) if starting a number sequence.
  - **Handling Capital Letters**: Inserts a capital indicator (`CAPITAL` token) before appending the lowercase Braille letter.
  - **Digit Sequence Reset**: Resets the `isNum` flag when processing a non-digit to signal the end of a number sequence.
  - **Appending Braille Characters**: After handling digits or capitals, appends the appropriate Braille token to the result.
3. Translating braille to english
  - **Handling Digits**: Appends the corresponding digit when in a number sequence (`numNext` is set).
  - **Handling Capitalization**: Sets the `capNext` flag when a capital indicator is encountered to capitalize the next letter.
  - **Number Sequence**: Differentiates between digits and letters when Braille tokens overlap (e.g., '1' vs. 'a').
  - **Handling Spaces**: Appends a space and resets `numNext` to end the number sequence.
  - **Appending Characters**: Capitalizes the next letter if `capNext` is set, otherwise appends the lowercase letter. 

## corner case
  - The case `OOOOOO` is not braille. It's not in our braille syntax but it is valid English. 

## assumptions:
- all inputs are syntactically sound. 
  - english lexicon does not include puncutation, decimal points, decimal numbers and so on. 
- all args are type uniformed (in english or in Braille)
  - if there are multiple args passed in, they are in english and will be joined with ' ' separating them. 
- translation functions are not bijective:
  - based on the available syntax of braille and english, some alphanumerical words make the translation non-bijective
  - `s != engToBra(braToEng(s))`  for the case 'a1a'. 