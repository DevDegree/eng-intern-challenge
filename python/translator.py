#Get user input
phrase = str(input())

#Initialize dictionary to store braille to character mapping
braille_dict = {
    #letters
    'a': "O.....", 
    'b': "O.O...", 
    'c': "OO....", 
    'd': "OO.O..", 
    'e': "O..O..", 
    'f': "OOO...", 
    'g': "OOOO..", 
    'h': "O.OO..", 
    'i': ".OO...", 
    'j': ".OOO..", 
    'k': "O...O.", 
    'l': "O.O.O.", 
    'm': "OO..O.", 
    'n': "OO.OO.", 
    'o': "O..OO.", 
    'p': "OOO.O.", 
    'q': "OOOOO.", 
    'r': "O.OOO.", 
    's': ".OO.O.", 
    't': ".OOOO.", 
    'u': "O...OO", 
    'v': "O.O.OO", 
    'w': ".OOO.O", 
    'x': "OO..OO", 
    'y': "OO.OOO", 
    'z': "O..OOO", 
    #numbers
    '1': "O.....", 
    '2': "O.O...", 
    '3': "OO....", 
    '4': "OO.O..", 
    '5': "O..O..", 
    '6': "OOO...", 
    '7': "OOOO..", 
    '8': "O.OO..", 
    '9': ".OO...", 
    '0': ".OOO..", 
    #punctuation
    '.': "..OO.O", 
    ',': "..O...", 
    '?': "..O.OO", 
    '!': "..OOO.", 
    ':': "..OO..", 
    ';': "..O.O.", 
    '-': "..O..O", 
    '/': ".O..O.", 
    '<': ".O..OO", 
    '>': ".OO..O", 
    '(': "OO...O", 
    ')': "OO.OOO", 
    #misc
    'capital': ".....O", 
    'decimal': "..O..O", 
    'number': ".O.OOO", 
    ' ': "......"
}

#Initialize key and value dictionaries for indexing
Braille = list(braille_dict.values())
Characters = list(braille_dict.keys())


def Braille_to_English(braille):
    #Initialize resulting translation as an array
    translation = []
    upper = False
    number_follows = False

    #Splitting into Braille code
    mapped_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    
    for chars in mapped_chars:
        if chars == ".....O":
            upper = True
            continue
        elif chars == ".O.OOO":
            number_follows = True
            continue
        elif chars == "......":
            translation.append(' ')
            number_follows = False
            continue

        if chars in Braille:
            pos = Braille.index(chars)

            if number_follows:
                #Check first 9 letters to see which number corresponds with it
                if Characters[pos] in 'abcdefghi': 
                    number = str(ord(Characters[pos]) - ord('a') + 1)
                    translation.append(number)
                elif Characters[pos] == 'j':
                    translation.append('0')
                continue
            
            #Gets value of the character index
            value = Characters[pos]
            if upper:
                translation.append(value.upper())
                upper = False
            else:
                translation.append(value)

    return print(''.join(translation))

def English_to_Braille(sentence):
    #Initialize resulting translation as an array
    translation = []
    sentence = list(sentence)
    number_follows = False

    #Checking for uppercase and digit cases
    for char in sentence:
        if char.isupper():
            translation.append(braille_dict['capital'])
            char = char.lower()

        if char.isdigit():
            if not number_follows:
                translation.append(braille_dict['number'])
                number_follows = True
            translation.append(braille_dict[char])
        else:
            number_follows = False
            translation.append(braille_dict[char])

    return print(''.join(translation))

#Check if the input is in English or Braille
if set(phrase).issubset(set('O. ')) and len(list(phrase))>=6:
    Braille_to_English(braille=phrase)
else:
    English_to_Braille(sentence=phrase)
    







