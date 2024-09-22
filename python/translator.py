'''
Braille Translator Submission by Frank Siyung Cho
20fsc@queensu.ca


Plan of Action:
1. Determine logic for classifying if input string is braille or english
    - if the input string only contains the characters O and . then it is braille
2. For a Braille to English conversion we can map the set of braille combinations into 6 bit binary values using this matrix:

[1][4]
[2][5]
[3][6]

Therefore, if the Braille Letter is O..... Then the 6 bit combination is 0b000001
From the provided braille to letter combinations, we can see that the letters A-J only use bit positions 1,2,4 and 5.
We can also see that the letters K-T add the bit position 3 to the same bit patterns as A-J.
The same occurs for letters U-Z however adding bit position 6 as well.
This means we can partition the alphabet into 3 sections and by distinguishing if bit positions 3 and 6 are used we can identify which corresponding letter should be added.
We can also use ASCII character encodings to transform the binary values of the 6 bit combination into characters.

3. Implement logic which identifies if 'capital follows', 'decimal follows' or 'number follows' 6 bit combinations are present
4. Implement numerical logic so that if 'decimal follows' or 'number follows' 6 bit combination is found then instead of letter combinations, number combinations are used.
5. Implement special characters logic to identify any ',', '.', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' '
'''

import sys

args = sys.argv[1:] # Ingest all the inputted text ie, Braille or English into a list where each element is a word

def braille_to_bits(arg):
    arg = arg.strip()
    if (len(arg) != 6): # Ensure Braille string is correct length
        raise ValueError("Braille input must be 6 characters long")
    
    bits = 0

    for i, char in enumerate(arg): # Loop through every character in string
        if char == 'O':
            bits |= 1 << i # Use bitwise OR operation |= and the Zero fill left shift to add 1 in correct bit position
        elif char =='.':
            pass
        else:
            raise ValueError("Inputted Braille must be either . or O")
    return bits

bit_string = braille_to_bits(args[0])
print(f"Bits: {bit_string:06b}")