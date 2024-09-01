import sys

# Mapping Braille to English
braille_2_english = {
    'O.....' : 'a', 'O.O...' : 'b', 'OO....' : 'c', 'OO.O..' : 'd',
    'O..O..' : 'e', 'OOO...' : 'f', 'OOOO..' : 'g', 'O.OO..' : 'h',
    '.OO...' : 'i', '.OOO..' : 'j', 'O...O.' : 'k', 'O.O.O.' : 'l',
    'OO..O.' : 'm', 'OO.OO.' : 'n', 'O..OO.' : 'o', 'OOO.O.' : 'p',
    'OOOOO.' : 'q', 'O.OOO.' : 'r', '.OO.O.' : 's', '.OOOO.' : 't',
    'O...OO' : 'u', 'O.O.OO' : 'v', '.OOO.O' : 'w', 'OO..OO' : 'x',
    'OO.OOO' : 'y', 'O..OOO' : 'z', 
    '......' : ' ', #space
    '.....O' : '^', #capital letter follows
    '.O.OOO' : '#', #number follows
}

#Number dictionary for Braille
braille_numbers = {
    'O.....' : '1', 'O.O...' : '2', 'OO....' : '3', 'OO.O..' : '4',
    'O..O..' : '5', 'OOO...' : '6', 'OOOO..' : '7', 'O.OO..' : '8',
    '.OO...' : '9', '.OOO..' : '0'
}

#Mapping English and Number to Braille
english_2_braille = {english: braille for braille, english in braille_2_english.items()}
english_2_braille.update({number: braille for braille, number in braille_numbers.items()})

def is_braille(input):
    return all(c in 'O. ' for c in input)

def braille_2_english_translator(braille):
    translation = []
    capital_follow = False
    number_follow = False
    words = [braille[i:i+6] for i in range(0, len(braille), 6)]

    for word in words:
        if word == '.O.OOO': #number follows
            number_follow = True
        elif word == '.....O': #capital letter follows
            capital_follow = True
        elif word in braille_2_english:
            char = braille_2_english[word]
            if number_follow:
                if char == ' ':
                    number_follow = False
                else:
                    char = braille_numbers.get(word, '?')
            elif capital_follow:
                char = char.upper()
                capital_follow = False
            translation.append(char)
        else:
            translation.append('?') #word isnt in the dictionary, it adds ? in the result

    return ''.join(translation)

def english_2_braille_translator(english):
    translation = []
    number_follow = False
    
    for char in english:
        if char.isdigit():
            if not number_follow:
                translation.append(english_2_braille['#'])
                number_follow = True
            translation.append(english_2_braille[char])
        else:
            if number_follow:
                number_follow = False
            
            if char.isupper():
                translation.append(english_2_braille['^'])
                char = char.lower()

            translation.append(english_2_braille.get(char, '??????'))
    
    return ''.join(translation)

def main():
    if len(sys.argv) < 2:
        print("Provide a string to translate")
        return
    
    input = ' '.join(sys.argv[1:])

    if is_braille(input):
        print(braille_2_english_translator(input.replace(' ', '')))
    else:
        print(english_2_braille_translator(input))

if __name__ == "__main__":
    main()