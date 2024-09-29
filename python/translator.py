import sys #Need this to read system input 

'''
Game Plan:
1. Define helper function to see if the input string is Braille or English
    - Braille contains only . and 0 
    - Braille text string should be divisible by 6 (since every Braille char is 6 chars)
        * Check if input_string mod 6 
2. Define Braille to English translate function
3. Define English to Braille translate function

Overall 'main' process goes like this:
1. Check if string is (valid) braille or if it's text
    - if it's an empty string, print nothing
2. If it's Braille, use braille to eng translator
3. If it's English, use eng to braille translator
4. Print result => since this is system output (Rmb to *only* print result)
'''
# Braille to English Dictionary
braille_to_english = {
"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
"O..OOO": "z", ".O.OOO": "num", ".....O": "cap", "......": " "
}

# English to Braille Dictionary
# Reversed it cause I'm too lazy to retype everything
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Helper function to check if input string is braille or not
def check_braille(str):
    for char in str: 
        if char not in 'O.': return False # Check if only 'O' or '.'
    if len(str) % 6 != 0: return False # Check if divisible by 6
    return True

# Translates input (English) string and outputs braille string
def translate_to_english(str):
    output_str = []
    is_capital = False

    for i in range(0, len(str)):
        braille_char = output_str[i:i+6]
        eng_char = braille_to_english[braille_char]
        # If we read "cap" from the dict, be sure to capitalize the next letter    
        if eng_char == "cap": 
            is_capital = True
        if is_capital: 
            eng_char = eng_char.upper()
            is_capital = False
        output_str.append(eng_char)
        i += 6
    
    return ''.join(output_str)


# Translates input (braille) string and outputs english string 
def translate_to_braille(str):
    output_str = []
    outputting_number = False # Realized I need this for multi-digit numbers

    for char in str:
        # If it's a number, add the number prefix & the number
        if char.isdigit():
            if not outputting_number : #If it's the first digit of the number, add the prefix
                output_str.append("O.OOOO") 
                outputting_number = True
            output_str.append(english_to_braille[char])
        # If it's a letter, check if it's upper or lower case and add the prefix (or don't)
        elif char.isalpha():
            if char.isupper():
                output_str.append(".....O")
                output_str.append(english_to_braille[char.lower()])
            else:
                output_str.append(english_to_braille[char])
            outputting_number = False  # Since it's a letter, disable this
        # If it's a space, add the braille-space char representation
        elif char == ' ':
            output_str.append("......")
            outputting_number = False  # Since it's a letter, disable this

    return ''.join(output_str)

def main():
    # input_str = sys.argv[1]
    #If it's braille, translate to english & vice-versa

    #TEST INPUT STRING
    input_str = "42"
    if check_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()