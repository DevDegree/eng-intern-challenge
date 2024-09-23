'''
Braille Translator Submission by Frank Siyung Cho
20fsc@queensu.ca


Plan of Action:
1. Determine logic for classifying if input string is braille or english
    - if the input string only contains the characters O and . then it is braille
2. For a Braille to English conversion we can map the set of braille combinations into 6 bit binary values using this matrix:

[1][2]
[3][4]
[5][6]

Therefore, if the Braille Letter is O..... Then the 6 bit combination is 0b000001
From the provided braille to letter combinations, we can see that the letters A-J only use bit positions 1,2,3 and 4.
We can also see that the letters K-T add the bit position 5 to the same bit patterns as A-J.
The same occurs for letters U-Z however adding bit position 6 as well.
This means we can partition the alphabet into 3 sections and by distinguishing if bit positions 3 and 6 are used we can identify which corresponding letter should be added.
We can also use ASCII character encodings to transform the binary values of the 6 bit combination into characters.

** After some testing it was found that the letter 'W' does not match the pattern and uses bits 2,4,5 instead of 1,4. An exception in the code will be made which identifies this edge case.

3. Implement logic which identifies if 'capital follows', 'decimal follows' or 'number follows' 6 bit combinations are present
4. Implement numerical logic so that if 'decimal follows' or 'number follows' 6 bit combination is found then instead of letter combinations, number combinations are used.
5. Implement special characters logic to identify any ',', '.', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', ' '
'''

import sys

args = sys.argv[1:] # Ingest all the inputted text ie, Braille or English into a list where each element is a word

'''
All logic functions for character decoding from Braille -> English
'''
def braille_to_bits(arg, switch):
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
        
    match switch:
        case 1 : return braille_decoder(bits, number_type=False)
        case 2 : return braille_decoder(bits, number_type=False).lower()
        case 3 : return braille_decoder(bits, number_type=True)
        case _ : return bits


def braille_decoder(bit_combination, number_type):
    # Create the base pattern template for bits 1,2,3,4
    base_patterns = {
        0b000001: 0,
        0b000101: 1,
        0b000011: 2,
        0b001011: 3,
        0b001001: 4,
        0b000111: 5,
        0b001111: 6,
        0b001101: 7,
        0b000110: 8,
        0b001110: 9
    }

    special_patterns = {
        0b101100: ".",
        0b000100: ",",
        0b110100: "?",
        0b011100: "!",
        0b001100: ":",
        0b110000: "-",
        0b010010: "/",
        0b100110: "<",
        0b111111: ">", # Ommited because > symbol has same brail combination as o which is a limitation as per instructions
        0b100101: "(",
        0b011010: ")",
        0b000000: " "
    }

    if special_patterns.get(bit_combination, False):
        return special_patterns.get(bit_combination)

    # Mask out bits 1 to 4 for pattern matching
    pattern = bit_combination & 0b1111

    # Gather bits for dot 5 and 6
    bit_5 = (bit_combination & 0b010000 ) >> 4
    bit_6 = (bit_combination & 0b100000 ) >> 5

    pattern_value = base_patterns.get(pattern, None) # Gather pattern number using bit pattern as key

    if (bit_5) and (number_type == False):
        pattern_value += 10

    if (bit_6) and (number_type == False):
        pattern_value += 10 if bit_5 else 13 # In case a W is present

    if (pattern_value > 22) and (number_type == False): # Adjust for every letter after W
        pattern_value += 1

    if (number_type == False):
        braille_value = chr(ord('A') + pattern_value) # Letter conversion from ascii value
    else:
        braille_value = pattern_value + 1

        if braille_value == 10:
            braille_value = 0

    return braille_value

def character_type_decoder(arg):
    logic_switch = braille_to_bits(arg, 0)

    character = ""

    match logic_switch:
        case 0b100000: character = braille_to_bits(args[1], 1)
        case 0b100010: character = "."
        case 0b111010: character = braille_to_bits(args[1], 3)
        case _ : character = braille_to_bits(arg, 2)

    return character

'''
All logic functions for character encoding from English -> Braille
'''

def bits_to_braille(bits):
    braille = ''
    for i in range(6):
        braille += 'O' if bits & (1 << i) else '.'

    return braille

def braille_encoder(arg):

    # Create the base pattern template for bits 1,2,3,4
    base_patterns = {
        0: 0b000001,
        1: 0b000101,
        2: 0b000011,
        3: 0b001011,
        4: 0b001001,
        5: 0b000111,
        6: 0b001111,
        7: 0b001101,
        8: 0b000110,
        9: 0b001110
    }

    letter = arg.upper()
    
    letter_pos = ord(letter) - ord('A')

    if letter_pos < 0 or letter_pos > 25:
        raise ValueError("Input must be a letter between A and Z")
    
    if letter == 'W':
        letter_pos = 9
    
    if letter_pos > 22:
        letter_pos -= 1
    
    bit_pattern = base_patterns[letter_pos % 10 if letter_pos!=0 else 0]

    print(f"{bit_pattern:06b}")

    if letter_pos >= 10 and letter != 'W':
        bit_pattern |= 0b010000

    if letter_pos >= 20 or letter == 'W':
        bit_pattern |= 0b100000

    return bits_to_braille(bit_pattern)
    
# letter = braille_to_bits(args[0])
# print("letter: " + letter)

# braille_string = braille_encoder(args[0])
# print("Braille: " + braille_string)
print(character_type_decoder(args[0]))