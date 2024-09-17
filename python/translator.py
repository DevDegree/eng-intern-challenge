import sys

# Define dictionary for translation
letters = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z"
}

nums = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "O",
}

operators = {
    ".....O": "Capital follows",
    ".O...O": "Decimal follows",
    ".O.OOO": "Number follows",
}

punc = {
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
}

space = { 
    "......": " " 
}

# Reverse dictionaries for english to braille
braille_letters = {v: k for k, v in letters.items()}
braille_nums = {v: k for k, v in nums.items()}
braille_punc = {v: k for k, v in punc.items()}
braille_operators = {v: k for k, v in operators.items()}
is_capital = {v: k for k, v in operators.items() if v == "Capital follows"}
is_num = {v: k for k, v in operators.items() if v == "Number follows"}
is_punc = {v: k for k, v in operators.items() if v == "Decimal follows"}

# Braille to english
def braille_to_english(braille):
    '''
    input: str
    rtype: str
    Assume input is given as a braille string
    '''
    res = ""
    is_capital = False
    is_num = False
    is_punc = False
    
    # Loop through 6-character chunks
    for index in range(0, len(braille), 6): 
        curr = braille[index:index + 6] 
        
        # handle operators
        if curr in operators:
            if operators[curr] == "Capital follows":
                is_capital = True
                pass
            elif operators[curr] == "Number follows":
                is_num = True
                pass
            elif operators[curr] == "Decimal follows":
                is_punc = True
                pass
        
        # handle numbers
        elif is_num:
            if curr in space:  # if space, reset to letters
                res += " "
                is_num = False
                pass
            else:
                res += nums[curr]
            
        # handle capital
        elif is_capital:
            res += letters[curr].upper()
            is_capital = False
        
        # handle punctuation
        elif is_punc and curr in punc:
            res += punc[curr]
            is_punc = False
        
        elif curr in space:
            res += space[curr]
        
        else:
            res += letters[curr]
    
    return(res)


def english_to_braille(text):
    '''
    input: str
    rtype: str
    Assume input is given as an English string, convert to braille
    '''
    res = ""
    num_sequence = False
    
    # Loop through each character in the text
    for char in text:        
        # handle ending number sequence
        if num_sequence and char not in braille_nums:
            num_sequence = False
            res += "......"
        
        # handle space
        if char == " ":
            res += "......"
        
        # handle punctuation
        elif char in braille_punc:
            res += is_punc["Decimal follows"]
            res += braille_punc[char]
        
        # handle numbers
        elif char in braille_nums:
            if not num_sequence:
                res += is_num["Number follows"]
                num_sequence = True
            res += braille_nums[char]

        # handle capital
        elif char.isupper():
            res += is_capital["Capital follows"]
            res += braille_letters[char.lower()]

        else:
            res += braille_letters[char]
    
    return res


def main():
    # Concatenate all arguments into a single string
    input_string = ' '.join(sys.argv[1:])    
    
    # Check if input is braille or english
    is_braille = all([char in "O." for char in input_string])
    
    result = braille_to_english(input_string) if is_braille else english_to_braille(input_string)

    print(result)
    
if __name__ == "__main__":
    main()