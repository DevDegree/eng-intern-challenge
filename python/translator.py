import sys


# Braille to English Mapping
B_to_E_char = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " "
}
B_to_E_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0", "......": " "
}

# English to Braille Mapping, we'll just reverse the dictionairy
def reverse_d(d):
    return {val: key for key, val in d.items()}

# We combine to make 1 English dictionairy since no repetitive symbols
E_to_B = reverse_d(B_to_E_char) | reverse_d(B_to_E_num)


# Now, our translate functions, 
# Keeping in mind: 
# When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
# When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.

def Braille_to_English(input):
    english_output = ""
    next_symbol = "lower" # 3 options: lower (default), upper or number
    word_size = int(len(input) / 6)
    for i in range(word_size):
        s = input[i*6 : i*6 + 6]

        if s == "......": # After a space, assume lower_case
            next_symbol = "lower"

        if s == ".....O":
            next_symbol = "upper"
        elif s == ".O.OOO":
            next_symbol = "number"     
        else:
            if next_symbol == "lower":
                english_output += B_to_E_char[s]
            elif next_symbol == "upper":
                english_output += B_to_E_char[s].upper()
                next_symbol = "lower" # only 1 uppercase, back to default
            else:
                english_output += B_to_E_num[s]
    
    return english_output



def English_to_Braille(input):
    braille_output = ""
    capital = ".....O" # when next char is uppercase
    number = ".O.OOO" # when next char is number
    number_sym_added = False  # True if already added number symbol
     
    for s in input:

        if s == " ": # After a space, assume non-digit is next
            number_sym_added = False

        if s.isupper():
            braille_output += capital + E_to_B[s.lower()].upper()
        elif s.isdigit() and not number_sym_added:
            number_sym_added = True
            braille_output += number + E_to_B[s.lower()]
        else:
            braille_output += E_to_B[s]
    
    return braille_output


if len(sys.argv) > 1:
    # Parses input passed in
    input = sys.argv[1:]
    input = " ".join(input)

    # We are checking if input is Braille or English
    if len(input) % 6 == 0 and (input[:6] in B_to_E_char or input[:6] in B_to_E_num):
        print(Braille_to_English(input))
    else:
        print(English_to_Braille(input))
else:
    print("input required")