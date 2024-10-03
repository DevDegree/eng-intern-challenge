"""
Created by Belal Abu-Thuraia
b.abuthuraia@gmail.com
4388694801
GitHub: BabuTheGreat
"""
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

# Main function to run translation logic
def translator(text):

    #Creating a list to seperate each letter or 6 character string
    letters = []

    #Main if else to determine language to translate
    if is_braille(text):
        #Setting support variables
        capital = False
        number = False

        #Iterating through given input
        for i in range(0, len(text), 6):
            #Special case if capital letter follows and if number follows (next elif)
            if text[i:i+6] == ".....O":
                capital = True
                continue
            elif text[i:i+6] == ".O.OOO":
                number = True
                continue
            #Setting number back to false once we see a space
            elif text[i:i+6] == "......":
                number = False
            elif text[i:i+6] not in letters_map:
                return None
            
            #If captital string was prior, then capitalize current letter 
            if capital:
                letters.append(letters_map[text[i:i+6]].upper())
                capital = False
            #If number was to follow, then retrieve from numbers dictionary 
            elif number:
                letters.append(numbers_map[text[i:i+6]])
            else:
                letters.append(letters_map[text[i:i+6]])

    #If given input is in english
    else:
        #Setting support variables. First number is only false after we see our first number. It is set back to true once we see a space character
        first_number = True
        #Going through words
        for i in text:
            #Add special braille string for capitals
            if i.isupper():
                letters.append(".....O")
                letters.append(letters_map[i.lower()])
                continue
            #Add special braille string for upcoming numbers
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
    # Append each argument into one string
    text = "" 
    for arg in sys.argv[1:]:
        text += arg + " " 

    braille_text = translator(text.strip()) 
    print(braille_text)

if __name__ == "__main__":
    main()
