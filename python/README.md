# Python Instructions

Note that the Python version used is 3.8

# Some challenges I've faced while working on this problem

Thank god I wrote unit tests. GUYS PLEASE WRITE UNIT TESTS
During the debugging process, I encountered several challenges, particularly with identifying and handling edge cases:

1. **Handling Spaces in Braille Translation**:
   - Initially, the translation from Braille to English did not correctly handle spaces(my ABC 123 in braille -> ABC 123 in english was missing spaces). This led to outputs where words and numbers were concatenated without spaces

2. **Number Mode Handling**:
   - Switching between number mode and text mode was another challenge. The translation sometimes failed to exit number mode, leading to incorrect translations of subsequent text.

3. **Edge Cases with Mixed Content**:
   - Edge cases involving mixed content (e.g., alternating numbers and letters, or numbers following spaces) were particularly tricky. These cases often resulted in incorrect translations due to the complexity of context switching.

# One quick question for the organizers
   (I might be missing something very obvious, sorry if that's the case >//< )
   - I find that for some test cases, it is not possible to reliably get the correct answer with the organizers' Technical Requirements of braille/english mapping .
   
   Take this example: 

   ```
   python translator.py A1b2:
   .....OO......O.OOOO.....O.O...O.O...
   ```
   This is correctly translated (according to the organizers' Technical Requirements).
   (logic used: "capital follows" -> "capital a" -> "number follows" -> "one" -> "normal b" -> "two"(as we have not encountered a space yet, we do not need another number follows))

   However this set of instructions will struggle to correctly translate the previous "A1b2" back from braille to english:
   ```
   python translator.py .....OO......O.OOOO.....O.O...O.O...:
   A122
   ```
   This is actually correctly translated as well (according to the organizers' Technical Requirements).
   But why is this? In this braille/mapping scenario, the first 10 letters in the alphabet has the same representation as the digits from 0-9 (a same mapping as 1, b same as 2, etc...), so in this test case, the logic that was applied was:
   "capital follows" -> "capital a" -> "number follows" -> "one" -> "normal b" -> "two"

   Since "normal b" and "two" has the same mapping, it is not possible to reliably translate this braille .....OO......O.OOOO.....O.O...O.O..., as this braille mapping could represent either A1b2 or A122 with the Technical Requirements given. 
   
   So is this a bug or a feature 🤔? (sorry for long text)





