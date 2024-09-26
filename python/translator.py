
alphabet = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w': '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO', 
    ' ' : '......',
}
numbers = {
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'O..O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..',
}
decimals = {
    '.' : '..OO.O',
    ',' : '..O...',
    '?' : '..O.OO',
    '!' : '..OOO.',
    ':' : '..OO..',
    ';' : '..O.O.',
    '-' : '....OO',
    '/' : '.O..O.',
    '<' : '.OO..O',
    '>' : 'O..OO.',
   '(' : 'O.O..O',
   ')' : '.O.OO.',
}

decode = "alpha"  # alpha, nums or deci
position = 0
result = ""

def translate(input_string):
    global decode, position, result
    if isBraille(input_string):
        translate_to_english(input_string)
    else:
        translate_to_braille(input_string)

def isBraille(string):
    characters = set(string)
    contains_period = '.' in characters
    contains_O = 'O' in characters
    return len(characters) == 2 and contains_period and contains_O

def translate_to_braille(string):
    global decode, result
    for c in string:
        if c == " ":
            decode = "alpha"
            result += alphabet.get(c)
        elif c.isalpha():
            if c.isupper():
                result += '.....O'
                c = c.lower()
            result += alphabet.get(c)
        elif c.isnumeric():
            if decode == "nums":
                result += numbers.get(c)
            else:
                result += ".O.OOO"
                decode = "nums"
                result += numbers.get(c)
        else:
            if decode == "deci":
                result += decimals.get(c)
            else:
                result += ".O...O"
                decode = "deci"
                result += decimals.get(c)

def translate_to_english(string):
    global decode, position, result
    if len(string) % 6 != 0:
        raise Exception("Invalid length")
    while position <= len(string) - 6:
        braille = string[position:position + 6]
        if braille == ".O.OOO":
            decode = "nums"
        elif braille == ".O...O":
            decode = "deci"
        elif braille == '......':
            decode = "alpha"
            index = list(alphabet.values()).index(braille)
            result += list(alphabet.keys())[index]
        else:
            handle_decode(braille, string)
        position += 6

def handle_decode(braille, string):
    global decode, position, result
    if decode == "alpha":
        if braille == ".....O":
            position += 6
            if position > len(string) - 6:
                return ''
            index = list(alphabet.values()).index(string[position:position + 6])
            result += list(alphabet.keys())[index].upper()
        else:
            index = list(alphabet.values()).index(braille)
            result += list(alphabet.keys())[index]
    elif decode == "nums":
        index = list(numbers.values()).index(braille)
        result += list(numbers.keys())[index]
    else:
        index = list(decimals.values()).index(braille)
        result += list(decimals.keys())[index]

def get_result():
    return result

# Entry point for running the translator script via command-line
if __name__ == "__main__":
    import sys
    input_string = ' '.join(sys.argv[1:])
    translate(input_string)
    print(get_result())