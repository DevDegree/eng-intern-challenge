import sys

eng_to_brl = {
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

number_to_brl = {
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

braille_to_eng = {v: k for k, v in eng_to_brl.items()}
braille_to_num = {v: k for k, v in number_to_brl.items()}

capital_follows = ".....O"
number_follows = ".O.OOO"
space = "......"

def isBraille(input):
    return not any(char not in 'O.' for char in input)


def translate(user_input): 
    if isBraille(user_input) and len(user_input) >= 6:
        output_string = translate_brl_to_eng(user_input)
    else:
        output_string = translate_eng_to_brl(user_input)


    return output_string

def translate_eng_to_brl(text):
    translated_text = ''
    previous_number = False
    for char in text:
        if char.isupper():
            translated_text += capital_follows
            char = char.lower()

        if char.isdigit():
            if not previous_number:
                translated_text += number_follows
                previous_number = True
            translated_text += number_to_brl.get(char)
        elif char == " ":
            translated_text += space
        else:
            previous_number = False
            translated_text += eng_to_brl.get(char)
    return translated_text

def translate_brl_to_eng(text):
    translated_text = ''
    uppercase_next = False
    number_next = False

    for i in range(0, len(text), 6):
        b_char = text[i:i+6]

        if b_char == capital_follows:
            uppercase_next = True
            continue
        if b_char == number_follows:
            number_next = True
            continue

        if b_char == space:
            translated_text += " "
            number_next = False
        elif uppercase_next:
            translated_text += braille_to_eng.get(b_char, "").upper()
            uppercase_next = False
        elif number_next:
            translated_text += braille_to_num.get(b_char, "")
        else:
            translated_text += braille_to_eng.get(b_char, "")

    return translated_text

        

if __name__ == "__main__":
    user_input = ' '.join(sys.argv[1:])
    output = translate(user_input)
    print(output) 




