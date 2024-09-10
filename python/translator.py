
import sys

# Dictionaries for Braille to English and numbers conversion
braille_to_english = {
    "O.....": "a",  "O.O...": "b",  "OO....": "c",  "OO.O..": "d",  "O..O..": "e",
    "OOO...": "f",  "OOOO..": "g",  "O.OO..": "h",  ".OO...": "i",  ".OOO..": "j",
    "O...O.": "k",  "O.O.O.": "l",  "OO..O.": "m",  "OO.OO.": "n",  "O..OO.": "o",
    "OOO.O.": "p",  "OOOOO.": "q",  "O.OOO.": "r",  ".OO.O.": "s",  ".OOOO.": "t",
    "O...OO": "u",  "O.O.OO": "v",  ".OOO.O": "w",  "OO..OO": "x",  "OO.OOO": "y",
    "O..OOO": "z",  "......": "space", ".....O": "capital", ".O.OOO": "number"
}

braille_to_nums = {
    "O.....": "1",  "O.O...": "2",  "OO....": "3",  "OO.O..": "4",
    "O..O..": "5",  "OOO...": "6",  "OOOO..": "7",  "O.OO..": "8",  ".OO...": "9",
    ".OOO..": "0"
}

english_to_braille = {
    "a": "O.....",  "b": "O.O...",  "c": "OO....",  "d": "OO.O..",  "e": "O..O..",
    "f": "OOO...",  "g": "OOOO..",  "h": "O.OO..",  "i": ".OO...",  "j": ".OOO..",
    "k": "O...O.",  "l": "O.O.O.",  "m": "OO..O.",  "n": "OO.OO.",  "o": "O..OO.",
    "p": "OOO.O.",  "q": "OOOOO.",  "r": "O.OOO.",  "s": ".OO.O.",  "t": ".OOOO.",
    "u": "O...OO",  "v": "O.O.OO",  "w": ".OOO.O",  "x": "OO..OO",  "y": "OO.OOO",
    "z": "O..OOO",  "0": ".OOO..",  "1": "O.....",  "2": "O.O...",  "3": "OO....",
    "4": "OO.O..",  "5": "O..O..",  "6": "OOO...",  "7": "OOOO..",  "8": "O.OO..",
    "9": ".OO...", " ": "......",  "capital": ".....O", "number": ".O.OOO"
}

def is_braille(string):
    # Check if input string is valid Braille by ensuring length is divisible by 6
    return len(string) % 6 == 0 and all(chunk in braille_to_english for chunk in [string[i:i+6] for i in range(0, len(string), 6)])

def braille_to_text(braille_str):
    # Convert Braille to text (English or numbers)
    res = []
    is_caps = False
    is_num = False
    
    for chunk in [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]:
        char = braille_to_english.get(chunk, "")
        if char == "capital":
            is_caps = True
        elif char == "number":
            is_num = True
        elif char == "space":
            res.append(" ")
            is_num = False
        else:
            if is_caps:
                res.append(char.upper())
                is_caps = False
            elif is_num:
                res.append(braille_to_nums.get(chunk, ""))
            else:
                res.append(char)
    
    return "".join(res)

def text_to_braille(text):
    # Convert text (English or numbers) to Braille
    res = []
    is_num = False

    for char in text:
        if char.isdigit():
            if not is_num:
                res.append(english_to_braille["number"])
                is_num = True
            res.append(english_to_braille[char])
        elif char.isupper():
            res.append(english_to_braille["capital"])
            res.append(english_to_braille[char.lower()])
        else:
            res.append(english_to_braille[char])
            if char == " ":
                is_num = False  # Reset number mode after space

    return "".join(res)

def main(args):
    
    text = ' '.join(args[1:])

    if is_braille(text):
        print(braille_to_text(text))
    else:
        print(text_to_braille(text))

if __name__ == "__main__":
    
    main(sys.argv)