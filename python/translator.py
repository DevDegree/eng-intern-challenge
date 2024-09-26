import sys  

#Braille to English mapping 
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",  
    "..OO.O": "."
}

number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

#Reverse the above dict to get the braille mappings
english_to_braille = {}
for k, v in braille_to_english.items():
    english_to_braille[v] = k



def translate_to_braille(text):
    #Translate english to braille
    is_number = False
    res = []

    #Parse each char within input text =
    for char in text:

        #case 1 char is a digit
        if char.isdigit():

            if is_number != True:

                is_number = True
                res.append(".O.OOO")
            res.append(number_to_braille[char])

        #case 2 char is letter
        elif char.isalpha():

            if is_number:
                is_number = False
                res.append("......")

            if char.isupper():
                res.append(".....O")
            res.append(english_to_braille[char.lower()])

        #Case 3 char is a space
        else:

            if is_number:
                is_number = False
            res.append("......")

    return ''.join(res)

def translate_to_english(braille):
    #Translate Braille to English
    result = []  # List to store the English translation
    i = 0  # Index for traversing the Braille string
    is_cap = False  
    is_number = False  

    while i < len(braille):
        group = braille[i:i+6]  # 6-character grouping

        # case 1 capital follows
        if group == ".....O":
            is_cap = True  
            i += 6
            continue

        # case 2 number follows
        elif group == ".O.OOO":
            is_number = True  # Enable number mode until next space
            i += 6
            continue

        # case 3 char mapping 
        if is_number:
            if group == "......":  # Exit number mode on space
                is_number = False
            else:
                # Convert Braille group to a digit
                digit = str(list(number_to_braille.values()).index(group) + 1)
                result.append(digit)
        else:
            # Convert Braille group to a letter or symbol
            if group == "......":  # Handle spaces
                result.append(" ")
            else:
                letter = braille_to_english[group]
                if is_cap:
                    letter = letter.upper()  # Convert to uppercase if capital mode is on
                    is_cap = False  # Reset capital mode
                result.append(letter)

        i += 6  # Move to the next Braille group

    return ''.join(result)  # Join and return the translated string

def main():
    """Main function to run the translator."""
    input_text = ' '.join(sys.argv[1:])  # Join all into single string

    # Check if the input is Braille or English
    is_braille = True
    for char in input_text:
        if char != 'O' and char != '.':
            is_braille = False

    if is_braille:
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text)) 

if __name__ == "__main__":
    main()  # Call the main function when the script is run






