import string 

#dictionary that stores english characters and their corresponding braille sequences
english_to_braille = {
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..", "f" : "OOO...", "g" : "OOOO..",
    "h" : "O.OO..",  "i" : ".OO...", "j" : ".OOO..", "k" : "O...O.", "l" : "O.O.O.", "m" : "OO..O.", "n" : "OO.OO.", 
    "o" : "O..OO.", "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.",
    "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO", "y" : "OO.OOO", "z" : "O..OOO",
    "0": ".OOO..", "1" : "O.....", "2" : "O.O...", "3" : "OO....", "4" : "OO.O..", "5" : "O..O..", "6" : "OOO...",
    "7" : "OOOO..", "8" : "O.OO..", "9" : ".OO...", "." : "..OO.O", "," : "..O...", "?" : "..O.OO",  "!" : "..OOO.",
    ":" : "..OO..", ";" : "..O.O.", "-" : "....OO", "/" : ".O..O.", "<" : ".OO..O", ">" : "O..OO.", "(" : "O.O..O",
    ")" : ".O.OO.", " " : "......", "cap" : ".....O", "dec" : ".O...O", "num" : ".O.OOO"
}

#check if inputted string is in english or braille
def is_english(phrase):
    #any string with less than 6 characters cannot be braille thus the function will return 'True' in this case
    if len(phrase) < 6: 
        return True
    for character in phrase:
        if(character != "." and character != "O" ):
            return True
    return False

#given a braille string and a boolean indicating whether or not it is a number, return the corresponding english character
def get_key(value, isnumber):
    for key, val in english_to_braille.items():
        if value == val and ((isnumber and (key.isdigit() or key in string.punctuation)) or (not isnumber and not key.isdigit())):
            return key

    return ""

#translate given phrase from braille to english or vice versa
def translate(phrase):
    output = ""
    if(is_english(phrase)):
        isnumber = False
        for character in phrase:
            if character.isupper() :
                output += english_to_braille["cap"] + english_to_braille[character.lower()]
            elif character.isdigit() and not isnumber:
                isnumber = True
                output += english_to_braille["num"] + english_to_braille[character]
            elif character == " ":
                output += english_to_braille[character]
                isnumber = False
            else:
                output += english_to_braille[character]
    else:
        iscapital = False
        isnumber = False
        for i in range (0, len(phrase), 6):
            character = phrase[i:i+6]
            if character ==english_to_braille[" "]:
                output += " "
                isnumber = False
            elif character == english_to_braille["cap"]:
                iscapital = True
            elif character == english_to_braille["num"]:
                isnumber = True
            elif iscapital:
                output += get_key(character, False).upper()
                iscapital = False
            else:
                output += get_key(character, isnumber)
    return output

def main():
    phrase = str(input(""))
    print(translate(phrase))


if __name__ == '__main__':
    main()

