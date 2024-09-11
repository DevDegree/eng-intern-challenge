import sys

braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOOOO.", "q": "OOOOOO", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.",
    "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
    " ": "......"
}

num_map = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

braille_to_text = {value: key for key, value in braille_map.items()}
num_to_text = {value: key for key, value in num_map.items()}

caps_indicator = ".....O"
num_indicator = ".O.OOO"

def is_braille_input(input_data):
    return set(input_data) <= {"O", "."} and len(input_data) % 6 == 0

def braille_to_english(braille_code):
    result = []
    caps_active = False
    num_active = False

    for i in range(0, len(braille_code), 6):
        chunk = braille_code[i:i+6]

        if chunk == caps_indicator:
            caps_active = True
            continue
        if chunk == num_indicator:
            num_active = True
            continue
        if chunk == "......":
            result.append(" ")
            num_active = False
        elif num_active:
            result.append(num_to_text.get(chunk, "?"))
        else:
            char = braille_to_text.get(chunk, "?")
            if caps_active:
                char = char.upper()
                caps_active = False
            result.append(char)

    return ''.join(result)

def english_to_braille(text):
    braille = []
    num_active = False

    for char in text:
        if char.isupper():
            braille.append(caps_indicator)
            char = char.lower()
        if char.isdigit():
            if not num_active:
                braille.append(num_indicator)
            braille.append(num_map[char])
            num_active = True
        else:
            braille.append(braille_map.get(char, "......"))
            if char == " ":
                num_active = False

    return ''.join(braille)

def main():
    user_input = " ".join(sys.argv[1:])

    if is_braille_input(user_input):
        print(braille_to_english(user_input))
    else:
        print(english_to_braille(user_input))

if __name__ == "__main__":
    main()
