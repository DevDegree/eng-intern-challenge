import sys

# Braille to English map
braille_to_english_letters = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ', '.....O': 'Capital', '.O.OOO': 'Number', '.O...O': 'Decimal',
}

braille_to_english_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}



# English to Braille map
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    'Capital': '.....O',
    'Number': '.O.OOO',
    'Decimal': '.O...O',
}


def is_braille(input_string):
    #this basically just checks if all of the 'c' characters in the input string are in '0.' so are either a . or a 0 and then also checks to make sure the length is divisible by 6 because each 
    # braille character is 6 characters long
    return all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0

def translate_to_braille(input_string):
    answer = ""
    number = False #boolean to know when to add number follows
    # loop through the input string and check each case to add the proper braille
    for c in input_string:
        # check each case and add the signifier character before adding the actual character
        if c.isdigit() and not number:
            number = True
            answer += english_to_braille.get('Number')
        elif c == ' ':
            number = False
        elif c.isupper():
            answer += english_to_braille.get('Capital')
            c = c.lower()
        elif c == '.':
            answer += english_to_braille.get('Decimal')

        answer += english_to_braille.get(c)

    return answer
        
def translate_to_english(input_string): #He1
    answer = ""
    capital = False
    number = False
    for i in range(0, len(input_string), 6):
        braille_char = input_string[i:i+6] #get each 6 length braille character separately

        # depending on what boolean is true, get from one of the two braille to english maps
        if number:
            answer += braille_to_english_numbers.get(braille_char)
            continue
        elif capital:
            answer += braille_to_english_letters.get(braille_char).upper()
            capital = False
            continue

        #if no boolean, then set the boolean properly
        temp = braille_to_english_letters.get(braille_char)

        if temp == 'Number':
            number = True
            continue
        elif temp == 'Capital':
            capital = True
            continue
        elif temp == ' ':
            number = False

        #if not a capital or a number then just add it regularly
        answer += temp

    return answer


if __name__ == '__main__':

    input_string = ' '.join(sys.argv[1:])
    
    #depending on if its the input string (system arguments together) are braille or not determines whats function to call and uses the proper dictionary
    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))
