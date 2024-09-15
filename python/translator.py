import sys

# Making dictioniary for chars to values
eng_to_b = {
    'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 'e':'O..O..', 'f':'OOO...', 'g':'OOOO..', 'h':'O.OO..',
    'i':'.OO...', 'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.', 'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 'p':'OOO.O.',
    'q':'OOOOO.', 'r':'O.OOO.', 's':'.OO.O.', 't':'.OOOO.', 'u':'O...OO', 'v':'O.O.OO', "w":'.OOO.O', 'x':'OO..OO',
    'y':'OO.OOO', 'z':'O..OOO', '1':'O.....', '2':'O.O...', '3':'OO....', '4':'OO.O..', '5':'O..O..', '6':'OOO...',
    '7':'OOOO..', '8':'O.OO..', '9':'.OO...', 'O':'.OOO..', 'cap':'.....O', 'dec':'.O...O', 'num':'.O.OOO', '.':'..OO.O',
    ',':'..O...', '?':'..O.OO', '!':'..OOO.', ':':'..OO..', ';':'..O.O.', '-':'....OO', '/':'.O..O.', '<':'.OO..O',
    '>':'.OO..O', '(':'O.O..O', ')':'.O.OO.', ' ':'......'
}

# Adding values from the eng_to_b dictioniary and any chars with the same braille text will be appending in the order of letter then number

b_to_eng ={}
for key, value in eng_to_b.items():
    if value in b_to_eng:
        b_to_eng[value].append(key)
    else:
        b_to_eng[value] = [key]

# Checking if input is eiher in braille or english text.

def is_text_braille(text):
    for char in text:
        if char not in 'O.':
            return False
    return True # If all charcters in the input are O or . it will be in braille so return true


def english_to_braille(text):
    res = []
    is_number = False

    for char in text:
        if char.isalpha(): # Checks if the current character is a letter
            is_number = False
            if char.isupper(): # Checks if the current character is a capital
                res.append(eng_to_b['cap']) # Appends the braille text for capital letter
                char = char.lower()
            res.append(eng_to_b[char])
        elif char.isdigit(): # Checks if the character is a number
            if is_number == False:
                is_number = True
                res.append(eng_to_b['num']) # Sends the braille text that the next character is a number
            res.append(eng_to_b[char])
        else:
            res.append(eng_to_b[char]) # Anything that is not a number or letter can be sent (there is no complications with these)

    return ''.join(res) # Puts everything in one text

def braille_to_english(braille):
    res = []
    i = 0
    is_number = False

    while i < len(braille):
        brailleChar = braille[i:i+6] # Grabs the first 6 available braille characters and puts them in a variable 
        
        if brailleChar == eng_to_b['cap']:
            nextChar = braille[i+6:i+12]
            res.append(b_to_eng[nextChar][0].upper()) # If the current braille value is a capital value then it sends the next brailler value as a capital letter
            i += 12
        elif brailleChar == eng_to_b['num']: # Lets the code know that the next character is going to be a number
            is_number = True
            i += 6
        elif brailleChar == "......":
            res.append(' ')
            is_number = False # in the case the current value is a number and it ends to send a letter, this lets the user know the next chacrter is either a new number or letter
            i += 6
        else:
            nextChar = b_to_eng[brailleChar] # takes the value of the the current 6 braille characters
            if is_number:
                res.append(nextChar[1]) # sends the 2nd value in the array which was previously set for only numbers ( check b_to_eng comment line 14)
            else:
                is_number = False
                res.append(nextChar[0]) # sends the 1st value in the array which was previously set for only letters ( check b_to_eng comment line 14)
            i += 6
    
    return ''.join(res) # sends the new english text to user


def main():
    inputString = " ".join(sys.argv[1:]) # takes input from terminal

    # Checks if the input is in braille or english and uses its respective function for conversion 
    if is_text_braille(inputString):
        print(braille_to_english(inputString))
    else:
        print(english_to_braille(inputString))

if __name__ == "__main__":
    main()

