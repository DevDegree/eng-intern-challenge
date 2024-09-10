import sys

letter_dic = {
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
     "p": "OOOOO.",
     "q": "OOOOOO",
     "r": "O.OOO.",
     "s": ".OO.O.",
     "t": ".OOOO.",
     "u": "O...OO",
     "v": "O.O.OO",
     "w": ".OOO.O",
     "x": "OO..OO",
     "y": "OO.OOO",
     "z": "O..OOO",
    
     ".": ".O.OO.",
     ",": ".O....",
     "?": ".O.O.O",
     "!": ".O.O.O",
     ":": ".O..O.",
     ";": ".O..O.",
     "-": ".O....",
     "/": ".O..O.",
     "<": ".OO..O",
     ">": "O..OO.",
     "(": "O.O..O",
     ")": ".O.OO.",
     " ": "......",
}

num_dic = {     
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

braille_letter_dic = {v: k for k, v in letter_dic.items()}
braille_num_dic = {v: k for k, v in num_dic.items()}

CAPITAL = ".....O"
DECIMAL = ".O...O"
NUMBER = ".O.OOO"

def english_to_braille(text: str) -> str:
    braille_text = ""
    num_toggle = False
    for char in text:
        if char.isupper():
            braille_text += CAPITAL
        if char.isdigit():
            if not num_toggle:
                braille_text += NUMBER
            num_toggle = True
            braille_text += num_dic[char]
        else:
            braille_text += letter_dic[char.lower()]
            if char == " ":
                num_toggle = False
                
    return braille_text

def braille_to_english(text):
    english_text = ""
    is_capital = False
    is_number = False
    i = 0
    while i < len(text):
        current_braille = text[i:i+6]
        if current_braille == CAPITAL:
            is_capital = True
            i += 6
            continue
        elif current_braille == DECIMAL:
            english_text += "."
            i += 6
            continue
        elif current_braille == NUMBER:
            is_number = True
            i += 6
            continue
        
        if current_braille == "......":
            english_text += " "
            is_number = False
        elif is_number:
            english_text += braille_num_dic[current_braille]
        else:
            if current_braille in braille_letter_dic:
                char = braille_letter_dic[current_braille]
                if is_capital:
                    char = char.upper()
                    is_capital = False
                english_text += char
            else:
                english_text += "?"
        i += 6
    
    return english_text

def braille_checker(text):
    if ".O" in text:
        return True
    return False

def main():
    args = sys.argv
    args = " ".join(args[1:])
    if braille_checker(args):
        print(braille_to_english(str(args)))
    else:
        print(english_to_braille(str(args)))

if __name__ == "__main__":
    main()
    


