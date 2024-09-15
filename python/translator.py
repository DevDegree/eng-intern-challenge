import sys
import re

# Checks if braille with Regex
def is_braille(input_str):
    return bool(re.fullmatch(r'[O.]+', input_str))

def process_input(input):
    chars = {
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
        " ": "......"
    }

    if is_braille(input):
        letter_to_num =  {
            "a": "1",
            "b": "2",
            "c": "3",
            "d": "4",
            "e": "5",
            "f": "6",
            "g": "7",
            "h": "8",
            "i": "9",
            "j": "0"
        }
        # Special character dictionary
        special = {
            ".....O": 1,
            ".O...O": 2,
            ".O.OOO": 3
        }
        reversed_chars = {v: k for k, v in chars.items()}
        listy = [input[i:i + 6] for i in range(0, len(input), 6)]
        
        res = ""
        spec = False
        capital = False
        number = False
        for i in range(len(listy)):

            # Check for special characters (capital, number, decimal)
            if listy[i] in special.keys():
                spec = special[listy[i]]
                
                if(spec == 1):
                    capital = True
                elif (spec == 2):
                    res += "."
                else:
                    number = True

            else:
                if number:
                    # Space then next phrase does not have to be a number
                    if reversed_chars[listy[i]] == " ":
                        res += " "
                        number = False
                    
                    # Check for special characters
                    elif reversed_chars[listy[i]] not in letter_to_num:
                        res += reversed_chars[listy[i]]
                    
                    # Adding a number
                    else: 
                        res += letter_to_num[reversed_chars[listy[i]]]

                elif capital:
                    res += reversed_chars[listy[i]].upper()
                    capital = False

                else:
                   res += reversed_chars[listy[i]]

        return res

    else: 
        num_to_letter = {
            "1": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "0": "j"
        }
        res = ""
        for i, ch in enumerate(input):
            n = ord(ch)

            # Lowercase alphabet
            if ( 97 <= n <= 122 ):
                res += chars[ch]

            # Uppercase characters
            elif (65 <= n <= 90):
                res += ".....O" + chars[ch.lower()]

            # Space character, see if next is number
            elif (n == 32):
                res += "......"

                if (i + 1 < len(input) and 48 <= ord(input[i + 1]) <= 57):
                    res += ".O.OOO"

            # Dot, assumming decimal
            elif (n == 46):
                res += "."

            # Numbers
            elif (48 <= n <= 57):
                # Add number braille if first char
                if i == 0:
                    res += ".O.OOO"
                
                res +=  chars[num_to_letter[ch]]
        
        return res


if __name__ == "__main__":
    # sys.argv[0] is the script name, so we take the arguments starting from sys.argv[1:]
    inputs = " ".join(sys.argv[1:])

    # Process the input arguments
    output = process_input(str(inputs))

    # Output the result
    print(output)
