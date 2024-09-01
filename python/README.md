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

4. **Trailing and Leading Whitespace**:
   - The presence of trailing and leading whitespace in the input or output caused discrepancies in test results. This was especially problematic when comparing expected and actual outputs in unit tests. Also one assumption that I am making while writing this program is there will be no "space-only" input.