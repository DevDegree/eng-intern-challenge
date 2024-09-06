import sys
# Program only designed to handle letters, numbers, capitals and spaces as per technical requirements
# Braille mappings
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'number': '.O.OOO',
    '.': '..OO.O'
}

# Reverse mappings
reverse_braille_map = {i: j for j, i in braille_map.items()}

# Number mappings 
number_map = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}

# Revese number mappings
reverse_number_map = {i: j for j, i in number_map.items()}

# Function to turn braille words into english 
def braille_to_english(braille):
    translation = ""
    capital = False
    number = False
    i = 0
    while i < len(braille):
        letter = braille[i:i+6]
        if letter not in reverse_braille_map:
            return False
        elif letter == braille_map["capital"]:
            capital = True
        elif letter == braille_map["number"]:
            number = True
        elif letter == braille_map[" "]:
            translation += reverse_braille_map[letter]
            number = False
        else:
            char = reverse_braille_map[letter]
            if number:
                char  = reverse_number_map[char]
            elif capital:
                char = char.upper()
                capital = False
            translation += char
        i += 6
    return translation

# Function to turn english words into braille
def english_to_braille(english):
    translation = ""
    char = ""
    for letter in english:
        char = letter.lower()
        if letter.isupper():
            translation += braille_map["capital"]
        elif letter.isnumeric():
            translation += braille_map["number"]
            char = number_map[letter]
        translation += braille_map[char]
    return translation

# Function to decide which translator to use based on input
def translator(input):
    ans = braille_to_english(input)
    if ans == False:
        ans = english_to_braille(input)
    return ans

if __name__ == "__main__":
  input_text = ' '.join(sys.argv[1:])
  print(translator(input_text))





