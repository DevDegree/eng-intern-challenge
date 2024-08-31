import sys

CAPITAL_FOLLOWS_SYMBOL = ".....O"
NUMBER_FOLLOWS_SYMBOL = ".O.OOO"

# Hashmap for quick character search
english_map = {
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
    " ": "......",
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

# Reverse the hashmap for quick braille to english search
braille_char_map = {braille: english for english, braille in list(english_map.items())[:39]}
braille_num_map = {braille: english for english, braille in list(english_map.items())[39:]}


def isBraille(text: str) -> bool:
    '''Check if the input text is in braille format'''
    if len(text) % 6 == 0 and set(text).issubset({"O", "."}):  
        return True


def english_to_braille(text: str) -> str:
    '''Convert english text to braille'''
    braille = ""
    isFirstDigit = True
    for char in text:
        if char.isupper():  # Add capital follows symbol
            braille += CAPITAL_FOLLOWS_SYMBOL
            char = char.lower()
        elif char.isdigit() and isFirstDigit:  # Add number follows symbol only at the start of a number
            braille += NUMBER_FOLLOWS_SYMBOL
            isFirstDigit = False
        elif char == " ":  # Reset first number flag once a space is encountered (end of number)
            isFirstDigit = True
        braille += english_map[char]
    return braille


def braille_to_english(text: str) -> str:
    '''Convert braille text to english'''
    english = ""
    isCapital = False
    isNum = False
    for i in range(0, len(text), 6):
        braille_char = text[i : i + 6]

        if braille_char == CAPITAL_FOLLOWS_SYMBOL: # Set capital flag once a capital follows symbol is encountered
            isCapital = True
            continue
        elif braille_char == NUMBER_FOLLOWS_SYMBOL: # Set number flag once a number follows symbol is encountered
            isNum = True
            continue
        elif braille_char == "......": # Reset number flag once a space is encountered (end of number)
            isNum = False

        if isCapital: # Convert to uppercase if capital flag is true
            english += braille_char_map[braille_char].upper()
            isCapital = False
        elif isNum: # Convert to number if number flag is true
            english += braille_num_map[braille_char]
        else: # else use the normal english character
            english += braille_char_map[braille_char]
    return english


def main() -> None:
    argTxt = " ".join(sys.argv[1:])

    if isBraille(argTxt):
        print(braille_to_english(argTxt))
    else:
        print(english_to_braille(argTxt))


if __name__ == "__main__":
    main()
