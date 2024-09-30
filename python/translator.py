import sys

BRAILLE_TO_ENGLISH = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
}

ENGLISH_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_ENGLISH.items()}
BRAILLE_TO_NUMBERS = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

NUMBERS_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_NUMBERS.items()}

special_chars_to_braille = {
    ".": "0.....",  
    ",": "0.0...",  
    "?": "00.0..",  
    "!": "00..0.",  
    ":": "0..00.",  
    ";": "0.00..",  
    "-": ".00...",  
    "/": ".0.0..",  
    "<": "0..0..",  
    ">": ".000..",  
    "(": "0...00",  
    ")": "00....", 
}

BRAILLE_SPACE = "......"
BRAILLE_CAPITAL = ".....O"
BRAILLE_NUMBER_SIGN = ".O.OOO"

def check_braille(text):
    if text in BRAILLE_TO_ENGLISH or text == BRAILLE_SPACE or text == BRAILLE_CAPITAL or text == BRAILLE_NUMBER_SIGN:
        return True
    return False

def braille_or_english(text):
    if len(text) % 6 == 0:
        index = 0
        while index < (len(text) // 6):
            braille_text = text[index:index + 6]
            if check_braille(braille_text):
                index+=6
            else:
                return "English"
        return "Braille"

def braille_to_english(braille):
    result = ""
    number = False
    capital = False
    for i in range(0, len(braille), 6):
        braille_text = braille[i:i + 6]
        if braille_text == BRAILLE_NUMBER_SIGN:
            number = True
        elif braille_text == BRAILLE_SPACE:
            if number:
                number = False
            result += " "
        elif braille_text == BRAILLE_CAPITAL:
            capital = True
        else:
            if number:
                result += BRAILLE_TO_NUMBERS[braille_text]
            elif capital:
                result += BRAILLE_TO_ENGLISH[braille_text].upper()
                capital = False
            else:
                result += BRAILLE_TO_ENGLISH[braille_text]
    return result

def english_to_braille(english):
    result = ""
    number = False
    for char in english:
        if number and not char.isdigit():
            number = False
            if char != " ":
                result += BRAILLE_SPACE
        if char == " ":
            result += BRAILLE_SPACE
        elif char.isupper():
            result += BRAILLE_CAPITAL
            result += ENGLISH_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            if not number:
                number = True
                result += BRAILLE_NUMBER_SIGN
            result += NUMBERS_TO_BRAILLE[char]
        elif char in special_chars_to_braille:
            result += special_chars_to_braille[char]
        else:
            result += ENGLISH_TO_BRAILLE[char]
    return result

def main():
    if len(sys.argv) < 2:
        print("ERROR: Missing arguments")
        return
    text = " ".join(sys.argv[1:]).strip()
    if braille_or_english(text) == "Braille":
        english = braille_to_english(text)
        print(english) 
    else:
        braille = english_to_braille(text)
        print(braille)

if __name__ == "__main__":
    main()