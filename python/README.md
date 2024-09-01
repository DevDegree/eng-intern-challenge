# Python Instructions

Note that the Python version used is 3.8

## Considerations
- The letters `a-j` and the numbers `0-9` are represented by the same symbols
in Braille, so the `number follows` symbol is necessary
- Therefore, there must be a space after the end of a sequence of numbers
in Braille; otherwise, it would be unclear to the reader that they should
switch back to letters
e.g. The input`H3ar h3ar` is problematic without deciding on further
specifications
- Based on the technical requirements and these considerations,
some assumptions were necessary in building the translator

## Assumptions
- All inputs must follow the technical requirements and consist of only
the Braille symbols for `capital follows` and `number follows` and the 
English and Braille representations of the letters `a-z`, 
the numbers `0-9`, and `space`
- These symbols or characters must be inputted in a way that is correct and
readable e.g. placing a `capital follows` symbol at the end of the input
will not result in an English translation for that symbol

## Final Thoughts
There are some edge cases that lie outside the technical specifications
that would be fun to tackle if this were to be made into a product, such as
if one were to input a `number follows` symbol before the Braille symbol
for `z`. Perhaps we could implement some error handling alongside a
"best guess" in such scenarios.