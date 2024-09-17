#Karmvir Singh Dhaliwal

#ASSUMPTIONS MADE: 
#   - all inputs will be well formatted, ie braille inputs will only include the braille characters that can be translated and same for english
#   - runtime instructions will be well formatted ie correct number of inputs


#steps:
#1. make dictionaries for translations (done)
#2. make function for replacing english letter with braille (done)
#3. make function for replacing braille with english (done)
#4. make main function running loop that does the replacements by: (done)
#   - check if input string is in english or braille
#   - if english, loop through each individual character and replace with braille, making sure to add spaces and capital/number characters
#   - if braille, look at 6 characters at a time and replace with english character

#imports
import sys

#dictionaries
english_letters_to_braille_map = {'a' : 'O.....',  'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f' : 'OOO...',
 'g' : 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j' : '.OOO..', 'k' :'O...O.', 'l' : 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
 'o' : 'O..OO.', 'p' : 'OOO.O.', 'q': 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.', 'u' : 'O...OO', 'v' : 'O.O.OO',
 'w': '.OOO.O', 'x': 'OO..OO', 'y' : 'OO.OOO', 'z' : 'O..OOO', ' ' : '......', 'cap' : '.....O', 'num' : '.O.OOO'}

#swapping keys and values to get the second map
braille_letters_to_english_map = {v: k for k,v in english_letters_to_braille_map.items()}

english_numbers_to_braille_map = {'1' : 'O.....',  '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6' : 'OOO...',
 '7' : 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0' : '.OOO..',}

braille_numbers_to_english_map = {v: k for k,v in english_numbers_to_braille_map.items()}

#testing
#print(english_letters_to_braille_map)
#print(english_numbers_to_braille_map)
#print(braille_letters_to_english_map)
#print(braille_numbers_to_english_map)

#function to turn english text to braille string
def english_to_braille(text):
    res = ''
    num_mode = False
    for ch in text:
        #want to turn on num mode so we use the num map, not the letter map
        if ch.isdigit() and not num_mode:
            res += english_letters_to_braille_map['num']
            num_mode = True
        #want to turn off num mode once we are looking at letters again so we can go back to letter map
        elif ch.isalpha() and num_mode:
            num_mode = False

        #if upper case letter, add upper case symbol then add letter
        if ch.isupper():
            res += english_letters_to_braille_map['cap']
            res += english_letters_to_braille_map[ch.lower()]

        #if lower case letter or space, just add it
        elif ch.islower() or ch == ' ':
            res += english_letters_to_braille_map[ch]
        #if not upper or lower case letter or space, must be number, so add number from number map
        else:
            res += english_numbers_to_braille_map[ch]

    return res

#function to turn braille string into english text

def braille_to_english(text):
    res = ''
    num_mode = False
    caps_mode = False

    for i in range(0, len(text), 6):
        ch = text[i:i+6]

        #if we see next character is num symbol, set to num mode to use num dictionary, continue to next char
        if ch == english_letters_to_braille_map['num']:
            num_mode = True
            continue
        
        #if we see next character is caps symbol, set caps mode to true, continue to next char
        if ch == english_letters_to_braille_map['cap']:
            caps_mode = True
            continue
        
        #if we see a space we know to leave num mode if we're in it, can add space and continue to next char
        if ch == english_letters_to_braille_map[' ']:
            res += ' '
            num_mode = False
            continue

        #if we're in num mode, we know we're dealing with a number so use the nums dictionary
        if num_mode:
            res += braille_numbers_to_english_map[ch]

        #if we're in caps mode we know to add a capital letter, then turn off caps mode
        elif caps_mode:
            res += braille_letters_to_english_map[ch].upper()
            caps_mode = False
        #if neither of the above cases are true, just dealing with a normal lower case letter so add it to string
        else:
            res += braille_letters_to_english_map[ch]

    return res

#main function
def main():

#concat all input words to one string
    input = ' '.join(sys.argv[1:])

#check if were dealing with a braille input or english input, call appropriate function
    if all(ch in "O." for ch in input):
        output = braille_to_english(input)
    else:
        output = english_to_braille(input)
    
    print(output)

if __name__ == "__main__":
    main()


        
#testing
#print(english_to_braille('Abc 123 xYz'))
#print(braille_to_english('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO'))

