# Python Instructions

Note that the Python version used is 3.8

**Assumptions:**

- more than one space is treated as a single space
- decimals do not exist before the digits (such as .5), they are treated as periods
- if decimal, it is followed by a "." character in the braille
- if any character not in dictionary, it gives an error message and exits
- if braille text cannot be split into 6 character chunks, it gives an error message and exits

**Time Complexity: O(n)**
Nested for loops and string concatenations are avoided to keep time complexity minimal. I avoided the for loops by reversing the dictionary in braille-to-english from the beginning instead of iterating through the english-to-braille dictionary for each character. As for string concatenations, I replaced those with list appending and then joined the list in the end as a string.

**Strategy Pattern:**
I used the Strategy Pattern here to enable flexible translation between English and Braille by encapsulating different translation algorithms in separate classes (EnglishToBrailleStrategy and BrailleToEnglishStrategy). This pattern allows me to:
- Dynamically choose the translation strategy based on the input text type (English or Braille) without modifying the Translator class.
- Extend the code in the future as each translation algorithm is isolated in its own class.