import sys

LETTER_TO_BRAILLE = {
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

NUMBER_TO_BRAILLE = {
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

SPECIAL_TO_BRAILLE = {
    "CAPITAL_FOLLOWS": ".....O",
    "NUMBER_FOLLOWS": ".O.OOO",
    " ": "......"
}

BRAILLE_TO_LETTER = {braille:letter for letter,braille in LETTER_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {braille:number for number,braille in NUMBER_TO_BRAILLE.items()}
BRAILLE_TO_SPECIAL = {braille:special for special,braille in SPECIAL_TO_BRAILLE.items()}

VALID_ENGLISH = LETTER_TO_BRAILLE | NUMBER_TO_BRAILLE | SPECIAL_TO_BRAILLE
VALID_BRAILLE = BRAILLE_TO_LETTER | BRAILLE_TO_NUMBER | BRAILLE_TO_SPECIAL


def is_braille(input:str)->bool: 
    """
    Check whether an inputted string is a valid braille sequence
    """
    if len(input)%6 != 0:
        return False
    
    cur_idx = 0
    while cur_idx+6 <= len(input):
        if input[cur_idx:cur_idx+6] not in VALID_BRAILLE:
            return False
        cur_idx+=6

    return True       

def is_english(input:str)->bool:
    """
    Check whether an inputted string is a valid english sequence
    """

    for char in input:
        if char.lower() not in VALID_ENGLISH:
            return False
        
    return True

def braille_to_english(input:str) -> str:
    CAPITALIZE_NEXT = False
    NUMBERS = False
    result = ""
    cur_idx = 0
    while cur_idx+6 <= len(input):
        cur_seq = input[cur_idx:cur_idx+6]
        if cur_seq == SPECIAL_TO_BRAILLE["CAPITAL_FOLLOWS"]:
            CAPITALIZE_NEXT = True
        elif cur_seq == SPECIAL_TO_BRAILLE["NUMBER_FOLLOWS"]:
            NUMBERS = True
        elif cur_seq in BRAILLE_TO_LETTER:
            if CAPITALIZE_NEXT:
                result += BRAILLE_TO_LETTER[cur_seq].upper()
                CAPITALIZE_NEXT = False
            elif NUMBERS:
                result += BRAILLE_TO_NUMBER[cur_seq]
            else:
                result += BRAILLE_TO_LETTER[cur_seq]
        elif cur_seq == SPECIAL_TO_BRAILLE[" "]:
            result += BRAILLE_TO_SPECIAL[cur_seq]
            NUMBERS = False
        
        cur_idx += 6

    return result
    
def english_to_braille(input:str) -> str:
    
    NUMBERS_STARTED = False
    result = ""

    for character in input:
        if character in NUMBER_TO_BRAILLE:
            if not NUMBERS_STARTED:
                result += SPECIAL_TO_BRAILLE["NUMBER_FOLLOWS"]
                NUMBERS_STARTED = True
            result += NUMBER_TO_BRAILLE[character]
        elif character.lower() in LETTER_TO_BRAILLE:
            if character.isupper():
                result += SPECIAL_TO_BRAILLE["CAPITAL_FOLLOWS"]
            result += LETTER_TO_BRAILLE[character.lower()]
        elif character == " ":
            result += SPECIAL_TO_BRAILLE[character]
            NUMBERS_STARTED = False

    return result

def main(): 
    input = " ".join(sys.argv[1:])

    if is_english(input):
        print(english_to_braille(input))
    elif is_braille(input):
        print(braille_to_english(input))
    else:
        print("invalid")

if __name__ == "__main__":
    main()