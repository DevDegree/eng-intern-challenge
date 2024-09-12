import sys

# Dictionaries for Braille translation
alphabets_to_braille = {
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
}

capital_to_braille = {
    "capital": ".....O",
    " ": "......"
}

nums_to_braille = {
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
    "number": ".O.OOO",
}

def determine_input_type(input_string):
    if "." in input_string and "0" in input_string and len(input_string) % 6 == 0:
        return get_english(input_string)
    else:
        return get_braille(input_string)

def get_english(output):
    word = ""
    number_mode = False
    is_capital = False

    for x in range(0, len(output), 6):
        braille_chunk = output[x:x+6]

        if braille_chunk == ".....O":
            is_capital = True
            number_mode = False
            continue
        
        if braille_chunk == "......":
            word += " "
            number_mode = False
            continue

        if braille_chunk == ".O.OOO":
            number_mode = True
            continue

        if number_mode:
            if braille_chunk in nums_to_braille.values():
                for key, value in nums_to_braille.items():
                    if value == braille_chunk:
                        word += key
                number_mode = False
        else:
            if braille_chunk in alphabets_to_braille.values():
                for key, value in alphabets_to_braille.items():
                    if value == braille_chunk:
                        english_char = key
                if is_capital:
                    english_char = english_char.upper()
                    is_capital = False
                word += english_char

    return word

def get_braille(english):
    word = ""
    number_mode = False

    for x in english:
        if x.isupper():
            word += capital_to_braille["capital"]
            x = x.lower()
        
        if x in alphabets_to_braille:
            if number_mode:
                word += nums_to_braille["number"]
                number_mode = False
            word += alphabets_to_braille[x]
        elif x == " ":
            word += capital_to_braille[x]
            number_mode = False
        elif x.isdigit():
            if not number_mode:
                word += nums_to_braille["number"]
                number_mode = True
            word += nums_to_braille[x]
    
    return word

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    output = determine_input_type(input_text)
    print(output)

if __name__ == "__main__":
    main()
