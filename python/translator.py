

alphabet = {
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
        "z": "O..OOO"
    }

numbers = {
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "0": ".OOO.."
    }

caps = ".....O"
decimal = ".O...O"
num = ".O.OOO"
    

punctuation = {
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
        " ": "......"
    }

reverse_alphabet = {v: k for k, v in alphabet.items()}
reverse_numbers = {v: k for k, v in numbers.items()}
reverse_punctuation = {v: k for k, v in punctuation.items()}

def mode_choice(input_txt):
    if all(c in "O." for c in input_txt):
        return "b2e"
    else:
        return "e2b"
    
def translate_to_braille(text):
    braille_text = ""
    num_flag = False
    caps_flag = False

    for char in text:
        if char.isupper():
            if not caps_flag:
                braille_text += caps
                caps_flag = True
            braille_text += alphabet[char.lower()]
            caps_flag = False
        elif char.isdigit():
            if not num_flag:
                braille_text += num
                num_flag = True
            braille_text += numbers[char]
        elif char in punctuation:
            braille_text += punctuation[char]
            if char == " ":
                num_flag = False
        else:
            braille_text += alphabet[char]
    return braille_text

def translate_to_english(braille):
    english_text = ""
    index = 0
    num_flag = False
    caps_flag = False

    while index < len(braille):
        chunk = braille[index:index+6]

        if chunk == caps:
            caps_flag = True
        elif chunk == num:
            num_flag = True
        elif num_flag:
            english_text += reverse_numbers[chunk]
        elif caps_flag:
            english_text += reverse_alphabet[chunk].upper()
            caps_flag = False
        elif chunk in reverse_alphabet:
            english_text += reverse_alphabet[chunk]
        elif chunk in reverse_punctuation:
            english_text += reverse_punctuation[chunk]
            num_flag = False
            caps_flag = False
        
        
        index += 6

    return english_text


def main():
    text = input()
    
    mode = mode_choice(text)

    if mode == "e2b":
        output = translate_to_braille(text)
    elif mode == "b2e":
        output = translate_to_english(text)

    print(output)
    

if __name__ == "__main__":
    main()