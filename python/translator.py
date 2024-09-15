import sys


braille_to_english = {'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.O.....O': '1', '.O.O...O': '2', '.OO....O': '3', '.OO.O..O': '4',
    '.O..O..O': '5', '.OOO...O': '6', '.OOOO..O': '7', '.O.OO..O': '8', '..OO...O': '9',
    '..OOO..O': '0'}



english_to_braille = {value: key for key, value in braille_to_english.items()}


for letter in "abcdefghijlmnopqrstuvwxyz":
    english_to_braille[letter.upper()] = ".....O" + english_to_braille[letter]
    

english_to_braille[" "] = "......"


def translate_to_braille(char):
    
    return english_to_braille.get(char, "......")

def translate_to_english(code):
    return braille_to_english.get(code, "?")


def main():
    
    if len(sys.argv) != 2:
        
        sys.exit(1)
    
    input = sys.argv[1]


    if 'O' in input or '.' in input:
        
        lst = []
        
        i = 0
        
        while i < len(input):
            
            braille_code = input[i:i+6]
            
            if braille_code == ".....O":
                i += 6
                braille_code = input[i:i+6]
                lst.append(translate_to_english(braille_code).upper())
        
            else:
                lst.append(translate_to_english(braille_code))
        
            i += 6
        print(''.join(lst))
    
    else:
        
        lst = []
    
        for char in input:
            
            lst.append(translate_to_braille(char))
        
        print(''.join(lst))


if __name__ == "__main__":
    main()
        
        
