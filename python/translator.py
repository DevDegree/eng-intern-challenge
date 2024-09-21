import sys

ENGLISH_TO_BRAILLE = {
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
    'z': 'O..OOO',
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

EXTRA_ENG= {
    "capital": ".....O",
    "number": ".O.OOO",
    "space":  "......"
}

# reverse both dictionaries for braille to english/number translations
BRAILLE_TO_ENGLISH = {braille: letter for letter, braille in ENGLISH_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {braille: number for number, braille in NUMBER_TO_BRAILLE.items()}
EXTRA_BRA = {braille: word for word, braille in EXTRA_ENG.items()}

def is_braille(input_string):
    # all six braille characters are either "O" or ".""
    for item in input_string:
        if ("O." in item) or (".O" in item) or ("." in item):
            return True
    return False

def b_to_e(given):
    x = [given[i:i+6] for i in range(0, len(given), 6)]
    answer = ""
    alpha = True
    cap = False
    print(x)
    for item in x:
        found = EXTRA_BRA.get(item)
        
        if found:
            if found == 'space':
                answer += " "
                alpha = True
            elif found == "number":
                alpha = False
            else:
                alpha = True
                cap = True
            continue
        

        if alpha:
            found = BRAILLE_TO_ENGLISH.get(item)
            if not found:
                found = EXTRA_BRA.get(item)
                if found == 'space':
                    answer += " "
                    alpha = True
                elif found == "number":
                    alpha = False
                else:
                    alpha = True
                    cap = True
                continue
            if cap:
                found = found.capitalize()
                cap = False
            answer += found
        else:
            found = BRAILLE_TO_NUMBER.get(item)
            if not found:
                
                found = EXTRA_BRA.get(item)
                if found == 'space':
                    answer += " "
                    alpha = True
                elif found == "number":
                    alpha = False
                else:
                    alpha = True
                    cap = True
                continue
            answer += found
    return answer

def e_to_b(given):
    answer = ""
    num = False
    for char in given:
        if char.isalpha():
            num = False
            if char.isupper():
                answer += EXTRA_ENG['capital'] + ENGLISH_TO_BRAILLE[char.lower()]
            else:
                answer += ENGLISH_TO_BRAILLE[char]
        elif char.isdigit():
            if not num:
                answer += EXTRA_ENG['number'] + NUMBER_TO_BRAILLE[char]
                num = True
            else:
                answer += NUMBER_TO_BRAILLE[char]
                num = False
        elif char == " ":
            answer += EXTRA_ENG['space']
            num = False
    return answer

def main():
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        answer = b_to_e(input_string)
        print(answer)
    else:
        answer = e_to_b(input_string)
        print(answer.strip())

if __name__ == "__main__":
    main()
