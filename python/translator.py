import sys

alphabet_to_braille = {
    'a': 'O.....','b': 'O.O...','c': 'OO....','d': 'OO.O..','e': 'O..O..','f': 'OOO...',
    'g': 'OOOO..','h': 'O.OO..','i': '.OO...','j': '.OO...','k': 'O...O.','l': 'O.O.O.',
    'm': 'OO..O.','n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.','q': 'OOOOO.','r': 'O.OOO.',
    's': '.OO.O.','t': '.OOOO.','u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO',
    'y': 'OO.OOO','z': 'O..OOO','cap': '.....O','dec': '.O...O','num': '.O.OOO',' ': '......'
}

numbers = {
    '1': 'O.....','2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..','6': 'OOO...',
    '7': 'OOOO..','8': 'O.OO..','9': '.OO...','0': '.OO...', '.': '..OO.O',',': '..O...',
    '?': '..O.OO','!': '..OOO.',':': '..OO..',';': '..O.O.','-': '....OO','/': '.O..O.',
    '<': '.OO..O','>': 'O..OO.','(': 'O.O..O',')': '.O.OO.'
}
braille_to_alphabet = {value: key for key, value in alphabet_to_braille.items()}
braille_to_numbers = {value: key for key, value in numbers.items()}



def translate_to_braille(message):
    braille_message = ""
    is_number = False
    for index, character in enumerate(message):

        if character in numbers.keys():
            if is_number == False:
                braille_message += alphabet_to_braille['num']
                is_number = True
            
            braille_message += numbers[character]

        if character.lower() in alphabet_to_braille.keys():
            is_number = False
            if character.isupper():

                braille_message += alphabet_to_braille['cap']
                character = character.lower()

            braille_message += alphabet_to_braille[character]

    return braille_message   


def translate_to_English(braille_message):
    english_message = ""

    is_cap = False
    is_num = False
    for index in range(0 ,len(braille_message), 6):
        braille_Alphabet = braille_message[index:index+6]

        if braille_to_alphabet[braille_Alphabet] == "cap":
            is_cap = True
            continue
        elif braille_to_alphabet[braille_Alphabet] == " ":
            is_num = False
        elif braille_to_alphabet[braille_Alphabet] == "num" or braille_to_alphabet[braille_Alphabet] == "dec":
            is_num = True
            continue


        if is_cap:
            english_message += braille_to_alphabet[braille_Alphabet].capitalize()
            is_cap = False
            continue
        if is_num:
            english_message += braille_to_numbers[braille_Alphabet]
            continue
        else:
            english_message += braille_to_alphabet[braille_Alphabet]



    return english_message     


def is_braille(message):
    contains_only_alpha = False
    contains_only_braille = False
    for i, character in enumerate(message):

        character = character.lower()
        if character != "." and character != "o" and (character in alphabet_to_braille.keys() or character in numbers.keys()):
            contains_only_alpha = True
        elif character != "o":
                contains_only_braille = True

    if contains_only_alpha and contains_only_braille :
        raise ValueError("you can't put english and braille, you have to choose one")

    if contains_only_alpha and contains_only_braille == False:
        return False
    else :
        return True



def main():

    message = ' '.join(sys.argv[1:])

    if is_braille(message):
        print(translate_to_English(message))
    else:
        print(translate_to_braille(message))

if __name__ == "__main__":
    main()


