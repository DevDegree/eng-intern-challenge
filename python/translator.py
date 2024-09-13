# translate braile to english

commands = {
    "capital": ".....O", 
    "number": ".O.OOO", 
}

chars = {
    "A": "O.....", 
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..", 
    "F": "OOO...",
    "G": "OOOO..", 
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.", 
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.", 
    "P": "OOO.O.", 
    "Q": "OOOOO.", 
    "R": "O.OOO.", 
    "S": ".OO.O.", 
    "T": ".OOOO.", 
    "U": "O...OO", 
    "V": "O.O.OO", 
    "W": ".OOO.O", 
    "X": "OO..OO", 
    "Y": "OO.OOO", 
    "Z": "O..OOO", 
    ".": "..OO.O", 
    ",": "..O...", 
    "?": "..OOO.", 
    "!": "..OOO.", 
    ":": "..O.O.", 
    ";": "..O.O.", 
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O", 
    ">": "O..OO.", 
    "(": "O.O..O",
    ")": ".O.OO.", 
    " ": "......"

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
    "0": ".OOO..",
}

braille_to_char = {braille: char for char, braille in chars.items()}
char_to_braille = {char: braille for char, braille in chars.items()}

braille_to_command = {braille: command for command, braille in commands.items()}
command_to_braille = {command: braille for command, braille in commands.items()}

braille_to_num = {braille: num for num, braille in numbers.items()}
num_to_braille = {num: braille for num, braille in numbers.items()}

def translate_braile_chars(phrase):
    result = ""
    isNumber = False
    isCapital = False
    for i in range(0, len(phrase), 6):
        ch = phrase[i:i+6]
        if ch in braille_to_command:
            if braille_to_command[ch] == "capital":
                isCapital = True
            if braille_to_command[ch] == "number":
                isNumber = True

        elif braille_to_char.get(ch, None) == " ":
                isNumber = False
                result += " "

        elif not isNumber:
            if isCapital:
                result += braille_to_char[ch]
                isCapital = False
            else:
                result += braille_to_char[ch].lower()

        else:
            result += braille_to_num[ch]

    return result

def translate_chars_to_braile(phrase):
    result = ""
    isNumber = False
    for ch in phrase:
        if ch in char_to_braille or chr(ord(ch) - 32) in char_to_braille:
            isNumber = False
            if ch.isupper():
                result += command_to_braille["capital"]
                result += char_to_braille[ch]
            else:
                result += char_to_braille[chr(ord(ch) - 32)]
        else:
            if not isNumber:
                isNumber = True
                result += command_to_braille["number"]
            result += num_to_braille[ch]

    return result

if __name__ == "__main__":
    import sys
    result = ""
    strings = sys.argv[1:]
    for i in range(len(strings)):
        if not all(char in "O." for char in strings[i]):
            result += (translate_chars_to_braile(strings[i]))
            if i < len(strings) - 1:
                result += char_to_braille[" "]
        else:
            result += translate_braile_chars(strings[i])
            print(result)
            if i < len(strings) - 1:
                result += " "
    print(result)
