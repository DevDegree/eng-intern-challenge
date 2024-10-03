import sys

"""
    Braille Translator
"""

# braille to english non numeric dictionary
br_to_en_nonnumeric = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', 
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 
    'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', 
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', 
    'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
}

# braille to english numeric dictionary
br_to_en_numeric = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# english to braille dictionary
en_to_br = {v: k for k, v in br_to_en_nonnumeric.items()}
en_to_br.update({v: k for k, v in br_to_en_numeric.items()})
en_to_br.update({
    'cap': '.....O',
    'num': '.O.OOO'
})


# converts english to braille
def en_to_braille(input_str):
    braille = ''
    num_flag = False
    for char in input_str:
        if char.isalpha():
            num_flag = False
            if char.isupper():
                braille += en_to_br["cap"]
        elif char.isnumeric():
            if not num_flag:
                braille += en_to_br["num"]
                num_flag = True
        braille += en_to_br[char.lower()]
    return braille


# converts braille to english
def braille_to_en(input_str):
    english = ''
    num_flag = False
    cap_flag = False
    for i in range(0, len(input_str), 6):
        # read characters in groups of 6
        char = input_str[i:i+6]

        # check for flags
        if char == en_to_br["cap"]:
            cap_flag = True
            continue
        elif char == en_to_br["num"]:
            num_flag = True
            continue

        # translate characters
        if num_flag:
            if char == '......':
                english += ' '
                num_flag = False
            else:
                english += br_to_en_numeric[char]
        else:
            if cap_flag:
                english += br_to_en_nonnumeric[char].upper()
                cap_flag = False
            else:
                english += br_to_en_nonnumeric[char]
    return english

# main translator function
def main(arg):
    input_str = ' '.join(arg)
    output = ''
    
    # assume all strings are braille until invalid character is found
    try:
        output = braille_to_en(input_str)
    except:
        output = en_to_braille(input_str)
    print(output)

if __name__ == "__main__":
    main(sys.argv[1:])