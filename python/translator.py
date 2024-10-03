import sys

braille_letters = { "a":"O.....", "b":"O.O...", "c":"OO....", "d":"OO.O..", "e":"O..O..", "f":"OOO...", "g":"OOOO..", "h":"O.OO..", "i":".OO...", "j":".OOO..", "k":"O...O.", "l":"O.O.O.", "m":"OO..O.",
               "n":"OO.OO.", "o":"O..OO.", "p":"OOO.O.", "q":"OOOOO.", "r":"O.OOO.", "s":".OO.O.", "t":".OOOO.", "u":"O...OO", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO", "z":"O..OOO",
                ".":"..OO.O", ",":"..O...", "?":"..O.OO", "!":"..OOO.", ":":"..OO..", ";":"..O.O.", "-":"....OO", "/":".O..O.",  "(":"O.O..O", ")":".O.OO.", " ":"......"}

braille_num = {"1":"O.....", "2":"O.O...", "3":"OO....", "4":"OO.O..", "5":"O..O..", "6":"OOO...", "7":"OOOO..", "8":"O.OO..", "9":".OO...", "0":".OOO.."}

conditions = {"capital_follows":".....O", "decimal_follows":".O...O", "number_follows":".O.OOO",}

reverse_braille_letters = {value: key for key, value in braille_letters.items()}
reverse_braille_num = {value: key for key, value in braille_num.items()}
reverse_conditions = {value: key for key, value in conditions.items()}

def english_to_braille(input_string):
    braille_string = ""
    num_flag = False

    for char in input_string:
        if char.isupper():
            braille_string += conditions["capital_follows"] + braille_letters[char.lower()]
        elif char == " ":
            num_flag = False
            braille_string += braille_letters[char]
        elif char == ".":
            if num_flag == True:
                braille_string += conditions["decimal_follows"]
            braille_string += braille_letters[char]
        elif char in braille_letters:
            braille_string += braille_letters[char]
        elif char in braille_num:
            if num_flag == False:
                braille_string += conditions["number_follows"]
                num_flag = True
            braille_string += braille_num[char]
        else:
            continue  # skip characters that are not defined in dictionaries

    print(braille_string)

def braille_to_english_letters(input_string):    
    english_string = ""
    num_flag = False
    i = 0
    while i < len(input_string):
        braille_segment = input_string[i : i + 6]

        if braille_segment in reverse_conditions:
            condition = reverse_conditions[braille_segment]
            if condition == "capital_follows":
                if i + 6 < len(input_string):
                    next_segment = input_string[i + 6 : i + 12]
                    if next_segment in reverse_braille_letters:
                        english_string += reverse_braille_letters[next_segment].upper()
                i += 12
            elif condition == "number_follows" or condition == "decimal_follows":
                num_flag = True
                i += 6
        elif num_flag and braille_segment in reverse_braille_num:
            english_string += reverse_braille_num[braille_segment]
            i += 6
        elif braille_segment in reverse_braille_letters:
            english_string += reverse_braille_letters[braille_segment]
            i += 6
            if reverse_braille_letters[braille_segment] == " ":
                num_flag = False
        else:
            i += 6
    print(english_string)

def main():
    if len(sys.argv) < 2:
        print("Please enter a string or braille code.")
    
    braille_symbols = {"O", "."}

    input_string = sys.argv[1:]
    input_string = " ".join(input_string).strip()

    check_if_braille = set(input_string)

    if input_string and len(input_string) > 5 and check_if_braille.issubset(braille_symbols):
        braille_to_english_letters(input_string)
    else:
        english_to_braille(input_string)
    

if __name__ == '__main__':
    main()