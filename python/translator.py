import sys

def main(input_text):
    braille_map = create_braille_map()

    if is_braille(input_text):
        print(braille_to_english(input_text, braille_map))
    else:
        print(english_to_braille(input_text, braille_map))

def is_braille(input_text):
    return set(input_text) <= {"O", "."}

def create_braille_map():
    return {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
        "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
        "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO", "capital": ".....O", "number": ".O.OOO", " ": "......"
    }

def english_to_braille(english_text, braille_map):
    result = []
    in_number_mode = False

    for char in english_text:
        if char.isupper():
            result.append(braille_map["capital"])
            char = char.lower()

        if char.isdigit():
            if not in_number_mode:
                result.append(braille_map["number"])
                in_number_mode = True
            mapped_letter = map_digit_to_braille_letter(char)
            result.append(braille_map[mapped_letter])
        elif char == " ":
            result.append(braille_map[" "])
            in_number_mode = False
        else:
            result.append(braille_map.get(char, "??????"))
            in_number_mode = False

    return "".join(result)

def braille_to_english(braille_text, braille_map):
    reverse_map = {v: k for k, v in braille_map.items()}
    result = []
    capital_next = number_mode = False

    for i in range(0, len(braille_text), 6):
        symbol = braille_text[i:i+6]

        if symbol == braille_map["capital"]:
            capital_next = True
        elif symbol == braille_map[" "]:
            result.append(" ")
            number_mode = False
        elif symbol == braille_map["number"]:
            number_mode = True
        elif number_mode:
            letter = reverse_map.get(symbol, "?")
            digit = map_braille_letter_to_digit(letter)
            result.append(digit)
        else:
            letter = reverse_map.get(symbol, "?")
            if capital_next:
                result.append(letter.upper())
                capital_next = False
            else:
                result.append(letter)

    return "".join(result)

def map_digit_to_braille_letter(digit):
    return chr(ord("a") + int(digit) - 1) if digit != "0" else "j"

def map_braille_letter_to_digit(letter):
    return str(ord(letter) - ord("a") + 1) if letter != "j" else "0"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        main(input_text)
    else:
        print("Please provide input for translation")
