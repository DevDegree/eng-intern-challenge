import sys

# Translation dicts
eng_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", " ": "......",
    "capital": ".....O", "number": ".O.OOO"
}
eng_to_braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO.."
}
# reverse key-value pairs for braille to english translation
braille_to_eng = {v: k for k, v in eng_to_braille.items()}
braille_to_eng_numbers = {v: k for k, v in eng_to_braille_numbers.items()}

# check if phrase is braille and convert to eng if valid
def check_is_braille(phrase):
    # ensure 6 character chunks for braille
    if len(phrase) % 6 != 0:
        return False
    
    # split phrase into braille chars
    braille_chars = [phrase[i:i+6] for i in range(0, len(phrase), 6)]

    # translate braille chars to english if they are valid
    capital_next = False
    number_next = False
    result = ""
    for i in range(len(braille_chars)):
        if braille_chars[i] in braille_to_eng:
            c = braille_chars[i]
            
            # handle capital next
            if braille_to_eng[c] == 'capital':
                capital_next = True

            # handle current capital
            elif capital_next:
                result += braille_to_eng[c].upper()
                capital_next = False

            # handle number next
            elif braille_to_eng[c] == 'number':
                number_next = True

            # handle current number
            elif number_next and braille_to_eng[c] != " ":
                result += braille_to_eng_numbers[c]

            # handle number end
            elif number_next and braille_to_eng[c] == " ":
                result += " "
                number_next = False

            # handle all other chars
            else:
                result += braille_to_eng[c]
        else:
            return False
    return result
    
# english to braille translation
def english_to_braille_translate(phrase):
    result = ""
    is_number = False
    for char in phrase:
        # handle capital
        if char.isupper():
            result += eng_to_braille["capital"] + eng_to_braille[char.lower()]
            continue

        # handle first number
        elif char.isdigit() and not is_number:
            is_number = True
            result += eng_to_braille["number"] + eng_to_braille_numbers[char]

        # handle middle numbers
        elif char.isdigit() and is_number:
            result += eng_to_braille_numbers[char]
        
        # handle number end
        elif char == " " and is_number:
            is_number = False
            result += eng_to_braille[" "]
        
        # handle all other chars
        else:
            result += eng_to_braille[char]
    return result
        

# Translation implementation
def braille_translate(phrase):
    is_braille_result = check_is_braille(phrase)

    # phrase is english - convert to braille and output translation
    if not is_braille_result:
        is_english_result = english_to_braille_translate(phrase)
        print(is_english_result)
    # phrase is braille - output english translation
    else:
        print(is_braille_result)

# command line functionality
if __name__ == "__main__":
    # ensure a phrase to translate is passed
    if len(sys.argv) < 2:
        print("Usage: python script.py <text_to_translate>")
        sys.exit(1)

    # call translator with the phrase passed through the command line
    input_text = " ".join(sys.argv[1:])
    braille_translate(input_text)