import sys

# HASH Map Braille to Alphabet and vice versa
toBraille_dict={
    'a':"O.....",
    'b':"O.O...",
    'c':"OO....",
    'd':"OO.O..",
    'e':"O..O..",
    'f':"OOO...",
    'g':"OOOO..",
    'h':"O.OO..",
    'i':".OO...",
    'j':".OOO..",
    'k':"O...O.",
    'l':"O.O.O.",
    'm':"OO..O.",
    'n':"OO.OO.",
    'o':"O..OO.",
    'p':"OOO.O.",
    'q':"OOOOO.",
    'r':"O.OOO.",
    's':".OO.O.",
    't':".OOOO.",
    'u':"O...OO",
    'v':"O.O.OO",
    'w':".OOO.O",
    'x':"OO..OO",
    'y':"OO.OOO",
    'z':"O..OOO",
    ' ':"......"
}
toAlpha_dict={v: k for k, v in toBraille_dict.items()}

# HASH Map Braille to Number and vice versa
num_to_braille={
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO..",
}
braile_to_num={v: k for k, v in num_to_braille.items()}

# HASH Map separators(capital and number indicatiors)
separators={
    ".....O":"capital",
    ".O.OOO":"number",
    "......":"space",
}


# Converting input to necessary output
def convert (input_wrd,is_braille):
    """This function converts the input from Alpanumeric to Braille and vice versa"""
    output=""
    # To Braille conversion
    if not is_braille:
        prev=None
        # Loop thru each character
        for i in input_wrd:
            # Do this if numeric
            if i.isnumeric():
                if prev=="alphabet" or prev==None:
                    output+=".O.OOO"
                    output+=num_to_braille[i.lower()]
                    prev="number"
                else:
                    output+=num_to_braille[i]
            # Do this if alphabet
            elif i.isalpha() or i==" ":
                if i.isupper():
                    output+=".....O"
                if prev=="number" or prev==None:
                    output+=toBraille_dict[i.lower()]
                    prev="alphabet"
                else:
                    
                    output+=toBraille_dict[i.lower()]
            else:
                output+=toBraille_dict[i.lower()]
    # To Alphanumeric conversion
    else:
        prev = None
        for i in range(6, len(input_wrd) + 1, 6): 
            # Check if its a separator
            cur=input_wrd[i-6:i]
            if cur in separators:
                if separators[cur]=="space":
                    output+=" "
                    prev=None
                else: prev=separators[cur]
            else:
                if prev in {"capital",None}:
                    if prev == "capital":
                        output+=toAlpha_dict[cur].upper()
                        prev = None
                    else:
                        output+=toAlpha_dict[cur]
                else:
                    output+=braile_to_num[cur]

    
    return output

# Converting input to necessary output
def isBraille (input_wrd):
    """This function checks if the argument is braille or not"""
    for x in input_wrd:
        if x not in {".","O"}:return False
    return True

# Main function to execute when running the script
if __name__ == "__main__":
    argument = sys.argv[1:] 
    user_input=" ".join(argument)
    output=convert(user_input, isBraille(user_input))
    print(output)
