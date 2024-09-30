import sys

braille_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ", 
    "..OO.O": ".", 
    "..O...": ",", 
    "..O.OO": "?", 
    "..OOO.": "!",
    "..OO..": ":",  
    "..O.O.": ";", 
    "....OO": "-", 
    ".O..O.": "/",  
    ".OO..O": "<",  
    "O.O..O": "(",  
    ".O.OO.": ")",  
    ".....O": "Capital follows",  
    ".O.OOO": "Number follows"    
}

number_in_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

reverse_map = {v: k for k, v in braille_map.items()}

def braille_translation(text):
    output = []
    in_number_mode = False
    for character in text:
        if character.isdigit():
            if not in_number_mode:
                output.append(".O.OOO")
                in_number_mode = True
            output.append(number_in_braille[character])
        elif character.isalpha():
            if in_number_mode:
                output.append("......")
                in_number_mode = False
            if character.isupper():
                output.append(".....O")
            output.append(reverse_map[character.lower()])
        else:
            if in_number_mode:
                in_number_mode = False
            output.append(reverse_map[character])
    return ''.join(output)

def english_translation(braille_text):
    output = []
    index = 0
    while index < len(braille_text):
        segment = braille_text[index:index+6]
        if segment == ".....O":
            index += 6
            next_segment = braille_text[index:index+6]
            output.append(braille_map[next_segment].upper())
        elif segment == ".O.OOO":
            index += 6
            while index < len(braille_text) and braille_text[index:index+6] != "......":
                output.append(str(list(number_in_braille.values()).index(braille_text[index:index+6]) + 1))
                index += 6
            continue
        else:
            output.append(braille_map[segment])
        index += 6
    return ''.join(output)

def main():
    input_text = ' '.join(sys.argv[1:])
    if all(char in 'O.' for char in input_text):
        print(english_translation(input_text))
    else:
        print(braille_translation(input_text))

if __name__ == "__main__":
    main()
