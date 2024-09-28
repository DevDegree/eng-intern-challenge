import sys

# Braille alphabet
braille_dict = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......',
    'capital': '.....O',    'number': '.O.OOO'
}

# Reverse the braille dictionary for English to Braille translation
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def english_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(braille_dict['capital'])
            if is_number:
                is_number = False
            result.append(braille_dict[char.lower()])
        elif char.isdigit():
            if not is_number:
                result.append(braille_dict['number'])
                is_number = True
            if char == '0':
                result.append(braille_dict['j'])
            else:
                result.append(braille_dict[chr(ord(char) - ord('0') + ord('a') - 1)])
        elif char == ' ':
            result.append(braille_dict[char])
            is_number = False
        else:
            is_number = False
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    is_number = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_dict['capital']:
            capitalize_next = True
        elif symbol == braille_dict['number']:
            is_number = True
        elif symbol in reverse_braille_dict:
            char = reverse_braille_dict[symbol]
            if is_number and char in 'abcdefghij':
                char = str('abcdefghij'.index(char))
            elif not is_number and char.isdigit():
                char = 'abcdefghij'[int(char)]
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            result.append(char)
            if char == ' ':
                is_number = False
        i += 6
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = ' '.join(sys.argv[1:])

    # Determine if the input is English or Braille
    if all(c in 'O.' for c in input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()

# .....OO.....O.O...OO............OO.OO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO - actual 
# .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO - expected

# .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO
# .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO

# .....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO