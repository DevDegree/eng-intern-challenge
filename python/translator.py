import sys

### CONSTS ###

english_to_braille = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO',
    'A' : '.....OO.....',
    'B' : '.....OO.O...',
    'C' : '.....OOO....',
    'D' : '.....OOO.O..',
    'E' : '.....OO..O..',
    'F' : '.....OOOO...',
    'G' : '.....OOOOO..',
    'H' : '.....OO.OO..',
    'I' : '.....O.OO...',
    'J' : '.....O.OOO..',
    'K' : '.....OO...O.',
    'L' : '.....OO.O.O.',
    'M' : '.....OOO..O.',
    'N' : '.....OOO.OO.',
    'O' : '.....OO..OO.',
    'P' : '.....OOOO.O.',
    'Q' : '.....OOOOOO.',
    'R' : '.....OO.OOO.',
    'S' : '.....O.OO.O.',
    'T' : '.....O.OOOO.',
    'U' : '.....OO...OO',
    'V' : '.....OO.O.OO',
    'W' : '.....O.OOO.O',
    'X' : '.....OOO..OO',
    'Y' : '.....OOO.OOO',
    'Z' : '.....OO..OOO',
    ' ' : '......',
    '.' : '..OO.O'
}

english_to_braille_numbers = {
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..',
}

braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english_numbers = {v: k for k, v in english_to_braille_numbers.items()}

capital = ".....O"
number = '.O.OOO'

################################

# Function to determine if a string input is braille or english
def is_braille(input):
    braille = {'O', '.'}
    return len(input) % 6 == 0 and set(input) == braille

# Function to translate from braille to english or english to braille
def translator(input):
    translated = []
    is_capital = False
    is_number = False

    if is_braille(input):
        for index in range(0, len(input), 6):
            current = input[index:index+6]
            if current == capital:
                is_capital = True
            elif is_capital:
                is_capital = False
                translated.append(braille_to_english[current].upper())
            elif current == number:
                is_number = True
            elif current == '......':
                is_number = False
                translated.append(' ')
            elif is_number:
                translated.append(braille_to_english_numbers[current])
            else:
                translated.append(braille_to_english[current]) 

    else:
        for char in input:
            if char in english_to_braille_numbers:
                if is_number:
                    translated.append(english_to_braille_numbers[char])
                else:
                    is_number = True
                    translated.append(number)
                    translated.append(english_to_braille_numbers[char])
            elif char == ' ':
                translated.append('......')
                is_number = False
            else:
                translated.append(english_to_braille[char])
    print(''.join(translated))

def main():
    input = ''
    for index in range(1, len(sys.argv)):
        input += (sys.argv[index]) + " "
    input = input.strip()
    (translator(input))

if __name__ == "__main__":
    main()