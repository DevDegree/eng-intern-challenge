import sys
# Create a dictionary to map out each letter translation
braille_map = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " "
}
# Another Dictionary for numbers
braille_map_nums = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

# Since the project is converting braille to english AND english to braille, we expand the dictionary to make a bidirectional dictionary
letters_map = {}
for key, value in braille_map.items():
    letters_map[key]= value
    letters_map[value] = key
numbers_map = {}
for key, value in braille_map_nums.items():
    numbers_map[key]= value
    numbers_map[value] = key
# Function to determine if given input is in braille or not
def is_braille(text):
    if any(i not in 'O.' for i in text) or len(text) % 6 != 0:
        return False
    return True
def translator(text):
    letters = []
    if is_braille(text):
        capital = False
        number = False
        for i in range(0, len(text), 6):
            if text[i:i+6] == ".....O":
                capital = True
                continue
            elif text[i:i+6] == ".O.OOO":
                number = True
                continue
            elif text[i:i+6] == "......":
                number = False
            elif text[i:i+6] not in letters_map:
                return None
              
            if capital:
                letters.append(letters_map[text[i:i+6]].upper())
                capital = False
            elif number:
                letters.append(numbers_map[text[i:i+6]])
            else:
                letters.append(letters_map[text[i:i+6]])
    else:

        first_number = True
        for i in text:
            if i.isupper():
                letters.append(".....O")
                letters.append(letters_map[i.lower()])
                continue
            elif i.isdigit():
                if first_number:
                    letters.append(".O.OOO")
                first_number = False
                letters.append(numbers_map[i])
                continue
            elif i not in letters_map:
                return None
            elif i == " ":
                first_number = True            
          
            letters.append(letters_map[i])
    return "".join(letters)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text to translate>")
        return 1

    text = ""  # Initialize an empty string
    for arg in sys.argv[1:]:
        text += arg + " "  # Append each argument with a space

    braille_text = translator(text.strip())  # Remove trailing space
    print(braille_text)

if __name__ == "__main__":
    main()
