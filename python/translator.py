import sys


#Define braille dictionaries
num_br_dict = {"1": "O.....", "2": "O.O...", 
				"3": "OO....", "4": "OO.O..", 
				"5": "O..O..", "6": "OOO...", 
				"7": "OOOO..", "8": "O.OO..", 
				"9": ".OO...", "0": ".OOO..", 
				" ": "......"}

eng_br_dict = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
				"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", 
                "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
				 "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", 
				"v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", 
				"capital": ".....O","decimal": ".O...O", "number": ".O.OOO", ".": "..OO.O",
				 ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.", 
				"(": "O.O..O", ")": ".O.OO.", " ": "......"}

br_num_dict = {v: k for k, v in num_br_dict.items()}
br_eng_dict = {v: k for k, v in eng_br_dict.items()}


#Check if string is braille/english where braille is made up of dot's and O's
def is_braille(string):
    for i in string:
        if i not in ['.', 'O']:
            return False
    return True

#Create a function that translates english to braille
#Input: string, Output: Braille (translation of english string)
def english_to_braille(s):
    output = ""
    number = False
    for i in s:
        if i.isupper():
            output += eng_br_dict["capital"]
            output += eng_br_dict[i.lower()]
        elif i.isdigit():
            if not number:
                output += eng_br_dict["number"]
                number = True
            output += num_br_dict[i]
        elif i == " ":
            output += eng_br_dict[i]
            number = False
        else:
            output += eng_br_dict[i]
    return output

#Create a function that translates braille to english
def braile_to_english(s):
    output = ""
    capital = False
    Number = False
    for i in range(0, len(s), 6):
        letter = s[i:i+6]
        if letter in br_eng_dict:
            if br_eng_dict[letter] == "capital":
                capital = True
                continue
            elif br_eng_dict[letter] == "number":
                Number = True
                continue
            if capital:
                output += br_eng_dict[letter].upper()
                capital = False
            elif Number and br_eng_dict[letter] == " ":
                output += br_eng_dict[letter]
                Number = False
            elif Number:
                output += br_num_dict[letter]
            else:
                output += br_eng_dict[letter]
    return output




def main():
    if len(sys.argv) < 2:
        print("Input Invalid.Please provide an input in English or Braille")
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        print(braile_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == '__main__':
    main()
