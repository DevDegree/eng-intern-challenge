import sys

letter_pairs = {
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
'capital_follows': '.....O',
'number_follows': '.O.OOO',
' ': '......' 
}


def english_to_braille(english_sentence):
    braille_result = ''
    i = 0
    while i != len(english_sentence): 
        if english_sentence[i].isupper():
            braille_result = braille_result + letter_pairs.get('capital_follows')
            braille_result = braille_result + letter_pairs.get(english_sentence[i].lower())
        elif english_sentence[i].isnumeric():
            braille_result = braille_result + letter_pairs.get('number_follows')
            while i < len(english_sentence) and english_sentence[i] != ' ':
                braille_result = braille_result + letter_pairs.get(english_sentence[i])
                i = i + 1
            i = i - 1
        else:
            braille_result = braille_result + letter_pairs.get(english_sentence[i])
        i = i + 1


    print(braille_result + '\n')

def braille_to_english(braille_sentence):
    result = ''
    i = 0
    flipped = {v : k for k, v in letter_pairs.items()}
    while i != len(braille_sentence):
        if (flipped.get(braille_sentence[i:i+6]) == 'number_follows'):
            i = i + 6
            while flipped.get(braille_sentence[i:i+6]) != ' ':
                if (flipped.get(braille_sentence[i:i+6]) == None):
                    break
                elif flipped.get(braille_sentence[i:i+6]) == 'j':
                    result = result + 'j'
                else:
                    adjusted = ord(flipped.get(braille_sentence[i:i+6])) - 96
                    result = result + str(adjusted)
                i = i + 6
        elif (flipped.get(braille_sentence[i:i+6]) == 'capital_follows'):
            i = i + 6
            result = result + flipped.get(braille_sentence[i:i+6]).upper()
            i = i + 6
        else:
            result = result + flipped.get(braille_sentence[i:i+6])
            i = i + 6
    print(result + '\n')
def main():
    if ('.' in sys.argv[1]):
        braille_to_english(sys.argv[1])
    else:
        sentence = sys.argv[1]
        for i in range(2,len(sys.argv)):
            sentence = sentence + " " + sys.argv[i]
        english_to_braille(sentence)

if __name__ == '__main__':
    main()


