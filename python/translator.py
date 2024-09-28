import sys

# Map english alphabet to braille
eng_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
}

num_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

braille_capital = '.....O'
braille_number = '.O.OOO'
braille_space = '......'

# Reverse mapping for braille to english translation
braille_to_eng = {v: k for k, v in eng_to_braille.items()}
braille_to_num = {v: k for k, v in num_to_braille.items()}

# Check if input is braille or english
def is_braille(input: str) -> bool:
    for char in input:
        if char not in "O.":
            return False
    return True

# Translate from english to braille
def translate_to_braille(text: str) -> str:
    result = ""
    currentNum = False

    # Iterate through each character in input string
    for char in text:
        # If we encounter a number
        if char.isdigit():
            # First number in series, set to True
            if not currentNum:
                currentNum = True
                result += braille_number
            result += num_to_braille[char]
        elif char == " ":
            currentNum = False
            result += braille_space
        # If we encounter a letter
        else:
            if char.isupper():
                result += braille_capital
            result += eng_to_braille[char.lower()]
    
    return result

# Translate from braille to english
def translate_to_english(text: str) -> str:
    result = ""
    currentNum = False
    currentCapital = False

    for i in range(0, len(text), 6):
        # Split string into sections of 6
        char = text[i : i + 6]

        if char == braille_capital:
            currentCapital = True
        elif char == braille_number:
            currentNum = True
        elif char == braille_space:
            currentNum = False
            result += " "
        else:
            if currentNum:
                result += braille_to_num[char]
            else:
                if currentCapital:
                    result += braille_to_eng[char].upper()
                    currentCapital = False
                    continue
                result += braille_to_eng[char]

    return result

def main():
    input_str = " ".join(sys.argv[1:])

    if is_braille(input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()