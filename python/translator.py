import sys


braille_letters = {
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
    " ": "......"
}

braille_numbers = {    
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
}

braille_instructions = {
    "capital_next": ".....O",
    "decimal_next": ".O...O",
    "number_next": ".O.OOO"
}

def to_braille(input_string):
    translated_text = []
    is_number_mode = False
    is_decimal_mode = False

    for char in input_string:
        if char.isupper():
            translated_text.append(braille_instructions["capital_next"])
            char = char.lower()
        if char == '.':
            if not is_decimal_mode:
                translated_text.append(braille_instructions["decimal_next"])
                is_decimal_mode = True
            translated_text.append(braille_numbers.get(char, '??????'))
        elif char.isdigit() or char in braille_numbers:
            if not is_number_mode:
                translated_text.append(braille_instructions["number_next"])
                is_number_mode = True
            translated_text.append(braille_numbers.get(char, '??????'))
            is_decimal_mode = False
        elif char in braille_letters:
            if is_number_mode or is_decimal_mode:
                is_number_mode = False
                is_decimal_mode = False
            translated_text.append(braille_letters.get(char, '??????'))
        else:
            translated_text.append('??????')
    
    return ''.join(translated_text)

def to_english(input_string):
    braille_to_characters = {v: k for k, v in braille_letters.items()}
    braille_to_numbers = {v: k for k, v in braille_numbers.items()}
    braille_to_instructions = {v: k for k, v in braille_instructions.items()}
    
    segments = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
    translated_text = []
    is_number_mode = False
    is_decimal_mode = False
    is_capital_next = False

    for segment in segments:
        if segment in braille_to_instructions:
            instruction = braille_to_instructions[segment]
            if instruction == "capital_next":
                is_capital_next = True
            elif instruction == "number_next":
                is_number_mode = True
            elif instruction == "decimal_next":
                is_decimal_mode = True
            continue
        
        if is_number_mode:
            if segment == "......":
                is_number_mode = False
                translated_text.append(braille_to_characters.get(segment, '?'))
            else:
                translated_text.append(braille_to_numbers.get(segment, '?'))
            is_decimal_mode = False
        elif is_decimal_mode:
            translated_text.append(braille_to_numbers.get(segment, '?'))
            is_decimal_mode = False
        else:
            char = braille_to_characters.get(segment, '?')
            if is_capital_next:
                char = char.upper()
                is_capital_next = False
            translated_text.append(char)

    return ''.join(translated_text)

def detect_input(input_string):
    if set(input_string) <= {"O", "."} and len(input_string.replace(" ", "")) % 6 == 0:
        return 'braille'
    else:
        return 'english'

if __name__ == "__main__":
    command_args = sys.argv
    input_string = ' '.join(command_args[1:])
    input_type = detect_input(input_string)

    if input_type == 'braille':
        output = to_english(input_string)
    else:
        output = to_braille(input_string)
    print(output)