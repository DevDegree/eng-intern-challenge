import sys
from collections import defaultdict

english_to_braille = {
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
    'capital': ".....O",
    'decimal': ".O...O",
    'number': ".O.OOO",
    'space':"......"

}

braille_to_english = defaultdict(list)
for k, v in english_to_braille.items():
    braille_to_english[v].append(k)

braille_to_english = dict(braille_to_english)

def braille_to_english_translation(braille_text):
    english_text = []
    i = 0
    capitalize_next = False
    interpreting_numbers = False

    while i < len(braille_text):
        braille_char = braille_text[i:i+6]  # each Braille letter is 6 chars long

        if braille_char == ".....O": # capital letter follows
            capitalize_next = True
            i += 6
            continue

        if braille_char == ".O.OOO": # number follows
            interpreting_numbers = True
            i += 6
            continue

        if braille_char == "......": # space
            interpreting_numbers = False
            english_text.append(' ')
            i += 6
            continue

        if braille_char in braille_to_english:
            possible_chars = braille_to_english[braille_char]

            if interpreting_numbers:
                possible_chars = [char for char in possible_chars if char.isdigit()]

            if possible_chars:
                letter = possible_chars[0]

                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False

                english_text.append(letter)

            else:
                english_text.append('?')
        else:
            english_text.append('?')  # unmapped or invalid Braille input

        i += 6

    return ''.join(english_text)

def english_to_braille_translation(english_text):
    braille_text = []
    interpreting_numbers = False
    
    for char in english_text:
        if char == ' ':
            braille_text.append("......")  # space
            interpreting_numbers = False 

        elif char.isupper():
            braille_text.append(".....O")  # capital letter follows
            char = char.lower() 
            braille_text.append(english_to_braille.get(char, '?'))

        elif char.isdigit():
            if not interpreting_numbers:
                braille_text.append(".O.OOO")  # numbers follow
                interpreting_numbers = True
            braille_text.append(english_to_braille.get(char, '?'))
            
        else:
            if interpreting_numbers:
                interpreting_numbers = False
            braille_text.append(english_to_braille.get(char, '?'))

    return ''.join(braille_text)

def is_braille(text):
    return bool(text.strip()) and all(c in 'O.' for c in text.replace(' ', ''))

def is_valid_braille(text):
    return len(text) % 6 == 0 

def translate(text):
    if is_braille(text):
        #it consists of braille (.,O)
        if is_valid_braille(text):
            return braille_to_english_translation(text)

        else:
            return "Braille text len should be divisible by 6."
    else:
        #its english
        return english_to_braille_translation(text)

def main():
    if len(sys.argv) > 1:
        user_input = ' '.join(sys.argv[1:]) # preserve spaces
        print(translate(user_input))

    else:
        print("No input provided.")

if __name__ == "__main__":
    main()