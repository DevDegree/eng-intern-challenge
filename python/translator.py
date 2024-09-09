import sys

english_char_to_braille_char = {
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
    "capital follows": ".....O",
    "number follows": ".O.OOO",
}

number_to_braille_char = {
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

braille_char_to_english_char = {v: k for k, v in english_char_to_braille_char.items()}
braille_char_to_number = {v: k for k, v in number_to_braille_char.items()}

def english_to_braille(input):
    number = False
    result = []
    for char in input:
        if char.isdigit():
            if not number:
                number = True
                result.append(english_char_to_braille_char["number follows"])
            result.append(number_to_braille_char[char])
        elif char.isupper():
            result.append(english_char_to_braille_char["capital follows"])
            result.append(english_char_to_braille_char[char.lower()])
        else:
            result.append(english_char_to_braille_char[char])
            if char == " ":
                number = False
    return "".join(result)

def braille_to_english(input):
    capitalize = False
    number = False
    result = []
    for i in range(0, len(input), 6):
        if input[i:i+6] == english_char_to_braille_char["capital follows"]:
            capitalize = True
            continue
        if input[i:i+6] == english_char_to_braille_char["number follows"]:
            number = True
            continue
        if input[i:i+6] == english_char_to_braille_char[" "]:
            number = False
        
        if number:
            result.append(braille_char_to_number[input[i:i+6]])
        elif capitalize:
            result.append(braille_char_to_english_char[input[i:i+6]].upper())
            capitalize = False
        else:
            result.append(braille_char_to_english_char[input[i:i+6]])
    return "".join(result)

def main():
    input = " ".join(sys.argv[1:])
    if all(c in "O." for c in input):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))

if __name__ == "__main__":
    main()

'''
.O.OOOOO.O..O.O...
.O.OOOOO.O...O.OOOO.O...
'''
