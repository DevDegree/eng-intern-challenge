import sys

def translator(arguments):
    input_string = " ".join(arguments)
    if set(input_string).issubset(set("O.")):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

def braille_to_text(braille):
    result = ""
    is_number_mode = False
    capitalize_next = False
    i = 0
    while i < len(braille):
        braille_char = braille[i:i+6]
        eng_char = brailleToEng(braille_char)
        
        if eng_char == "CAPITAL":
            capitalize_next = True
        elif eng_char == "NUMBER":
            is_number_mode = True
        elif eng_char == " ":
            is_number_mode = False
            result += eng_char
        else:
            if capitalize_next:
                result += eng_char.upper()
                capitalize_next = False
            elif is_number_mode:
                result += str("1234567890"["abcdefghij".index(eng_char.lower())])
            else:
                result += eng_char.lower()
        i += 6
    return result

def text_to_braille(text):
    result = ""
    is_number_mode = False
    for char in text:
        if char.isupper():
            result += engToBraille("CAPITAL")
            result += engToBraille(char.lower())
        elif char.isdigit():
            if not is_number_mode:
                result += engToBraille("NUMBER")
                is_number_mode = True
            result += engToBraille("abcdefghij"["1234567890".index(char)])
        else:
            if char == " ":
                is_number_mode = False
            result += engToBraille(char.lower())
    return result

def engToBraille(string):
    switcher = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
        "z": "O..OOO",
        "CAPITAL": ".....O", "NUMBER": ".O.OOO", " ": "......"
    }
    return switcher.get(string, "")

def brailleToEng(string):
    switcher = {v: k for k, v in engToBraille.items()}
    return switcher.get(string, "")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(translator(arguments))