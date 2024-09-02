import sys

braille_english_letters = {
    "a":"O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
}
braille_english_numbers={
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "O":".OOO..",
}

braille_english_specials={
    "capital":".....O",
    "decimal":".O...O",
    "number":".O.OOO",
    " ":"......",
    ".":"..OO.O",
    ",":"..O...",
    "?":"..O.OO",
    "!":"..OOO.",
    ":":"..OO..",
    ";":"..O.O.",
    "-":"....OO",
    "/":".O..O.",
    "<":".OO..O",
    ">":"O..OO.",
    "(":"O,O,,O",
    ")":".O.OO."
}

def input_type_checker(line):
    if len(line) % 6 == 0:
        if all(char in {'O', '.'} for char in line):
            return True #represents braille to english
    return False # represents english to braille

def braille_to_english(line):
    braille_to_char = {v: k for k, v in braille_english_letters.items()}
    braille_to_number = {v: k for k, v in braille_english_numbers.items()}
    braille_to_special = {v: k for k, v in braille_english_specials.items()}

    # Split the Braille text by 6-character chunks
    braille_chunks = [line[i:i+6] for i in range(0, len(line), 6)]
    
    result = []
    is_number_mode = False
    is_capital_mode = False
    
    for chunk in braille_chunks:
        if chunk in braille_to_special:
            special_char = braille_to_special[chunk]
            if special_char == "capital":
                is_capital_mode = True
                continue
            elif special_char == "number":
                is_number_mode = True
                continue
            elif special_char == " ":
                is_number_mode = False
                is_capital_mode = False
                result.append(" ")
                continue
        if is_number_mode:
            if chunk in braille_to_number:
                result.append(braille_to_number[chunk])
            else:
                result.append("?")  # In case of an unknown chunk
        else:
            if chunk in braille_to_char:
                char = braille_to_char[chunk]
                if is_capital_mode:
                    result.append(char.upper())
                    is_capital_mode = False
                else:
                    result.append(char)
            else:
                sys.stderr.write("braille to english failed.\n")  # In case of an unknown chunk
    
    return ''.join(result)

def english_to_braille(line):
    char_to_braille = braille_english_letters
    number_to_braille = braille_english_numbers
    special_to_braille = braille_english_specials

    result = []
    is_number_mode = False
    
    for char in line:
        if char.isalpha():
            if char.isupper():
                result.append(special_to_braille["capital"])
                result.append(char_to_braille[char.lower()])
            else:
                if is_number_mode:
                    result.append(special_to_braille["number"])
                    is_number_mode = False
                result.append(char_to_braille[char])
        elif char.isdigit():
            if not is_number_mode:
                result.append(special_to_braille["number"])
                is_number_mode = True
            result.append(number_to_braille[char])
        elif char in braille_english_letters:
            result.append(char_to_braille.get(char, '?'))
        elif char == ' ':
            result.append(special_to_braille[" "])
            is_number_mode = False
        elif char in ".?!:;,/-<>()":
            result.append(char_to_braille.get(char, '?'))
        else:
            sys.stderr.write("english to braille failed.\n")

    return ''.join(result)

if __name__ == "__main__":
    line = input()
    if input_type_checker(line) == True:
        print(braille_to_english(line))
    else:
        print(english_to_braille(line))