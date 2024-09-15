from sys import argv

# Create a Dictionary for our conversion
ENGLISH_TO_BRAILLE = {
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
    " ": "......",
    "cap": ".....O",
    "num": ".O.OOO",
}

# Create Separate Dictionaries for Braille to Letters and Numbers 
BRAILLE_TO_LETTER = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if not k.isnumeric()}
BRAILLE_TO_NUMBER = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k.isnumeric()}

class Translator:
    def __init__(self, input_text):
        self.input_text = input_text
        self.output_text = ""

    # Convert English to Braille
    def to_braille(self) -> str:
        num_flag = False # Flag to check if we're in number mode
        for char in self.input_text: # Loop through each character in the input text
            # Manage space
            if char == " ": 
                self.output_text += ENGLISH_TO_BRAILLE[char]
                num_flag = False
            # Manage number
            elif char.isnumeric() or num_flag == True:
                if num_flag == False:
                    self.output_text += ENGLISH_TO_BRAILLE["num"] # Add the number indicator
                    num_flag = True
                self.output_text += ENGLISH_TO_BRAILLE[char]
            # Manage uppercase 
            elif char.isupper(): 
                self.output_text += ENGLISH_TO_BRAILLE["cap"]
                char = char.lower()
                self.output_text += ENGLISH_TO_BRAILLE[char]
            # Manage normal characters
            else:
                self.output_text += ENGLISH_TO_BRAILLE[char]
        return self.output_text

    # Convert Braille to English
    def to_english(self) -> str:
        # Split the input text into 6 character chunks
        braille_chars = [self.input_text[i:i + 6] for i in range(0, len(self.input_text), 6)]
        num_flag = False
        cap_flag = False
        for char in braille_chars:
            # Manage space
            if char == ENGLISH_TO_BRAILLE[" "]:
                self.output_text += " "
                num_flag = False
                continue
            # Manage uppercase
            if char == ENGLISH_TO_BRAILLE["cap"]:
                cap_flag = True
                continue
            # Manage number symbol
            elif char == ENGLISH_TO_BRAILLE["num"]:
                num_flag = True
                continue
            else:
                # If we're not in number mode, convert to letter
                if cap_flag == True and num_flag == False: 
                    self.output_text += BRAILLE_TO_LETTER[char].upper()
                    cap_flag = False # Reset the flag
                elif num_flag == True:
                    self.output_text += BRAILLE_TO_NUMBER[char]
                else: 
                    self.output_text += BRAILLE_TO_LETTER[char]
        return self.output_text

    
    # Check if the input text is Braille and valid Braille
    def is_braille(self) -> bool:
        for char in self.input_text:
            if char == '.' or char == 'O':
                continue
            else:
                return False
            
        # Now make sure the input text is valid
        braille_chars = [self.input_text[i:i + 6] for i in range(0, len(self.input_text), 6)]
        
        # Check if the input text is valid
        for braille in braille_chars:
            # Only need to check b to l dict which contains all combos
            if braille not in BRAILLE_TO_LETTER: 
                return False
        return True
    
    # Check if the input text is English and valid English
    def is_english(self) -> bool:
        # Make all characters lowercase since the dictionary is lowercase
        input_copy = self.input_text.lower()
        for char in input_copy:
            if char not in ENGLISH_TO_BRAILLE:
                return False
        return True

# Determine the type of input
def type_of_input(input_text: str) -> str:
    if Translator(input_text).is_braille():
        return "braille"
    elif Translator(input_text).is_english():
        return "english"
    else:
        return "invalid"
    
# Translate the input text
def translate(input_text: str) -> str:
    if type_of_input(input_text) == "english":
        return Translator(input_text).to_braille()
    elif type_of_input(input_text) == "braille":
        return Translator(input_text).to_english()
    else:
        return "Invalid input"

def main():
    if len(argv) < 2:
        print("Please provide a string to translate")
        return
    
    input_text = " ".join(argv[1:])

    # Translate and print the input
    print(translate(input_text))

if __name__ == "__main__":
    main()