import sys

#Dictionary mapping Braille to English letters & symbols
braille_to_english_dict = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", "..OO.O": ".", "..O...": ",", ".O..O.": "/",
    "....OO": "-", "O.O..O": "(", "..O.O.": ";", "..OOO.": "!", "..O.OO": "?",
    ".OO..O": "<", "..OO..": ":", ".O.OO.": ")", ".....O": "Capital follows",
    ".O.OOO": "Number follows"
}

#Dictionary mapping numbers to Braille
numeric_to_braille_dict = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

#Reverse dictionary mapping Braille to English letters & symbols
english_map_to_braille = {v: k for k, v in braille_to_english_dict.items()}

def convert_to_english(braille):
    output = []
    index = 0
    while index < len(braille):
        pattern = braille[index:index+6]
        
#Handles capital letters
        if pattern == ".....O":
            index += 6
            next_pattern = braille[index:index+6]
            output.append(braille_to_english_dict[next_pattern].upper())
        
#Handles numbers
        elif pattern == ".O.OOO":
            index += 6
            number_str = []
            while index < len(braille) and braille[index:index+6] != "......":
                number_str.append(str(list(numeric_to_braille_dict.values()).index(braille[index:index+6]) + 1))
                index += 6
            output.append(''.join(number_str))
            continue
        
#Handles Braille chars
        else:
            output.append(braille_to_english_dict.get(pattern, ""))
        
        index += 6
    
    return ''.join(output)

def convert_to_braille(text):
    output = []
    in_number_mode = False
    
    for char in text:
        if char.isdigit():
            if not in_number_mode:
                output.append(".O.OOO")  
                in_number_mode = True
            output.append(numeric_to_braille_dict[char])
        
        elif char.isalpha():
            if in_number_mode:
                output.append("......") 
                in_number_mode = False
            if char.isupper():
                output.append(".....O")  #Indicates capital letters
            output.append(english_map_to_braille[char.lower()])
        
        else:
            if in_number_mode:
                output.append("......") 
                in_number_mode = False
            output.append(english_map_to_braille.get(char, "......")) 
    
    return ''.join(output)



def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)
    
    input_msg = ' '.join(sys.argv[1:])
    
#Checks if all characters are valid Braille chars
    valid_chars = {'O', '.'}
    is_braille = all(c in valid_chars for c in input_msg)
    
    if is_braille:
        print(convert_to_english(input_msg))
    else:
        print(convert_to_braille(input_msg))

if __name__ == "__main__":
    main()
