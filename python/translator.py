import sys

alphabet = {      'a': 'O.....'
                , 'b': 'O.O...'
                , 'c': 'OO....'
                , 'd': 'OO.O..'
                , 'e': 'O..O..'
                , 'f': 'OOO...'
                , 'g': 'OOOO..'
                , 'h': 'O.OO..'
                , 'i': '.OO...'
                , 'j': '.OOO..'
                , 'k': 'O...O.'
                , 'l': 'O.O.O.'
                , 'm': 'OO..O.'
                , 'n': 'OO.OO.'
                , 'o': 'O..OO.'
                , 'p': 'OOO.O.'
                , 'q': 'OOOOO.'
                , 'r': 'O.OOO.'
                , 's': '.OO.O.'
                , 't': '.OOOO.'
                , 'u': 'O...OO'
                , 'v': 'O.O.OO'
                , 'w': '.OOO.O'
                , 'x': 'OO..OO'
                , 'y': 'OO.OOO'
                , 'z': 'O..OOO'
                , ' ': '......'
}

numbers = {
                  '1': 'O.....'
                , '2': 'O.O...'
                , '3': 'OO....'
                , '4': 'OO.O..'
                , '5': 'O..O..'
                , '6': 'OOO...'
                , '7': 'OOOO..'
                , '8': 'O.OO..'
                , '9': '.OO...'
                , '0': '.OOO..'
                , ' ': '......'
}

special = {
    'capital': '.....O',
    'number':  '.O.OOO'
}

braille_alphabet = {v:k for k,v in alphabet.items()}
braille_numbers = {v:k for k,v in numbers.items()} 

# Function to convert english to braille
def english_to_braille(text):
    braille_output = []
    i = 0
    while i < len(text):
        letter = text[i]
        if letter.isupper():
            braille_output.append(special['capital'])
            letter = letter.lower()
        if letter.isdigit():
            braille_output.append(special['number'])
            while i < len(text) and text[i].isdigit():
                braille_output.append(numbers[text[i]])
                i += 1
            continue
        braille_output.append(alphabet[letter])
        i += 1
    return ''.join(braille_output)

# Function to convert braille to english
def braille_to_english(text):
    arr = [text[i:i+6] for i in range(0, len(text), 6)]
    english_output = []
    i=0
    while i < len(arr):
        if arr[i] == special['capital']:
            i+=1
            english_output.append(braille_alphabet[arr[i]].upper())
            i+=1
            continue
        elif arr[i] == special['number']: 
            i+=1
            while i < len(arr) and arr[i] != '......' :
                english_output.append(braille_numbers[arr[i]])
                i+=1
            continue
        english_output.append(braille_alphabet[arr[i]])
        i+=1
    return ''.join(english_output)

if __name__ == '__main__':
    word = sys.argv[1:]
    word = ' '.join(word)

    if '.'  in word:
        print(braille_to_english(word))
    else:
        print(english_to_braille(word))