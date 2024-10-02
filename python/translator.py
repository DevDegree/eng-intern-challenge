import sys

# Define the hashmap for braille alphabets and english alphabets
BRAILLE_LEN = 6
ALPHABETS_TO_BRAILLE = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", # A - G
    'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", # H - N
    'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO", # O - U
    'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO", # V - Z
    }
NUMBERS_TO_BRAILLE = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", 
    "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
    }
SPECIAL_TO_BRAILLE = {
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO",
    "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO."
}
BRAILLE_TO_ALPHABETS = {v: k for k, v in ALPHABETS_TO_BRAILLE.items()}
BRAILLE_TO_NUMBERS = {v: k for k, v in NUMBERS_TO_BRAILLE.items()}
SPECIAL_TO_BRAILLE = {v: k for k, v in SPECIAL_TO_BRAILLE.items()}
CAPITAL_FOLLOW = ".....O"
NUMBER_FOLLOW = ".O.OOO"
SPACE = "......"

def check_braille(input: str) -> bool:
    '''
    Given the 'input' string, it determines if the given parameter is a valid representation of Braille.
    '''
    if all(char in "O." for char in input):
        if len(input) % BRAILLE_LEN == 0:
            return True
        else:
            raise ValueError(f"Invalid braille input was given: {input}")
    return False

def translate(input: str) -> str:
    '''
    Depending on the 'input' string, it translates English word(s) into Braille or Braille into English word(s).
    '''
    translate_string = ""
    number_status = False
    capital_status = False
    
    # If the given 'input' string is in Braille representation, it translates into English.
    # Otherwise, it translates into Braille representation.
    if check_braille(input):
        for i in range(0, len(input), 6):
            symbol = input[i: i+6]

            if symbol == SPACE:
                if number_status:
                    number_status = False
                translate_string += " "
                continue
            elif symbol == CAPITAL_FOLLOW:
                capital_status = True
                continue
            elif symbol == NUMBER_FOLLOW:
                number_status = True
                continue 

            if number_status:
                translate_string += BRAILLE_TO_NUMBERS[symbol]
            elif capital_status:
                capital_status = False
                translate_string += BRAILLE_TO_ALPHABETS[symbol].upper()
            else:
                translate_string += BRAILLE_TO_ALPHABETS[symbol]
 
    else:
        for char in input:
            if char in ALPHABETS_TO_BRAILLE:
                translate_string += ALPHABETS_TO_BRAILLE[char]
            elif char.lower() in ALPHABETS_TO_BRAILLE:
                translate_string += CAPITAL_FOLLOW + ALPHABETS_TO_BRAILLE[char.lower()]
            elif char in NUMBERS_TO_BRAILLE:
                if not number_status:
                    number_status = True
                    translate_string += NUMBER_FOLLOW 
                translate_string += NUMBERS_TO_BRAILLE[char]
            elif char in SPECIAL_TO_BRAILLE:
                translate_string += SPECIAL_TO_BRAILLE[char]
            elif char == " ":
                if number_status:
                    number_status = False
                translate_string += SPACE
    
    return translate_string

def main() -> None:
    '''
    It handles the input(s) from the users and perform translation
    '''
    # Verify if the correct number of parameters were given and it translates the input string
    try:
        if len(sys.argv) < 2:
            raise ValueError(f"Invalid number of argument is provided")
        inputs = sys.argv[1:]
        input_string = ' '.join(str(arg) for arg in inputs)
        ans = translate(input_string)
        print(ans)

    except Exception as e:
        print(f"Unable to translate, {e}")

if __name__ == "__main__":
    main()