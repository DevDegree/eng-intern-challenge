import sys

letter_to_braille = {
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

numbers_to_braille = {
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


braille_to_letter = {v: k for k, v in letter_to_braille.items()}
braille_to_number = {v: k for k, v in numbers_to_braille.items()}

CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"



def text_to_braille(text: str) -> str:
    
    # States for checking the current state we are in
    state = {
        'num_follows': False,
        'last_was_number': False
    }

    def process_char(char: str) -> str:
        nonlocal state
        result = []

        if char.isdigit():
            if not state['num_follows']:
                result.append(NUMBER_FOLLOWS)
                state['num_follows'] = True
            result.append(numbers_to_braille.get(char, ''))
            state['last_was_number'] = True
        elif char.isalpha():
            if state['num_follows']:
                state['num_follows'] = False
            if char.isupper():
                result.append(CAPITAL_FOLLOWS)
            result.append(letter_to_braille.get(char.lower(), ''))
            state['last_was_number'] = False
        elif char == ' ':
            result.append(SPACE)
            state['num_follows'] = False
            state['last_was_number'] = False
        elif char == '.':
            if state['last_was_number']:
                result.append(DECIMAL_FOLLOWS)
            else:
                result.append(letter_to_braille.get('.', ''))
            state['last_was_number'] = False
        else:
            # For any other character, we'll just ignore it
            pass

        return ''.join(result)

    return ''.join(process_char(char) for char in text)
    

def process_symbol(symbol: str, state: dict) -> str:
    
    if state['number_follows'] or state['decimal_follows']:
        char = braille_to_number.get(symbol, '')
        if not char.isdigit():
            state['number_follows'] = False
            state['decimal_follows'] = False
        return char
    
    char = braille_to_letter.get(symbol)
    
    return char.upper() if state['capital_follows'] else char


def braille_to_text(text: str):
    """Braille to Plain Text translation function
    
    input: str - Braille string to translate
    output: str - Plain text string
    """
    
    # Iterating through the text and making a group of 6 characters
    braille_symbols = [text[i:i+6] for i in range(0, len(text), 6)]

    # Plain text array
    plain_text = []
    
    # States for knowing what state we are in currently
    state = {
        'capital_follows': False,
        'number_follows': False,
        'decimal_follows': False
    }
    
    
    for symbol in braille_symbols:
        if symbol == CAPITAL_FOLLOWS:
            state['capital_follows'] = True
        elif symbol == NUMBER_FOLLOWS:
            state['number_follows'] = True
        elif symbol == DECIMAL_FOLLOWS:
            state['decimal_follows'] = True
            plain_text.append('.')
        elif symbol == SPACE:
            state['number_follows'] = False
            state['decimal_follows'] = False
            plain_text.append(' ')
        else:
            char = process_symbol(symbol, state)
            plain_text.append(char)
            
            # Reset states after processing
            state['capital_follows'] = False
            if char == ' ':
                state['number_follows'] = False
                state['decimal_follows'] = False

    return ''.join(plain_text)
        


def is_braille(braille: str):
    """Checks if the string is a braille string
    
    input: braille string
    output: Boolean
    """
    for char in braille:
        if char != '.' and char != 'O':
            return False
        
    return len(braille) % 6 == 0


def translate():
    """Trasnlate function takes the bulk of processing the input
    """
    
    # Check if less than 2 arguemnts are given
    if(len(sys.argv) < 2):
        print("Correct use: python translator.py <input>")
        sys.exit(-1)
    
    # get input and combine into a single string
    inpt = sys.argv[1] if len(sys.argv) >= 2 else ''
    
    for i in range(2, len(sys.argv)):
        inpt = f'{inpt} {sys.argv[i]}'
    
    
    # Check if the string is braille or plain text
    if is_braille(inpt):
        print(braille_to_text(inpt))
        pass
    else:
        print(text_to_braille(inpt))

def main():
    translate()
    
    
    
if __name__ == '__main__':
    main()