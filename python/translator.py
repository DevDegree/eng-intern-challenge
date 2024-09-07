import sys


#Map for each character to braille
word_translations = {
    'a': 'O.....', 'b': 'O.O...',
    'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO',
    'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    'capital follows': '.....O', 'number follows': '.O.OOO',
    ' ': '......'
}

#Map for each number to braille
number_translations = {
    '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..',
    ' ': '......'
}

#Opposite maps for braille to english
braille_word_translations = {v: k for k, v in word_translations.items()}
braille_number_translations = {v: k for k, v in number_translations.items()}



def braille_to_english(text):
    full_text = ""
    number_mode = False
    capital_mode = False
    i = 0
    while i < len(text): 
        full_braille = text[i: i + 6]
        if not number_mode: #Adding a character to string
            char = braille_word_translations.get(full_braille)
            if capital_mode:  #Capital Letter Converter 
                full_text += char.upper()
                capital_mode = False
            elif char == "capital follows": #Capital Letter Converter for next character
                capital_mode = True
            elif char == "number follows": #Switches to number mode
                number_mode = True
            else:
                full_text += char
        else: #Adding a number to string
            char = braille_number_translations.get(full_braille)
            if char == " ": #Turns off number mode for next character
                number_mode = False 
            full_text += char
        i += 6
    return full_text


def english_to_braille(text):
    full_text = ""
    number_mode = False
    for char in text:
        if char.isnumeric():
            if not number_mode:  #Makes sure to print number "follows only" onces
                number_mode = True
                full_text += word_translations.get("number follows")
            full_text += number_translations.get(char)
        elif char.isupper(): #Prints capital letters 
            full_text += word_translations.get("capital follows") + word_translations.get(char.lower())
        elif char == " ": #Turns off number mode
            number_mode = False
            full_text += word_translations.get(char)
        else:
            full_text += word_translations.get(char)
    return full_text 


def translate(text): #Figures out if text needs to be translated based on if the text only contains "." or "O" and its length
    if all(c in 'O.' for c in text) and len(text) % 6 == 0:
        return braille_to_english(text)
    else:
        return english_to_braille(text)


def main():
    input_text = sys.argv[1:]
    input_text = ' '.join(input_text)
    print(translate(input_text))

if __name__ == "__main__":
    main()