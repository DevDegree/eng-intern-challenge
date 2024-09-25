import sys

english_to_braille_map = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OO.OO",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    " ": "......",
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "capital follows": ".....O",
    "number follows": ".O.OOO",
}

number_to_braille = {
    "0": ".OOO..",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
}

braille_to_english = {v: k for k, v in english_to_braille_map.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}

def translate_to_braille(input_str):
    translated = []
    for char in input_str:
        if char.isalpha():
            if char.isupper():
                translated.append(english_to_braille_map["capital follows"])
                translated.append(english_to_braille_map[char])
            else:
                translated.append(english_to_braille_map[char.upper()])
        elif char.isdigit():
            if not translated or translated[-1] != english_to_braille_map["number follows"]:
                translated.append(english_to_braille_map["number follows"])
            translated.append(number_to_braille[char])
        else:
            translated.append(english_to_braille_map.get(char, english_to_braille_map[" "]))
    
    return ''.join(translated)

def translate_to_english(braille_str):
    translated = []
    is_capital = False
    is_number = False
    for i in range(0, len(braille_str), 6):
        group = braille_str[i:i+6]
        if group == english_to_braille_map["capital follows"]:
            is_capital = True
            continue
        elif group == english_to_braille_map["number follows"]:
            is_number = True
            continue

        if is_number:
            translated.append(braille_to_number.get(group, ''))
            is_number = False
        else:
            char = braille_to_english.get(group, ' ')
            if is_capital:
                char = char.upper()
                is_capital = False
            translated.append(char.lower())
    
    return ''.join(translated)

def main():
    if len(sys.argv) < 2:
        print("Please provide input for translation.")
        return

    input_str = ' '.join(sys.argv[1:])
    
    if all(char in 'O.' for char in input_str):
        print(translate_to_english(input_str))
    else:
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    main()