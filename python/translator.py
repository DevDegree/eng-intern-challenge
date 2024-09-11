# 2025 Engineering Internship Application - Braille To English, English to Braille Conversion Technical Challenge
# Applicant Name: Prisha Jhajj
# Code Written in Python

alphabetToBraille = {
    "a":"O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", 
    "i": ".OO...", "j":".OOO..", "k":"O...O.", "l":"O.O.O.", "m":"OO..O.", "n":"OO.OO.", "o": "O..OO.", "p": "OOO.O.", 
    "q": "OOOOO.", "r":"O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", 
    "y": "OO.OOO", "z": "O..OOO", " ": "......", "capital": ".....O", "number": ".O.OOO", "decimal": ".O...O"
}

uppercaseBraille = {
    'A': 'O..... ..', 'B': 'O.O... ..', 'C': 'O.O.. ..', 'D': 'O.O. ..', 'E': 'O.O.. ..', 'F': 'O.O. ..', 'G': 'O.O. ..', 'H': 'O.O.. ..', 
    'I': '.O.. ..', 'J': '.O.. ..', 'K': 'O..... O.', 'L': 'O.O.. O.', 'M': 'O.O.. O.', 'N': 'O.O. O.', 'O': 'O.O.. O.', 'P': 'O.O. O.', 
    'Q': 'O.O. O.', 'R': 'O.O.. O.', 'S': '.O.. O.', 'T': '.O.. O.', 'U': 'O..... O..', 'V': 'O.O.. O..', 'W': '.O.. ..', 'X': 'O.O.. O..', 'Y': 'O.O. O..', 'Z': 'O.O.. O..'
}

numBraille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..'
}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

punctuation = [',', ';', ':', '.', '?', '!', '(', ')', '/', '-']
puntuationBraille = ['O.O..', 'O.O.O.', 'O.OO.O', 'O.....', 'O..O.', 'O.OO.', 'O.O.O.', 'O..O..', 'O..O.O', 'O..O.', 'O..O..']

characters = ['&', '*', '@', '©', '®', '™', '°']
characterBraille = ['O.O.O..', 'O.O.O.', 'O.OO.O', 'O..O.O', 'O.O.OO', 'O.O.OO', 'O.O..']

follows_a_number = ".O.OOO"
follows_a_capital = ".....O"

dictionary_of_letters = {m: n for n, m in alphabetToBraille.items() if n not in ["num", "cap", " "]}

number_dict = {m: n for n, m in numBraille.items()}

def is_braille(braille_string):
    return all(x in "O." for x in braille_string) and len(braille_string) % 6 == 0

def translate_braille_to_text(braille_string):
    stringInput = ''
    words = braille_string.split('  ')
    
    for word in words:
        braille_symbols = word.split()
        for braille_symbol in braille_symbols:
            if braille_symbol in alphabetToBraille:
                stringInput += alphabet[alphabetToBraille.index(braille_symbol)]
            elif braille_symbol in numBraille:
                stringInput += numbers[numBraille.index(braille_symbol)]
            elif braille_symbol in puntuationBraille:
                stringInput += punctuation[puntuationBraille.index(braille_symbol)]
            elif braille_symbol in characterBraille:
                stringInput += characters[characterBraille.index(braille_symbol)]
            elif braille_symbol in uppercaseBraille:
                stringInput += alphabet[uppercaseBraille.index(braille_symbol)].upper()
            else:
                stringInput += '?'
        stringInput += ' '
    
    return stringInput.strip()
            
def translate_text_to_braille(text_string):
    stringInput = ''
    for n in text_string:
        lower_n = n.lower()
        if lower_n in alphabet:
            braille_char = alphabetToBraille[lower_n]
            if n.isupper():
                braille_char = follows_a_capital + braille_char
            stringInput += braille_char + ' '
        elif n in numbers:
            stringInput += numBraille[n] + ' '
        elif n in punctuation:
            stringInput += puntuationBraille[punctuation.index(n)] + ' '
        elif n in characters:
            stringInput += characterBraille[characters.index(n)] + ' '
        elif n == ' ':
            stringInput += " " + " " + " "
        else:
            stringInput += '?'
    return stringInput.strip()

def main():
    choice = input("Enter '1' to translate text to Braille or '2' to translate Braille to text: ")

    if choice == '1':
        text_to_translate = input("Enter the text to translate to Braille: ")
        result = translate_text_to_braille(text_to_translate)
        print(result)
    
    elif choice == '2':
        braille_to_translate = input("Enter the Braille to translate to text: ")
        result = translate_braille_to_text(braille_to_translate)
        print(result)
    
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
