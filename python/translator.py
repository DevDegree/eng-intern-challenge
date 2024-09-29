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
"O..OOO": "z", ".O.OOO": "num", ".....O": "cap", "......": " ", ".O...O": "dec",

#Extended version (Numbers & Punctuation):
#Never mind, don't use the numbers from here since keys conflict => use numbers_dict
"..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", 
"..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", 
"O.O..O": "(", ".O.OO.": ")"
}

#For the ambiguity between "o" and ">"
ambiguous_dict = {"O..OO.": ">"}

braille_to_english_numbers = {
"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
"OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

# English to Braille Dictionary
english_to_braille = {
"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
"z": "O..OOO", "num": ".O.OOO", "cap": ".....O", "dec": ".O...O", " ": "......",
#Numbers
"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", 
"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
#Punctuation
".": "..OO.O", ",": "..O...",  "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", 
"-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO."
}


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
    is_number = False
    previous_eng_char = ""

    for i in range(0, len(str), 6):
        braille_char = str[i:i+6]
        eng_char = braille_to_english[braille_char]

        if braille_char == "O..OO." and not previous_eng_char.isalpha(): #To handle the ambiguous edge case
            output_str.append(">")
            continue

        if is_number:
            eng_char = braille_to_english_numbers[braille_char] #Since there's overlap in the Braille chars (a-j / 0-9)

        # If we read "cap" from the dict, be sure to capitalize the next letter    
        if eng_char == "cap": 
            is_capital = True
            continue
        # If we read "num or dec" from the dict, a number is coming
        elif eng_char == "num" or eng_char == "dec":
            is_number = True
            continue

        elif not eng_char.isdigit() :
            is_number = False

        if is_capital: 
            eng_char = eng_char.upper()
            is_capital = False
        
        previous_eng_char = eng_char
        output_str.append(eng_char)
    
    return ''.join(output_str)


# Translates input (braille) string and outputs english string 
def translate_to_braille(str):
    output_str = []
    outputting_number = False # Realized I need this for multi-digit numbers

    for char in str:
        # If it's a number, add the number prefix & the number
        if char.isdigit():
            if not outputting_number : #If it's the first digit of the number, add the prefix
                output_str.append(english_to_braille["num"])
                outputting_number = True
            output_str.append(english_to_braille[char])
            continue
        # If it's a letter, check if it's upper or lower case and add the prefix (or don't)
        elif char.isalpha():
            outputting_number = False  # Since it's a letter, disable this
            if char.isupper():
                output_str.append(english_to_braille["cap"])
                output_str.append(english_to_braille[char.lower()])
            else:
                output_str.append(english_to_braille[char])
            continue
        # If it's a space, add the braille-space char representation
        elif char == ' ':
            output_str.append(english_to_braille[" "])
            outputting_number = False  # Since it's a letter, disable this
            continue
        #For the ambiguous edge case:
        elif char == ">":
            output_str.append(ambiguous_dict[char])
            continue
        else:
            output_str.append(english_to_braille[char])

    return ''.join(output_str)

def main():
    #Check for empty string - edge case
    if len(sys.argv) < 2:
        return
    
    input_str = ' '.join(sys.argv[1:])

    #If it's braille, translate to english & vice-versa
    if check_braille(input_str):
        sys.stdout.write(translate_to_english(input_str))
    else:
        sys.stdout.write(translate_to_braille(input_str))

if __name__ == "__main__":
    main()