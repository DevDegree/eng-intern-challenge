import sys

ENG_TO_BRAILLE_MAP = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    " ": "......"
}
BRAILLE_TO_ENG_MAP = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", 
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", 
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", 
    "......": " "
}
ENG_TO_BRAILLE_MAP_NUMBERS = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}
BRAILLE_TO_ENG_MAP_NUMBERS = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

CAPITALIZE_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"
BRAILLE_SPACE = "......"

def main(input: str) -> str:
    if is_braille(input):
        return braille_to_eng(input)
    else:
        return eng_to_braille(input)

def is_braille(input: str) -> bool:
    if len(input) % 6 != 0:
        return False
    
    for char in input:
        if char not in ['O', '.']:
            return False
    return True

def braille_to_eng(input: str) -> str:
    result = []
    braille_chars = [input[i : i + 6] for i in range(0, len(input), 6)]

    capital_flag = False
    number_flag = False

    for char in braille_chars:
        if char == CAPITALIZE_FOLLOWS:
            capital_flag = True
        elif char == NUMBER_FOLLOWS:
            number_flag = True
        else:
            eng_char = BRAILLE_TO_ENG_MAP[char]
            
            if char == BRAILLE_SPACE:
                number_flag = False

            if capital_flag:
                capital_flag = False
                eng_char = eng_char.upper()
            
            if number_flag:
                eng_char = BRAILLE_TO_ENG_MAP_NUMBERS[char]
            
            result.append(eng_char)
            
    return "".join(result)

def eng_to_braille(input: str) -> str:
    result = []
    
    number_flag = False
    
    for char in input:
        if char.isupper():
            result.append(CAPITALIZE_FOLLOWS)
            braille_char = ENG_TO_BRAILLE_MAP[char.lower()]
        elif char.isnumeric():
            if not number_flag:
                result.append(NUMBER_FOLLOWS)
                number_flag = True
            braille_char = ENG_TO_BRAILLE_MAP_NUMBERS[char]
        else:
            if char == " ":
                number_flag = False
            braille_char = ENG_TO_BRAILLE_MAP[char]
        result.append(braille_char)

    return "".join(result)
            

if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    result = main(input)
    print(result)