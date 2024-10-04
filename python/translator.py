import sys

letters_to_braille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
}
numbers_to_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}
misc_to_braille = {
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}


output_text = ""
buffer = ""
position = 0
count = 0
braille = False

if len(sys.argv) == 2:
    for i in sys.argv[1]:
        if i == ".":
            count += 1
    if count / len(sys.argv[1]) > 0.3:
        braille = True
elif len(sys.argv) < 2: 
    exit()

capital = False
number = False
decimal = False

def get_key_by_value(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key
    return None  # If value is not found
    

# input is english
if(not braille):
    input_text = ""
    for i in sys.argv[1:]:
        input_text += i + " "
    input_text = input_text[0:-1]
    # print(input_text)
    
    while(position < len(input_text)):
        buffer = input_text[position]
        # print(position, buffer)
        # if we encounter a number
        if(buffer in numbers_to_braille.keys()):
            # if we are not already in a number
            if(number == False):
                number = True
                output_text += misc_to_braille["number"]
            output_text += numbers_to_braille[buffer]
        
        # if we encounter a letter or space
        elif(buffer.lower() in letters_to_braille.keys()):
            number = False
            if(buffer.isupper()):
                output_text += misc_to_braille["capital"]
            output_text += letters_to_braille[buffer.lower()]
        position += 1
        # print(output_text)

# input is braille
else:
    input_text = sys.argv[1]
    # print(input_text)
    while(position < len(input_text)):
        buffer = input_text[position:position+6]
        # print(buffer, position)
        if(buffer == misc_to_braille["capital"]):
            capital = True
            position += 6
            continue
        elif(buffer == misc_to_braille["number"] and number == False):
            position += 6
            number = True
            continue
        
        if(capital):
            output_text += get_key_by_value(letters_to_braille, buffer).capitalize()
            capital = False
        elif(number):
            if(buffer == misc_to_braille[" "]):
                number = False
                output_text += " "
                continue
            output_text += get_key_by_value(numbers_to_braille, buffer)
        else:
            output_text += get_key_by_value(letters_to_braille, buffer)
        
        position += 6

print(output_text)