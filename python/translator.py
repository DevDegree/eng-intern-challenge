import sys

braille_chars = ['O', '.']

letters_to_braille = {
    'a': 'O.....',
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..', 
    'f': 'OOO...', 
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..',
    'k': 'O...O.', 
    'l': 'O.O.O.', 
    'm': 'OO..O.', 
    'n': 'OO.OO.', 
    'o': 'O..OO.', 
    'p': 'OOO.O.', 
    'q': 'OOOOO.', 
    'r': 'O.OOO.', 
    's': '.OO.O.', 
    't': '.OOOO.',
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO', 
    'z': 'O..OOO'
}

numbers_to_braille = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..'
}

braille_to_letters = {b:l for l,b in letters_to_braille.items()}

braille_to_numbers = {b:n for n,b in numbers_to_braille.items()}

space_braille = '......'
to_cap_braille = '.....O'
to_num_braille = '.O.OOO'

def main():
    to_trans = " ".join(sys.argv[1:])
    if(all(c in braille_chars for c in to_trans) and len(to_trans) % 6 == 0):
        print(braille_to_eng(to_trans))
    elif(all(c.isalnum() or c.isspace() for c in to_trans)):
        print(eng_to_braille(to_trans))
    else:
        print("invalid argument, please provide either Braille string or English string with letters, numbers, and spaces only")

def braille_to_eng(braille):
    eng = ""
    numbers = False
    capital = False
    for i in range(0, len(braille), 6):
        braille_sym = braille[i:i+6]

        if(braille_sym == to_cap_braille):
            capital = True
        elif(braille_sym == to_num_braille):
            numbers = True
        elif(braille_sym == space_braille):
            numbers = False
            eng += " "
        else:
            if(numbers):
                eng += braille_to_numbers[braille_sym]
            elif(capital):
                eng += braille_to_letters[braille_sym].upper()
                capital = False
            else:
                eng += braille_to_letters[braille_sym]
    return eng

def eng_to_braille(eng):
    braille = ""
    numbers = False
    for i in range(0, len(eng), 1):
        eng_sym = eng[i]
        if(eng_sym >= '0' and eng_sym <= '9'):
            if(not numbers):
                braille += to_num_braille
                numbers = True
            braille += numbers_to_braille[eng_sym]
        elif(eng_sym == ' '):
            numbers = False
            braille += space_braille
        elif(eng_sym >= 'A' and eng_sym <= 'Z'):
            braille += to_cap_braille
            braille += letters_to_braille[eng_sym.lower()]
        else:
            braille += letters_to_braille[eng_sym]
    return braille

if __name__ == "__main__":
    main()
