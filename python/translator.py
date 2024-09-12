import sys

alpha_to_b = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    " ": "......"
}
numbers_to_b = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}
b_iscapital = ".....O"
b_isnumber = ".O.OOO"
b_isdecimal = ".O...O"

b_to_alpha = {b:alpha for alpha,b in alpha_to_b.items()}
b_to_numbers = {b:number for number,b in numbers_to_b.items()}

def translate():
    string = " ".join(sys.argv[1:])
    if "." in string:
        return braille_to_eng(string)
    else:
        return eng_to_braille(string)

def eng_to_braille(string):
    message = []
    is_number  = False
    for i in range(len(string)):
        character = string[i]
        if character.isnumeric():
            if not is_number:
                message.append(b_isnumber)
                is_number = True
            message.append(numbers_to_b[character])
        elif character.isupper():
            message.append(b_iscapital)
            message.append(alpha_to_b[character.lower()])
        else:
            message.append(alpha_to_b[character])
        if character == " ":
            is_number = False

    print("".join(message))
        
def braille_to_eng(string):
    message = []
    is_number = False
    is_capital = False
    for i in range(0, len(string), 6):
        b = string[i: i+6]
        if b == b_isnumber:
            is_number = True
            continue
        if b == b_iscapital:
            is_capital = True
            continue
        
        if is_number:
            message.append(b_to_numbers[b])
        else:
            character = b_to_alpha[b]      
            if is_capital:
                character = character.upper()
                is_capital = False
            message.append(character)
            
    print("".join(message))
    
if __name__ == "__main__":
    translate()
