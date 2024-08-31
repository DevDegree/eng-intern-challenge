import sys

# Mapping Braille to English
braille_2_english = {
    'O.....' : 'a', 'OO....' : 'b', 'O..O..' : 'c', 'O..OO.' : 'd',
    'O...O.' : 'e', 'OO.O..' : 'f', 'OO.OO.' : 'g', 'OO..O.' : 'h',
    '.O.O..' : 'i', '.O.OO.' : 'j', 'O.O...' : 'k', 'OOO...' : 'l',
    'O.OO..' : 'm', 'O.OOO.' : 'n', 'O.O.O.' : 'o', 'OOOO..' : 'p',
    'OOOOO.' : 'q', 'OOO.O.' : 'r', '.OOO..' : 's', '.OOOO.' : 't',
    'O.O..O' : 'u', 'OOO..O' : 'v', '.O.OOO' : 'w', 'O.OO.O' : 'x',
    'O.OOOO' : 'y', 'O.O.OO' : 'z', 
    '......' : ' ', #space
    '.....O' : '^', #capital letter follows
    '..OOOO' : '#', #number follows
}

#Number dictionary for Braille
braille_numbers = {
    'O.....' : '1', 'OO....' : '2', 'O..O..' : '3', 'O..OO.' : '4',
    'O...O.' : '5', 'OO.O..' : '6', 'OO.OO.' : '7', 'OO..O.' : '8',
    '.O.O..' : '9', '.O.OO.' : '0'
}

#Mapping English and Number to Braille
english_2_braille = {english: braille for braille, english in braille_2_english.items()}
english_2_braille.update({number: braille for braille, number in braille_numbers.items()})

def is_braille(input):
    return all(t in 'O. ' for t in input)

def braille_2_english_translator(braille):
    translation = []
    capital_follow = False
    number_follow = False
    words = [braille[i:i+6] for i in range(0, len(braille), 6)]

    for word in words:
        if word == '..OOOO': #number follows
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
                translation.append(english_2_braille[' '])
            
            if char.isupper():
                translation.append(english_2_braille['^'])
                char = char.lower()

            translation.append(english_2_braille.get(char, '??????'))
    
    return ' '.join(translation)

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