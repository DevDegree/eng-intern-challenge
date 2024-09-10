# Create English to Braille dictionary
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", 
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", 
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO"
}

number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", 
    "9": ".OO...", "0": ".OOO.."
}

CAPS = ".....O"
NUMS = ".O.OOO"
SPACE = "......"

# Create Braille to English dictionary
braille_to_english = dict((v, k) for k, v in english_to_braille.items())
braille_to_number = dict((v, k) for k, v in number_to_braille.items())


# Function to change English to Braille
def e_to_b(text):
    end_string = ""
    number = False

    # Parses through the entire input
    for char in text: 
        # Checks if the character is a space
        if(char.isspace()):
            number = False
            end_string += SPACE
        else:
            # Checks if the character is a number
            if(char.isnumeric() and not number):
                end_string += NUMS # Adds the braille to indicate number(s) follows
                number = True

            # Checks if the character is uppercase
            if(char.isupper()):
                end_string += CAPS # Adds the braille to indicate a capital follows
                char = char.lower()

            # Adds character in Braille
            if(number):
                end_string += number_to_braille[char]
            else:
                end_string += english_to_braille[char]
    
    return end_string

# Function to change English to Braille
def b_to_e(text):
    end_string = ""
    capital = False
    number = False

    for i in range(0, len(text), 6): 
        braille = text[i:i+6]

        # Checks if next character is a number
        if(braille == NUMS):
            number = True
        
        # Checks if next letter is capitalized
        elif(braille == CAPS):
            capital = True
        
        # Checks if there's a space to end number sequence
        elif(braille == SPACE):
            number = False
            end_string += " "

        else:
            # Adds a number
            if(number):
                end_string += braille_to_number[braille]
            else:
                # Changes the Braille to characters
                char = braille_to_english[braille]
            
                # Adds a capital letter
                if(capital):
                    end_string += char.upper()
                    capital = False
                # Adds a lowercase letter
                else:
                    end_string += char
    
    return end_string

if __name__ == "__main__":
    import sys
    input = ' '.join(sys.argv[1:])

    # Checks if the input is Braille characters only
    if(set(input).issubset({"O", ".", " "})):
        print(b_to_e(input))
    # Otherwise input is English
    else:
        print(e_to_b(input))

