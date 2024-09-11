import sys

#dictionary to map English characters to Braille equivalents
e_to_b = {
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
    ".": "..OO.O",
    ",": "..O....",
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
    "space": "......",
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO"
}

#dictionary to map Braille to English characters equivalents
b_to_e = {v: k for k, v in e_to_b.items()}

#this method decides if the arguments are Braille or English
def detect(text):
    #if there is any other character in the argument other than 0 or . then we know it's in English
    if any(c not in "O." for c in text):
        return english_to_braille(text)
    else:
        return braille_to_english(text)

def braille_to_english(input):
    output = []
    i = 0

    while i < len(input):
        #we will deal with slices of 6 characters because each Braille letter takes 6 characters as encoded
        sliced = input[i:i+6]
        i += 6
        character = b_to_e.get(sliced, '')
        
        #if the current character is a space, we just append it to the answer list
        if character == 'space':
            output.append(" ")
        
        #if the current character is a capital, we process the following character to make it uppercase
        elif character == 'capital':
            following = input[i:i+6]
            following_character = b_to_e.get(following, '')
            output.append(following_character.upper())
            i += 6
        
        #if the current character indicates there is some type of number ahead, then we know we can just
        #keep appending the numbers and/or the decimal point until there is a space at some point
        elif character == 'number' or character == 'decimal':
            while i < len(input) - 6:
                following = input[i:i+6]
                following_character = b_to_e.get(following, '')
                #if a space was found, then we can break out of the loop
                if following_character == 'space':
                    output.append(" ")
                    i += 6
                    break
                else:
                    output.append(following_character)
                    i += 6
        else:
            output.append(character)

    return "".join(output)

def english_to_braille(input):
    output = []
    i = 0
    
    while i < len(input):
        char = input[i]
        
        #if the character is a capital letter, then we need to add the Braille prefix to indicate it
        if char.isupper():
            output.append(e_to_b['capital'])
            output.append(e_to_b.get(char, ''))
            i += 1

        #if the character is a number, then we need to add the Braille prefix to indicate it
        #then we can process the rest of the numbers in the sequence until a space is met
        elif char.isdigit():
            output.append(e_to_b['number'])  
            while i < len(input) and input[i].isdigit():
                output.append(e_to_b.get(input[i], ''))
                i += 1

            if i < len(input) and input[i] == ' ':
                output.append(e_to_b['space'])
                i += 1

        #if the character is a space then we can add that to the output list
        elif char == ' ':
            output.append(e_to_b['space'])
            i += 1
        
        #otherwise, keep appending the Braille equivalent of the character (the capital version)
        else:
            output.append(e_to_b.get(char.upper(), ''))
            i += 1

    return "".join(output)

def main():
    if len(sys.argv) < 2:
        print("ERROR. Usage: python3 translator.py [str] ... [str]")
        return

    args = " ".join(sys.argv[1:])
    result = detect(args)

    print(result)

if __name__ == "__main__":
    main()
