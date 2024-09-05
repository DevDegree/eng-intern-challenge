import sys

### Dictionairies to store associated braille and english values

english_to_braille = {
"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", 
"g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", 
"m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", 
"s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", 
"y": "OO.OOO", "z": "O..OOO", 
" ": "......", ".": "..OO.O", ",": "..O...", "?": "..O.O.", "!": "..OOO.", ":": "OO....",
";": "..0.0.", "-": "..O..O", "/": ".O..O.", "(": ".O.O.O", ")": ".O.O.O",
"cap_next": ".....O", "num_next": ".O.OOO", "decimal_next": ".O...O"
}
braille_to_english = {value: key for key, value in english_to_braille.items()} # Swapping keys/values of previous dict


nums_to_braille = {
"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}
braille_to_nums = {value: key for key, value in nums_to_braille.items()} # Swapping keys/values of previous dict



### Translation-performing Functions


# Checking whether the input is braille or not (length must be mult. of 6 and only '0' and '.' allowed)
def is_braille(input):
    return (len(input) % 6 == 0) and all(c in '0.' for c in input)


# Translating from english to braille
def translate_to_braille(input):
    result = ""
    num_marker = False

    for char in input:
        if char.isdigit():  # If char is digit, use the num to braille dict and ensure the num_marker is updated
            if not num_marker:
                result += english_to_braille['num_next']
                num_marker = True
            
            result += nums_to_braille[char]

        elif char.isAlpha():  # If char is letter, use the english to braille dict and check for upper cases
            if char.isUpper():
                result += english_to_braille['cap_next']
            
            result += english_to_braille[char.toLower()]

        elif char == ' ':  
            result += english_to_braille[char]
            num_marker = False  # The space marks the end of a number sequence

    return result
            

def translate_to_english(input):
    chars = [input[i:i+6] for i in range(0, len(input), 6)]  # Efficient way to seperate braille sequences into list

    result = ""
    num_marker = False
    cap_next = False

    for brl in chars:

        # Updating capitalization and number markers based on braille sequence
        if brl == "....0":
            cap_next = True
        elif brl == ".0.000":
            num_marker = True
        elif brl == "......":
            num_marker = False
            result += braille_to_english[brl]

        # Checking for markers and adding chars to result string accordingly
        else:
            if num_marker:
                result += braille_to_nums[brl]
            elif cap_next:
                result += braille_to_english[brl].upper()
                cap_next = False
            else:
                result += braille_to_english[brl]

    return result


# Wraper to choose which translating function to use based on is_braille function
def translate(input):
    if is_braille(input):
        return braille_to_english(input)
    else:
        return english_to_braille(input)


# Checks command-line arguments and feeds them into program
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = "".join(sys.argv[1:])
        result = translate(input)
        print(result)
    else:
        print("Did not provide a string argument")