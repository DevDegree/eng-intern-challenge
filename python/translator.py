import sys

braille_letter_dict = {"a":"O.....", "b":"O.O...", "c":"OO....", "d":"OO.O..", "e":"O..O..",
                "f":"OOO...", "g":"OOOO..", "h":"O.OO..", "i":".OO...", "j":".OOO..",
                "k":"O...O.", "l":"O.O.O.", "m":"OO..O.", "n":"OO.OO.", "o":"O..OO.",
                "p":"OOO.O.", "q":"OOOOO.", "r":"O.OOO.", "s":".OO.O.", "t":".OOOO.",
                "u":"O...OO", "v":"O.O.OO", "w":".OOO.O", "x":"OO..OO", "y":"OO.OOO",
                "z":"O..OOO"}
braille_number_dict = {"1":"O.....", "2":"O.O...", "3":"OO....", "4":"OO.O..", "5":"O..O..",
                       "6":"OOO...", "7":"OOOO..", "8":"O.OO..", "9":".OO...", "0":".OOO.."}

capital_follows = ".....O"
number_follows = ".O.OOO"
space = "......"

def translate(str):
    """Returns appropriate translation of string, allowing 
    -Letters a through z, lowercase and capitalized
    -Numbers 0 through 9
    -Spaces
    """
    if "." in str:
        return braille_to_english(str)
    else:
        return english_to_braille(str)

def braille_to_english(str):
    """Returns translation of Braille to English,
    or error message if string length is invalid unable to be parsed as Braille cells
    """
    braille_cells = []
    if len(str) % 6 == 0:
        braille_cell_count = int(len(str) / 6)
    else:
        return "not a valid length of braille"
    
    for braille_cell_num in range(0, braille_cell_count):
        cell = str[braille_cell_num*6:braille_cell_num*6+6]
        braille_cells.append(cell)
    
    return translate_braille_cells(braille_cells)

def translate_braille_cells(braille_cells):
    """Returns translation of Braille cells to English"""    
    english_string = ""
    capital = False
    number = False
    for cell in braille_cells:
        if cell == space:
            english_string += " "
            number = False
        elif capital == True:
            english_string += translate_letter(cell).upper()
            capital = False
        elif number == True:
            english_string += translate_number(cell)
        elif cell == capital_follows:
            capital = True
        elif cell == number_follows:
            number = True
        else:
            english_string += translate_letter(cell)
    return english_string

def translate_letter(cell):
    """Returns translation of Braille letter cell to English,
    or error message if corresponding letter does not exist
    """   
    for english_value, braille_value in braille_letter_dict.items():
        if cell == braille_value:
            return english_value
    return "not found"

def translate_number(cell):
    """Returns string translation of Braille number cell to English,
    or error message if corresponding number does not exist
    """   
    for number_value, braille_value in braille_number_dict.items():
        if cell == braille_value:
            return number_value
    return "not found"

def english_to_braille(str):
    """Returns translation of English to Braille"""
    braille_string = ""
    number = False
    for char in str:
        if char.isupper():
            braille_string += capital_follows
            braille_string += braille_letter_dict[char.lower()]
        elif char.isnumeric():
            if number == False:
                braille_string += number_follows
                braille_string += braille_number_dict[char]
                number = True
            else:
                braille_string += braille_number_dict[char]
        elif char == " ":
            braille_string += space
            number = False
        else:
            braille_string += braille_letter_dict[char]
    return braille_string

if __name__ == "__main__":
    """Prints result of translator on given argument(s), 
    parsing multiple arguments into one string, separated by spaces"""
    combined_args = ""
    for arg in sys.argv[1:]:
        combined_args += arg + " "
    print(translate(combined_args[:-1]))

