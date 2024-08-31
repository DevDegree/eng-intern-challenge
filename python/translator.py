def is_braille(str1):
    for item in str1:
        if item != "." and item != "o" and item != "O":
            return False
    return True


def translate_to_braille(str1):
    output = ""
    is_number = False

    for item in str1:
        if item.isupper():
            output += ".....O"  # Check for capital
            item = item.lower()

        if item.isdigit():
            if not is_number:
                output += ".O.OOO"  # Check for number
                is_number = True
            output += list(number_translations.keys())[list(number_translations.values()).index(item)]
        else:
            if is_number:
                is_number = False  # Reset after numbers
            output += list(character_translations.keys())[list(character_translations.values()).index(item)]

    print(output)
    return


def translate_to_english(str1):
    output = ""
    counter = 1
    capitalize = False
    number = False
    for x in range(len(str1)):
        output += str1[x]

        if counter % 6 == 0:

            if output == ".O.OOO":
                number = True
            elif output == "......":
                number = False


            if capitalize:
                print(character_translations[output].capitalize(), end="")
            elif number and output != ".O.OOO":
                print(number_translations[output], end="")
            elif not number:
                print(character_translations[output], end="")

            if output == ".....O":
                capitalize = True

            else:
                capitalize = False

            output = ""
        counter += 1


    return



character_translations = {

    "O.....": "a",  "O.O...": "b",  "OO....": "c",
    "OO.O..": "d",  "O..O..": "e",  "OOO...": "f",
    "OOOO..": "g",  "O.OO..": "h",  ".OO...": "i",
    ".OOO..": "j",  "O...O.": "k",  "O.O.O.": "l",
    "OO..O.": "m",  "OO.OO.": "n",  "O..OO.": "o",
    "OOO.O.": "p",  "OOOOO.": "q",  "O.OOO.": "r",
    ".OO.O.": "s",  ".OOOO.": "t",  "O...OO": "u",
    "O.O.OO": "v",  ".OOO.O": "w",  "OO..OO": "x",
    "OO.OOO": "y",  "O..OOO": "z",
    ".....O": "",  # Capital follows
    ".O.OOO": "",  # Number follows
    "......": " "  # Space

 }

number_translations = {

    "O.....": "1", "O.O...": "2", "OO....": "3",
    "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".OOO..": "0"

}


text = input()



if is_braille(text):
    translate_to_english(text)
else:
    translate_to_braille(text)
