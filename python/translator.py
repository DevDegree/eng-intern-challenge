import sys

class translator:

    braille_map = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO', " ": '......', '1': 'O.....',
        '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
        '9': '.OO...', '0': '.OOO..', '.': '..OO.O', ',': '..O...',
        '?': '..O.OO', '!': '..OOO.', '-': '....OO',':': '..OO..',
        '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O',
        ')': '.O.OO.', ' ': '......'
    }

    numbers_map = {
        '1': 'O.....',
        '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
        '9': '.OO...', '0': '.OOO..'}
    
    alpha_and_specialchar_map = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
        'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
        'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
        'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
        'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...',
        '?': '..O.OO', '!': '..OOO.', '-': '....OO',':': '..OO..',
    }

    def text_to_braille(self, braille_map, text: str) -> str:
        res = ""
        first_encounter = True
        for c in text:
            if c.isalpha():
                if c.isupper():
                    res += ".....O"
                    res += braille_map[c.lower()]
                else:
                    res += braille_map[c]
            elif c.isnumeric() and first_encounter:
                res += ".O.OOO"
                res += braille_map[c]
                first_encounter = False
            elif c == " ":
                first_encounter = True
                res += braille_map[c]
            else:
                res += braille_map[c]


        return res 
    
    def braille_to_text(self, alpha_and_specialchar_map, numbers_map, text: str) -> str:
        inv_alpha_special = {v: k for k, v in alpha_and_specialchar_map.items()}
        inv_nums = {v: k for k, v in numbers_map.items()}
        res = ""
        i = 0
        while i < len(text):
            currBraille = text[i:i+6]
            
            if currBraille == ".O.OOO":
                i += 6
                numBraillie = text[i:i+6]

                while numBraillie != "......" and i < len(text):
                    res += inv_nums[numBraillie]
                    i += 6
                    numBraillie = text[i:i+6]
                
                if numBraillie == "......":
                    res += " "
            
                    
            elif currBraille == ".....O":
                i += 6
                nextBraille = text[i:i+6]
                nextLetter = inv_alpha_special[nextBraille]
                res += nextLetter.upper()

            else:
                res += inv_alpha_special[currBraille]

            
            i += 6

        return res


def main():
    
    args = sys.argv[1:]
    obj = translator()

    if all(c in 'O.' for c in args[0]):
    
        print(obj.braille_to_text(obj.alpha_and_specialchar_map, obj.numbers_map, ' '.join(args)))

    else:
        print(obj.text_to_braille(obj.braille_map, ' '.join(args)))

    while True:
        input_text = input("")

        if all(c in 'O.' for c in input_text):
    
            print(obj.braille_to_text(obj.alpha_and_specialchar_map, obj.numbers_map, input_text))

        else:
            print(obj.text_to_braille(obj.braille_map, input_text))



    
if __name__ == "__main__":
    main()
