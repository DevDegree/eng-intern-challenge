import sys

braille_alph = {

    #uppercase letters
    'A':'O.....', 'B':'O.O...', 'C':'OO....', 'D':'OO.O..', 'E':'O..O..', 'F':'OOO...',
    'G':'OOOO..', 'H':'O.OO..', 'I':'.OO...', 'J':'.OOO..', 'K':'O...O.', 'L':'O.O.O.',
    'M':'OO..O.', 'N':'OO.OO.', 'O':'O..OO.', 'P':'OOO.O.', 'Q':'OOOOO.', 'R':'O.OOO.',
    'S':'.OO.O.', 'T':'.OOOO.', 'U':'O...OO', 'V':'O.O.OO', 'W':'.OOO.O', 'X':'OO..OO',
    'Y':'OO.OOO', 'Z':'O..OOO',
    'capital': '.....O', 'number':'.O.OOO', ' ': '......',

    #lowercase letters
    'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 'e':'O..O..', 'f':'OOO...',
    'g':'OOOO..', 'h':'O.OO..', 'i':'.OO...', 'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.',
    'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 'p':'OOO.O.', 'q':'OOOOO.', 'r':'O.OOO.',
    's':'.OO.O.', 't':'.OOOO.', 'u':'O...OO', 'v':'O.O.OO', 'w':'.OOO.O', 'x':'OO..OO',
    'y':'OO.OOO', 'z':'O..OOO',
}

braille_num = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


# reverse the dictionary for braille to regular text
text_alphabet = {v: k for k, v in braille_alph.items()}
text_numbers = {v: k for k, v in braille_num.items()}


#checking if the user input is in braille
def is_braille(inp):
    return all(i in 'O.' for i in inp)


#text to braille 
def to_braille(string):
    res = []
    #flag for indicating if next character is a number
    is_number = False
    
    for char in string:
        if char.isupper():
            res.append(braille_alph['capital'])  #adding the capital symbol
            res.append(braille_alph[char.lower()])
            is_number = False
            
        elif char.isdigit():
            if not is_number:
                res.append(braille_alph['number'])
                is_number = True  #flagging the start of a number sequence
            res.append(braille_num[char])
        elif char == ' ':  #when theres a space
            res.append(braille_alph[char])
            is_number = False  #number sequence ends when encountering a space character
        else:
            res.append(braille_alph[char])
            is_number = False
    #join list into a string 
    return ''.join(res) 


#braille to text
def to_text(string):
    res = []
    i = 0

    #flags to indicate if next characters are either numbers or capitals
    is_capital = False
    is_num = False

    while i < len(string):
        braille_char = string[i:i+6] 
        if braille_char == braille_alph['capital']: #if theres a capital symbol, set flag to true
            is_capital = True
        elif braille_char == braille_alph['number']: #if theres a number symbol, set flag to true 
            is_number = True
        elif is_num: #if the number flag is set, get the corresponding digit
            res.append(text_numbers[braille_char])
            is_num = False #reset flag
        else:
            #finding the character in text_alphabet
            char = text_alphabet.get(braille_char, ' ') 
            if is_capital:
                res.append(char.upper()) #converts character to uppercase if is_capital is true
                is_capital = False
            else:
                res.append(char) #append regular character
        #moves to the next braille character sequence
        i += 6
    return ''.join(res) #joins the list into a string 

def main():
    #since only one argument is expected
    if len(sys.argv) < 2:
        print("Usage: python translator.py")
        return
    
    inp = " ".join(sys.argv[1:]) #getting input from command line argument

    #checks if input is braille - executes braille to text function if it is 
    if is_braille(inp):
        print(to_text(inp))
    else:
        #if input is text
        print(to_braille(inp)) 


if __name__ == "__main__":
    main()


